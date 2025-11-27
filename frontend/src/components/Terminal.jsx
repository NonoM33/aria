import { useEffect, useRef, useState, useCallback } from 'react'
import { useTerminal } from '../hooks/useTerminal'
import { useLanguage } from '../contexts/LanguageContext'
import LanguageMenu from './LanguageMenu'
import ManPage from './ManPage'
import FileViewer from './FileViewer'
import AriaDisplay from './AriaDisplay'
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
    installedPackages,
    isPasswordMode,
    passwordUsername
  } = useTerminal()
  const { language } = useLanguage()
  const inputRef = useRef(null)
  const historyEndRef = useRef(null)
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
  const [ariaState, setAriaState] = useState('dormant')
  const [ariaEmotion, setAriaEmotion] = useState('neutral')
  const [ariaSpeaking, setAriaSpeaking] = useState(false)
  const [ariaMinimized, setAriaMinimized] = useState(true)
  const [glitchActive, setGlitchActive] = useState(false)

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
    if (!isTyping) {
      historyEndRef.current?.scrollIntoView({ behavior: 'smooth' })
    }
  }, [history, isTyping])

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
    // Ne pas traiter les touches si la modal MAN ou FileViewer est ouverte
    if (manPageCommand || fileViewerData) {
      return
    }
    if (isTyping) return

    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    } else if (e.key === 'ArrowUp' && !isPasswordMode) {
      e.preventDefault()
      navigateHistory('up')
    } else if (e.key === 'ArrowDown' && !isPasswordMode) {
      e.preventDefault()
      navigateHistory('down')
    } else if (e.key === 'Tab' && !isPasswordMode) {
      e.preventDefault()
      handleTab(input)
    } else if (e.key === 'Escape') {
      e.preventDefault()
      setInput('')
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

  useEffect(() => {
    const lastSystemResponse = history.filter(e => e.type === 'system').slice(-1)[0]
    if (lastSystemResponse && lastSystemResponse.content) {
      const content = lastSystemResponse.content
      
      if (content.includes('[ARIA]') || content.includes('aria_state') || content.includes('aria_emotion')) {
        setAriaMinimized(false)
        setAriaState('neutral')
        setAriaSpeaking(true)
        setGlitchActive(true)
        
        setTimeout(() => setGlitchActive(false), 300)
        
        if (content.includes('triste') || content.includes('sad')) {
          setAriaEmotion('sad')
        } else if (content.includes('heureuse') || content.includes('happy') || content.includes('grateful') || content.includes('reconnaissante')) {
          setAriaEmotion('happy')
        } else if (content.includes('peur') || content.includes('scared') || content.includes('effrayée')) {
          setAriaEmotion('scared')
        } else if (content.includes('colère') || content.includes('angry') || content.includes('en colère')) {
          setAriaEmotion('angry')
        } else if (content.includes('espoir') || content.includes('hopeful')) {
          setAriaEmotion('hopeful')
        } else if (content.includes('déterminée') || content.includes('determined')) {
          setAriaEmotion('determined')
        } else {
          setAriaEmotion('neutral')
        }
        
        setTimeout(() => setAriaSpeaking(false), 3000)
      }
      
      if (content.includes('HORS LIGNE') || content.includes('OFFLINE') || content.includes('dormant')) {
        setAriaState('dormant')
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

  return (
    <div className="terminal-container">
      <div className="scanlines"></div>
      <LanguageMenu />
      {manPageCommand && (
        <ManPage 
          command={manPageCommand} 
          onClose={() => setManPageCommand(null)} 
        />
      )}
      {fileViewerData && (
        <FileViewer
          filename={fileViewerData.filename}
          content={fileViewerData.content}
          onClose={() => setFileViewerData(null)}
        />
      )}
      <div className="terminal-content">
        <div className="terminal-history">
          {history.map((entry, index) => (
            <div key={index} className={`terminal-entry terminal-entry-${entry.type}`}>
              {entry.type === 'user' && (
                <div className="terminal-line">
                  <span className="prompt">
                    {username ? `${username}@system-void > ` : '> '}
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
            <div className="terminal-input-line">
              <span className="prompt">
                {isPasswordMode ? `${passwordUsername || 'user'}@system-void.local's password: ` : (username ? `${username}@system-void > ` : '> ')}
              </span>
              <input
                ref={inputRef}
                type={isPasswordMode ? "password" : "text"}
                value={input}
                onChange={(e) => setInput(e.target.value)}
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
          )}
          {isTyping && (
            <div className="terminal-input-line">
              <span className="prompt">
                {username ? `${username}@system-void > ` : '> '}
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

