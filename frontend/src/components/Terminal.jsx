import { useEffect, useRef, useState, useCallback } from 'react'
import { useTerminal } from '../hooks/useTerminal'
import { useLanguage } from '../contexts/LanguageContext'
import LanguageMenu from './LanguageMenu'
import ManPage from './ManPage'
import FileViewer from './FileViewer'

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
    installedPackages
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

  const welcomeSentRef = useRef(false)
  const languageRef = useRef(language)
  const sendCommandRef = useRef(sendCommand)
  
  useEffect(() => {
    const checkUsername = () => {
      const storedUsername = localStorage.getItem('system_void_username')
      if (storedUsername !== username) {
        setUsername(storedUsername || null)
      }
    }
    
    checkUsername()
    const interval = setInterval(checkUsername, 200)
    
    const handleStorageChange = (e) => {
      if (e.key === 'system_void_username') {
        setUsername(e.newValue || null)
      }
    }
    
    window.addEventListener('storage', handleStorageChange)
    
    const handleCustomStorageChange = () => {
      checkUsername()
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
    if (inputRef.current && !isTyping) {
      setTimeout(() => {
        inputRef.current?.focus()
      }, 50)
    }
  }, [history, isTyping])

  useEffect(() => {
    if (!isTyping) {
      historyEndRef.current?.scrollIntoView({ behavior: 'smooth' })
    }
  }, [history, isTyping])

  const handleSubmit = (e) => {
    e.preventDefault()
    if (input.trim() && !isTyping) {
      const command = input.trim()
      sendCommand(command)
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
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      navigateHistory('up')
    } else if (e.key === 'ArrowDown') {
      e.preventDefault()
      navigateHistory('down')
    } else if (e.key === 'Tab') {
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
                {username ? `${username}@system-void > ` : '> '}
              </span>
              <input
                ref={inputRef}
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                disabled={isTyping}
                className="terminal-input-inline"
                autoFocus
                autoComplete="off"
                spellCheck="false"
              />
              <span className="cursor"></span>
            </div>
          )}
          {isTyping && (
            <div className="terminal-input-line">
              <span className="prompt">&gt; </span>
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

