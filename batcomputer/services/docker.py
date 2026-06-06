import docker

client = docker.from_env()


def get_containers():

    containers = []

    for container in client.containers.list():

        containers.append({
            "name": container.name,
            "status": container.status,
            "image": container.image.tags[0]
            if container.image.tags else "unknown"
        })

    return containers
