class ContainerId:
    """
    podchanで管理するContainerの識別子。
    """

    def __init__(self, value: str):
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def to_debug_string(self) -> str:
        return f"ContainerId(value={self._value})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, ContainerId):
            return False

        return self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)