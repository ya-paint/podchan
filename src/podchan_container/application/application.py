
from podchan_container.application.application_command import (
    PodchanContainerApplicationDeleteCommand,
    PodchanContainerApplicationRegistCommand,
    PodchanContainerApplicationStartCommand,
    PodchanContainerApplicationStopCommand,
    PodchanContainerApplicationUpdateCommand,
)
from podchan_container.application.application_event import (
    PodchanContainerApplicationEvent,
    PodchanContainerStartedEvent,
    PodchanContainerStatusEvent,
    PodchanContainerStoppedEvent,
    PodchanContainerApplicationEventListener,
)
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.operator import PodchanContainerOperator
from podchan_container.domain.operator_event import (
    PodchanContainerOperatorEvent,
    PodchanContainerOperatorStartedEvent,
    PodchanContainerOperatorStatusEvent,
    PodchanContainerOperatorStoppedEvent,
    PodchanContainerOperatorEventListener,
)
from podchan_container.domain.repository import PodchanContainerRepository
from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.value_object import PodchanContainerConfig, PodchanContainerId, PodchanContainerName


class PodchanContainerApplicationEventPublisher(
    PodchanContainerOperatorEventListener,
):
    """
    OperatorEventをApplicationEventへ変換して配信するクラスです。
    """

    def __init__(self,repository : PodchanContainerRepository) -> None:
        self._repository = repository
        self._listeners: list[
            PodchanContainerApplicationEventListener
        ] = []

    def subscribe(
        self,
        listener: PodchanContainerApplicationEventListener,
    ) -> None:
        if listener not in self._listeners:
            self._listeners.append(listener)

    def unsubscribe(
        self,
        listener: PodchanContainerApplicationEventListener,
    ) -> None:
        if listener in self._listeners:
            self._listeners.remove(listener)

    def _publish(self, event : PodchanContainerApplicationEvent ) -> None:
        for listener in self._listeners:
            listener.on_event(event)

    def _convert_event(
        self,
        event: PodchanContainerOperatorEvent
    ) -> PodchanContainerApplicationEvent | None :

        if isinstance(event, PodchanContainerOperatorStartedEvent) :
            if self._repository.exists(event.container_id):
                return PodchanContainerStartedEvent(
                    self._repository.find(event.container_id)
                )
        if isinstance(event, PodchanContainerOperatorStoppedEvent) :
            if self._repository.exists(event.container_id):
                return PodchanContainerStoppedEvent(
                    self._repository.find(event.container_id)
                )
        if isinstance(event, PodchanContainerOperatorStatusEvent) :
            if self._repository.exists(event.container_id):
                return PodchanContainerStatusEvent(
                    self._repository.find(event.container_id)
                )

        return None

    def on_event(
        self,
        event: PodchanContainerOperatorEvent,
    ) -> None:
        """
        OperatorEvent → ApplicationEvent変換
        """

        app_event = self._convert_event(event)

        if app_event != None :
            self._publish(app_event)

class PodchanContainerApplication:
    def __init__(
        self,
        repository: PodchanContainerRepository,
        runtime: PodchanContainerRuntime,
    ) -> None:
        self._repository = repository
        self._runtime = runtime

        self._event_publisher = (
            PodchanContainerApplicationEventPublisher(
                self._repository
            )
        )

    def regist(
        self,
        command: PodchanContainerApplicationRegistCommand,
    ) -> None:
        container = PodchanContainer(
            id=PodchanContainerId(
                command.container_id
            ),
            name=PodchanContainerName(
                command.name
            ),
            config=PodchanContainerConfig(
                command.image
            ),
        )

        self._repository.save(container)

    def delete(
        self,
        command: PodchanContainerApplicationDeleteCommand,
    ) -> PodchanContainer:
        return self._repository.delete(
            PodchanContainerId(
                command.container_id
            )
        )

    def start(
        self,
        command: PodchanContainerApplicationStartCommand,
    ) -> None:
        container = self._repository.find(
            PodchanContainerId(
                command.container_id
            )
        )

        operator = PodchanContainerOperator(
            container,
            self._runtime,
        )

        operator.subscribe(
            self._event_publisher
        )

        operator.start()

    def stop(
        self,
        command: PodchanContainerApplicationStopCommand,
    ) -> None:
        container = self._repository.find(
            PodchanContainerId(
                command.container_id
            )
        )

        operator = PodchanContainerOperator(
            container,
            self._runtime,
        )

        operator.subscribe(
            self._event_publisher
        )

        operator.stop()

    def update(
        self,
        command: PodchanContainerApplicationUpdateCommand,
    ) -> None:
        container = self._repository.find(
            PodchanContainerId(
                command.container_id
            )
        )

        operator = PodchanContainerOperator(
            container,
            self._runtime,
        )

        operator.subscribe(
            self._event_publisher
        )

        operator.sync()

    def subscribe(
        self,
        listener: PodchanContainerApplicationEventListener,
    ) -> None:
        self._event_publisher.subscribe(
            listener
        )

    def unsubscribe(
        self,
        listener: PodchanContainerApplicationEventListener,
    ) -> None:
        self._event_publisher.unsubscribe(
            listener
        )