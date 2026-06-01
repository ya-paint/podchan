from domain.container.entity.container import (
    Container,
)
from domain.container.repository.container_repository import (
    ContainerRepository,
)
from domain.container.value_object.container_id import (
    ContainerId,
)


class ContainerInMemoryRepository(
    ContainerRepository
):
    """
    メモリ上でContainerを管理するRepositoryです。

    テスト用途や開発用途で利用します。
    """

    _containers: dict[
        ContainerId,
        Container
    ]

    def __init__(self) -> None:
        self._containers = {}

    def save(
        self,
        container: Container,
    ) -> None:
        self._containers[
            container.id
        ] = container

    def read(
        self,
        container_id: ContainerId,
    ) -> Container:
        return self._containers[
            container_id
        ]

    def find_all(
        self,
    ) -> list[Container]:
        return list(
            self._containers.values()
        )

    def delete(
        self,
        container_id: ContainerId,
    ) -> None:
        del self._containers[
            container_id
        ]