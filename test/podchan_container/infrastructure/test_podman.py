import subprocess
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

def test_podman_runtime_sync_not_exists_real():
    subprocess.run(
        ["podman", "rm", "-f", "not-exists-container"],
        check=False,
        capture_output=True,
    )

    container = PodchanContainer(
        PodchanContainerId("not-exists-container"),
        PodchanContainerName("not-exists-container"),
        PodchanContainerConfig("nginx"),
    )

    runtime = PodmanContainerRuntime()

    runtime.sync(container)

    assert isinstance(container.status, StoppedStatus)
