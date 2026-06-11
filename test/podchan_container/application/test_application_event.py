import pytest

from podchan_container.application.application_event import (
    PodchanContainerApplicationEventListener,
    PodchanContainerApplicationEvent,
    PodchanContainerStartedEvent,
    PodchanContainerStoppedEvent,
    PodchanContainerStatusEvent,
)
from podchan_container.domain.entity import (
    PodchanContainer,
)
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerName,
    PodchanContainerConfig,
    RunningStatus,
)


def create_container() -> PodchanContainer:
    return PodchanContainer(
        id=PodchanContainerId("container-id"),
        name=PodchanContainerName("container-name"),
        config=PodchanContainerConfig(
            image="nginx:latest",
        ),
    )


def test_started_event_container_data():
    container = create_container()
    container.change_status(RunningStatus())

    event = PodchanContainerStartedEvent(
        container,
    )

    container_data = (
        event.get_container_data()
    )

    assert (
        container_data.get_id()
        == "container-id"
    )
    assert (
        container_data.get_name()
        == "container-name"
    )
    assert (
        container_data.get_image()
        == "nginx:latest"
    )
    assert (
        container_data.get_status()
        == "running"
    )


def test_stopped_event_container_data():
    container = create_container()

    event = PodchanContainerStoppedEvent(
        container,
    )

    container_data = (
        event.get_container_data()
    )

    assert (
        container_data.get_id()
        == "container-id"
    )
    assert (
        container_data.get_name()
        == "container-name"
    )
    assert (
        container_data.get_image()
        == "nginx:latest"
    )
    assert (
        container_data.get_status()
        == "stop"
    )


def test_status_event_container_data():
    container = create_container()

    event = PodchanContainerStatusEvent(
        container,
    )

    container_data = (
        event.get_container_data()
    )

    assert (
        container_data.get_id()
        == "container-id"
    )
    assert (
        container_data.get_name()
        == "container-name"
    )
    assert (
        container_data.get_image()
        == "nginx:latest"
    )
    assert (
        container_data.get_status()
        == "stop"
    )

    container.change_status(RunningStatus())

    event = PodchanContainerStatusEvent(
        container,
    )

    container_data = (
        event.get_container_data()
    )

    assert (
        container_data.get_status()
        == "running"
    )


class DummyEvent(
    PodchanContainerApplicationEvent,
):
    pass


class DummyListener(
    PodchanContainerApplicationEventListener,
):
    def __init__(self):
        self.received_event = None

    def on_event(
        self,
        event: PodchanContainerApplicationEvent,
    ) -> None:
        self.received_event = event


def test_listener_receives_event():
    listener = DummyListener()
    event = DummyEvent()

    listener.on_event(event)

    assert listener.received_event is event


def test_listener_requires_on_event():
    class InvalidListener(
        PodchanContainerApplicationEventListener,
    ):
        pass

    with pytest.raises(TypeError):
        InvalidListener()