import pytest

from podchan_container.infrastructure.podman import PodmanContainerRuntime
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerName,
    PodchanContainerConfig,
    RunningStatus,
    StoppedStatus,
)


def test_podman_runtime_start_real():
    container = PodchanContainer(
        PodchanContainerId("test-container"),
        PodchanContainerName("test-container"),
        PodchanContainerConfig("nginx"),
    )

    runtime = PodmanContainerRuntime()

    runtime.start(container)

    # 実Podmanなので状態だけ確認
    assert isinstance(container.status, RunningStatus)


def test_podman_runtime_stop_real():
    container = PodchanContainer(
        PodchanContainerId("test-container"),
        PodchanContainerName("test-container"),
        PodchanContainerConfig("nginx"),
    )

    runtime = PodmanContainerRuntime()

    runtime.stop(container)

    assert isinstance(container.status, StoppedStatus)