import Terminal from './components/Terminal'
import { LanguageProvider } from './contexts/LanguageContext'

function App() {
  return (
    <LanguageProvider>
      <div className="app">
        <Terminal />
      </div>
    </LanguageProvider>
  )
}

export default App

