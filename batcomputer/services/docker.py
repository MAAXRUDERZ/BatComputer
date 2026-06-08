import docker

from datetime import (
    datetime,
    timezone,
)

client = docker.from_env()


def get_containers():

    containers = []

    for container in client.containers.list(
        all=True
    ):

        containers.append({
            "name": container.name,
            "status": container.status,
            "image": (
                container.image.tags[0]
                if container.image.tags
                else "unknown"
            )
        })

    return containers


def get_container(name):

    return client.containers.get(name)


def start_container(name):

    get_container(name).start()


def stop_container(name):

    get_container(name).stop()


def restart_container(name):

    get_container(name).restart()


def get_container_health(name):

    container = get_container(name)

    status = container.status

    started_at = (
        container.attrs["State"]["StartedAt"]
    )

    started_at = datetime.fromisoformat(
        started_at.replace(
            "Z",
            "+00:00"
        )
    )

    if status == "running":

        uptime = (
            datetime.now(timezone.utc)
            - started_at
        )

    else:

        uptime = "OFFLINE"

    created_at = (
        container.attrs["Created"]
    )

    pid = (
        container.attrs["State"]["Pid"]
    )

    networks = (
        container.attrs
        .get("NetworkSettings", {})
        .get("Networks", {})
    )

    ip = "N/A"
    network_name = "N/A"

    if networks:

        network_name = next(
            iter(networks.keys())
        )

        first_network = next(
            iter(networks.values())
        )

        ip = first_network.get(
            "IPAddress",
            "N/A"
        )

    image = (
        container.image.tags[0]
        if container.image.tags
        else "unknown"
    )

    return {
        "name": container.name,
        "status": status,
        "id": container.short_id,
        "uptime": uptime,
        "created": created_at,
        "pid": pid,
        "ip": ip,
        "image": image,
        "network": network_name,
        "ports": container.attrs["NetworkSettings"]["Ports"],
    }


def get_container_details(name):

    container = get_container(name)

    return {
        "name": container.name,
        "status": container.status,
        "image": (
            container.image.tags[0]
            if container.image.tags
            else "unknown"
        ),
        "id": container.short_id,
    }


def get_container_ports(name):

    container = get_container(name)

    ports = (
        container.attrs
        ["NetworkSettings"]
        ["Ports"]
    )

    return ports
