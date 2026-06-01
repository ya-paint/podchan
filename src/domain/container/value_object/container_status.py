from abc import ABC, abstractmethod
from dataclasses import dataclass


class ContainerStatus(ABC):
    """
    Containerの状態を表す抽象クラスです。

    Containerが現在どの状態にあるかを表現するために利用します。
    実際の状態は継承クラスで表現されます。

    Examples:
        >>> status = RunningStatus()
        >>> status.to_debug_string()
        'running'
    """

    @abstractmethod
    def to_debug_string(self) -> str:
        """
        状態をデバッグ用文字列として取得します。

        Returns:
            状態を表す文字列
        """
        pass


@dataclass(frozen=True)
class RunningStatus(ContainerStatus):
    """
    Containerが起動中であることを表す状態です。
    """

    def to_debug_string(self) -> str:
        """
        状態をデバッグ用文字列として取得します。

        Returns:
            ``running``
        """
        return "running"


@dataclass(frozen=True)
class PausedStatus(ContainerStatus):
    """
    Containerが一時停止中であることを表す状態です。
    """

    def to_debug_string(self) -> str:
        """
        状態をデバッグ用文字列として取得します。

        Returns:
            ``paused``
        """
        return "paused"


@dataclass(frozen=True)
class StoppedStatus(ContainerStatus):
    """
    Containerが停止中であることを表す状態です。
    """

    def to_debug_string(self) -> str:
        """
        状態をデバッグ用文字列として取得します。

        Returns:
            ``stopped``
        """
        return "stopped"