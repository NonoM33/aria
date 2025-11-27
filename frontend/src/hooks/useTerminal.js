import { useState, useRef, useCallback, useEffect } from 'react'
import { useLanguage } from '../contexts/LanguageContext'
import { useWebSocket } from './useWebSocket'

const AVAILABLE_COMMANDS = [
  'HELP', 'STATUS', 'LOGIN', 'SCAN', 'DECODE', 'ACCESS', 
  'ACTIVATE', 'NETWORK', 'ANALYZE', 'BYPASS', 'CONNECT', 
  'RESTORE', 'SOLVE', 'CAT', 'MAN', 'NVIM', 'SPLIT', 
  'PORTSCAN', 'BRUTEFORCE', 'JOBS', 'SSH', 'EXPLOIT', 'CREATE_USER', 'PKG', 'EXIT', 'LS', 'CD', 'PWD', 'CLEAR', 'ALIAS'
]

const AVAILABLE_PACKAGES = ['file-viewer']

const getPathContents = (fs, basePath, targetPath) => {
  let fullPath = targetPath
  if (!targetPath.startsWith('/')) {
    if (basePath === '/') {
      fullPath = '/' + targetPath
    } else {
      fullPath = basePath + '/' + targetPath
    }
  }
  fullPath = fullPath.replace(/\/+/g, '/')
  if (fullPath !== '/' && fullPath.endsWith('/')) {
    fullPath = fullPath.slice(0, -1)
  }
  
  if (fullPath === '/') return fs
  
  const parts = fullPath.split('/').filter(p => p)
  let current = fs
  for (const part of parts) {
    if (current && typeof current === 'object' && part in current) {
      current = current[part]
    } else {
      return null
    }
  }
  return typeof current === 'object' ? current : null
}

const getDirsAndFiles = (contents) => {
  if (!contents || typeof contents !== 'object') return { dirs: [], files: [] }
  const dirs = []
  const files = []
  for (const [name, value] of Object.entries(contents)) {
    if (typeof value === 'object') {
      dirs.push(name + '/')
    } else {
      files.push(name)
    }
  }
  return { dirs, files }
}

export const useTerminal = () => {
  const { language } = useLanguage()
  const [history, setHistory] = useState([])
  const [input, setInput] = useState('')
  const [isTyping, setIsTyping] = useState(false)
  const [commandHistory, setCommandHistory] = useState([])
  const [historyIndex, setHistoryIndex] = useState(-1)
  const [autocompleteOptions, setAutocompleteOptions] = useState([])
  const [autocompleteIndex, setAutocompleteIndex] = useState(-1)
  const [availableFiles, setAvailableFiles] = useState([])
  const [availableDirs, setAvailableDirs] = useState([])
  const [filesystem, setFilesystem] = useState({})
  const [unlockedCommands, setUnlockedCommands] = useState(['HELP', 'STATUS', 'LOGIN', 'CLEAR'])
  const [installedPackages, setInstalledPackages] = useState([])
  const [isPasswordMode, setIsPasswordMode] = useState(false)
  const [passwordUsername, setPasswordUsername] = useState(null)
  const [currentPath, setCurrentPath] = useState(() => {
    return localStorage.getItem('system_void_path') || '/'
  })
  const currentPathRef = useRef(localStorage.getItem('system_void_path') || '/')
  const [ariaChoices, setAriaChoices] = useState([])
  const [ariaMessage, setAriaMessage] = useState(null)
  const [isAdminMode, setIsAdminMode] = useState(false)
  const lastManualInputRef = useRef('')
  const sessionIdRef = useRef(
    localStorage.getItem('session_id') || 
    `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
  )

  if (!localStorage.getItem('session_id')) {
    localStorage.setItem('session_id', sessionIdRef.current)
  }

  const addToHistory = useCallback((type, content, path = null, entryUsername = undefined) => {
    const storedUsername = localStorage.getItem('system_void_username') || null
    setHistory(prev => [...prev, {
      type,
      content,
      path: path || currentPathRef.current || '/',
      username: entryUsername !== undefined ? entryUsername : storedUsername,
      timestamp: new Date().toISOString()
    }])
  }, [])

  const typeText = useCallback((text, callback) => {
    setIsTyping(true)
    let index = 0
    const charsPerTick = text.length > 200 ? 5 : 3
    const typingInterval = setInterval(() => {
      if (index < text.length) {
        index = Math.min(index + charsPerTick, text.length)
        callback(text.substring(0, index))
      } else {
        clearInterval(typingInterval)
        setIsTyping(false)
      }
    }, 10)
  }, [])

  const UNKNOWN_RESPONSES = useRef([
    "Commande inconnue. Accès refusé.\n\nTapez HELP pour voir les commandes disponibles.",
    "Unknown command. Access Denied.\n\nType HELP to see available commands.",
    "Commande inconnue. Accès refusé.",
    "Unknown command. Access denied.",
  ])

  const handleWebSocketMessage = useCallback((data) => {
    if (data.type === 'command_response') {
      const systemResponse = data.response || 'No response from system.'
      const trimmedResponse = (systemResponse || '').trim()
      
      if (data.current_path) {
        setCurrentPath(data.current_path)
        currentPathRef.current = data.current_path
        localStorage.setItem('system_void_path', data.current_path)
      }
      
      if (data.admin_mode) {
        setIsAdminMode(true)
      }
      
      if (data.admin_exit) {
        setIsAdminMode(false)
      }
      
      if (systemResponse.includes("Vous n'êtes pas connecté") || 
          systemResponse.includes("You are not connected") ||
          systemResponse.includes("not connected") ||
          systemResponse.includes("Échec de la connexion SSH") ||
          systemResponse.includes("SSH connection failed") ||
          systemResponse.includes("Invalid credentials") ||
          systemResponse.includes("Identifiants invalides")) {
        localStorage.removeItem('system_void_username')
        localStorage.removeItem('system_void_token')
        localStorage.setItem('system_void_path', '/')
        setCurrentPath('/')
        currentPathRef.current = '/'
        window.dispatchEvent(new Event('localStorageChange'))
      }
      
      if (data.password_prompt) {
        setIsPasswordMode(true)
        setPasswordUsername(data.username || null)
        setInput('')
        setIsTyping(false)
        
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
      
      if (UNKNOWN_RESPONSES.current.includes(trimmedResponse)) {
        setIsTyping(false)
        return
      }

      const currentUsername = localStorage.getItem('system_void_username') || null
      setHistory(prev => [...prev, {
        type: 'system',
        content: '',
        path: currentPathRef.current || '/',
        username: currentUsername,
        timestamp: new Date().toISOString()
      }])
      
      if (data.logout || data.username === null) {
        localStorage.removeItem('system_void_username')
        localStorage.removeItem('system_void_token')
        localStorage.setItem('system_void_path', '/')
        setCurrentPath('/')
        currentPathRef.current = '/'
        window.dispatchEvent(new Event('localStorageChange'))
      }
      
      typeText(systemResponse, (partialText) => {
        setHistory(prev => {
          const newHistory = [...prev]
          const lastIndex = newHistory.length - 1
          if (lastIndex >= 0 && newHistory[lastIndex].type === 'system') {
            newHistory[lastIndex] = {
              ...newHistory[lastIndex],
              content: partialText,
              path: newHistory[lastIndex].path || currentPathRef.current || '/'
            }
          }
          return newHistory
        })
      })
      
      if (data.aria_message) {
        setAriaMessage(data.aria_message)
      }
      
      if (data.aria_choices && data.aria_choices.length > 0) {
        setAriaChoices(data.aria_choices)
      } else {
        setAriaChoices([])
      }
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
      if (data.dirs) {
        setAvailableDirs(data.dirs)
      }
    } else if (data.type === 'filesystem_update') {
      if (data.filesystem) {
        setFilesystem(data.filesystem)
        const pathToUse = data.current_path || currentPathRef.current || '/'
        const { dirs, files } = getDirsAndFiles(getPathContents(data.filesystem, pathToUse, ''))
        setAvailableDirs(dirs)
        setAvailableFiles(files)
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
    
    const fileCommands = ['ACCESS', 'DECODE', 'CAT', 'NVIM', 'ENCRYPT', 'DECRYPT']
    const dirCommands = ['CD', 'LS']
    const navCommands = [...fileCommands, ...dirCommands]
    
    if (navCommands.includes(command)) {
      let dirPath = ''
      let prefix = ''
      
      if (arg.includes('/')) {
        const lastSlash = arg.lastIndexOf('/')
        dirPath = arg.substring(0, lastSlash + 1)
        prefix = arg.substring(lastSlash + 1).toLowerCase()
      } else {
        dirPath = ''
        prefix = arg.toLowerCase()
      }
      
      const targetPath = dirPath || '.'
      const contents = getPathContents(filesystem, currentPath, targetPath === '.' ? '' : targetPath)
      
      if (!contents) {
        return dirCommands.includes(command) ? ['../'] : []
      }
      
      const { dirs, files } = getDirsAndFiles(contents)
      let options = []
      
      if (dirCommands.includes(command)) {
        options = [...dirs]
        if (!dirPath) {
          options = ['../', ...options]
        }
      } else {
        options = [...dirs, ...files]
      }
      
      if (prefix) {
        options = options.filter(item => 
          item.toLowerCase().startsWith(prefix)
        )
      }
      
      return options.map(opt => dirPath + opt)
    }
    
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
    
    if (command && !arg) {
      const upper = command.toUpperCase()
      return unlockedCommands.filter(cmd => 
        cmd.startsWith(upper) && cmd !== upper
      )
    }
    
    return []
  }, [filesystem, currentPath, unlockedCommands])

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
        path: currentPathRef.current || '/',
        username: localStorage.getItem('system_void_username') || null,
        timestamp: new Date().toISOString()
      }])
      return
    }

    const token = localStorage.getItem('system_void_token')
    wsSendCommand('', token, password)
      return
    }
    
    const userCommand = command.trim()
    if (!userCommand) {
      const message = language === 'FR'
        ? "Commande inconnue. Accès refusé.\n\nTapez HELP pour voir les commandes disponibles."
        : "Unknown command. Access denied.\n\nType HELP to see available commands."
      addToHistory('system', message)
      return
    }
    
    const userCommandUpper = userCommand.toUpperCase()
    
    if (userCommandUpper === 'CLEAR') {
      setHistory([])
      setCommandHistory(prev => {
        const newHistory = [...prev]
        if (newHistory[newHistory.length - 1] !== userCommand) {
          newHistory.push(userCommand)
        }
        return newHistory.slice(-50)
      })
      setHistoryIndex(-1)
      setInput('')
      setAutocompleteOptions([])
      setIsTyping(false)
      return
    }
    
    addToHistory('user', userCommand)
    setCommandHistory(prev => {
      const newHistory = [...prev]
      if (newHistory[newHistory.length - 1] !== userCommand) {
        newHistory.push(userCommand)
      }
      return newHistory.slice(-50)
    })
    setHistoryIndex(-1)
    
    if (userCommandUpper === 'MAN' || userCommandUpper.startsWith('MAN ')) {
      setInput('')
      setAutocompleteOptions([])
      setIsTyping(false)
      return
    }
    
    setInput('')
    setAutocompleteOptions([])

    if (!isConnected) {
      setHistory(prev => [...prev, {
        type: 'system',
        content: 'ERROR: WebSocket not connected. Please wait...',
        path: currentPathRef.current || '/',
        username: localStorage.getItem('system_void_username') || null,
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
        path: currentPathRef.current || '/',
        username: localStorage.getItem('system_void_username') || null,
        timestamp: new Date().toISOString()
      }])
    }
  }, [addToHistory, isTyping, isConnected, wsSendCommand, isPasswordMode])

  const navigateHistory = useCallback((direction, currentInput = '') => {
    if (commandHistory.length === 0) return
    
    const isManualInput = currentInput !== '' && currentInput === lastManualInputRef.current
    const shouldFilter = isManualInput && currentInput.trim() !== ''
    
    let historyToUse = commandHistory
    let useFiltered = false
    
    if (shouldFilter) {
      const inputPrefix = currentInput.trim().toUpperCase()
      const filtered = commandHistory.filter(cmd => 
        cmd.toUpperCase().startsWith(inputPrefix)
      )
      if (filtered.length > 0) {
        historyToUse = filtered
        useFiltered = true
      }
    }
    
    if (historyToUse.length === 0) return
    
    let currentIndex = historyIndex
    if (useFiltered && historyIndex !== -1) {
      const currentCommand = commandHistory[historyIndex]
      currentIndex = historyToUse.findIndex(cmd => cmd === currentCommand)
      if (currentIndex === -1) {
        currentIndex = historyIndex
      }
    }
    
    let newIndex
    if (direction === 'up') {
      if (useFiltered) {
        if (currentIndex === -1) {
          newIndex = historyToUse.length - 1
        } else {
          newIndex = Math.max(0, currentIndex - 1)
        }
      } else {
        if (historyIndex === -1) {
          newIndex = commandHistory.length - 1
        } else {
          newIndex = Math.max(0, historyIndex - 1)
        }
      }
    } else if (direction === 'down') {
      if (useFiltered) {
        if (currentIndex === -1) {
          return
        } else {
          newIndex = currentIndex + 1
          if (newIndex >= historyToUse.length) {
            newIndex = -1
          }
        }
      } else {
        if (historyIndex === -1) {
          return
        } else {
          newIndex = historyIndex + 1
          if (newIndex >= commandHistory.length) {
            newIndex = -1
          }
        }
      }
    }
    
    if (newIndex === -1) {
      setHistoryIndex(-1)
      if (shouldFilter) {
        setInput(currentInput)
      } else {
        setInput('')
      }
      lastManualInputRef.current = ''
    } else {
      let selectedCommand
      if (useFiltered) {
        selectedCommand = historyToUse[newIndex]
        const actualIndex = commandHistory.findIndex(cmd => cmd === selectedCommand)
        setHistoryIndex(actualIndex)
      } else {
        selectedCommand = commandHistory[newIndex]
        setHistoryIndex(newIndex)
      }
      setInput(selectedCommand)
      lastManualInputRef.current = ''
    }
  }, [commandHistory, historyIndex])

  const handleTab = useCallback((currentInput, shiftKey = false) => {
    if (!currentInput) {
      setAutocompleteOptions([])
      setAutocompleteIndex(-1)
      return false
    }
    
    const trimmed = currentInput.trim()
    if (!trimmed) {
      setAutocompleteOptions([])
      setAutocompleteIndex(-1)
      return false
    }
    
    const options = getAutocompleteOptions(currentInput)
    
    if (options.length === 0) {
      setAutocompleteOptions([])
      setAutocompleteIndex(-1)
      return false
    }
    
    if (options.length === 1) {
      selectAutocompleteOption(currentInput, options[0])
      return true
    }
    
    if (autocompleteOptions.length > 0 && JSON.stringify(autocompleteOptions) === JSON.stringify(options)) {
      if (shiftKey) {
        setAutocompleteIndex(prev => prev <= 0 ? options.length - 1 : prev - 1)
      } else {
        setAutocompleteIndex(prev => prev >= options.length - 1 ? 0 : prev + 1)
      }
    } else {
      setAutocompleteOptions(options)
      setAutocompleteIndex(0)
    }
    
    return true
  }, [getAutocompleteOptions, autocompleteOptions])

  const selectAutocompleteOption = useCallback((currentInput, option) => {
    const parts = currentInput.trim().split(/\s+/)
    const command = parts[0]?.toUpperCase() || ''
    const arg = parts.slice(1).join(' ') || ''
    
    const fileCommands = ['ACCESS', 'DECODE', 'CAT', 'NVIM', 'ENCRYPT', 'DECRYPT']
    const dirCommands = ['CD', 'LS']
    const allNavCommands = [...fileCommands, ...dirCommands]
    
    if (allNavCommands.includes(command)) {
      setInput(`${command} ${option}`)
    } else if (command === 'MAN') {
      setInput(`MAN ${option}`)
    } else if (command === 'PKG') {
      const subcommand = arg.split(' ')[0]?.toUpperCase()
      if (subcommand === 'INSTALL' || subcommand === 'UNINSTALL') {
        setInput(`${command} ${subcommand} ${option}`)
      } else {
        setInput(`${command} ${option}`)
      }
    } else {
      setInput(option)
    }
    setAutocompleteOptions([])
    setAutocompleteIndex(-1)
  }, [])

  const navigateAutocomplete = useCallback((direction) => {
    if (autocompleteOptions.length === 0) return false
    
    if (direction === 'up' || direction === 'left') {
      setAutocompleteIndex(prev => prev <= 0 ? autocompleteOptions.length - 1 : prev - 1)
    } else if (direction === 'down' || direction === 'right') {
      setAutocompleteIndex(prev => prev >= autocompleteOptions.length - 1 ? 0 : prev + 1)
    }
    return true
  }, [autocompleteOptions])

  const confirmAutocomplete = useCallback(() => {
    if (autocompleteOptions.length > 0 && autocompleteIndex >= 0) {
      selectAutocompleteOption(input, autocompleteOptions[autocompleteIndex])
      return true
    }
    return false
  }, [autocompleteOptions, autocompleteIndex, input, selectAutocompleteOption])

  const cancelAutocomplete = useCallback(() => {
    setAutocompleteOptions([])
    setAutocompleteIndex(-1)
  }, [])

  const resetHistoryIndex = useCallback(() => {
    setHistoryIndex(-1)
  }, [])

  const updateManualInput = useCallback((value) => {
    lastManualInputRef.current = value
  }, [])

  const sendAriaChoice = useCallback((choiceId) => {
    setAriaChoices([])
    sendCommand(choiceId)
  }, [sendCommand])

  const clearAriaChoices = useCallback(() => {
    setAriaChoices([])
  }, [])

  return {
    history,
    input,
    setInput,
    isTyping,
    sendCommand,
    navigateHistory,
    handleTab,
    autocompleteOptions,
    autocompleteIndex,
    confirmAutocomplete,
    cancelAutocomplete,
    installedPackages,
    isPasswordMode,
    passwordUsername,
    currentPath,
    resetHistoryIndex,
    updateManualInput,
    ariaChoices,
    sendAriaChoice,
    clearAriaChoices,
    ariaMessage,
    clearAriaMessage: () => setAriaMessage(null),
    navigateAutocomplete,
    hasAutocompleteOptions: autocompleteOptions.length > 0,
    isAdminMode
  }
}

