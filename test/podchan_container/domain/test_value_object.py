import pytest

from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerName,
    PodchanContainerConfig,
    RunningStatus,
    StoppedStatus,
)

# -------------------------
# PodchanContainerId
# -------------------------

def test_container_id_success():
    cid = PodchanContainerId("abc")
    assert cid.value == "abc"


def test_container_id_empty():
    with pytest.raises(ValueError):
        PodchanContainerId("")


# -------------------------
# PodchanContainerName
# -------------------------

def test_container_name_success():
    name = PodchanContainerName("nginx")
    assert name.value == "nginx"


def test_container_name_empty():
    with pytest.raises(ValueError):
        PodchanContainerName("")


# -------------------------
# PodchanContainerConfig
# -------------------------

def test_container_config_success():
    config = PodchanContainerConfig("nginx:latest")
    assert config.image == "nginx:latest"


def test_container_config_empty():
    with pytest.raises(ValueError):
        PodchanContainerConfig("")


# -------------------------
# Status
# -------------------------

def test_running_status():
    status = RunningStatus()
    assert status.is_change_config() is False
    assert status.is_change_name() is False


def test_stopped_status():
    status = StoppedStatus()
    assert status.is_change_config() is True
    assert status.is_change_name() is True