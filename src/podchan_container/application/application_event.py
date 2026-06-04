from abc import ABC, abstractmethod

from podchan_container.application.data_transfer_object import (
    PodchanContainerData,
)
from podchan_container.domain.entity import (
    PodchanContainer,
)


class PodchanContainerApplicationEvent(ABC):
    """
    Application層のイベント基底クラスです。
    """

class PodchanContainerApplicationEventListener(
    ABC,
):
    """
    Applicationイベントを受け取るリスナーです。
    """

    @abstractmethod
    def on_event(
        self,
        event: PodchanContainerApplicationEvent,
    ) -> None:
        pass


class PodchanContainerStartedEvent(
    PodchanContainerApplicationEvent
):
    def __init__(
        self,
        container: PodchanContainer,
    ) -> None:
        self._container_data = (
            PodchanContainerData(container)
        )

    def get_container_data(
        self,
    ) -> PodchanContainerData:
        return self._container_data


class PodchanContainerStoppedEvent(
    PodchanContainerApplicationEvent
):
    def __init__(
        self,
        container: PodchanContainer,
    ) -> None:
        self._container_data = (
            PodchanContainerData(container)
        )

    def get_container_data(
        self,
    ) -> PodchanContainerData:
        return self._container_data
