import { createContext, useContext, useState, useEffect } from 'react'

const LanguageContext = createContext()

export const useLanguage = () => {
  const context = useContext(LanguageContext)
  if (!context) {
    throw new Error('useLanguage must be used within LanguageProvider')
  }
  return context
}

export const LanguageProvider = ({ children }) => {
  const [language, setLanguage] = useState(() => {
    const stored = localStorage.getItem('system_void_language')
    if (stored) {
      const upper = stored.toUpperCase().trim()
      if (upper === 'FR' || upper === 'EN') {
        return upper
      }
    }
    return 'FR'
  })

  useEffect(() => {
    const upperLang = language.toUpperCase().trim()
    localStorage.setItem('system_void_language', upperLang)
  }, [language])

  const toggleLanguage = () => {
    setLanguage(prev => {
      const newLang = prev === 'FR' ? 'EN' : 'FR'
      return newLang
    })
  }

  return (
    <LanguageContext.Provider value={{ language, toggleLanguage }}>
      {children}
    </LanguageContext.Provider>
  )
}

