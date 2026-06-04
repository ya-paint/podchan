from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import (
    PodchanContainerConfig,
    PodchanContainerId,
    PodchanContainerName
)

from podchan_container.infrastructure.in_memory import (
    PodchanContainerInMemoryRepository,
)


def test_save_and_find() -> None:
    repository = PodchanContainerInMemoryRepository()

    container = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig(
            image="nginx:latest",
        ),
    )

    repository.save(container)

    actual = repository.find(
        PodchanContainerId("container-1"),
    )

    assert actual is container


def test_delete() -> None:
    repository = PodchanContainerInMemoryRepository()

    container = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig(
            image="nginx:latest",
        ),
    )

    repository.save(container)

    deleted = repository.delete(
        PodchanContainerId("container-1"),
    )

    assert deleted is container
    assert repository.find_all() == []


def test_find_all() -> None:
    repository = PodchanContainerInMemoryRepository()

    container1 = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig(
            image="nginx:latest",
        ),
    )

    container2 = PodchanContainer(
        PodchanContainerId("container-2"),
        PodchanContainerName("name1"),
        PodchanContainerConfig(
            image="redis:latest",
        ),
    )

    repository.save(container1)
    repository.save(container2)

    actual = repository.find_all()

    assert actual == [
        container1,
        container2,
    ]


def test_save_overwrite_same_id() -> None:
    repository = PodchanContainerInMemoryRepository()

    container1 = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig(
            image="nginx:latest",
        ),
    )

    container2 = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig(
            image="redis:latest",
        ),
    )

    repository.save(container1)
    repository.save(container2)

    actual = repository.find(
        PodchanContainerId("container-1"),
    )

    assert actual is container2