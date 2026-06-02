import pytest

from infrastructure.memory.container_in_memory_repository import (
    ContainerInMemoryRepository,
)

from domain.container.entity.container import Container
from domain.container.value_object.container_id import ContainerId
from domain.container.value_object.container_config import ContainerConfig
from domain.container.value_object.container_status import (
    RunningStatus,
)

class TestContainerInMemoryRepository:

    def create_container_config(self) -> ContainerConfig:
        return ContainerConfig(
            image="nginx",
            name="test",
            env={},
            ports=[],
            volumes=[],
            restart="no",
        )

    def test_save_and_read(self) -> None:
        repository = ContainerInMemoryRepository()

        container = Container(
            container_id=ContainerId("test"),
            container_config=self.create_container_config(),
            container_status=RunningStatus(),
        )

        repository.save(container)

        actual = repository.read(
            ContainerId("test")
        )

        assert actual == container

    def test_find_all(self) -> None:
        repository = ContainerInMemoryRepository()

        container_1 = Container(
            container_id=ContainerId("container_1"),
            container_config=self.create_container_config(),
            container_status=RunningStatus(),
        )

        container_2 = Container(
            container_id=ContainerId("container_2"),
            container_config=self.create_container_config(),
            container_status=RunningStatus(),
        )

        repository.save(container_1)
        repository.save(container_2)

        actual = repository.find_all()

        assert len(actual) == 2
        assert container_1 in actual
        assert container_2 in actual

    def test_delete(self) -> None:
        repository = ContainerInMemoryRepository()

        container = Container(
            container_id=ContainerId("test"),
            container_config=self.create_container_config(),
            container_status=RunningStatus(),
        )

        repository.save(container)

        repository.delete(
            ContainerId("test")
        )

        with pytest.raises(KeyError):
            repository.read(
                ContainerId("test")
            )

    def test_save_overwrites_existing_container(self) -> None:
        repository = ContainerInMemoryRepository()

        container_1 = Container(
            container_id=ContainerId("test"),
            container_config=self.create_container_config(),
            container_status=RunningStatus(),
        )

        container_2 = Container(
            container_id=ContainerId("test"),
            container_config=self.create_container_config(),
            container_status=RunningStatus(),
        )

        repository.save(container_1)
        repository.save(container_2)

        actual = repository.find_all()

        assert len(actual) == 1
        assert actual[0] == container_2