from textual.widgets import Static

from batcomputer.services import docker_state
from batcomputer.services.docker import (
    get_container_ports,
    get_container_health,
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

            health = get_container_health(
                selected
            )

            output = (
                "[bold #FF003C]ACCESS[/]\n\n"
            )

            if not ports:

                output += (
                    "No ports exposed\n"
                )

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

            image = (
                health["image"]
                .split("/")[-1]
                [:20]
            )

            output += (
                f"\nIMG:{image}\n"
                f"NET:{health['network']}\n"
                f"IP :{health['ip']}\n"
                f"ID :{health['id']}"
            )

            self.update(output)

        except Exception as e:

            self.update(
f"""[bold #F7C600]PORTS[/]

ERROR

{repr(e)}
"""
            )
