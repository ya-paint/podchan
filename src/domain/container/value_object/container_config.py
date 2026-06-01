class ContainerConfig:
    """
    podchanで管理するContainerの設定。
    """

    def __init__(
        self,
        image: str,
        name: str,
        env: list[str],
        ports: list[str],
        volumes: list[str],
        restart: str,
    ):
        self._image = image
        self._name = name
        self._env = env
        self._ports = ports
        self._volumes = volumes
        self._restart = restart

    @property
    def image(self) -> str:
        return self._image

    @property
    def name(self) -> str:
        return self._name

    @property
    def env(self) -> list[str]:
        return self._env

    @property
    def ports(self) -> list[str]:
        return self._ports

    @property
    def volumes(self) -> list[str]:
        return self._volumes

    @property
    def restart(self) -> str:
        return self._restart

    def to_debug_string(self) -> str:
        return (
            "ContainerConfig("
            f"image={self._image}, "
            f"name={self._name}, "
            f"env={self._env}, "
            f"ports={self._ports}, "
            f"volumes={self._volumes}, "
            f"restart={self._restart}"
            ")"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, ContainerConfig):
            return False

        return (
            self._image == other._image
            and self._name == other._name
            and self._env == other._env
            and self._ports == other._ports
            and self._volumes == other._volumes
            and self._restart == other._restart
        )

    def __hash__(self) -> int:
        return hash(
            (
                self._image,
                self._name,
                tuple(self._env),
                tuple(self._ports),
                tuple(self._volumes),
                self._restart,
            )
        )