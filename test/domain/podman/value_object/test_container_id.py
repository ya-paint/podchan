from domain.podman.value_object.container_id import ContainerId


def test_equals():
    a = ContainerId("abc")
    b = ContainerId("abc")

    assert a == b


def test_not_equals():
    a = ContainerId("abc")
    b = ContainerId("def")

    assert a != b


def test_value():
    container_id = ContainerId("abc")

    assert container_id.value == "abc"


def test_hash_equals():
    a = ContainerId("abc")
    b = ContainerId("abc")

    assert hash(a) == hash(b)


def test_not_equals_other_type():
    container_id = ContainerId("abc")

    assert container_id != "abc"


def test_to_debug_string():
    container_id = ContainerId("abc")

    assert (
        container_id.to_debug_string()
        == "ContainerId(value=abc)"
    )