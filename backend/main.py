from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import CORS_ORIGINS, CORS_ALLOW_ALL
from database import init_db
from api.routes import router

app = FastAPI()

if CORS_ALLOW_ALL:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_origin_regex=".*",
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
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
