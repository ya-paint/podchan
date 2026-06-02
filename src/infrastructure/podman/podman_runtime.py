import json
import subprocess

from domain.container.entity.container import Container
from domain.container.runtime.container_runtime import ContainerRuntime
from domain.container.value_object.container_config import ContainerConfig
from domain.container.value_object.container_id import ContainerId
from domain.container.value_object.container_status import (
    RunningStatus,
    PausedStatus,
    StoppedStatus,
)


class PodmanRuntime(ContainerRuntime):
    def create(
        self,
        container_config: ContainerConfig,
    ) -> ContainerId:
        command = [
            "podman",
            "create",
            "--name",
            container_config.name,
        ]

        for env in container_config.env:
            command.extend(
                [
                    "-e",
                    env,
                ]
            )

        for port in container_config.ports:
            command.extend(
                [
                    "-p",
                    port,
                ]
            )

        for volume in container_config.volumes:
            command.extend(
                [
                    "-v",
                    volume,
                ]
            )

        if container_config.restart:
            command.extend(
                [
                    "--restart",
                    container_config.restart,
                ]
            )

        command.append(container_config.image)

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        return ContainerId(result.stdout.strip())

    def start(
        self,
        container_id: ContainerId,
    ) -> None:
        subprocess.run(
            [
                "podman",
                "start",
                container_id.value,
            ],
            check=True,
        )

    def stop(
        self,
        container_id: ContainerId,
    ) -> None:
        subprocess.run(
            [
                "podman",
                "stop",
                container_id.value,
            ],
            check=True,
        )

    def restart(
        self,
        container_id: ContainerId,
    ) -> None:
        subprocess.run(
            [
                "podman",
                "restart",
                container_id.value,
            ],
            check=True,
        )

    def delete(
        self,
        container_id: ContainerId,
    ) -> None:
        subprocess.run(
            [
                "podman",
                "rm",
                "-f",
                container_id.value,
            ],
            check=True,
        )

    def list_containers(
        self,
    ) -> list[Container]:
        result = subprocess.run(
            [
                "podman",
                "ps",
                "-a",
                "--format",
                "json",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        containers = []

        for item in json.loads(result.stdout):
            container_id = ContainerId(item["Id"])

            containers.append(
                self.inspect(container_id)
            )

        return containers

    def inspect(
        self,
        container_id: ContainerId,
    ) -> Container:
        result = subprocess.run(
            [
                "podman",
                "inspect",
                container_id.value,
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        data = json.loads(result.stdout)[0]

        state = data["State"]["Status"]

        if state == "running":
            status = RunningStatus()
        elif state == "paused":
            status = PausedStatus()
        else:
            status = StoppedStatus()

        config = ContainerConfig(
            image=data["Config"]["Image"],
            name=data["Name"].lstrip("/"),
            env={},
            ports={},
            volumes={},
            restart="",
        )

        return Container(
            container_id=ContainerId(data["Id"]),
            container_config=config,
            container_status=status,
        )