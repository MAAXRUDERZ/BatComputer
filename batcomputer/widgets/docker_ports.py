from textual.widgets import Static

from batcomputer.services import docker_state
from batcomputer.services.docker import (
    get_container_ports
)


class DockerPorts(Static):

    def on_mount(self):

        self.refresh_ports()

        self.set_interval(
            1,
            self.refresh_ports
        )

    def refresh_ports(self):

        selected = (
            docker_state.selected_container
        )

        if not selected:
            return

        try:

            ports = get_container_ports(
                selected
            )

            output = (
                "[bold #F7C600]PORTS[/]\n\n"
            )

            if not ports:

                output += "No ports exposed"

            else:

                for port, bindings in ports.items():

                    if bindings:

                        host_port = (
                            bindings[0]
                            ["HostPort"]
                        )

                        output += (
                            f"{port} → {host_port}\n"
                        )

                    else:

                        output += (
                            f"{port}\n"
                        )

            self.update(output)

        except Exception as e:

            self.update(
f"""[bold #F7C600]PORTS[/]

ERROR

{repr(e)}
"""
            )
