from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import RunningStatus,StoppedStatus

class PodchanContainerData:
    def __init__(
        self,
        container: PodchanContainer,
    ):
        self._id = container.id.value
        self._name = container.name.value
        self._image = container.config.image

        if isinstance( container.status, RunningStatus ):
            self._status = "running"
        if isinstance( container.status, StoppedStatus ):
            self._status = "stop"

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_image(self) -> str:
        return self._image

    def get_status(self) -> str:
        return self._status
