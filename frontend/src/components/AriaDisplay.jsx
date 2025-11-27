import { useState, useEffect, useCallback } from 'react';
import { ARIA_STATES } from '../assets/aria_ascii';

const AriaDisplay = ({ 
  state = 'dormant', 
  emotion = 'neutral',
  isSpeaking = false,
  isMinimized = false,
  onMinimize 
}) => {
  const [currentFrame, setCurrentFrame] = useState(0);
  const [isBlinking, setIsBlinking] = useState(false);
  const [glitchActive, setGlitchActive] = useState(false);

  const getAriaArt = useCallback(() => {
    let artState = state;
    
    if (emotion && ARIA_STATES[emotion]) {
      artState = emotion;
    }

    if (glitchActive && ARIA_STATES.glitch) {
      const frames = ARIA_STATES.glitch;
      return frames[currentFrame % frames.length];
    }

    if (state === 'waking' && Array.isArray(ARIA_STATES.waking)) {
      return ARIA_STATES.waking[currentFrame % ARIA_STATES.waking.length];
    }

    if (isSpeaking && ARIA_STATES.speaking) {
      const speakingFrames = ARIA_STATES.speaking;
      return speakingFrames[currentFrame % speakingFrames.length];
    }

    if (state === 'thinking' && Array.isArray(ARIA_STATES.thinking)) {
      return ARIA_STATES.thinking[currentFrame % ARIA_STATES.thinking.length];
    }

    if (artState === 'neutral' && isBlinking && ARIA_STATES.neutralBlink) {
      return ARIA_STATES.neutralBlink;
    }

    return ARIA_STATES[artState] || ARIA_STATES.neutral;
  }, [state, emotion, isSpeaking, currentFrame, isBlinking, glitchActive]);

  useEffect(() => {
    if (state === 'waking' || isSpeaking || state === 'thinking') {
      const interval = setInterval(() => {
        setCurrentFrame(prev => prev + 1);
      }, state === 'waking' ? 800 : 300);
      return () => clearInterval(interval);
    }
  }, [state, isSpeaking]);

  useEffect(() => {
    const blinkInterval = setInterval(() => {
      if (state === 'neutral' || emotion === 'neutral') {
        setIsBlinking(true);
        setTimeout(() => setIsBlinking(false), 150);
      }
    }, 3000 + Math.random() * 2000);

    return () => clearInterval(blinkInterval);
  }, [state, emotion]);

  useEffect(() => {
    const glitchInterval = setInterval(() => {
      if (Math.random() < 0.1) {
        setGlitchActive(true);
        setCurrentFrame(0);
        setTimeout(() => setGlitchActive(false), 200 + Math.random() * 300);
      }
    }, 5000 + Math.random() * 10000);

    return () => clearInterval(glitchInterval);
  }, []);

  if (isMinimized) {
    return (
      <button 
        onClick={onMinimize}
        className="aria-minimized"
      >
        <span className="aria-minimized-icon">◉</span>
        <span className="aria-minimized-text">ARIA</span>
      </button>
    );
  }

  return (
    <div className={`aria-display ${glitchActive ? 'glitch' : ''} ${state}`}>
      <div className="aria-header">
        <span className="aria-status">
          {state === 'dormant' ? '○ HORS LIGNE' : '● EN LIGNE'}
        </span>
        {onMinimize && (
          <button onClick={onMinimize} className="aria-minimize-btn">
            ─
          </button>
        )}
      </div>
      <pre className="aria-ascii">
        {getAriaArt()}
      </pre>
      <div className="aria-scanlines"></div>
    </div>
  );
};

export default AriaDisplay;

