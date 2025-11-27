import { useLanguage } from '../contexts/LanguageContext'

const LanguageMenu = () => {
  const { language, toggleLanguage } = useLanguage()

  return (
    <div className="language-menu">
      <button 
        onClick={toggleLanguage}
        className="language-button"
        title={language === 'FR' ? 'Switch to English' : 'Passer en français'}
      >
        {language}
      </button>
    </div>
  )
}

export default LanguageMenu

