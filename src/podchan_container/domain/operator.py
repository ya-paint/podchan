from typing import List

from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.operator_event import (
    PodchanContainerOperatorErrorEvent,
    PodchanContainerOperatorEventListener,
    PodchanContainerOperatorStartedEvent,
    PodchanContainerOperatorStatusEvent,
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
        try:
            self._runtime.start(self._container)

            event = PodchanContainerOperatorStartedEvent(
                self._container.id
            )
            self._emit(event)

        except Exception as e:
            self._emit_error(str(e))
            raise

    # -------------------------
    # stop
    # -------------------------
    def stop(self):
        try:
            self._runtime.stop(self._container)

            event = PodchanContainerOperatorStoppedEvent(
                self._container.id
            )
            self._emit(event)

        except Exception as e:
            self._emit_error(str(e))
            raise

    # -------------------------
    # sync
    # -------------------------
    def sync(self):
        try:
            self._runtime.sync(self._container)

            event = PodchanContainerOperatorStatusEvent(
                self._container.id
            )
            self._emit(event)

        except Exception as e:
            self._emit_error(str(e))
            raise

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

    # -------------------------
    # internal emit error
    # -------------------------
    def _emit_error(self, message: str):
        event = PodchanContainerOperatorErrorEvent(
            self._container.id,
            message,
        )

        self._emit(event)
