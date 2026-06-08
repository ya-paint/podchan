import pytest

from podchan_container.application.application import (
    PodchanContainerApplication,
)
from podchan_container.application.application_command import (
    PodchanContainerApplicationDeleteCommand,
    PodchanContainerApplicationRegistCommand,
    PodchanContainerApplicationStartCommand,
    PodchanContainerApplicationStopCommand,
    PodchanContainerApplicationUpdateCommand,
)
from podchan_container.domain.entity import (
    PodchanContainer,
)
from podchan_container.infrastructure.in_memory import (
    PodchanContainerInMemoryRepository,
)
from podchan_container.domain.runtime import (
    PodchanContainerRuntime,
)
from podchan_container.domain.value_object import (
    PodchanContainerId,
)


class DummyRuntime(PodchanContainerRuntime):
    def __init__(self):
        self.started = []
        self.stopped = []
        self.synced = []

    def start(self, container):
        self.started.append(container)

    def stop(self, container):
        self.stopped.append(container)

    def sync(self, container):
        self.synced.append(container)


def create_application():
    repository = (
        PodchanContainerInMemoryRepository()
    )

    runtime = DummyRuntime()

    application = (
        PodchanContainerApplication(
            repository,
            runtime,
        )
    )

    return application, repository, runtime


def test_regist():
    application, repository, _ = (
        create_application()
    )

    application.regist(
        PodchanContainerApplicationRegistCommand(
            container_id="id1",
            name="container1",
            image="nginx",
        )
    )

    container = repository.find(
        PodchanContainerId("id1")
    )

    assert container.id.value == "id1"
    assert container.name.value == "container1"
    assert (
        container.config.image
        == "nginx"
    )


def test_delete():
    application, repository, _ = (
        create_application()
    )

    application.regist(
        PodchanContainerApplicationRegistCommand(
            container_id="id1",
            name="container1",
            image="nginx",
        )
    )

    deleted = application.delete(
        PodchanContainerApplicationDeleteCommand(
            container_id="id1",
        )
    )

    assert deleted.id.value == "id1"
    assert not repository.exists(
        PodchanContainerId("id1")
    )


def test_start():
    application, repository, runtime = (
        create_application()
    )

    application.regist(
        PodchanContainerApplicationRegistCommand(
            container_id="id1",
            name="container1",
            image="nginx",
        )
    )

    application.start(
        PodchanContainerApplicationStartCommand(
            container_id="id1",
        )
    )

    assert len(runtime.started) == 1
    assert (
        runtime.started[0].id.value
        == "id1"
    )


def test_stop():
    application, repository, runtime = (
        create_application()
    )

    application.regist(
        PodchanContainerApplicationRegistCommand(
            container_id="id1",
            name="container1",
            image="nginx",
        )
    )

    application.stop(
        PodchanContainerApplicationStopCommand(
            container_id="id1",
        )
    )

    assert len(runtime.stopped) == 1
    assert (
        runtime.stopped[0].id.value
        == "id1"
    )


def test_update():
    application, repository, runtime = (
        create_application()
    )

    application.regist(
        PodchanContainerApplicationRegistCommand(
            container_id="id1",
            name="container1",
            image="nginx",
        )
    )

    application.update(
        PodchanContainerApplicationUpdateCommand(
            container_id="id1",
        )
    )

    assert len(runtime.synced) == 1
    assert (
        runtime.synced[0].id.value
        == "id1"
    )