from fastapi import FastAPI, Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send
from config import CORS_ORIGINS, CORS_ALLOW_ALL
from database import init_db
from api.routes import router
from api.admin_routes import router as admin_router


class CORSWebSocketMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] == "websocket":
            await self.app(scope, receive, send)
            return

        if scope["type"] == "http":
            headers = dict(scope.get("headers", []))
            origin = headers.get(b"origin", b"").decode()
            method = scope.get("method", "GET")

            if method == "OPTIONS":
                response = Response(
                    status_code=200,
                    headers={
                        "Access-Control-Allow-Origin": origin or "*",
                        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                        "Access-Control-Allow-Headers": "*",
                        "Access-Control-Allow-Credentials": "true",
                    }
                )
                await response(scope, receive, send)
                return

            async def send_with_cors(message):
                if message["type"] == "http.response.start":
                    headers = list(message.get("headers", []))
                    headers.append((b"access-control-allow-origin", (origin or "*").encode()))
                    headers.append((b"access-control-allow-credentials", b"true"))
                    headers.append((b"access-control-allow-methods", b"GET, POST, PUT, DELETE, OPTIONS"))
                    headers.append((b"access-control-allow-headers", b"*"))
                    message["headers"] = headers
                await send(message)

            await self.app(scope, receive, send_with_cors)
            return

        await self.app(scope, receive, send)


app = FastAPI()
app.add_middleware(CORSWebSocketMiddleware)
print(f"CORS: WebSocket middleware enabled, allow_all={CORS_ALLOW_ALL}")

try:
    init_db()
    from database import _migrate_installed_packages
    _migrate_installed_packages()
except Exception as e:
    print(f"Database initialization error: {e}")
    pass

app.include_router(router)
app.include_router(admin_router)
