import { useState, useEffect, useCallback } from 'react'
import { ARIA_STATES } from '../assets/aria_ascii'

const AriaFloatingPanel = ({ 
  message, 
  emotion = 'neutral', 
  choices = [], 
  onChoice, 
  onClose,
  visible = false 
}) => {
  const [currentFrame, setCurrentFrame] = useState(0)
  const [displayedText, setDisplayedText] = useState('')
  const [isTyping, setIsTyping] = useState(false)

  const getAriaArt = useCallback(() => {
    if (isTyping) {
      const frames = ARIA_STATES.speaking
      if (Array.isArray(frames)) {
        return frames[currentFrame % frames.length]
      }
    }
    
    if (emotion && ARIA_STATES[emotion]) {
      const art = ARIA_STATES[emotion]
      if (Array.isArray(art)) {
        return art[currentFrame % art.length]
      }
      return art
    }
    
    return ARIA_STATES.neutral || ARIA_STATES.dormant
  }, [emotion, currentFrame, isTyping])

  useEffect(() => {
    if (isTyping) {
      const interval = setInterval(() => {
        setCurrentFrame(prev => prev + 1)
      }, 250)
      return () => clearInterval(interval)
    }
  }, [isTyping])

  useEffect(() => {
    if (!message || !visible) {
      setDisplayedText('')
      return
    }

    const cleanMessage = message.replace(/\[ARIA\]\n?/g, '').trim()
    setIsTyping(true)
    setDisplayedText('')
    let index = 0
    const charsPerTick = 3

    const typingInterval = setInterval(() => {
      if (index < cleanMessage.length) {
        index = Math.min(index + charsPerTick, cleanMessage.length)
        setDisplayedText(cleanMessage.substring(0, index))
      } else {
        clearInterval(typingInterval)
        setIsTyping(false)
        
        if (choices.length === 0) {
          const autoCloseTimer = setTimeout(() => {
            onClose && onClose()
          }, 5000)
          return () => clearTimeout(autoCloseTimer)
        }
      }
    }, 20)

    return () => clearInterval(typingInterval)
  }, [message, visible, choices.length, onClose])

  const handleKeyDown = useCallback((e) => {
    if (e.key === 'Escape' || e.key === 'q' || e.key === 'Q') {
      onClose && onClose()
    }
  }, [onClose])

  useEffect(() => {
    if (visible) {
      window.addEventListener('keydown', handleKeyDown)
      return () => window.removeEventListener('keydown', handleKeyDown)
    }
  }, [visible, handleKeyDown])

  if (!visible || !message) {
    return null
  }

  return (
    <div className="aria-notification-container">
      <div className="aria-notification">
        <div className="aria-notification-header">
          <span className="aria-notification-status">● ARIA</span>
          <button className="aria-notification-close" onClick={onClose}>×</button>
        </div>
        
        <div className="aria-notification-content">
          <div className="aria-notification-message">
            <span className="aria-notification-prefix">[ARIA]</span>
            <span className="aria-notification-text">{displayedText}</span>
            {isTyping && <span className="aria-typing-cursor">▊</span>}
          </div>

          {choices.length > 0 && !isTyping && (
            <div className="aria-notification-choices">
              {choices.map((choice, idx) => (
                <button
                  key={idx}
                  className="aria-notification-choice-btn"
                  onClick={() => onChoice && onChoice(choice.id)}
                >
                  &gt; {choice.label}
                </button>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default AriaFloatingPanel
