import { useEffect, useRef, useState, useCallback } from 'react'
import { useTerminal } from '../hooks/useTerminal'
import { useLanguage } from '../contexts/LanguageContext'
import LanguageMenu from './LanguageMenu'
import ManPage from './ManPage'
import FileViewer from './FileViewer'
import AriaFloatingPanel from './AriaFloatingPanel'
import IntroSequence from './IntroSequence'

const Terminal = () => {
  const { 
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
    ariaMessage,
    clearAriaMessage,
    navigateAutocomplete,
    hasAutocompleteOptions
  } = useTerminal()
  const { language } = useLanguage()
  const inputRef = useRef(null)
  const historyEndRef = useRef(null)
  const terminalContentRef = useRef(null)
  const [showInput, setShowInput] = useState(true)
  const [welcomeShown, setWelcomeShown] = useState(false)
  const [manPageCommand, setManPageCommand] = useState(null)
  const [fileViewerData, setFileViewerData] = useState(null)
  const [username, setUsername] = useState(() => {
    return localStorage.getItem('system_void_username') || null
  })
  const [showIntro, setShowIntro] = useState(() => {
    const introSeen = localStorage.getItem('system_void_intro_seen')
    return introSeen !== 'true'
  })
  const [glitchActive, setGlitchActive] = useState(false)
  const [ariaFloatingVisible, setAriaFloatingVisible] = useState(false)
  const [ariaFloatingMessage, setAriaFloatingMessage] = useState('')
  const [ariaFloatingEmotion, setAriaFloatingEmotion] = useState('neutral')

  const welcomeSentRef = useRef(false)
  const languageRef = useRef(language)
  const sendCommandRef = useRef(sendCommand)
  
  useEffect(() => {
    const checkUsername = () => {
      const storedUsername = localStorage.getItem('system_void_username')
      const newUsername = storedUsername || null
      if (newUsername !== username) {
        setUsername(newUsername)
      }
    }
    
    checkUsername()
    const interval = setInterval(checkUsername, 50)
    
    const handleStorageChange = (e) => {
      if (e.key === 'system_void_username' || !e.key) {
        const storedUsername = localStorage.getItem('system_void_username')
        setUsername(storedUsername || null)
      }
    }
    
    window.addEventListener('storage', handleStorageChange)
    
    const handleCustomStorageChange = () => {
      const storedUsername = localStorage.getItem('system_void_username')
      const newUsername = storedUsername || null
      setUsername(newUsername)
    }
    
    window.addEventListener('localStorageChange', handleCustomStorageChange)
    
    return () => {
      clearInterval(interval)
      window.removeEventListener('storage', handleStorageChange)
      window.removeEventListener('localStorageChange', handleCustomStorageChange)
    }
  }, [username])

  // Mettre à jour la ref de sendCommand
  useEffect(() => {
    sendCommandRef.current = sendCommand
  }, [sendCommand])

  // Envoyer le welcome une seule fois au démarrage
  useEffect(() => {
    if (!welcomeSentRef.current && history.length === 0) {
      welcomeSentRef.current = true
      languageRef.current = language
      const timer = setTimeout(() => {
        sendCommandRef.current('')
        setWelcomeShown(true)
      }, 500)
      return () => clearTimeout(timer)
    }
  }, [history.length]) // Seulement dépendre de history.length

  // Quand la langue change après l'initialisation, réafficher le welcome
  useEffect(() => {
    if (welcomeSentRef.current && languageRef.current !== language && history.length > 0) {
      languageRef.current = language
      const timer = setTimeout(() => {
        sendCommandRef.current('')
      }, 100)
      return () => clearTimeout(timer)
    }
  }, [language, history.length]) // Dépendre de language et history.length

  useEffect(() => {
    if (ariaMessage) {
      setAriaFloatingMessage(ariaMessage)
      setAriaFloatingEmotion('neutral')
      setAriaFloatingVisible(true)
    }
  }, [ariaMessage])

  useEffect(() => {
    if (isPasswordMode) {
      setShowInput(true)
      setTimeout(() => {
        if (inputRef.current) {
          inputRef.current.focus()
          inputRef.current.select()
        }
      }, 100)
    }
  }, [isPasswordMode])

  useEffect(() => {
    const handlePasswordPrompt = () => {
      setShowInput(true)
      setTimeout(() => {
        if (inputRef.current) {
          inputRef.current.focus()
          inputRef.current.select()
        }
      }, 150)
    }
    
    window.addEventListener('passwordPrompt', handlePasswordPrompt)
    return () => window.removeEventListener('passwordPrompt', handlePasswordPrompt)
  }, [])

  useEffect(() => {
    if (inputRef.current && !isTyping && showInput) {
      const timer = setTimeout(() => {
        if (inputRef.current && showInput) {
          inputRef.current.focus()
          if (isPasswordMode) {
            inputRef.current.select()
          }
        }
      }, isPasswordMode ? 250 : 50)
      return () => clearTimeout(timer)
    }
  }, [history, isTyping, isPasswordMode, showInput])

  useEffect(() => {
    if (terminalContentRef.current) {
      requestAnimationFrame(() => {
        if (terminalContentRef.current) {
          terminalContentRef.current.scrollTop = terminalContentRef.current.scrollHeight
        }
      })
    }
  }, [history])

  const handleSubmit = (e) => {
    e.preventDefault()
    if (isTyping) return
    
    if (isPasswordMode) {
      const password = input
      sendCommand(password)
      setInput('')
      return
    }
    
    if (input.trim()) {
      const command = input.trim()
      sendCommand(command)
      setInput('')
      setShowInput(false)
      setTimeout(() => {
        setShowInput(true)
        inputRef.current?.focus()
      }, 100)
    }
  }

  const handleKeyDown = (e) => {
    if (manPageCommand || fileViewerData) {
      return
    }
    if (isTyping) return

    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      if (autocompleteOptions.length > 0 && autocompleteIndex >= 0) {
        confirmAutocomplete()
      } else {
        handleSubmit(e)
      }
    } else if (e.key === 'ArrowUp' && !isPasswordMode) {
      e.preventDefault()
      if (hasAutocompleteOptions) {
        navigateAutocomplete('up')
      } else {
        navigateHistory('up', input)
      }
    } else if (e.key === 'ArrowDown' && !isPasswordMode) {
      e.preventDefault()
      if (hasAutocompleteOptions) {
        navigateAutocomplete('down')
      } else {
        navigateHistory('down', input)
      }
    } else if (e.key === 'ArrowLeft' && hasAutocompleteOptions && !isPasswordMode) {
      e.preventDefault()
      navigateAutocomplete('left')
    } else if (e.key === 'ArrowRight' && hasAutocompleteOptions && !isPasswordMode) {
      e.preventDefault()
      navigateAutocomplete('right')
    } else if (e.key === 'Tab' && !isPasswordMode) {
      e.preventDefault()
      handleTab(input, e.shiftKey)
    } else if (e.key === 'Escape') {
      e.preventDefault()
      if (hasAutocompleteOptions) {
        cancelAutocomplete()
      } else {
        setInput('')
      }
    }
  }

  useEffect(() => {
    const lastUserCommand = history.filter(e => e.type === 'user').slice(-1)[0]
    if (lastUserCommand && lastUserCommand.content.toUpperCase().startsWith('MAN ')) {
      const command = lastUserCommand.content.split(' ')[1]?.toUpperCase()
      if (command) {
        setManPageCommand(command)
      }
    }
  }, [history])

  
  const handleIntroComplete = useCallback(() => {
    localStorage.setItem('system_void_intro_seen', 'true')
    setShowIntro(false)
  }, [])

  useEffect(() => {
    if (isTyping) {
      return
    }
    
    const timeoutId = setTimeout(() => {
      const hasFileViewer = Array.isArray(installedPackages) && installedPackages.includes('file-viewer')
      
      if (!hasFileViewer) {
        if (fileViewerData) {
          setFileViewerData(null)
        }
        return
      }
      
      const lastUserCommand = history.filter(e => e.type === 'user').slice(-1)[0]
      const lastSystemResponse = history.filter(e => e.type === 'system').slice(-1)[0]
      
      if (!lastUserCommand || !lastUserCommand.content.toUpperCase().startsWith('ACCESS ')) {
        if (fileViewerData) {
          setFileViewerData(null)
        }
        return
      }
      
      if (!lastSystemResponse || !lastSystemResponse.content) {
        return
      }
      
      const responseContent = lastSystemResponse.content
      const filename = lastUserCommand.content.split(' ').slice(1).join(' ').trim()
      
      if (!filename) {
        return
      }
      
      if (responseContent.includes('Fichier:') || responseContent.includes('File:')) {
        const lines = responseContent.split('\n')
        let fileContent = ''
        let inFileContent = false
        let skipNextEmpty = false
        let fileHeaderFound = false
        
        for (let i = 0; i < lines.length; i++) {
          const line = lines[i]
          
          if ((line.includes('Fichier:') || line.includes('File:')) && !fileHeaderFound) {
            fileHeaderFound = true
            inFileContent = true
            skipNextEmpty = true
            continue
          }
          
          if (inFileContent) {
            if (line.trim() === '' && skipNextEmpty) {
              skipNextEmpty = false
              continue
            }
            
            if (line.includes('[Indice:') || line.includes('[Hint:') || 
                (line.trim().startsWith('[') && line.includes(']') && 
                 (line.includes('Indice') || line.includes('Hint') || line.includes('Utilisez') || line.includes('Use')))) {
              break
            }
            
            fileContent += line + '\n'
            skipNextEmpty = false
          }
        }
        
        const trimmedContent = fileContent.trim()
        if (trimmedContent && trimmedContent.length > 0) {
          const newFileViewerData = {
            filename: filename,
            content: trimmedContent
          }
          
          if (!fileViewerData || fileViewerData.filename !== filename || fileViewerData.content !== trimmedContent) {
            setFileViewerData(newFileViewerData)
          }
        } else if (fileViewerData && fileViewerData.filename === filename) {
          setFileViewerData(null)
        }
      } else if (fileViewerData && fileViewerData.filename === filename) {
        setFileViewerData(null)
      }
    }, 100)
    
    return () => clearTimeout(timeoutId)
  }, [history, installedPackages, isTyping])

  if (showIntro) {
    return (
      <IntroSequence 
        language={language}
        onComplete={handleIntroComplete}
        skipIntro={false}
      />
    )
  }

  return (
    <div className={`terminal-container ${glitchActive ? 'terminal-glitch' : ''}`}>
      <div className="scanlines"></div>
      <LanguageMenu />
      {manPageCommand && (
        <ManPage 
          command={manPageCommand} 
          onClose={() => {
            setManPageCommand(null)
            setTimeout(() => {
              if (inputRef.current) {
                inputRef.current.focus()
              }
            }, 100)
          }} 
        />
      )}
      {fileViewerData && (
        <FileViewer
          filename={fileViewerData.filename}
          content={fileViewerData.content}
          onClose={() => {
            setFileViewerData(null)
            setTimeout(() => {
              if (inputRef.current) {
                inputRef.current.focus()
              }
            }, 100)
          }}
        />
      )}
      <AriaFloatingPanel
        message={ariaFloatingMessage}
        emotion={ariaFloatingEmotion}
        choices={ariaChoices}
        onChoice={(id) => {
          sendAriaChoice(id)
          setAriaFloatingVisible(false)
          clearAriaMessage()
          inputRef.current?.focus()
        }}
        onClose={() => {
          setAriaFloatingVisible(false)
          clearAriaMessage()
        }}
        visible={ariaFloatingVisible}
      />
      <div className="terminal-content" ref={terminalContentRef}>
        <div className="terminal-history">
          {history.map((entry, index) => (
            <div key={index} className={`terminal-entry terminal-entry-${entry.type}`}>
              {entry.type === 'user' && (
                <div className="terminal-line">
                  <span className="prompt">
                    {username ? `${username}@system-void:${entry.path || currentPath}$ ` : `guest:${entry.path || currentPath}$ `}
                  </span>
                  <span className="terminal-text">{entry.content}</span>
                </div>
              )}
              {entry.type === 'system' && (
                <div className="terminal-line">
                  <span className="terminal-text">{entry.content}</span>
                </div>
              )}
            </div>
          ))}
          {showInput && !isTyping && (
            <>
              <div className="terminal-input-line">
                <span className={`prompt ${isAdminMode ? 'admin-prompt' : ''}`}>
                  {isPasswordMode 
                    ? `${passwordUsername || 'user'}@system-void.local's password: ` 
                    : isAdminMode 
                      ? `root@system-void# ` 
                      : (username ? `${username}@system-void:${currentPath}$ ` : `guest:${currentPath}$ `)}
                </span>
                <input
                  ref={inputRef}
                  type={isPasswordMode ? "password" : "text"}
                  value={input}
                  onChange={(e) => {
                    const newValue = e.target.value
                    setInput(newValue)
                    cancelAutocomplete()
                    resetHistoryIndex()
                    updateManualInput(newValue)
                  }}
                  onKeyDown={handleKeyDown}
                  disabled={isTyping}
                  className="terminal-input-inline"
                  autoFocus
                  autoComplete="off"
                  spellCheck="false"
                  placeholder={isPasswordMode ? "" : ""}
                />
                <span className="cursor"></span>
              </div>
              {autocompleteOptions.length > 0 && (
                <div className="autocomplete-menu">
                  {autocompleteOptions.map((option, idx) => (
                    <span
                      key={idx}
                      className={`autocomplete-option ${idx === autocompleteIndex ? 'autocomplete-selected' : ''}`}
                      onClick={() => {
                        const parts = input.trim().split(/\s+/)
                        const command = parts[0]?.toUpperCase() || ''
                        const fileCommands = ['ACCESS', 'DECODE', 'CAT', 'NVIM', 'ENCRYPT', 'DECRYPT', 'CD', 'LS']
                        if (fileCommands.includes(command)) {
                          setInput(`${command} ${option}`)
                        } else if (command === 'MAN') {
                          setInput(`MAN ${option}`)
                        } else {
                          setInput(option)
                        }
                        cancelAutocomplete()
                        inputRef.current?.focus()
                      }}
                    >
                      {option.split('/').filter(p => p).pop() || option}{option.endsWith('/') ? '/' : ''}
                    </span>
                  ))}
                </div>
              )}
            </>
          )}
          {isTyping && (
            <div className="terminal-input-line">
              <span className="prompt">
                {username ? `${username}@system-void:${currentPath}$ ` : `guest:${currentPath}$ `}
              </span>
              <span className="cursor"></span>
            </div>
          )}
          <div ref={historyEndRef} />
        </div>
      </div>
    </div>
  )
}

export default Terminal

