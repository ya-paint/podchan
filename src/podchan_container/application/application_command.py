from dataclasses import dataclass


@dataclass(frozen=True)
class PodchanContainerApplicationRegistCommand:
    container_id: str
    name: str
    image: str

    def __post_init__(self):
        if not isinstance(self.container_id, str):
            raise TypeError("container_id must be str")

        if not isinstance(self.name, str):
            raise TypeError("name must be str")

        if not isinstance(self.image, str):
            raise TypeError("image must be str")

@dataclass(frozen=True)
class PodchanContainerApplicationDeleteCommand:
    container_id: str

    def __post_init__(self):
        if not isinstance(self.container_id, str):
            raise TypeError("container_id must be str")


@dataclass(frozen=True)
class PodchanContainerApplicationStartCommand:
    container_id: str

    def __post_init__(self):
        if not isinstance(self.container_id, str):
            raise TypeError("container_id must be str")


@dataclass(frozen=True)
class PodchanContainerApplicationStopCommand:
    container_id: str

    def __post_init__(self):
        if not isinstance(self.container_id, str):
            raise TypeError("container_id must be str")


@dataclass(frozen=True)
class PodchanContainerApplicationUpdateCommand:
    container_id: str

    def __post_init__(self):
        if not isinstance(self.container_id, str):
            raise TypeError("container_id must be str")