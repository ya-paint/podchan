from abc import ABC, abstractmethod

from src.domain.container.entity.container import Container
from src.domain.container.value_object.container_id import ContainerId


class ContainerRepository(ABC):
    """
    Containerを管理するRepositoryです。

    Containerの永続化および取得を担当します。
    """

    @abstractmethod
    def save(self, container: Container) -> None:
        """
        Containerを保存します。

        Args:
            container: 保存するContainer
        """
        pass

    @abstractmethod
    def read(self, container_id: ContainerId) -> Container:
        """
        Containerを取得します。

        Args:
            container_id: Container識別子

        Returns:
            Container
        """
        pass

    @abstractmethod
    def find_all(self) -> list[Container]:
        """
        すべてのContainerを取得します。

        Returns:
            Container一覧
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