from typing import List

from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.operator_event import (
    PodchanContainerOperatorEventListener,
    PodchanContainerOperatorStartedEvent,
    PodchanContainerOperatorStoppedEvent,
)


class PodchanContainerOperator:
    def __init__(
        self,
        container: PodchanContainer,
        runtime: PodchanContainerRuntime,
    ):
        self._container = container
        self._runtime = runtime
        self._listeners: List[PodchanContainerOperatorEventListener] = []

    # -------------------------
    # start
    # -------------------------
    def start(self):
        self._runtime.start()

        event = PodchanContainerOperatorStartedEvent(
            self._container.id
        )
        self._emit(event)

    # -------------------------
    # stop
    # -------------------------
    def stop(self):
        self._runtime.stop()

        event = PodchanContainerOperatorStoppedEvent(
            self._container.id
        )
        self._emit(event)

    # -------------------------
    # sync
    # -------------------------
    def sync(self):
        self._runtime.sync()

    # -------------------------
    # subscribe
    # -------------------------
    def subscribe(self, listener: PodchanContainerOperatorEventListener):
        if listener not in self._listeners:
            self._listeners.append(listener)

    # -------------------------
    # unsubscribe
    # -------------------------
    def unsubscribe(self, listener: PodchanContainerOperatorEventListener):
        if listener in self._listeners:
            self._listeners.remove(listener)

    # -------------------------
    # internal emit
    # -------------------------
    def _emit(self, event):
        for listener in self._listeners:
            listener.on_event(event)