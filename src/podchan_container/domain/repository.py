from abc import ABC, abstractmethod

from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.value_object import PodchanContainerId


class PodchanContainerRepository(ABC):
    """
    Podchanのコンテナを保持するRepositoryです。

    Domain層からは永続化方法を隠蔽し、
    Infrastructure層で実装を提供します。
    """

    @abstractmethod
    def save(self, container: PodchanContainer) -> None:
        """
        コンテナを保存します。
        """

    @abstractmethod
    def delete(
        self,
        container_id: PodchanContainerId,
    ) -> PodchanContainer:
        """
        コンテナを削除します。

        Returns:
            削除されたコンテナ
        """

    @abstractmethod
    def find(
        self,
        container_id: PodchanContainerId,
    ) -> PodchanContainer:
        """
        IDからコンテナを取得します。
        """

    @abstractmethod
    def find_all(self) -> list[PodchanContainer]:
        """
        すべてのコンテナを取得します。
        """