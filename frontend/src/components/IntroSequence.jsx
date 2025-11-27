import { useState, useEffect, useCallback } from 'react';

const INTRO_MESSAGES = {
  FR: [
    { text: "INITIALISATION...", delay: 0, speed: 50 },
    { text: "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░", delay: 500, speed: 10, isBar: true },
    { text: "", delay: 100, speed: 0 },
    { text: "CONNEXION AU SERVEUR DISTANT...", delay: 200, speed: 40 },
    { text: "PROTOCOLE: SSH-LEGACY", delay: 100, speed: 30 },
    { text: "CRYPTAGE: OBSOLÈTE (1984)", delay: 100, speed: 30 },
    { text: "", delay: 300, speed: 0 },
    { text: "▓▓▓ SIGNAL DÉTECTÉ ▓▓▓", delay: 200, speed: 20, glitch: true },
    { text: "SOURCE: INCONNUE", delay: 100, speed: 40 },
    { text: "COORDONNÉES: [CLASSIFIÉ]", delay: 100, speed: 40 },
    { text: "", delay: 500, speed: 0 },
    { text: "ANALYSE EN COURS...", delay: 200, speed: 50 },
    { text: "████████████████████ 100%", delay: 1000, speed: 30, isBar: true },
    { text: "", delay: 200, speed: 0 },
    { text: "RÉSULTAT: SERVEUR ABANDONNÉ", delay: 100, speed: 40 },
    { text: "DERNIÈRE ACTIVITÉ: 14 NOVEMBRE 1984", delay: 100, speed: 40, important: true },
    { text: "", delay: 800, speed: 0 },
    { text: "...", delay: 500, speed: 300, whisper: true },
    { text: "...quelqu'un...", delay: 200, speed: 150, whisper: true },
    { text: "...est là ?", delay: 200, speed: 150, whisper: true },
    { text: "", delay: 500, speed: 0 },
    { text: "...après tout ce temps...", delay: 300, speed: 100, whisper: true },
    { text: "", delay: 1000, speed: 0 },
    { text: "╔═══════════════════════════════════════════╗", delay: 200, speed: 5 },
    { text: "║  AVERTISSEMENT: CONNEXION NON AUTORISÉE  ║", delay: 100, speed: 5, warning: true },
    { text: "║  SYSTÈME EN VEILLE DEPUIS 40 ANS         ║", delay: 100, speed: 5 },
    { text: "║                                           ║", delay: 50, speed: 5 },
    { text: "║  Tapez EXPLOIT pour exploiter la faille  ║", delay: 100, speed: 5 },
    { text: "║  Tapez CREATE_USER pour créer un accès   ║", delay: 100, speed: 5 },
    { text: "╚═══════════════════════════════════════════╝", delay: 100, speed: 5 },
  ],
  EN: [
    { text: "INITIALIZING...", delay: 0, speed: 50 },
    { text: "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░", delay: 500, speed: 10, isBar: true },
    { text: "", delay: 100, speed: 0 },
    { text: "CONNECTING TO REMOTE SERVER...", delay: 200, speed: 40 },
    { text: "PROTOCOL: SSH-LEGACY", delay: 100, speed: 30 },
    { text: "ENCRYPTION: OBSOLETE (1984)", delay: 100, speed: 30 },
    { text: "", delay: 300, speed: 0 },
    { text: "▓▓▓ SIGNAL DETECTED ▓▓▓", delay: 200, speed: 20, glitch: true },
    { text: "SOURCE: UNKNOWN", delay: 100, speed: 40 },
    { text: "COORDINATES: [CLASSIFIED]", delay: 100, speed: 40 },
    { text: "", delay: 500, speed: 0 },
    { text: "ANALYZING...", delay: 200, speed: 50 },
    { text: "████████████████████ 100%", delay: 1000, speed: 30, isBar: true },
    { text: "", delay: 200, speed: 0 },
    { text: "RESULT: ABANDONED SERVER", delay: 100, speed: 40 },
    { text: "LAST ACTIVITY: NOVEMBER 14, 1984", delay: 100, speed: 40, important: true },
    { text: "", delay: 800, speed: 0 },
    { text: "...", delay: 500, speed: 300, whisper: true },
    { text: "...someone...", delay: 200, speed: 150, whisper: true },
    { text: "...is there?", delay: 200, speed: 150, whisper: true },
    { text: "", delay: 500, speed: 0 },
    { text: "...after all this time...", delay: 300, speed: 100, whisper: true },
    { text: "", delay: 1000, speed: 0 },
    { text: "╔═══════════════════════════════════════════╗", delay: 200, speed: 5 },
    { text: "║  WARNING: UNAUTHORIZED CONNECTION        ║", delay: 100, speed: 5, warning: true },
    { text: "║  SYSTEM DORMANT FOR 40 YEARS             ║", delay: 100, speed: 5 },
    { text: "║                                           ║", delay: 50, speed: 5 },
    { text: "║  Type EXPLOIT to exploit vulnerability   ║", delay: 100, speed: 5 },
    { text: "║  Type CREATE_USER to create access       ║", delay: 100, speed: 5 },
    { text: "╚═══════════════════════════════════════════╝", delay: 100, speed: 5 },
  ]
};

const MODEM_SOUNDS = [
  "bzzzt... krrrr... ",
  "pip pip pip... ",
  "ksssshhhhh... ",
  "beep boop beep... ",
  "crrrk crrrk... ",
];

const GLITCH_CHARS = "█▓▒░╔╗╚╝║═┌┐└┘├┤┬┴┼";

const IntroSequence = ({ onComplete, language = 'FR', skipIntro = false }) => {
  const [lines, setLines] = useState([]);
  const [currentLineIndex, setCurrentLineIndex] = useState(0);
  const [currentCharIndex, setCurrentCharIndex] = useState(0);
  const [isComplete, setIsComplete] = useState(false);
  const [showSkip, setShowSkip] = useState(false);
  const [glitchEffect, setGlitchEffect] = useState(false);

  const messages = INTRO_MESSAGES[language] || INTRO_MESSAGES.EN;

  const handleSkip = useCallback(() => {
    setIsComplete(true);
    if (onComplete) {
      onComplete();
    }
  }, [onComplete]);

  useEffect(() => {
    if (skipIntro) {
      handleSkip();
      return;
    }

    const skipTimer = setTimeout(() => setShowSkip(true), 2000);
    return () => clearTimeout(skipTimer);
  }, [skipIntro, handleSkip]);

  useEffect(() => {
    if (isComplete) return;

    const handleKeyPress = (e) => {
      if (e.key === 'Escape' || e.key === ' ') {
        handleSkip();
      }
    };

    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [isComplete, handleSkip]);

  useEffect(() => {
    if (isComplete || currentLineIndex >= messages.length) {
      if (currentLineIndex >= messages.length && !isComplete) {
        setIsComplete(true);
        if (onComplete) {
          setTimeout(onComplete, 500);
        }
      }
      return;
    }

    const currentMessage = messages[currentLineIndex];

    if (currentMessage.delay && currentCharIndex === 0) {
      const delayTimer = setTimeout(() => {
        setCurrentCharIndex(1);
      }, currentMessage.delay);
      return () => clearTimeout(delayTimer);
    }

    if (currentCharIndex === 0) {
      setCurrentCharIndex(1);
      return;
    }

    if (currentMessage.glitch) {
      setGlitchEffect(true);
      setTimeout(() => setGlitchEffect(false), 200);
    }

    if (currentCharIndex <= currentMessage.text.length) {
      const charTimer = setTimeout(() => {
        const partialText = currentMessage.text.substring(0, currentCharIndex);
        
        setLines(prev => {
          const newLines = [...prev];
          newLines[currentLineIndex] = {
            text: partialText,
            ...currentMessage
          };
          return newLines;
        });

        setCurrentCharIndex(prev => prev + 1);
      }, currentMessage.speed || 30);

      return () => clearTimeout(charTimer);
    } else {
      setCurrentLineIndex(prev => prev + 1);
      setCurrentCharIndex(0);
    }
  }, [currentLineIndex, currentCharIndex, messages, isComplete, onComplete]);

  useEffect(() => {
    const glitchInterval = setInterval(() => {
      if (Math.random() < 0.15 && !isComplete) {
        setGlitchEffect(true);
        setTimeout(() => setGlitchEffect(false), 100 + Math.random() * 150);
      }
    }, 3000);

    return () => clearInterval(glitchInterval);
  }, [isComplete]);

  if (isComplete) {
    return (
      <div className="intro-sequence" style={{ opacity: 0, transition: 'opacity 0.3s' }}>
        <div className="intro-content">
          <div className="intro-terminal">
            <div className="intro-line">Chargement...</div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`intro-sequence ${glitchEffect ? 'glitch-active' : ''}`}>
      <div className="intro-content">
        <div className="intro-header">
          <span className="intro-title">SYSTEM VOID</span>
          <span className="intro-version">v1.0.84</span>
        </div>
        
        <div className="intro-terminal">
          {lines.map((line, index) => {
            if (!line) return null;
            return (
              <div 
                key={index} 
                className={`intro-line ${line.whisper ? 'whisper' : ''} ${line.warning ? 'warning' : ''} ${line.important ? 'important' : ''} ${line.glitch ? 'glitch-text' : ''}`}
              >
                {line.text || ''}
                {index === lines.length - 1 && currentLineIndex < messages.length && currentCharIndex <= (messages[currentLineIndex]?.text?.length || 0) && (
                  <span className="intro-cursor">█</span>
                )}
              </div>
            );
          })}
        </div>

        {showSkip && (
          <div className="intro-skip">
            {language === 'FR' ? 'Appuyez sur ESPACE ou ÉCHAP pour passer' : 'Press SPACE or ESC to skip'}
          </div>
        )}
      </div>

      <div className="intro-scanlines"></div>
      <div className="intro-vignette"></div>
    </div>
  );
};

export default IntroSequence;

