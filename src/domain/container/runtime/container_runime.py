from abc import ABC, abstractmethod

from src.domain.container.entity.container import Container
from src.domain.container.value_object.container_id import ContainerId
from src.domain.container.value_object.container_config import ContainerConfig


class ContainerRuntime(ABC):
    """
    Container Runtime を操作するインターフェースです。

    Podman や Docker などの実行環境を抽象化します。
    """

    @abstractmethod
    def create(self, container_config: ContainerConfig) -> None:
        """
        Containerを作成します。

        Args:
            container: 作成するContainer
        """
        pass

    @abstractmethod
    def start(self, container_id: ContainerId) -> None:
        """
        Containerを起動します。

        Args:
            container_id: Container識別子
        """
        pass

    @abstractmethod
    def stop(self, container_id: ContainerId) -> None:
        """
        Containerを停止します。

        Args:
            container_id: Container識別子
        """
        pass

    @abstractmethod
    def restart(self, container_id: ContainerId) -> None:
        """
        Containerを再起動します。

        Args:
            container_id: Container識別子
        """
        pass

    @abstractmethod
    def delete(self, container_id: ContainerId) -> None:
        """
        Containerを削除します。

        Args:
            container_id: Container識別子
        """
        pass

    @abstractmethod
    def list_containers(self) -> list[Container]:
        """
        Runtime上に存在するContainerを取得します。

        Returns:
            Container一覧
        """
        pass

    @abstractmethod
    def inspect(self, container_id: ContainerId) -> Container:
        """
        Containerの詳細情報を取得します。

        Args:
            container_id: Container識別子

        Returns:
            Container
        """
        pass