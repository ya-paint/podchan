from abc import ABC, abstractmethod

from podchan_container.application.data_transfer_object import (
    PodchanContainerData,
)
from podchan_container.domain.entity import (
    PodchanContainer,
)
from podchan_container.domain.value_object import PodchanContainerId


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


class PodchanContainerStatusEvent(
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


class PodchanContainerErrorEvent(
    PodchanContainerApplicationEvent
):
    def __init__(
        self,
        container_id: PodchanContainerId,
        message: str,
    ) -> None:
        self._container_id = container_id.value
        self._message = message

    @property
    def container_id(self) -> str :
        return self._container_id

    @property
    def message(self) -> str :
        return self._message
