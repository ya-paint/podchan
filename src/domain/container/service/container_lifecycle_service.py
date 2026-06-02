from typing import Final

from container_domain.entity.container import Container
from container_domain.event.container_created_event import (
    ContainerCreatedEvent,
)
from container_domain.event.container_deleted_event import (
    ContainerDeletedEvent,
)
from container_domain.event.container_event import ContainerEvent
from container_domain.event.container_event_listener import (
    ContainerEventListener,
)
from container_domain.event.container_status_changed_event import (
    ContainerStatusChangedEvent,
)
from container_domain.repository.container_repository import (
    ContainerRepository,
)
from container_domain.runtime.container_runtime import (
    ContainerRuntime,
)
from container_domain.value_object.container_id import (
    ContainerId,
)


class ContainerLifecycleService:
    """
    Containerを操作するDomain Serviceです。

    RuntimeとRepositoryの同期を担当し、
    状態変化が発生した場合はDomain Eventを通知します。
    """

    _runtime: Final[ContainerRuntime]
    _repository: Final[ContainerRepository]

    _listeners: list[ContainerEventListener]

    def __init__(
        self,
        runtime: ContainerRuntime,
        repository: ContainerRepository,
    ) -> None:
        self._runtime = runtime
        self._repository = repository
        self._listeners = []

    def subscribe(
        self,
        listener: ContainerEventListener,
    ) -> None:
        """
        EventListenerを登録します。
        """
        self._listeners.append(listener)

    def unsubscribe(
        self,
        listener: ContainerEventListener,
    ) -> None:
        """
        EventListenerを解除します。
        """
        self._listeners.remove(listener)

    def create(
        self,
        container_config: ContainerConfig,
    ) -> None:
        self._runtime.create(container_config)

    def start(
        self,
        container: Container,
    ) -> None:
        self._runtime.start(container.container_id)

    def stop(
        self,
        container: Container,
    ) -> None:
        self._runtime.stop(container.container_id)

    def restart(
        self,
        container: Container,
    ) -> None:
        self._runtime.restart(container.container_id)

    def delete(
        self,
        container: Container,
    ) -> None:
        self._runtime.delete(container.container_id)
        self._repository.delete(
            container.container_id
        )

        self._notify(
            ContainerDeletedEvent(
                container.container_id
            )
        )

    def sync_all(self) -> None:
        """
        Runtimeの状態をRepositoryへ同期します。
        """
        pass

    def sync_container(
        self,
        container_id: ContainerId,
    ) -> None:
        """
        指定Containerを同期します。
        """
        pass

    def _notify(
        self,
        event: ContainerEvent,
    ) -> None:
        for listener in self._listeners:
            listener.on_event(event)