from podchan_container.domain.entity import PodchanContainer

class PodchanContainerData:
    def __init__(
        self,
        container: PodchanContainer,
    ):
        self._id = container.id.value
        self._name = container.name.value
        self._image = container.config.image

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_image(self) -> str:
        return self._image