import pytest
from dataclasses import FrozenInstanceError

from podchan_container.application.application_command import (
    PodchanContainerApplicationRegistCommand,
    PodchanContainerApplicationDeleteCommand,
    PodchanContainerApplicationStartCommand,
    PodchanContainerApplicationStopCommand,
    PodchanContainerApplicationUpdateCommand,
)


def test_regist_command():
    command = (
        PodchanContainerApplicationRegistCommand(
            container_id="container1",
            name="nginx",
            image="nginx:latest",
        )
    )

    assert command.container_id == "container1"
    assert command.name == "nginx"
    assert command.image == "nginx:latest"


def test_regist_command_invalid_container_id():
    with pytest.raises(TypeError):
        PodchanContainerApplicationRegistCommand(
            container_id=1,
            name="nginx",
            image="nginx:latest",
        )


def test_regist_command_invalid_name():
    with pytest.raises(TypeError):
        PodchanContainerApplicationRegistCommand(
            container_id="container1",
            name=1,
            image="nginx:latest",
        )


def test_regist_command_invalid_image():
    with pytest.raises(TypeError):
        PodchanContainerApplicationRegistCommand(
            container_id="container1",
            name="nginx",
            image=1,
        )


def test_regist_command_is_frozen():
    command = (
        PodchanContainerApplicationRegistCommand(
            container_id="container1",
            name="nginx",
            image="nginx:latest",
        )
    )

    with pytest.raises(FrozenInstanceError):
        command.container_id = "container2"


@pytest.mark.parametrize(
    "command_class",
    [
        PodchanContainerApplicationDeleteCommand,
        PodchanContainerApplicationStartCommand,
        PodchanContainerApplicationStopCommand,
        PodchanContainerApplicationUpdateCommand,
    ],
)
def test_single_id_command(command_class):
    command = command_class(
        container_id="container1",
    )

    assert command.container_id == "container1"


@pytest.mark.parametrize(
    "command_class",
    [
        PodchanContainerApplicationDeleteCommand,
        PodchanContainerApplicationStartCommand,
        PodchanContainerApplicationStopCommand,
        PodchanContainerApplicationUpdateCommand,
    ],
)
def test_single_id_command_invalid_type(
    command_class,
):
    with pytest.raises(TypeError):
        command_class(
            container_id=1,
        )


@pytest.mark.parametrize(
    "command_class",
    [
        PodchanContainerApplicationDeleteCommand,
        PodchanContainerApplicationStartCommand,
        PodchanContainerApplicationStopCommand,
        PodchanContainerApplicationUpdateCommand,
    ],
)
def test_single_id_command_is_frozen(
    command_class,
):
    command = command_class(
        container_id="container1",
    )

    with pytest.raises(FrozenInstanceError):
        command.container_id = "container2"