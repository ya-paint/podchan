# runtime.py

from abc import ABC, abstractmethod
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import PodchanContainerId


class PodchanContainerRuntime(ABC):
    @abstractmethod
    def start(self, container: PodchanContainer):
        pass

    @abstractmethod
    def stop(self, container: PodchanContainer):
        pass

    @abstractmethod
    def sync(self, container: PodchanContainer):
        pass

class PodchanContainerRuntimeError(Exception):
    pass


class PodchanContainerStartError(PodchanContainerRuntimeError):
    pass


class PodchanContainerStopError(PodchanContainerRuntimeError):
    pass
