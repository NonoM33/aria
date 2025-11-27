import { useLanguage } from '../contexts/LanguageContext'
import { Link } from 'react-router-dom'

const AVAILABLE_PACKAGES = {
    "file-viewer": {
        name: "file-viewer",
        description_fr: "Visualiseur de fichiers avancé avec interface style vim. Permet de visualiser les fichiers du système de manière plus intuitive et visuelle.",
        description_en: "Advanced file viewer with vim-like interface. Allows viewing system files in a more intuitive and visual way.",
        version: "1.0.0",
        author: "SYSTEM_VOID Team"
    }
}

const Wiki = () => {
  const { language } = useLanguage()
  const lang = language === 'FR' ? 'FR' : 'EN'

  return (
    <div className="wiki-container">
      <div className="scanlines"></div>
      <div className="wiki-content">
        <div className="wiki-header">
          <h1 className="wiki-title">SYSTEM_VOID PACKAGE WIKI</h1>
          <Link to="/" className="wiki-back-link">
            ← {lang === 'FR' ? 'Retour au terminal' : 'Back to terminal'}
          </Link>
        </div>
        
        <div className="wiki-body">
          <div className="wiki-intro">
            {lang === 'FR' ? (
              <>
                <p>Bienvenue dans le wiki des packages SYSTEM_VOID.</p>
                <p>Les packages peuvent être installés via le gestionnaire de packages intégré.</p>
                <p>Pour installer un package, utilisez la commande: <code>PKG INSTALL &lt;package&gt;</code></p>
                <p className="wiki-note">Note: Vous devez être authentifié pour installer des packages.</p>
              </>
            ) : (
              <>
                <p>Welcome to the SYSTEM_VOID package wiki.</p>
                <p>Packages can be installed via the integrated package manager.</p>
                <p>To install a package, use the command: <code>PKG INSTALL &lt;package&gt;</code></p>
                <p className="wiki-note">Note: You must be authenticated to install packages.</p>
              </>
            )}
          </div>

          <div className="wiki-packages">
            <h2 className="wiki-section-title">
              {lang === 'FR' ? 'Packages disponibles' : 'Available packages'}
            </h2>
            
            {Object.values(AVAILABLE_PACKAGES).map((pkg) => (
              <div key={pkg.name} className="wiki-package-card">
                <div className="wiki-package-header">
                  <h3 className="wiki-package-name">{pkg.name}</h3>
                  <span className="wiki-package-version">v{pkg.version}</span>
                </div>
                <div className="wiki-package-body">
                  <p className="wiki-package-description">
                    {lang === 'FR' ? pkg.description_fr : pkg.description_en}
                  </p>
                  <div className="wiki-package-meta">
                    <span className="wiki-package-author">
                      {lang === 'FR' ? 'Auteur' : 'Author'}: {pkg.author}
                    </span>
                  </div>
                  <div className="wiki-package-install">
                    <code className="wiki-install-command">
                      PKG INSTALL {pkg.name}
                    </code>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="wiki-commands">
            <h2 className="wiki-section-title">
              {lang === 'FR' ? 'Commandes du gestionnaire de packages' : 'Package manager commands'}
            </h2>
            <div className="wiki-command-list">
              <div className="wiki-command-item">
                <code>PKG INSTALL &lt;package&gt;</code>
                <span>{lang === 'FR' ? 'Installer un package' : 'Install a package'}</span>
              </div>
              <div className="wiki-command-item">
                <code>PKG UNINSTALL &lt;package&gt;</code>
                <span>{lang === 'FR' ? 'Désinstaller un package' : 'Uninstall a package'}</span>
              </div>
              <div className="wiki-command-item">
                <code>PKG LIST</code>
                <span>{lang === 'FR' ? 'Lister les packages installés' : 'List installed packages'}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Wiki

