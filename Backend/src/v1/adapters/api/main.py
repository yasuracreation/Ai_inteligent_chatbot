from fastapi import FastAPI

from intalentasia.composition.container import create_container


def create_app() -> FastAPI:
    container = create_container()
    app = FastAPI(title="Commercial Bank AI Assistant")
    app.state.container = container

    @app.get("/health")
    async def health():
        return {"status": "ok", "api_port": container.settings.api_port}

    return app


app = create_app()
