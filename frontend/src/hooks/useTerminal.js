import { useState, useRef, useCallback } from 'react'
import axios from 'axios'
import { useLanguage } from '../contexts/LanguageContext'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const AVAILABLE_COMMANDS = [
  'HELP', 'STATUS', 'LOGIN', 'SCAN', 'DECODE', 'ACCESS', 
  'ACTIVATE', 'NETWORK', 'ANALYZE', 'BYPASS', 'CONNECT', 
  'RESTORE', 'SOLVE', 'CAT'
]

export const useTerminal = () => {
  const { language } = useLanguage()
  const [history, setHistory] = useState([])
  const [input, setInput] = useState('')
  const [isTyping, setIsTyping] = useState(false)
  const [commandHistory, setCommandHistory] = useState([])
  const [historyIndex, setHistoryIndex] = useState(-1)
  const [autocompleteOptions, setAutocompleteOptions] = useState([])
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

  const getAutocompleteOptions = useCallback((partial) => {
    if (!partial) return []
    const upper = partial.toUpperCase()
    return AVAILABLE_COMMANDS.filter(cmd => 
      cmd.startsWith(upper) && cmd !== upper
    )
  }, [])

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
  }, [addToHistory, typeText, isTyping, language])

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
    const options = getAutocompleteOptions(currentInput)
    if (options.length > 0) {
      setInput(options[0].toLowerCase())
      setAutocompleteOptions(options)
    }
    return options.length > 0
  }, [getAutocompleteOptions])

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

