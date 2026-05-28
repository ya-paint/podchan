from domain.podman.entity.container import Container
from domain.podman.value_object.container_config import ContainerConfig
from domain.podman.value_object.container_id import ContainerId

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


def test_equals():
    container_id = ContainerId("abc")

    a = Container(
        container_id=container_id,
        config=create_config(),
    )

    b = Container(
        container_id=container_id,
        config=create_config(),
    )

    assert a == b


def test_not_equals():
    a = Container(
        container_id=ContainerId("abc"),
        config=create_config(),
    )

    b = Container(
        container_id=ContainerId("def"),
        config=create_config(),
    )

    assert a != b


def test_id():
    container_id = ContainerId("abc")

    container = Container(
        container_id=container_id,
        config=create_config(),
    )

    assert container.id == container_id


def test_config():
    config = create_config()

    container = Container(
        container_id=ContainerId("abc"),
        config=config,
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
        config=old_config,
    )

    container.change_config(new_config)

    assert container.config == new_config


def test_hash_equals():
    container_id = ContainerId("abc")

    a = Container(
        container_id=container_id,
        config=create_config(),
    )

    b = Container(
        container_id=container_id,
        config=create_config(),
    )

    assert hash(a) == hash(b)


def test_not_equals_other_type():
    container = Container(
        container_id=ContainerId("abc"),
        config=create_config(),
    )

    assert container != "container"


def test_to_debug_string():
    container = Container(
        container_id=ContainerId("abc"),
        config=create_config(),
    )

    assert (
        container.to_debug_string()
        == "Container("
        "id=ContainerId(value=abc), "
        "config=ContainerConfig("
        "image=nginx:latest, "
        "name=web, "
        "env=['ENV=prod'], "
        "ports=['8080:80'], "
        "volumes=['./data:/data'], "
        "restart=always))"
    )


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
        config=config,
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