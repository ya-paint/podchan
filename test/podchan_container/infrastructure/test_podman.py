import pytest

from podchan_container.infrastructure.podman import PodmanContainerRuntime
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerConfig,
    RunningStatus,
    StoppedStatus,
)


def test_podman_runtime_start_real():
    container = PodchanContainer(
        PodchanContainerId("test-container"),
        PodchanContainerConfig("nginx"),
    )

    runtime = PodmanContainerRuntime(container)

    runtime.start()

    # 実Podmanなので状態だけ確認
    assert isinstance(container.status, RunningStatus)


def test_podman_runtime_stop_real():
    container = PodchanContainer(
        PodchanContainerId("test-container"),
        PodchanContainerConfig("nginx"),
    )

    runtime = PodmanContainerRuntime(container)

    runtime.stop()

    assert isinstance(container.status, StoppedStatus)