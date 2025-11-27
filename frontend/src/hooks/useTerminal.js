import { useState, useRef, useCallback, useEffect } from 'react'
import { useLanguage } from '../contexts/LanguageContext'
import { useWebSocket } from './useWebSocket'

const AVAILABLE_COMMANDS = [
  'HELP', 'STATUS', 'LOGIN', 'SCAN', 'DECODE', 'ACCESS', 
  'ACTIVATE', 'NETWORK', 'ANALYZE', 'BYPASS', 'CONNECT', 
  'RESTORE', 'SOLVE', 'CAT', 'MAN', 'NVIM', 'SPLIT', 
  'PORTSCAN', 'BRUTEFORCE', 'JOBS', 'SSH', 'EXPLOIT', 'CREATE_USER', 'PKG', 'EXIT', 'LS'
]

const AVAILABLE_PACKAGES = ['file-viewer']

export const useTerminal = () => {
  const { language } = useLanguage()
  const [history, setHistory] = useState([])
  const [input, setInput] = useState('')
  const [isTyping, setIsTyping] = useState(false)
  const [commandHistory, setCommandHistory] = useState([])
  const [historyIndex, setHistoryIndex] = useState(-1)
  const [autocompleteOptions, setAutocompleteOptions] = useState([])
  const [availableFiles, setAvailableFiles] = useState([])
  const [unlockedCommands, setUnlockedCommands] = useState(['HELP', 'STATUS', 'LOGIN'])
  const [installedPackages, setInstalledPackages] = useState([])
  const [isPasswordMode, setIsPasswordMode] = useState(false)
  const [passwordUsername, setPasswordUsername] = useState(null)
  const sessionIdRef = useRef(
    localStorage.getItem('session_id') || 
    `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
  )

  if (!localStorage.getItem('session_id')) {
    localStorage.setItem('session_id', sessionIdRef.current)
  }

  const addToHistory = useCallback((type, content) => {
    setHistory(prev => [...prev, {
      type,
      content,
      timestamp: new Date().toISOString()
    }])
  }, [])

  const typeText = useCallback((text, callback) => {
    setIsTyping(true)
    let index = 0
    const typingInterval = setInterval(() => {
      if (index < text.length) {
        callback(text.substring(0, index + 1))
        index++
      } else {
        clearInterval(typingInterval)
        setIsTyping(false)
      }
    }, 30)
  }, [])

  const handleWebSocketMessage = useCallback((data) => {
    if (data.type === 'command_response') {
      const systemResponse = data.response || 'No response from system.'
      
      if (systemResponse.includes("Vous n'êtes pas connecté") || 
          systemResponse.includes("You are not connected") ||
          systemResponse.includes("not connected") ||
          systemResponse.includes("Échec de la connexion SSH") ||
          systemResponse.includes("SSH connection failed") ||
          systemResponse.includes("Invalid credentials") ||
          systemResponse.includes("Identifiants invalides")) {
        localStorage.removeItem('system_void_username')
        localStorage.removeItem('system_void_token')
        window.dispatchEvent(new Event('localStorageChange'))
      }
      
      if (data.password_prompt) {
        setIsPasswordMode(true)
        setPasswordUsername(data.username || null)
        setInput('')
        setIsTyping(false)
        
        setHistory(prev => [...prev, {
          type: 'system',
          content: systemResponse,
          timestamp: new Date().toISOString()
        }])
        
        window.dispatchEvent(new CustomEvent('passwordPrompt', { detail: { username: data.username } }))
        
        setTimeout(() => {
          const inputElement = document.querySelector('.terminal-input-inline')
          if (inputElement) {
            inputElement.focus()
            inputElement.click()
          }
        }, 200)
        
        return
      }
      
      const wasPasswordMode = isPasswordMode
      
      if (wasPasswordMode && !data.password_prompt) {
        setIsPasswordMode(false)
        setPasswordUsername(null)
      }
      
      setHistory(prev => [...prev, {
        type: 'system',
        content: '',
        timestamp: new Date().toISOString()
      }])
      
      if (data.logout || data.username === null) {
        localStorage.removeItem('system_void_username')
        localStorage.removeItem('system_void_token')
        window.dispatchEvent(new Event('localStorageChange'))
      }
      
      typeText(systemResponse, (partialText) => {
        setHistory(prev => {
          const newHistory = [...prev]
          const lastIndex = newHistory.length - 1
          if (lastIndex >= 0 && newHistory[lastIndex].type === 'system') {
            newHistory[lastIndex] = {
              ...newHistory[lastIndex],
              content: partialText
            }
          }
          return newHistory
        })
      })
    } else if (data.type === 'token_update') {
      if (data.token) {
        localStorage.setItem('system_void_token', data.token)
        window.dispatchEvent(new Event('localStorageChange'))
      }
    } else if (data.type === 'username_update') {
      if (data.username) {
        localStorage.setItem('system_void_username', data.username)
        window.dispatchEvent(new Event('localStorageChange'))
      }
    } else if (data.type === 'logout') {
      localStorage.removeItem('system_void_username')
      localStorage.removeItem('system_void_token')
      window.dispatchEvent(new Event('localStorageChange'))
    } else if (data.type === 'files_update') {
      if (data.files) {
        setAvailableFiles(data.files)
      }
    } else if (data.type === 'commands_update') {
      if (data.commands) {
        setUnlockedCommands(data.commands)
      }
    } else if (data.type === 'packages_update') {
      if (data.packages) {
        setInstalledPackages(data.packages)
      }
    }
  }, [typeText])

  const { isConnected, sendCommand: wsSendCommand, subscribe } = useWebSocket(
    sessionIdRef.current,
    language,
    handleWebSocketMessage
  )

  useEffect(() => {
    if (isConnected) {
      subscribe(['files', 'commands', 'packages'])
    }
  }, [isConnected, subscribe])

  const getAutocompleteOptions = useCallback((partial) => {
    if (!partial || !partial.trim()) return []
    
    const trimmed = partial.trim()
    const parts = trimmed.split(/\s+/)
    const command = parts[0]?.toUpperCase() || ''
    const arg = parts.slice(1).join(' ') || ''
    
    // Commandes qui prennent des noms de fichiers en argument
    const fileCommands = ['ACCESS', 'DECODE', 'CAT', 'NVIM', 'ENCRYPT', 'DECRYPT']
    
    // Auto-complétion pour LS (liste les fichiers)
    if (command === 'LS') {
      return availableFiles.length > 0 ? availableFiles : []
    }
    
    // Auto-complétion pour les commandes de fichiers
    if (fileCommands.includes(command)) {
      if (arg && arg.trim()) {
        const lowerArg = arg.toLowerCase().trim()
        const matches = availableFiles.filter(file => 
          file.toLowerCase().startsWith(lowerArg) && file.toLowerCase() !== lowerArg
        )
        return matches
      } else if (trimmed.endsWith(' ') || arg === '') {
        // Si juste "COMMANDE " (avec espace) ou commande complète sans arg, retourner tous les fichiers
        return availableFiles.length > 0 ? availableFiles : []
      }
    }
    
    // Auto-complétion pour MAN <commande>
    if (command === 'MAN') {
      if (arg) {
        const upperArg = arg.toUpperCase()
        return unlockedCommands.filter(cmd => 
          cmd.startsWith(upperArg) && cmd !== upperArg
        )
      } else {
        return unlockedCommands
      }
    }
    
    // Auto-complétion pour PKG INSTALL/UNINSTALL
    if (command === 'PKG') {
      const subcommand = arg.split(' ')[0]?.toUpperCase()
      const packageArg = arg.split(' ').slice(1).join(' ')
      
      if (subcommand === 'INSTALL' || subcommand === 'UNINSTALL') {
        if (packageArg) {
          const lowerArg = packageArg.toLowerCase()
          return AVAILABLE_PACKAGES.filter(pkg => 
            pkg.startsWith(lowerArg) && pkg !== lowerArg
          )
        } else {
          return AVAILABLE_PACKAGES
        }
      } else if (!subcommand || subcommand === '') {
        return ['INSTALL', 'UNINSTALL', 'LIST'].filter(cmd => 
          cmd.startsWith(arg.toUpperCase()) && cmd !== arg.toUpperCase()
        )
      }
    }
    
    // Auto-complétion pour les commandes simples
    if (command && !arg) {
      const upper = command.toUpperCase()
      return unlockedCommands.filter(cmd => 
        cmd.startsWith(upper) && cmd !== upper
      )
    }
    
    return []
  }, [availableFiles, unlockedCommands])

  const sendCommand = useCallback((command) => {
    if (isTyping && !isPasswordMode) return
    
    if (isPasswordMode) {
      const password = command || ''
      
      setInput('')
      setAutocompleteOptions([])
      setIsPasswordMode(false)
      setPasswordUsername(null)
      
      if (!isConnected) {
        setHistory(prev => [...prev, {
          type: 'system',
          content: 'ERROR: WebSocket not connected. Please wait...',
          timestamp: new Date().toISOString()
        }])
        return
      }

      const token = localStorage.getItem('system_void_token')
      wsSendCommand('', token, password)
      return
    }
    
    const userCommand = command.trim()
    
    if (userCommand) {
      addToHistory('user', userCommand)
      setCommandHistory(prev => {
        const newHistory = [...prev]
        if (newHistory[newHistory.length - 1] !== userCommand) {
          newHistory.push(userCommand)
        }
        return newHistory.slice(-50)
      })
      setHistoryIndex(-1)
    }
    
    setInput('')
    setAutocompleteOptions([])

    if (!isConnected) {
      setHistory(prev => [...prev, {
        type: 'system',
        content: 'ERROR: WebSocket not connected. Please wait...',
        timestamp: new Date().toISOString()
      }])
      return
    }

    const token = localStorage.getItem('system_void_token')
    const sent = wsSendCommand(userCommand, token)
    
    if (!sent) {
      setHistory(prev => [...prev, {
        type: 'system',
        content: 'ERROR: Failed to send command. WebSocket may be disconnected.',
        timestamp: new Date().toISOString()
      }])
    }
  }, [addToHistory, isTyping, isConnected, wsSendCommand, isPasswordMode])

  const navigateHistory = useCallback((direction) => {
    if (commandHistory.length === 0) return
    
    let newIndex = historyIndex
    if (direction === 'up') {
      if (historyIndex === -1) {
        newIndex = commandHistory.length - 1
      } else {
        newIndex = Math.max(0, historyIndex - 1)
      }
    } else if (direction === 'down') {
      if (historyIndex === -1) {
        return
      } else {
        newIndex = historyIndex + 1
        if (newIndex >= commandHistory.length) {
          newIndex = -1
        }
      }
    }
    
    setHistoryIndex(newIndex)
    if (newIndex === -1) {
      setInput('')
    } else {
      setInput(commandHistory[newIndex])
    }
  }, [commandHistory, historyIndex])

  const handleTab = useCallback((currentInput) => {
    if (!currentInput) {
      return false
    }
    
    const trimmed = currentInput.trim()
    if (!trimmed) {
      return false
    }
    
    const options = getAutocompleteOptions(currentInput)
    
    if (options.length === 0) {
      return false
    }
    
    const parts = currentInput.trim().split(/\s+/)
    const command = parts[0]?.toUpperCase() || ''
    const arg = parts.slice(1).join(' ') || ''
    
    // Commandes qui prennent des fichiers
    const fileCommands = ['ACCESS', 'DECODE', 'CAT', 'NVIM', 'ENCRYPT', 'DECRYPT']
    
    // Auto-complétion pour LS (retourne les fichiers disponibles)
    if (command === 'LS') {
      return availableFiles.length > 0 ? availableFiles : []
    }
    
    if (options.length === 1) {
      // Une seule option : compléter automatiquement
      if (fileCommands.includes(command)) {
        setInput(`${command} ${options[0]}`)
      } else if (command === 'MAN') {
        setInput(`MAN ${options[0]}`)
      } else if (command === 'PKG') {
        const subcommand = arg.split(' ')[0]?.toUpperCase()
        if (subcommand === 'INSTALL' || subcommand === 'UNINSTALL') {
          const packageArg = arg.split(' ').slice(1).join(' ')
          if (packageArg) {
            setInput(`${command} ${subcommand} ${options[0]}`)
          } else {
            setInput(`${command} ${subcommand} ${options[0]}`)
          }
        } else {
          setInput(`${command} ${options[0]}`)
        }
      } else {
        // Commande simple
        setInput(options[0])
      }
      setAutocompleteOptions([])
      return true
    } else if (options.length > 1) {
      // Plusieurs options : compléter avec le premier et afficher la liste
      setAutocompleteOptions(options)
      
      if (fileCommands.includes(command)) {
        if (arg && arg.trim()) {
          // Si on a déjà tapé quelque chose, compléter avec le premier match
          setInput(`${command} ${options[0]}`)
        } else {
          // Si juste la commande, ne pas compléter mais afficher les options
          setInput(currentInput)
        }
        addToHistory('system', `Fichiers disponibles: ${options.join(', ')}`)
      } else if (command === 'MAN') {
        if (arg) {
          setInput(`MAN ${options[0]}`)
        } else {
          setInput(currentInput)
        }
        addToHistory('system', `Commandes disponibles: ${options.join(', ')}`)
      } else {
        setInput(options[0])
        addToHistory('system', `Suggestions: ${options.join(', ')}`)
      }
      return true
    }
    
    return false
  }, [getAutocompleteOptions, addToHistory, availableFiles])

  return {
    history,
    input,
    setInput,
    isTyping,
    sendCommand,
    navigateHistory,
    handleTab,
    autocompleteOptions,
    installedPackages,
    isPasswordMode,
    passwordUsername
  }
}

