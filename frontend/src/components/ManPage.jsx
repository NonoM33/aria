import { useState, useEffect, useRef } from 'react'
import { useLanguage } from '../contexts/LanguageContext'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const ManPage = ({ command, onClose }) => {
  const { language } = useLanguage()
  const [content, setContent] = useState('')
  const [loading, setLoading] = useState(true)
  const contentRef = useRef(null)
  const overlayRef = useRef(null)

  useEffect(() => {
    const fetchManPage = async () => {
      try {
        setLoading(true)
        // Utiliser la commande MAN via l'API /api/command au lieu de /api/man
        const response = await axios.post(`${API_URL}/api/command`, {
          command: `MAN ${command}`,
          session_id: localStorage.getItem('session_id') || 'default',
          language: language
        })
        setContent(response.data.response || `No manual page found for ${command}`)
      } catch (error) {
        setContent(`Erreur lors du chargement de la page de manuel pour ${command}`)
      } finally {
        setLoading(false)
      }
    }

    if (command) {
      fetchManPage()
    }
  }, [command, language])

  useEffect(() => {
    if (contentRef.current) {
      contentRef.current.scrollTop = 0
    }
  }, [content])

  useEffect(() => {
    // Focus sur l'overlay dès qu'il est monté
    if (overlayRef.current) {
      overlayRef.current.focus()
    }
  }, [])

  useEffect(() => {
    // Focus sur l'overlay dès qu'il est monté pour capturer les touches
    const timeoutId = setTimeout(() => {
      if (overlayRef.current) {
        overlayRef.current.focus()
      }
    }, 100)

    const handleKeyDown = (e) => {
      // Ignorer si on est dans un input ou textarea
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
        return
      }
      
      // ESC ou Q (majuscule ou minuscule) pour fermer
      if (e.key === 'Escape' || e.key === 'q' || e.key === 'Q') {
        e.preventDefault()
        e.stopPropagation()
        e.stopImmediatePropagation()
        onClose()
        return false
      }
    }

    // Ajouter l'event listener avec capture pour intercepter avant les autres
    // Utiliser capture phase pour intercepter avant les autres handlers
    const options = { capture: true, passive: false }
    window.addEventListener('keydown', handleKeyDown, options)
    document.addEventListener('keydown', handleKeyDown, options)
    
    // Nettoyer à la fermeture
    return () => {
      clearTimeout(timeoutId)
      window.removeEventListener('keydown', handleKeyDown, options)
      document.removeEventListener('keydown', handleKeyDown, options)
    }
  }, [onClose])

  if (!command) return null

  const handleOverlayClick = (e) => {
    if (e.target === e.currentTarget || e.target.classList.contains('man-page-overlay')) {
      e.preventDefault()
      e.stopPropagation()
      onClose()
    }
  }

  const handleCloseClick = (e) => {
    e.preventDefault()
    e.stopPropagation()
    onClose()
  }

  const handleKeyDownOverlay = (e) => {
    if (e.key === 'Escape' || e.key === 'q' || e.key === 'Q') {
      e.preventDefault()
      e.stopPropagation()
      onClose()
    }
  }

  return (
    <div 
      ref={overlayRef}
      className="man-page-overlay"
      onClick={handleOverlayClick}
      onKeyDown={handleKeyDownOverlay}
      role="dialog"
      aria-modal="true"
      aria-labelledby="man-page-title"
      tabIndex={-1}
      style={{ outline: 'none' }}
    >
      <div 
        className="man-page-container"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="man-page-header">
          <span className="man-page-title" id="man-page-title">MANUAL PAGE</span>
          <button 
            className="man-page-close" 
            onClick={handleCloseClick}
            aria-label="Fermer"
            title="Fermer (ESC ou Q)"
            type="button"
          >×</button>
        </div>
        <div 
          className="man-page-content" 
          ref={contentRef}
          tabIndex={0}
        >
          {loading ? (
            <div className="man-page-loading">Loading...</div>
          ) : (
            <pre className="man-page-text">{content}</pre>
          )}
        </div>
        <div className="man-page-footer">
          Press ESC or Q to close
        </div>
      </div>
    </div>
  )
}

export default ManPage

