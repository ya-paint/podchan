from domain.container.entity.container import Container
from domain.container.value_object.container_config import ContainerConfig
from domain.container.value_object.container_id import ContainerId
from domain.container.value_object.container_status import (
    ContainerStatus,
    RunningStatus,
)

import subprocess

def create_config() -> ContainerConfig:
    return ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=["./data:/data"],
        restart="always",
    )

def create_status() -> ContainerStatus:
    return RunningStatus()


def test_equals():
    container_id = ContainerId("abc")

    a = Container(
        container_id=container_id,
        container_config=create_config(),
        container_status=create_status(),
    )

    b = Container(
        container_id=container_id,
        container_config=create_config(),
        container_status=create_status(),
    )

    assert a == b


def test_not_equals():
    a = Container(
        container_id=ContainerId("abc"),
        container_config=create_config(),
        container_status=create_status(),
    )

    b = Container(
        container_id=ContainerId("def"),
        container_config=create_config(),
        container_status=create_status(),
    )

    assert a != b


def test_id():
    container_id = ContainerId("abc")

    container = Container(
        container_id=container_id,
        container_config=create_config(),
        container_status=create_status(),
    )

    assert container.id == container_id


def test_config():
    config = create_config()

    container = Container(
        container_id=ContainerId("abc"),
        container_config=config,
        container_status=create_status(),
    )

    assert container.config == config

def test_status():
    config = create_status()

    container = Container(
        container_id=ContainerId("abc"),
        container_config=create_status(),
        container_status=config,
    )

    assert container.config == config

def test_change_config():
    old_config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=[],
        ports=[],
        volumes=[],
        restart="always",
    )

    new_config = ContainerConfig(
        image="redis:latest",
        name="cache",
        env=[],
        ports=[],
        volumes=[],
        restart="no",
    )

    container = Container(
        container_id=ContainerId("abc"),
        container_config=old_config,
        container_status=create_status(),
    )

    container.change_config(new_config)

    assert container.config == new_config


def test_hash_equals():
    container_id = ContainerId("abc")

    a = Container(
        container_id=container_id,
        container_config=create_config(),
        container_status=create_status(),
    )

    b = Container(
        container_id=container_id,
        container_config=create_config(),
        container_status=create_status(),
    )

    assert hash(a) == hash(b)


def test_not_equals_other_type():
    container = Container(
        container_id=ContainerId("abc"),
        container_config=create_config(),
        container_status=create_status(),
    )

    assert container != "container"

def test_create_container_from_podman():
    config = ContainerConfig(
        image="docker.io/library/nginx:latest",
        name="podchan-test",
        env=[],
        ports=[],
        volumes=[],
        restart="no",
    )

    result = subprocess.run(
        [
            "podman",
            "create",
            "--name",
            config.name,
            config.image,
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    container_raw_id = result.stdout.strip()

    container = Container(
        container_id=ContainerId(container_raw_id),
        container_config=config,
        container_status=create_status(),
    )

    assert container.id.value == container_raw_id
    assert container.config == config

    subprocess.run(
        [
            "podman",
            "rm",
            "-f",
            container_raw_id,
        ],
        check=True,
    )