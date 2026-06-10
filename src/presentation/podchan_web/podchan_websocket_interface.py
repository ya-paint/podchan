
from fastapi import WebSocket, WebSocketDisconnect
import json
import asyncio

from podchan_container.application.application import PodchanContainerApplication
from podchan_container.application.application_event import (
    PodchanContainerApplicationEvent, 
    PodchanContainerApplicationEventListener,
    PodchanContainerData,
    PodchanContainerStartedEvent,
    PodchanContainerStoppedEvent
)
from podchan_container.application.application_command import (
    PodchanContainerApplicationRegistCommand,
    PodchanContainerApplicationDeleteCommand,
    PodchanContainerApplicationStartCommand,
    PodchanContainerApplicationStopCommand,
    PodchanContainerApplicationUpdateCommand
)
from podchan_container.domain.repository import PodchanContainerRepository
from podchan_container.domain.runtime import PodchanContainerRuntime

class PodchanWebAppEventListener(PodchanContainerApplicationEventListener):
    """
    Application層のイベントをPresentation層で受信するためのクラス
    """
    def __init__(self, 
            websocket : WebSocket
        ):
        self._websocket = websocket
    
    def on_event(
        self,
        event: PodchanContainerApplicationEvent,
    ) -> None:
        
        if isinstance(event,PodchanContainerStartedEvent):
            container_data : PodchanContainerData = event.get_container_data()
            self._send_container_data(container_data)

        if isinstance(event,PodchanContainerStoppedEvent):
            container_data : PodchanContainerData = event.get_container_data()
            self._send_container_data(container_data)

    def _send_container_data(self, container_data : PodchanContainerData):
        
        send_data = {}
        send_data["id"]     = container_data.get_id()
        send_data["name"]   = container_data.get_name()
        send_data["image"]  = container_data.get_image()

        asyncio.create_task(self._websocket.send_text(json.dumps(send_data)))

class PodchanWebSocketInterface:
    """
    Presentation層のWebSocketを使用してPodchanのコンテナ操作を行うクラスです
    """

    def __init__(self, 
            websocket : WebSocket, 
            podchan_app : PodchanContainerApplication
        ):
        self._websocket = websocket
        self._podchan_app = podchan_app
        self._event_listener = PodchanWebAppEventListener(websocket)

        self._podchan_app.subscribe(self._event_listener)

    def __del__(self):
        self._podchan_app.unsubscribe(self._event_listener)

    async def receive_cycle(self):
        try:
            while True:
                try:
                    text_data = await self._websocket.receive_text()
                    command_data = json.loads(text_data)
                    if isinstance(command_data, dict):
                        self._command_data_receive(command_data)
                except json.JSONDecodeError:
                    continue
        except WebSocketDisconnect:
            print("client disconnected")

    def _command_data_receive(
            self,
            command_data : dict
        ):
        # dictからcommandを生成し、appに入力する

        if not "command" in command_data:
            return
        
        command_name = command_data["command"]

        if (
            command_name == "regist"
            and "container_id" in command_data
            and "name" in command_data
            and "image" in command_data
        ):
            command = PodchanContainerApplicationRegistCommand(
                container_id    = command_data["container_id"],
                name            = command_data["name"],
                image           = command_data["image"],
            )
            self._podchan_app.regist(command)

        if command_name == "delete" and ("container_id" in command_data):
            command = PodchanContainerApplicationDeleteCommand(
                container_id    = command_data["container_id"],
            )
            self._podchan_app.delete(command)

        if command_name == "start" and ("container_id" in command_data):
            command = PodchanContainerApplicationStartCommand(
                container_id    = command_data["container_id"],
            )
            self._podchan_app.start(command)

        if command_name == "stop" and ("container_id" in command_data):
            command = PodchanContainerApplicationStopCommand(
                container_id    = command_data["container_id"],
            )
            self._podchan_app.stop(command)

        if command_name == "update" and ("container_id" in command_data):
            command = PodchanContainerApplicationUpdateCommand(
                container_id    = command_data["container_id"],
            )
            self._podchan_app.update(command)
        