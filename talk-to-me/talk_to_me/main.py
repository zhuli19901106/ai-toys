from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import get_config, load_config

# Global variable to store config path
_config_path = None

def create_app(config_path: str = None) -> FastAPI:
    if config_path:
        load_config(config_path)
    config = get_config()
    
    app = FastAPI(
        title=config.app_title,
        description=config.app_description,
        version=config.app_version
    )

    # Store config in app state
    app.state.config = config

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_allow_origins,
        allow_credentials=config.cors_allow_credentials,
        allow_methods=config.cors_allow_methods,
        allow_headers=config.cors_allow_headers,
    )

    @app.get("/hello")
    async def hello():
        """
        A simple hello endpoint.
        """
        return {"message": "Hello!"}

    @app.get("/health")
    async def health_check():
        """
        Health check endpoint to verify the service is running.
        """
        return {"status": "healthy"}

    return app

def set_config_path(path: str):
    global _config_path
    _config_path = path
    return create_app(path)

# Create app instance
app = FastAPI(
    title="Talk to Me API",
    description="A FastAPI web service with Swagger UI support",
    version="0.1.0"
)
