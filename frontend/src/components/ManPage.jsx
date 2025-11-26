import { useState, useEffect, useRef } from 'react'
import { useLanguage } from '../contexts/LanguageContext'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const ManPage = ({ command, onClose }) => {
  const { language } = useLanguage()
  const [content, setContent] = useState('')
  const [loading, setLoading] = useState(true)
  const contentRef = useRef(null)

  useEffect(() => {
    const fetchManPage = async () => {
      try {
        setLoading(true)
        const response = await axios.get(`${API_URL}/api/man/${command}`, {
          params: { language: language }
        })
        setContent(response.data.content || '')
      } catch (error) {
        setContent(`Error loading manual page for ${command}`)
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

  const handleKeyDown = (e) => {
    if (e.key === 'Escape' || e.key === 'q') {
      onClose()
    }
  }

  if (!command) return null

  return (
    <div 
      className="man-page-overlay"
      onClick={onClose}
      onKeyDown={handleKeyDown}
      tabIndex={0}
    >
      <div 
        className="man-page-container"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="man-page-header">
          <span className="man-page-title">MANUAL PAGE</span>
          <button className="man-page-close" onClick={onClose}>×</button>
        </div>
        <div className="man-page-content" ref={contentRef}>
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

