from abc import ABC, abstractmethod

from container_domain.event.container_event import ContainerEvent


class ContainerEventListener(ABC):
    """
    ContainerEventを受け取るリスナーです。

    ContainerLifecycleServiceなどが発行した
    Domain Eventを受け取り、処理を実行します。

    Application Layerでは、このインターフェースを実装した
    クラスを登録してイベントを受信します。
    """

    @abstractmethod
    def on_event(self, event: ContainerEvent) -> None:
        """
        ContainerEventを受け取ります。

        Args:
            event:
                発生したContainerEvent
        """
        pass