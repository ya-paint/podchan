import pytest

from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerName,
    PodchanContainerConfig,
    RunningStatus,
    StoppedStatus,
)

# -------------------------
# 初期状態
# -------------------------

def test_initial_state():
    container = PodchanContainer(
        id=PodchanContainerId("id1"),
        config=PodchanContainerConfig("nginx")
    )

    assert container.id.value == "id1"
    assert container.config.image == "nginx"
    assert container.name is None
    assert container.status is None


# -------------------------
# change_name（状態なしOK）
# -------------------------

def test_change_name_without_status():
    container = PodchanContainer(
        id=PodchanContainerId("id1"),
        config=PodchanContainerConfig("nginx")
    )

    container.change_name(PodchanContainerName("web"))

    assert container.name.value == "web"


# -------------------------
# change_config（状態なしOK）
# -------------------------

def test_change_config_without_status():
    container = PodchanContainer(
        id=PodchanContainerId("id1"),
        config=PodchanContainerConfig("nginx")
    )

    with pytest.raises(Exception):
        container.change_config(PodchanContainerConfig("redis"))


# -------------------------
# RunningStatus: config変更不可
# -------------------------

def test_change_config_running_status():
    container = PodchanContainer(
        id=PodchanContainerId("id1"),
        config=PodchanContainerConfig("nginx")
    )

    container.change_status(RunningStatus())

    with pytest.raises(Exception):
        container.change_config(PodchanContainerConfig("redis"))


# -------------------------
# StoppedStatus: config変更可能
# -------------------------

def test_change_config_stopped_status():
    container = PodchanContainer(
        id=PodchanContainerId("id1"),
        config=PodchanContainerConfig("nginx")
    )

    container.change_status(StoppedStatus())
    container.change_config(PodchanContainerConfig("redis"))

    assert container.config.image == "redis"


# -------------------------
# RunningStatus: name変更不可（※未定義なら失敗）
# -------------------------

def test_change_name_running_status():
    container = PodchanContainer(
        id=PodchanContainerId("id1"),
        config=PodchanContainerConfig("nginx")
    )

    container.change_status(RunningStatus())

    with pytest.raises(Exception):
        container.change_name(PodchanContainerName("web"))


# -------------------------
# StoppedStatus: name変更可能
# -------------------------

def test_change_name_stopped_status():
    container = PodchanContainer(
        id=PodchanContainerId("id1"),
        config=PodchanContainerConfig("nginx")
    )

    container.change_status(StoppedStatus())
    container.change_name(PodchanContainerName("web"))

    assert container.name.value == "web"