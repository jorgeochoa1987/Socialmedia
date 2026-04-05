from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.core.config import settings
from app.core.errors import rate_limit_handler, register_exception_handlers
from app.core.logging import configure_logging, logger
from app.core.rate_limit import limiter
from app.routes import ai, export, health, videos


def create_app() -> FastAPI:
    configure_logging()
    application = FastAPI(title=settings.app_name, version="1.0.0")

    application.state.limiter = limiter
    application.add_exception_handler(RateLimitExceeded, rate_limit_handler)
    application.add_middleware(SlowAPIMiddleware)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_exception_handlers(application)

    application.include_router(health.router, prefix=settings.api_prefix)
    application.include_router(videos.router, prefix=settings.api_prefix)
    application.include_router(ai.router, prefix=settings.api_prefix)
    application.include_router(export.router, prefix=settings.api_prefix)

    logger.info("app_initialized", env=settings.app_env)
    return application


app = create_app()
