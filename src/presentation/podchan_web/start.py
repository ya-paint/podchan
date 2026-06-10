from pathlib import Path
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

from presentation.podchan_web.podchan_websocket_interface import PodchanWebSocketInterface

from podchan_container.application.application import PodchanContainerApplication
from podchan_container.infrastructure.in_memory import PodchanContainerInMemoryRepository
from podchan_container.infrastructure.podman import PodmanContainerRuntime

BASE_DIR = Path(__file__).parent

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

podchan_app = PodchanContainerApplication(
    PodchanContainerInMemoryRepository(),
    PodmanContainerRuntime()
)

@app.websocket("/ws")
async def websocket(
    websocket: WebSocket,
):
    await websocket.accept()
    
    podchan_websocket = PodchanWebSocketInterface(websocket,podchan_app)
    await podchan_websocket.receive_cycle()

app.mount(
    "/",
    StaticFiles(directory=BASE_DIR / "static", html=True),
    name="static",
)
