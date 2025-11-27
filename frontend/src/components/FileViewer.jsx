import { useState, useEffect, useRef } from 'react'
import { useLanguage } from '../contexts/LanguageContext'

const FileViewer = ({ filename, content, onClose }) => {
  const { language } = useLanguage()
  const contentRef = useRef(null)
  const overlayRef = useRef(null)
  const [lines, setLines] = useState([])

  useEffect(() => {
    if (content) {
      const contentLines = content.split('\n')
      setLines(contentLines)
    }
  }, [content])

  useEffect(() => {
    if (contentRef.current) {
      contentRef.current.scrollTop = 0
    }
  }, [content])

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      if (overlayRef.current) {
        overlayRef.current.focus()
      }
    }, 100)

    const handleKeyDown = (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
        return
      }
      
      if (e.key === 'Escape' || e.key === 'q' || e.key === 'Q') {
        e.preventDefault()
        e.stopPropagation()
        e.stopImmediatePropagation()
        onClose()
        return false
      }
    }

    const options = { capture: true, passive: false }
    window.addEventListener('keydown', handleKeyDown, options)
    document.addEventListener('keydown', handleKeyDown, options)
    
    return () => {
      clearTimeout(timeoutId)
      window.removeEventListener('keydown', handleKeyDown, options)
      document.removeEventListener('keydown', handleKeyDown, options)
    }
  }, [onClose])

  if (!filename || !content) return null

  const handleOverlayClick = (e) => {
    if (e.target === e.currentTarget || e.target.classList.contains('file-viewer-overlay')) {
      e.preventDefault()
      e.stopPropagation()
      onClose()
    }
  }

  const handleCloseClick = (e) => {
    e.preventDefault()
    e.stopPropagation()
    e.stopImmediatePropagation()
    onClose()
  }

  const handleKeyDownOverlay = (e) => {
    if (e.key === 'Escape' || e.key === 'q' || e.key === 'Q') {
      e.preventDefault()
      e.stopPropagation()
      e.stopImmediatePropagation()
      onClose()
    }
  }

  const lang = language === 'FR' ? 'FR' : 'EN'

  return (
    <div 
      ref={overlayRef}
      className="file-viewer-overlay"
      onClick={handleOverlayClick}
      onKeyDown={handleKeyDownOverlay}
      role="dialog"
      aria-modal="true"
      aria-labelledby="file-viewer-title"
      tabIndex={-1}
      style={{ outline: 'none' }}
    >
      <div 
        className="file-viewer-container"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="file-viewer-header">
          <div className="file-viewer-title-section">
            <span className="file-viewer-title" id="file-viewer-title">
              {lang === 'FR' ? 'VISUALISEUR DE FICHIERS' : 'FILE VIEWER'}
            </span>
            <span className="file-viewer-filename">{filename}</span>
          </div>
          <button 
            className="file-viewer-close" 
            onClick={handleCloseClick}
            aria-label={lang === 'FR' ? 'Fermer' : 'Close'}
            title={lang === 'FR' ? 'Fermer (ESC ou Q)' : 'Close (ESC or Q)'}
            type="button"
          >×</button>
        </div>
        <div 
          className="file-viewer-content" 
          ref={contentRef}
          tabIndex={0}
        >
          <div className="file-viewer-lines">
            {lines.map((line, index) => (
              <div key={index} className="file-viewer-line">
                <span className="file-viewer-line-number">{String(index + 1).padStart(4, ' ')}</span>
                <span className="file-viewer-line-content">{line || ' '}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="file-viewer-footer">
          {lang === 'FR' ? 'Appuyez sur ESC ou Q pour fermer' : 'Press ESC or Q to close'}
        </div>
      </div>
    </div>
  )
}

export default FileViewer

