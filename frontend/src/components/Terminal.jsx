import { useEffect, useRef, useState } from 'react'
import { useTerminal } from '../hooks/useTerminal'
import { useLanguage } from '../contexts/LanguageContext'
import LanguageMenu from './LanguageMenu'
import ManPage from './ManPage'

const Terminal = () => {
  const { 
    history, 
    input, 
    setInput, 
    isTyping, 
    sendCommand, 
    navigateHistory, 
    handleTab,
    autocompleteOptions 
  } = useTerminal()
  const { language } = useLanguage()
  const inputRef = useRef(null)
  const historyEndRef = useRef(null)
  const [showInput, setShowInput] = useState(true)
  const [welcomeShown, setWelcomeShown] = useState(false)
  const [manPageCommand, setManPageCommand] = useState(null)

  useEffect(() => {
    if (!welcomeShown && history.length === 0) {
      setTimeout(() => {
        const currentLang = language || localStorage.getItem('system_void_language') || 'FR'
        sendCommand('')
        setWelcomeShown(true)
      }, 500)
    }
  }, [welcomeShown, history.length, sendCommand, language])

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
      <div className="terminal-content">
        <div className="terminal-history">
          {history.map((entry, index) => (
            <div key={index} className={`terminal-entry terminal-entry-${entry.type}`}>
              {entry.type === 'user' && (
                <div className="terminal-line">
                  <span className="prompt">&gt; </span>
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
              <span className="prompt">&gt; </span>
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

