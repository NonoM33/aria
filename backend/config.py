import os
from typing import List

DEV_MODE = os.getenv("DEV_MODE", "false").lower() == "true"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./system_void.db")

CORS_ORIGINS: List[str] = [
    "http://localhost:5173",
    "http://localhost:3000"
]

ENCRYPTION_KEY = "VOID2024"

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "system-void-secret-key-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24 * 7

SUPPORTED_LANGUAGES = ["FR", "EN"]
DEFAULT_LANGUAGE = "FR"

