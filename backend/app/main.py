from fastapi import FastAPI

from app.api.routes import router
from app.api.upload import router as upload_router

app = FastAPI(
    title="AI Manga Translator API",
    version="1.0.0",
    description="Backend API for OCR, Translation, and Image Processing."
)

app.include_router(router)
app.include_router(upload_router)