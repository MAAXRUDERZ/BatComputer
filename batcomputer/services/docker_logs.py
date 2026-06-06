import docker

client = docker.from_env()


def get_container_logs(
    name,
    tail=50,
):

    container = client.containers.get(name)

    logs = container.logs(
        tail=tail
    ).decode(
        errors="ignore"
    )

    return logs
