from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.repository import (
    PodchanContainerRepository,
)
from podchan_container.domain.value_object import (
    PodchanContainerId,
)


class PodchanContainerInMemoryRepository(
    PodchanContainerRepository
):
    def __init__(self) -> None:
        self._containers: dict[
            PodchanContainerId,
            PodchanContainer,
        ] = {}

    def save(
        self,
        container: PodchanContainer,
    ) -> None:
        self._containers[container.id] = container

    def delete(
        self,
        container_id: PodchanContainerId,
    ) -> PodchanContainer:
        return self._containers.pop(container_id)
    
    def exists(
        self,
        container_id: PodchanContainerId,
    ) -> bool:
        return container_id in self._containers.keys()
    
    def find(
        self,
        container_id: PodchanContainerId,
    ) -> PodchanContainer:
        return self._containers[container_id]

    def find_all(
        self,
    ) -> list[PodchanContainer]:
        return list(self._containers.values())