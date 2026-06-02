from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerConfig,
    PodchanContainerName,
)

from podchan_container.domain.operator_event import (
    PodchanContainerOperatorStartedEvent,
    PodchanContainerOperatorStoppedEvent,
    PodchanContainerOperatorEventListener,
)

from podchan_container.domain.operator import PodchanContainerOperator


# -------------------------
# Fake Runtime
# -------------------------
class FakeRuntime(PodchanContainerRuntime):
    def __init__(self, container):
        super().__init__(container)
        self.started = False
        self.stopped = False
        self.synced = False

    def start(self):
        self.started = True

    def stop(self):
        self.stopped = True

    def sync(self):
        self.synced = True


# -------------------------
# Fake Listener
# -------------------------
class FakeListener(PodchanContainerOperatorEventListener):
    def __init__(self):
        self.events = []

    def on_event(self, event):
        self.events.append(event)


# -------------------------
# startイベントテスト
# -------------------------
def test_operator_start_event():
    container_id = PodchanContainerId("id1")

    container = PodchanContainer(
        container_id,
        PodchanContainerConfig("nginx"),
    )

    runtime = FakeRuntime(container)
    operator = PodchanContainerOperator(container, runtime)

    listener = FakeListener()
    operator.subscribe(listener)

    operator.start()

    # runtime確認
    assert runtime.started is True

    # event確認
    assert len(listener.events) == 1

    event = listener.events[0]

    assert isinstance(event, PodchanContainerOperatorStartedEvent)
    assert event.container_id.value == "id1"


# -------------------------
# stopイベントテスト
# -------------------------
def test_operator_stop_event():
    container_id = PodchanContainerId("id1")

    container = PodchanContainer(
        container_id,
        PodchanContainerConfig("nginx"),
    )

    runtime = FakeRuntime(container)
    operator = PodchanContainerOperator(container, runtime)

    listener = FakeListener()
    operator.subscribe(listener)

    operator.stop()

    # runtime確認
    assert runtime.stopped is True

    # event確認
    assert len(listener.events) == 1

    event = listener.events[0]

    assert isinstance(event, PodchanContainerOperatorStoppedEvent)
    assert event.container_id.value == "id1"


# -------------------------
# unsubscribeテスト
# -------------------------
def test_operator_unsubscribe():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerConfig("nginx"),
    )

    runtime = FakeRuntime(container)
    operator = PodchanContainerOperator(container, runtime)

    listener = FakeListener()
    operator.subscribe(listener)
    operator.unsubscribe(listener)

    operator.start()

    assert len(listener.events) == 0