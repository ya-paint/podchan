from abc import ABC

from podchan_container.domain.value_object import (
    PodchanContainerId
)

# -------------------------
# Base Event
# -------------------------
class PodchanContainerOperatorEvent(ABC):
    pass

# -------------------------
# Started Event
# -------------------------
class PodchanContainerOperatorStartedEvent(PodchanContainerOperatorEvent):
    def __init__(self, container_id: PodchanContainerId):
        self._container_id = container_id

    @property
    def container_id(self):
        return self._container_id

# -------------------------
# Stopped Event
# -------------------------
class PodchanContainerOperatorStoppedEvent(PodchanContainerOperatorEvent):
    def __init__(self, container_id: PodchanContainerId):
        self._container_id = container_id

    @property
    def container_id(self):
        return self._container_id

# -------------------------
# Listener
# -------------------------
class PodchanContainerOperatorEventListener:
    def on_event(self, event: PodchanContainerOperatorEvent):
        raise NotImplementedError()
