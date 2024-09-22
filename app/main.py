from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from .routers import game


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)
    
    _app.include_router(game.router) 

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
