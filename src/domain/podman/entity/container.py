from domain.podman.value_object.container_id import ContainerId
from domain.podman.value_object.container_config import ContainerConfig


class Container:
    """
    podchanで管理するContainer Entity。
    """

    def __init__(
        self,
        container_id: ContainerId,
        config: ContainerConfig,
    ):
        self._id = container_id
        self._config = config

    @property
    def id(self) -> ContainerId:
        return self._id

    @property
    def config(self) -> ContainerConfig:
        return self._config
    
    def change_config(
        self,
        config: ContainerConfig
    ) -> None:
        self._config = config

    def to_debug_string(self) -> str:
        return (
            "Container("
            f"id={self._id.to_debug_string()}, "
            f"config={self._config.to_debug_string()}"
            ")"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Container):
            return False

        return self._id == other._id


    def __hash__(self) -> int:
        return hash(self._id)