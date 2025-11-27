import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Terminal from './components/Terminal'
import Wiki from './components/Wiki'
import { LanguageProvider } from './contexts/LanguageContext'

function App() {
  return (
    <LanguageProvider>
      <Router>
        <div className="app">
          <Routes>
            <Route path="/" element={<Terminal />} />
            <Route path="/wiki" element={<Wiki />} />
          </Routes>
        </div>
      </Router>
    </LanguageProvider>
  )
}

export default App

