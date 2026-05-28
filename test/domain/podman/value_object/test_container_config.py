from domain.podman.value_object.container_config import ContainerConfig


def test_equals():
    a = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=["./data:/data"],
        restart="always",
    )

    b = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=["./data:/data"],
        restart="always",
    )

    assert a == b


def test_not_equals():
    a = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=["./data:/data"],
        restart="always",
    )

    b = ContainerConfig(
        image="redis:latest",
        name="cache",
        env=["ENV=dev"],
        ports=["6379:6379"],
        volumes=["./redis:/data"],
        restart="no",
    )

    assert a != b


def test_image():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=[],
        ports=[],
        volumes=[],
        restart="always",
    )

    assert config.image == "nginx:latest"


def test_name():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=[],
        ports=[],
        volumes=[],
        restart="always",
    )

    assert config.name == "web"


def test_env():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=[],
        volumes=[],
        restart="always",
    )

    assert config.env == ["ENV=prod"]


def test_ports():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=[],
        ports=["8080:80"],
        volumes=[],
        restart="always",
    )

    assert config.ports == ["8080:80"]


def test_volumes():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=[],
        ports=[],
        volumes=["./data:/data"],
        restart="always",
    )

    assert config.volumes == ["./data:/data"]


def test_restart():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=[],
        ports=[],
        volumes=[],
        restart="always",
    )

    assert config.restart == "always"


def test_hash_equals():
    a = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=["./data:/data"],
        restart="always",
    )

    b = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=["./data:/data"],
        restart="always",
    )

    assert hash(a) == hash(b)


def test_not_equals_other_type():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=[],
        ports=[],
        volumes=[],
        restart="always",
    )

    assert config != "config"


def test_to_debug_string():
    config = ContainerConfig(
        image="nginx:latest",
        name="web",
        env=["ENV=prod"],
        ports=["8080:80"],
        volumes=["./data:/data"],
        restart="always",
    )

    assert (
        config.to_debug_string()
        == "ContainerConfig(image=nginx:latest, "
        "name=web, "
        "env=['ENV=prod'], "
        "ports=['8080:80'], "
        "volumes=['./data:/data'], "
        "restart=always)"
    )