# entity.py

from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerName,
    PodchanContainerConfig,
    PodchanContainerStatus,
    StoppedStatus
)


class PodchanContainer:
    def __init__(
        self,
        id: PodchanContainerId,
        name: PodchanContainerName,
        config: PodchanContainerConfig,
    ):
        self._id = id
        self._name = name
        self._config = config
        self._status: PodchanContainerStatus = StoppedStatus()

    # --------------------
    # change name
    # --------------------
    def change_name(self, name: PodchanContainerName):
        if self._status and not self._status.is_change_name():
            raise Exception("name cannot be changed in current status")

        self._name = name

    # --------------------
    # change config
    # --------------------
    def change_config(self, config: PodchanContainerConfig):
        if not self._status or not self._status.is_change_config():
            raise Exception("config cannot be changed in current status")

        self._config = config

    # --------------------
    # change status
    # --------------------
    def change_status(self, status: PodchanContainerStatus):
        self._status = status

    # --------------------
    # getters (必要最小限)
    # --------------------
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def config(self):
        return self._config

    @property
    def status(self):
        return self._status