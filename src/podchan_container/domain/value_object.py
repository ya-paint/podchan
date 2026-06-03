# value_object.py

class PodchanContainerId:
    def __init__(self, value: str):
        if not value:
            raise ValueError("id cannot be empty")
        self._value = value

    @property
    def value(self):
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PodchanContainerId):
            return False

        return self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

class PodchanContainerName:
    def __init__(self, value: str):
        if not value:
            raise ValueError("name cannot be empty")
        self._value = value

    @property
    def value(self):
        return self._value

class PodchanContainerConfig:
    def __init__(self, image: str):
        if not image:
            raise ValueError("image cannot be empty")
        self._image = image

    @property
    def image(self):
        return self._image

class PodchanContainerStatus:
    def is_change_config(self) -> bool:
        raise NotImplementedError
    def is_change_name(self) -> bool:
        raise NotImplementedError

class RunningStatus(PodchanContainerStatus):
    def is_change_config(self):
        return False
    def is_change_name(self):
        return False

class StoppedStatus(PodchanContainerStatus):
    def is_change_config(self):
        return True
    def is_change_name(self):
        return True