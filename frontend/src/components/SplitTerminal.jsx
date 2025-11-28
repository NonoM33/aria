import { useState, useRef, useEffect } from 'react'
import Terminal from './Terminal'

const SplitTerminal = ({ onClose, terminalId, sessionId }) => {
  const [isActive, setIsActive] = useState(false)
  const splitRef = useRef(null)

  useEffect(() => {
    setIsActive(true)
    if (splitRef.current) {
      splitRef.current.focus()
    }
  }, [])

  const handleFocus = () => {
    setIsActive(true)
  }

  const handleBlur = () => {
    setIsActive(false)
  }

  const handleClick = () => {
    setIsActive(true)
    if (splitRef.current) {
      splitRef.current.focus()
    }
  }

  return (
    <div 
      ref={splitRef}
      className={`split-terminal ${isActive ? 'active' : ''}`}
      onFocus={handleFocus}
      onBlur={handleBlur}
      onClick={handleClick}
      tabIndex={0}
    >
      <div className="split-terminal-header">
        <span className="split-terminal-title">Terminal {terminalId}</span>
        <button 
          className="split-terminal-close"
          onClick={(e) => {
            e.stopPropagation()
            onClose()
          }}
          title="Fermer (CTRL+W)"
        >
          ×
        </button>
      </div>
      <div className="split-terminal-content">
        <Terminal />
      </div>
    </div>
  )
}

export default SplitTerminal

