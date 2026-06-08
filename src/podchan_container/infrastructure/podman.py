import subprocess
import json

from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.entity import PodchanContainer


class PodmanContainerRuntime(PodchanContainerRuntime):
    # -------------------------
    # start
    # -------------------------
    def start(self, container: PodchanContainer):
        container_id = container.id.value

        # ① 存在確認 → なければ作る
        subprocess.run(
            ["podman", "create", "--name", container_id, container.config.image],
            check=False,
        )

        # ② 起動
        subprocess.run(
            ["podman", "start", container_id],
            check=True,
        )

        self.sync(container)

    # -------------------------
    # stop
    # -------------------------
    def stop(self, container: PodchanContainer):
        container_id = container.id.value

        subprocess.run(["podman", "stop", container_id], check=False)
        subprocess.run(["podman", "rm", container_id], check=False)

        from podchan_container.domain.value_object import StoppedStatus
        container.change_status(StoppedStatus())

    # -------------------------
    # sync
    # -------------------------
    def sync(self, container: PodchanContainer):
        """
        Podmanの実状態をContainerに反映する
        """
        container_id = container.id.value

        result = subprocess.run(
            ["podman", "inspect", container_id],
            capture_output=True,
            text=True,
            check=True,
        )

        # 最小実装：状態だけ見る（簡略版）
        data = json.loads(result.stdout)

        state = data[0].get("State", {}).get("Status")

        from podchan_container.domain.value_object import RunningStatus, StoppedStatus
        if state == "running":
            container.change_status(RunningStatus())
        else:
            container.change_status(StoppedStatus())