from typing import Dict, Set
from fastapi import WebSocket, WebSocketDisconnect
import json
import asyncio
from datetime import datetime

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.session_connections: Dict[str, Set[str]] = {}
        
    async def connect(self, websocket: WebSocket, connection_id: str, session_id: str):
        await websocket.accept()
        self.active_connections[connection_id] = websocket
        
        if session_id not in self.session_connections:
            self.session_connections[session_id] = set()
        self.session_connections[session_id].add(connection_id)
        
    def disconnect(self, connection_id: str, session_id: str):
        if connection_id in self.active_connections:
            del self.active_connections[connection_id]
        
        if session_id in self.session_connections:
            self.session_connections[session_id].discard(connection_id)
            if not self.session_connections[session_id]:
                del self.session_connections[session_id]
    
    async def send_personal_message(self, message: dict, connection_id: str):
        if connection_id in self.active_connections:
            try:
                await self.active_connections[connection_id].send_json(message)
            except Exception:
                pass
    
    async def send_to_session(self, message: dict, session_id: str):
        if session_id in self.session_connections:
            disconnected = []
            for connection_id in self.session_connections[session_id]:
                try:
                    await self.active_connections[connection_id].send_json(message)
                except Exception:
                    disconnected.append(connection_id)
            
            for conn_id in disconnected:
                self.disconnect(conn_id, session_id)
    
    async def broadcast(self, message: dict):
        disconnected = []
        for connection_id, websocket in self.active_connections.items():
            try:
                await websocket.send_json(message)
            except Exception:
                disconnected.append(connection_id)
        
        for conn_id in disconnected:
            for session_id, connections in list(self.session_connections.items()):
                if conn_id in connections:
                    self.disconnect(conn_id, session_id)
                    break

manager = ConnectionManager()

