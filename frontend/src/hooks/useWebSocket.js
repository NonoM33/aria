import { useState, useEffect, useRef, useCallback } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
const WS_URL = API_URL.replace('http://', 'ws://').replace('https://', 'wss://')

export const useWebSocket = (sessionId, language, onMessage) => {
  const [isConnected, setIsConnected] = useState(false)
  const [reconnectAttempts, setReconnectAttempts] = useState(0)
  const wsRef = useRef(null)
  const reconnectTimeoutRef = useRef(null)
  const sessionIdRef = useRef(sessionId)
  const languageRef = useRef(language)
  const onMessageRef = useRef(onMessage)
  const subscriptionsRef = useRef([])

  useEffect(() => {
    sessionIdRef.current = sessionId
    languageRef.current = language
  }, [sessionId, language])

  useEffect(() => {
    onMessageRef.current = onMessage
  }, [onMessage])

  const connect = useCallback(() => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      return
    }

    if (!sessionIdRef.current) {
      return
    }

    try {
      const wsUrl = `${WS_URL}/ws?session_id=${sessionIdRef.current}`
      const ws = new WebSocket(wsUrl)

      ws.onopen = () => {
        setIsConnected(true)
        setReconnectAttempts(0)
        
        if (subscriptionsRef.current.length > 0) {
          ws.send(JSON.stringify({
            type: 'subscribe',
            subscriptions: subscriptionsRef.current
          }))
        }
      }

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data)
          
          if (data.type === 'connected') {
            if (subscriptionsRef.current.length > 0) {
              ws.send(JSON.stringify({
                type: 'subscribe',
                subscriptions: subscriptionsRef.current
              }))
            }
            return
          }

          if (onMessageRef.current) {
            onMessageRef.current(data)
          }
        } catch (error) {
          console.error('Error parsing WebSocket message:', error)
        }
      }

      ws.onerror = (error) => {
        console.error('WebSocket error:', error)
      }

      ws.onclose = () => {
        setIsConnected(false)
        wsRef.current = null

        if (reconnectAttempts < 10) {
          const delay = Math.min(1000 * Math.pow(2, reconnectAttempts), 30000)
          reconnectTimeoutRef.current = setTimeout(() => {
            setReconnectAttempts(prev => prev + 1)
            connect()
          }, delay)
        }
      }

      wsRef.current = ws
    } catch (error) {
      console.error('Error creating WebSocket:', error)
      setIsConnected(false)
    }
  }, [reconnectAttempts])

  const sendCommand = useCallback((command, token, password = null) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      const message = {
        type: 'command',
        command: command,
        language: languageRef.current,
        token: token || null
      }
      if (password !== null) {
        message.password = password
      }
      wsRef.current.send(JSON.stringify(message))
      return true
    }
    return false
  }, [])

  const subscribe = useCallback((subscriptions) => {
    subscriptionsRef.current = subscriptions
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'subscribe',
        subscriptions: subscriptions
      }))
    }
  }, [])

  const ping = useCallback(() => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'ping'
      }))
    }
  }, [])

  useEffect(() => {
    connect()

    const pingInterval = setInterval(() => {
      ping()
    }, 30000)

    return () => {
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current)
      }
      if (wsRef.current) {
        wsRef.current.close()
      }
      clearInterval(pingInterval)
    }
  }, [connect, ping])

  return {
    isConnected,
    sendCommand,
    subscribe,
    ping
  }
}

