from textual.widgets import Static

from batcomputer.services import docker_state
from batcomputer.services.docker import (
    get_container_health
)


class DockerHealth(Static):

    def on_mount(self):

        self.refresh_health()

        self.set_interval(
            1,
            self.refresh_health
        )

    def refresh_health(self):

        selected = (
            docker_state.selected_container
        )

        if not selected:
            return

        try:

            health = get_container_health(
                selected
            )

            status = health["status"]

            if status == "running":

                color = "#00FF88"

            elif status == "restarting":

                color = "#F7C600"

            else:

                color = "#FF4444"

            uptime = str(
                health["uptime"]
            ).split(".")[0]

            created = (
                health["created"]
                .split("T")[0]
            )

            self.update(
f"""[bold #FF003C]STATUS[/]

[{color}]● {status.upper()}[/]
CTR:{health["name"]}
UP :{uptime}
CRT:{created}
PID:{health["pid"]}
IP :{health["ip"]}
"""
            )

        except Exception as e:

            self.update(
f"""[bold #FF003C]STATUS[/]

ERROR

{repr(e)}
"""
            )
