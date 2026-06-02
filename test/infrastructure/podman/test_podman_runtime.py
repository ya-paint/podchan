
from domain.container.entity.container import Container
from domain.container.value_object.container_config import ContainerConfig
from domain.container.value_object.container_status import ContainerStatus,RunningStatus,PausedStatus,StoppedStatus
from infrastructure.podman.podman_runtime import PodmanRuntime


def create_config() -> ContainerConfig:
    return ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=[],
        restart="always",
    )

def test_create_returns_stopped_container() -> None:
    runtime = PodmanRuntime()
    container_id = runtime.create(create_config())

    container = runtime.inspect(container_id)

    runtime.delete(container_id)

    assert isinstance(
        container.status,
        StoppedStatus,
    )

def test_start_and_stop() -> None:
    runtime = PodmanRuntime()
    container_id = runtime.create(create_config())
    
    runtime.start(container_id)
    runtime.stop(container_id)

    runtime.delete(container_id)

def test_restart() -> None:
    runtime = PodmanRuntime()
    container_id = runtime.create(create_config())
    
    runtime.restart(container_id)

    runtime.delete(container_id)
