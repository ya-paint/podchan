# runtime.py

from abc import ABC, abstractmethod
from podchan_container.domain.entity import PodchanContainer


class PodchanContainerRuntime(ABC):
    def __init__(self, container: PodchanContainer):
        self._container = container

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def sync(self):
        pass