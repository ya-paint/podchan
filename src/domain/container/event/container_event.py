from abc import ABC
from dataclasses import dataclass

from container_domain.entity.container import Container
from container_domain.value_object.container_id import ContainerId


class ContainerEvent(ABC):
    """
    Containerに関係するDomain Eventです。

    Containerの状態変更や作成・削除など、
    Domain内で発生した出来事を表現します。
    """
    pass


@dataclass(frozen=True)
class ContainerStatusChangedEvent(ContainerEvent):
    """
    Containerの状態が変更された際のイベントです。

    Attributes:
        container:
            状態が変更されたContainer
    """

    container: Container


@dataclass(frozen=True)
class ContainerCreatedEvent(ContainerEvent):
    """
    Containerが作成された際のイベントです。

    Attributes:
        container_id:
            作成されたContainerのID
    """

    container_id: ContainerId


@dataclass(frozen=True)
class ContainerDeletedEvent(ContainerEvent):
    """
    Containerが削除された際のイベントです。

    Attributes:
        container_id:
            削除されたContainerのID
    """

    container_id: ContainerId