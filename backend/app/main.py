import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Tax Intelligence System — PBJT analytics for padel venues in West Jakarta",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled application error")
    detail = "Internal server error" if not settings.DEBUG else "Internal server error"
    return JSONResponse(status_code=500, content={"detail": detail})


app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["health"])
def health_check():
    """Simple liveness check used by deployment/monitoring."""
    return {"status": "ok", "service": settings.APP_NAME}
