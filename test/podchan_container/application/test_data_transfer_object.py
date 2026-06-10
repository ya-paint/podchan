from podchan_container.application.data_transfer_object import (
    PodchanContainerData,
)
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import (
    PodchanContainerConfig,
    PodchanContainerId,
    PodchanContainerName,
)


def test_create_from_container() -> None:
    container = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("test-container"),
        PodchanContainerConfig(
            image="nginx:latest",
        )
    )

    data = PodchanContainerData(container)

    assert data.get_id() == "container-1"
    assert data.get_name() == "test-container"
    assert data.get_image() == "nginx:latest"


def test_get_id() -> None:
    container = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("test-container"),
        PodchanContainerConfig(
            image="nginx:latest",
        )
    )

    data = PodchanContainerData(container)

    assert data.get_id() == "container-1"


def test_get_name() -> None:
    container = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("test-container"),
        PodchanContainerConfig(
            image="nginx:latest",
        )
    )

    data = PodchanContainerData(container)

    assert data.get_name() == "test-container"


def test_get_image() -> None:
    container = PodchanContainer(
        PodchanContainerId("container-1"),
        PodchanContainerName("test-container"),
        PodchanContainerConfig(
            image="nginx:latest",
        )
    )

    data = PodchanContainerData(container)

    assert data.get_image() == "nginx:latest"