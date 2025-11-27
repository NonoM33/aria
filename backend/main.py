from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import CORS_ORIGINS, CORS_ALLOW_ALL
from database import init_db
from api.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if CORS_ALLOW_ALL else CORS_ORIGINS,
    allow_origin_regex=None if CORS_ALLOW_ALL else None,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print(f"CORS_ORIGINS: {CORS_ORIGINS}, allow_all={CORS_ALLOW_ALL}")

try:
    init_db()
    from database import _migrate_installed_packages
    _migrate_installed_packages()
except Exception as e:
    print(f"Database initialization error: {e}")
    pass

app.include_router(router)
