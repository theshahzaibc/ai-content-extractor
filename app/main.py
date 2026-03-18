from fastapi import FastAPI
from app.api.endpoints import auth, extract

app = FastAPI(title="AI Content Extractor API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(extract.router, prefix="/api", tags=["extract"])