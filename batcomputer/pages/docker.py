from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical

from batcomputer.widgets.docker_container_list import DockerContainerList
from batcomputer.widgets.docker_health import DockerHealth
from batcomputer.widgets.docker_network import DockerNetwork
from batcomputer.widgets.docker_io import DockerIO
from batcomputer.widgets.docker_processes import DockerProcesses
from batcomputer.widgets.docker_ports import DockerPorts
from batcomputer.widgets.docker_logs import DockerLogs
from batcomputer.widgets.docker_actions import DockerActions
from batcomputer.widgets.docker_cpu_graph import DockerCPUGraph


class DockerPage(Widget):

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

            yield DockerContainerList()

            with Vertical():

                with Horizontal():

                    yield DockerHealth()
                    yield DockerPorts()

                with Horizontal():

                    yield DockerCPUGraph()
                    #yield DockerMemory()

                with Horizontal():

                    yield DockerNetwork()
                    yield DockerIO()

                yield DockerProcesses()

        yield DockerLogs()

        yield DockerActions()
