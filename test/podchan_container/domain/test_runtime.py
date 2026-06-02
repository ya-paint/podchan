import pytest

from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerConfig,
)

# -------------------------
# テスト用のダミーRuntime
# -------------------------

class FakeRuntime(PodchanContainerRuntime):
    def __init__(self, container):
        super().__init__(container)
        self.start_called = False
        self.stop_called = False
        self.sync_called = False

    def start(self):
        self.start_called = True

    def stop(self):
        self.stop_called = True

    def sync(self):
        self.sync_called = True


# -------------------------
# 初期化テスト
# -------------------------

def test_runtime_init():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerConfig("nginx")
    )

    runtime = FakeRuntime(container)

    assert runtime._container == container


# -------------------------
# start呼び出し確認
# -------------------------

def test_runtime_start():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerConfig("nginx")
    )

    runtime = FakeRuntime(container)
    runtime.start()

    assert runtime.start_called is True


# -------------------------
# stop呼び出し確認
# -------------------------

def test_runtime_stop():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerConfig("nginx")
    )

    runtime = FakeRuntime(container)
    runtime.stop()

    assert runtime.stop_called is True


# -------------------------
# sync呼び出し確認
# -------------------------

def test_runtime_sync():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerConfig("nginx")
    )

    runtime = FakeRuntime(container)
    runtime.sync()

    assert runtime.sync_called is True