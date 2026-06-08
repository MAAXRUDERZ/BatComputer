from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from textual.binding import Binding

from batcomputer.widgets.log_popup import LogPopup
from batcomputer.services import docker_state

from batcomputer.widgets.docker_system import (
    DockerSystem
)

from batcomputer.services.docker import (
    start_container,
    stop_container,
    restart_container,
)

from batcomputer.widgets.docker_container_list import DockerContainerList
from batcomputer.widgets.docker_health import DockerHealth
from batcomputer.widgets.docker_ports import DockerPorts
from batcomputer.widgets.docker_logs import DockerLogs
from batcomputer.widgets.docker_actions import DockerActions


class DockerPage(Widget):

    BINDINGS = [
        Binding("s", "start", "Start"),
        Binding("t", "stop", "Stop"),
        Binding("r", "restart", "Restart"),
        Binding("l", "full_logs", "Logs"),
    ]

    def action_start(self):

        if not docker_state.selected_container:
            return

        start_container(
            docker_state.selected_container
        )

        self.notify(
            f"Started {docker_state.selected_container}"
        )

    def action_stop(self):

        if not docker_state.selected_container:
            return

        stop_container(
            docker_state.selected_container
        )

        self.notify(
            f"Stopped {docker_state.selected_container}"
        )

    def action_restart(self):

        if not docker_state.selected_container:
            return

        restart_container(
            docker_state.selected_container
        )

        self.notify(
            f"Restarted {docker_state.selected_container}"
        )

    def action_full_logs(self):

        if not docker_state.selected_container:
            return

        self.app.push_screen(
            LogPopup(
                docker_state.selected_container
            )
        )

    def compose(self):

        yield Static(
"""[bold #90A4AE]
╔══════════════════════════════════════════════╗
 ║          BATCOMPUTER DOCKER CENTER         ║
 ║        CONTAINER OBSERVABILITY HUB         ║
╚══════════════════════════════════════════════╝
[/]
"""
        )

        with Horizontal():

            with Vertical(
                classes="docker-left"
            ):

                yield DockerContainerList()

                yield DockerSystem()

            with Vertical():

                with Horizontal():

                    yield DockerHealth()

                    yield DockerPorts()

                yield DockerLogs()

        yield DockerActions()
