import subprocess
import json

from podchan_container.domain.runtime import (
    PodchanContainerRuntime,
    PodchanContainerStartError,
    PodchanContainerStopError,
)
from podchan_container.domain.entity import PodchanContainer


class PodmanContainerRuntime(PodchanContainerRuntime):
    # -------------------------
    # start
    # -------------------------
    def start(self, container: PodchanContainer):
        container_id = container.id.value

        # ① 存在確認 → なければ作る
        subprocess.run(
            [
                "podman",
                "create",
                "--name",
                container_id,
                container.config.image,
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        # ② 起動
        subprocess.run(
            ["podman", "start", container_id],
            capture_output=True,
            text=True,
            check=False,
        )

        self.sync(container)

        from podchan_container.domain.value_object import RunningStatus

        if not isinstance(container.status, RunningStatus):
            raise PodchanContainerStartError(
                f"failed to start container '{container_id}'"
            )

    # -------------------------
    # stop
    # -------------------------
    def stop(self, container: PodchanContainer):
        container_id = container.id.value

        subprocess.run(
            ["podman", "stop", container_id],
            capture_output=True,
            text=True,
            check=False,
        )

        subprocess.run(
            ["podman", "rm", container_id],
            capture_output=True,
            text=True,
            check=False,
        )

        self.sync(container)

        from podchan_container.domain.value_object import StoppedStatus

        if not isinstance(container.status, StoppedStatus):
            raise PodchanContainerStopError(
                f"failed to stop container '{container_id}'"
            )

    # -------------------------
    # sync
    # -------------------------
    def sync(self, container: PodchanContainer):
        """
        Podmanの実状態をContainerに反映する
        """
        container_id = container.id.value

        from podchan_container.domain.value_object import (
            RunningStatus,
            StoppedStatus,
        )

        result = subprocess.run(
            ["podman", "inspect", container_id],
            capture_output=True,
            text=True,
            check=False,
        )

        # コンテナが存在しない
        if result.returncode != 0:
            container.change_status(StoppedStatus())
            return

        data = json.loads(result.stdout)

        state = data[0].get("State", {}).get("Status")

        if state == "running":
            container.change_status(RunningStatus())
        else:
            container.change_status(StoppedStatus())