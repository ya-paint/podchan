import pytest

from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerName,
    PodchanContainerConfig,
)

# -------------------------
# テスト用のダミーRuntime
# -------------------------

class FakeRuntime(PodchanContainerRuntime):
    def __init__(self):
        self.start_called = False
        self.stop_called = False
        self.sync_called = False

    def start(self, container):
        self.start_called = True

    def stop(self, container):
        self.stop_called = True

    def sync(self, container):
        self.sync_called = True

# -------------------------
# start呼び出し確認
# -------------------------

def test_runtime_start():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx")
    )

    runtime = FakeRuntime()
    runtime.start(container)

    assert runtime.start_called is True


# -------------------------
# stop呼び出し確認
# -------------------------

def test_runtime_stop():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx")
    )

    runtime = FakeRuntime()
    runtime.stop(container)

    assert runtime.stop_called is True


# -------------------------
# sync呼び出し確認
# -------------------------

def test_runtime_sync():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx")
    )

    runtime = FakeRuntime()
    runtime.sync(container)

    assert runtime.sync_called is True

import pytest

from podchan_container.domain.runtime import (
    PodchanContainerRuntimeError,
    PodchanContainerStartError,
    PodchanContainerStopError,
)


def test_podchan_container_start_error_is_runtime_error():
    error = PodchanContainerStartError("start failed")

    assert isinstance(error, PodchanContainerStartError)
    assert isinstance(error, PodchanContainerRuntimeError)
    assert isinstance(error, Exception)


def test_podchan_container_stop_error_is_runtime_error():
    error = PodchanContainerStopError("stop failed")

    assert isinstance(error, PodchanContainerStopError)
    assert isinstance(error, PodchanContainerRuntimeError)
    assert isinstance(error, Exception)


def test_podchan_container_start_error_message():
    with pytest.raises(PodchanContainerStartError) as exc_info:
        raise PodchanContainerStartError("start failed")

    assert str(exc_info.value) == "start failed"


def test_podchan_container_stop_error_message():
    with pytest.raises(PodchanContainerStopError) as exc_info:
        raise PodchanContainerStopError("stop failed")

    assert str(exc_info.value) == "stop failed"
