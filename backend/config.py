import os
from typing import List

DEV_MODE = os.getenv("DEV_MODE", "false").lower() == "true"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./system_void.db")

CORS_ORIGINS: List[str] = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://localhost:5173",
    "https://localhost:3000"
]

extra_origins = os.getenv("CORS_EXTRA_ORIGINS", "")
if extra_origins:
    for origin in extra_origins.split(","):
        origin = origin.strip()
        if origin and origin not in CORS_ORIGINS:
            CORS_ORIGINS.append(origin)

ENCRYPTION_KEY = "VOID2024"

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "system-void-secret-key-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24 * 7

SUPPORTED_LANGUAGES = ["FR", "EN"]
DEFAULT_LANGUAGE = "FR"

