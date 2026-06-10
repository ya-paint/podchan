# runtime.py

from abc import ABC, abstractmethod
from podchan_container.domain.entity import PodchanContainer


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