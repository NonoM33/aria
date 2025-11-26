import { useState, useRef, useCallback, useEffect } from 'react'
import axios from 'axios'
import { useLanguage } from '../contexts/LanguageContext'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const AVAILABLE_COMMANDS = [
  'HELP', 'STATUS', 'LOGIN', 'SCAN', 'DECODE', 'ACCESS', 
  'ACTIVATE', 'NETWORK', 'ANALYZE', 'BYPASS', 'CONNECT', 
  'RESTORE', 'SOLVE', 'CAT', 'MAN', 'NVIM', 'SPLIT', 
  'PORTSCAN', 'BRUTEFORCE', 'JOBS'
]

export const useTerminal = () => {
  const { language } = useLanguage()
  const [history, setHistory] = useState([])
  const [input, setInput] = useState('')
  const [isTyping, setIsTyping] = useState(false)
  const [commandHistory, setCommandHistory] = useState([])
  const [historyIndex, setHistoryIndex] = useState(-1)
  const [autocompleteOptions, setAutocompleteOptions] = useState([])
  const [availableFiles, setAvailableFiles] = useState([])
  const sessionIdRef = useRef(
    localStorage.getItem('session_id') || 
    `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
  )

  if (!localStorage.getItem('session_id')) {
    localStorage.setItem('session_id', sessionIdRef.current)
  }

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        let currentLanguage = language || localStorage.getItem('system_void_language') || 'FR'
        currentLanguage = currentLanguage.toUpperCase()
        if (currentLanguage !== 'FR' && currentLanguage !== 'EN') {
          currentLanguage = 'FR'
        }
        
        const response = await axios.get(`${API_URL}/api/files`, {
          params: {
            session_id: sessionIdRef.current,
            language: currentLanguage
          }
        })
        if (response.data && response.data.files) {
          setAvailableFiles(response.data.files)
          console.log('Files loaded:', response.data.files)
        }
      } catch (error) {
        console.error('Error loading files:', error)
      }
    }
    
    fetchFiles()
    const interval = setInterval(fetchFiles, 5000)
    return () => clearInterval(interval)
  }, [language])

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

  const getAutocompleteOptions = useCallback((partial) => {
    if (!partial || !partial.trim()) return []
    
    const trimmed = partial.trim()
    const parts = trimmed.split(/\s+/)
    const command = parts[0]?.toUpperCase() || ''
    const arg = parts.slice(1).join(' ') || ''
    
    // Commandes qui prennent des noms de fichiers en argument
    const fileCommands = ['ACCESS', 'DECODE', 'CAT', 'NVIM', 'ENCRYPT', 'DECRYPT']
    
    // Auto-complétion pour les commandes de fichiers
    if (fileCommands.includes(command)) {
      if (arg) {
        const lowerArg = arg.toLowerCase()
        const matches = availableFiles.filter(file => 
          file.toLowerCase().startsWith(lowerArg) && file.toLowerCase() !== lowerArg
        )
        return matches
      } else {
        // Si juste "COMMANDE " (avec espace), retourner tous les fichiers
        return availableFiles.length > 0 ? availableFiles : []
      }
    }
    
    // Auto-complétion pour MAN <commande>
    if (command === 'MAN') {
      if (arg) {
        const upperArg = arg.toUpperCase()
        return AVAILABLE_COMMANDS.filter(cmd => 
          cmd.startsWith(upperArg) && cmd !== upperArg
        )
      } else {
        return AVAILABLE_COMMANDS
      }
    }
    
    // Auto-complétion pour les commandes simples
    if (command && !arg) {
      const upper = command.toUpperCase()
      return AVAILABLE_COMMANDS.filter(cmd => 
        cmd.startsWith(upper) && cmd !== upper
      )
    }
    
    return []
  }, [availableFiles])

  const sendCommand = useCallback(async (command) => {
    if (isTyping) return
    
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

    try {
      let currentLanguage = language || localStorage.getItem('system_void_language') || 'FR'
      currentLanguage = currentLanguage.toUpperCase()
      if (currentLanguage !== 'FR' && currentLanguage !== 'EN') {
        currentLanguage = 'FR'
      }
      
      const response = await axios.post(`${API_URL}/api/command`, {
        command: userCommand,
        session_id: sessionIdRef.current,
        language: currentLanguage
      })

      const systemResponse = response.data.response || 'No response from system.'
      
      // Mettre à jour les fichiers disponibles après SCAN ou LOGIN
      if (userCommand.toUpperCase().startsWith('SCAN') || userCommand.toUpperCase().startsWith('LOGIN')) {
        setTimeout(async () => {
          try {
            const fileResponse = await axios.get(`${API_URL}/api/files`, {
              params: {
                session_id: sessionIdRef.current,
                language: currentLanguage
              }
            })
            if (fileResponse.data && fileResponse.data.files) {
              setAvailableFiles(fileResponse.data.files)
              console.log('Files updated after command:', fileResponse.data.files)
            }
          } catch (error) {
            console.error('Error updating files:', error)
          }
        }, 100)
      }
      
      setHistory(prev => [...prev, {
        type: 'system',
        content: '',
        timestamp: new Date().toISOString()
      }])
      
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
    } catch (error) {
      const errorMessage = error.response?.data?.detail || error.message || 'Connection failed.'
      
      setHistory(prev => [...prev, {
        type: 'system',
        content: '',
        timestamp: new Date().toISOString()
      }])
      
      typeText(`ERROR: ${errorMessage}`, (partialText) => {
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
    }
  }, [addToHistory, typeText, isTyping, language, setAvailableFiles])

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
    
    const options = getAutocompleteOptions(trimmed)
    console.log('Tab pressed, input:', trimmed, 'options:', options, 'availableFiles:', availableFiles)
    
    if (options.length === 0) {
      return false
    }
    
    const parts = trimmed.split(/\s+/)
    const command = parts[0]?.toUpperCase() || ''
    const arg = parts.slice(1).join(' ') || ''
    
    // Commandes qui prennent des fichiers
    const fileCommands = ['ACCESS', 'DECODE', 'CAT', 'NVIM', 'ENCRYPT', 'DECRYPT']
    
    if (options.length === 1) {
      // Une seule option : compléter automatiquement
      if (fileCommands.includes(command)) {
        setInput(`${command} ${options[0]}`)
      } else if (command === 'MAN') {
        setInput(`MAN ${options[0]}`)
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
        if (arg) {
          // Si on a déjà tapé quelque chose, compléter avec le premier match
          setInput(`${command} ${options[0]}`)
        }
        addToHistory('system', `Fichiers disponibles: ${options.join(', ')}`)
      } else if (command === 'MAN') {
        if (arg) {
          setInput(`MAN ${options[0]}`)
        }
        addToHistory('system', `Commandes disponibles: ${options.join(', ')}`)
      } else {
        setInput(options[0])
        addToHistory('system', `Suggestions: ${options.join(', ')}`)
      }
      return true
    }
    
    return false
  }, [getAutocompleteOptions, addToHistory])

  return {
    history,
    input,
    setInput,
    isTyping,
    sendCommand,
    navigateHistory,
    handleTab,
    autocompleteOptions
  }
}

