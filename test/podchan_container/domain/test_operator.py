import pytest
from podchan_container.domain.entity import PodchanContainer
from podchan_container.domain.runtime import PodchanContainerRuntime
from podchan_container.domain.value_object import (
    PodchanContainerId,
    PodchanContainerConfig,
    PodchanContainerName,
)

from podchan_container.domain.operator_event import (
    PodchanContainerOperatorErrorEvent,
    PodchanContainerOperatorStartedEvent,
    PodchanContainerOperatorStoppedEvent,
    PodchanContainerOperatorStatusEvent,
    PodchanContainerOperatorEventListener,
)

from podchan_container.domain.operator import PodchanContainerOperator


# -------------------------
# Fake Runtime
# -------------------------
class FakeRuntime(PodchanContainerRuntime):
    def __init__(self):
        self.started = False
        self.stopped = False
        self.synced = False

    def start(self, container):
        self.started = True

    def stop(self, container):
        self.stopped = True

    def sync(self, container):
        self.synced = True

# -------------------------
# Error Runtime
# -------------------------
class ErrorRuntime(PodchanContainerRuntime):
    def start(self, container):
        raise RuntimeError("start failed")

    def stop(self, container):
        raise RuntimeError("stop failed")

    def sync(self, container):
        raise RuntimeError("sync failed")

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
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx"),
    )

    runtime = FakeRuntime()
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
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx"),
    )

    runtime = FakeRuntime()
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
# syncイベントテスト
# -------------------------
def test_operator_sync_event():
    container_id = PodchanContainerId("id1")

    container = PodchanContainer(
        container_id,
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx"),
    )

    runtime = FakeRuntime()
    operator = PodchanContainerOperator(container, runtime)

    listener = FakeListener()
    operator.subscribe(listener)

    operator.sync()

    # runtime確認
    assert runtime.synced is True

    # event確認
    assert len(listener.events) == 1

    event = listener.events[0]

    assert isinstance(event, PodchanContainerOperatorStatusEvent)
    assert event.container_id.value == "id1"


# -------------------------
# unsubscribeテスト
# -------------------------
def test_operator_unsubscribe():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx"),
    )

    runtime = FakeRuntime()
    operator = PodchanContainerOperator(container, runtime)

    listener = FakeListener()
    operator.subscribe(listener)
    operator.unsubscribe(listener)

    operator.start()

    assert len(listener.events) == 0

def test_operator_start_error_event():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx"),
    )

    runtime = ErrorRuntime()
    operator = PodchanContainerOperator(container, runtime)

    listener = FakeListener()
    operator.subscribe(listener)

    with pytest.raises(RuntimeError):
        operator.start()

    assert len(listener.events) == 1

    event = listener.events[0]

    assert isinstance(
        event,
        PodchanContainerOperatorErrorEvent,
    )

    assert event.container_id.value == "id1"
    assert event.message == "start failed"

def test_operator_stop_error_event():
    container = PodchanContainer(
        PodchanContainerId("id1"),
        PodchanContainerName("name1"),
        PodchanContainerConfig("nginx"),
    )

    runtime = ErrorRuntime()
    operator = PodchanContainerOperator(container, runtime)

    listener = FakeListener()
    operator.subscribe(listener)

    with pytest.raises(RuntimeError):
        operator.stop()

    assert len(listener.events) == 1

    event = listener.events[0]

    assert isinstance(
        event,
        PodchanContainerOperatorErrorEvent,
    )

    assert event.container_id.value == "id1"
    assert event.message == "stop failed"
