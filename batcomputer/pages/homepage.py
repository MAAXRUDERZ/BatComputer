from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from textual.binding import Binding
from textual.screen import ModalScreen
import subprocess
import os
import socket
import webbrowser
from batcomputer.widgets.service_card import ServiceCard
from batcomputer.services.docker import get_containers


class UrlPopup(ModalScreen):

    def __init__(self, url):

        super().__init__()

        self.url = url

    def compose(self):

        yield Static(
f"""[bold #F7C600]
SERVICE URL
[/]

{self.url}

[bold #90A4AE]
Press ESC to close
[/]
"""
        )


class HomepagePage(Widget):

    can_focus = True
    selected_index = 0

    BINDINGS = [
        Binding("up", "move_up", "Up"),
        Binding("down", "move_down", "Down"),
        Binding("left", "move_left", "Left"),
        Binding("right", "move_right", "Right"),
        Binding("enter", "launch_service", "Launch")
    ]

    def on_mount(self):

        self.focus()

    def compose(self):

        yield Static(
"""[bold #90A4AE]
╔══════════════════════════════════════════════╗
 ║             BATCOMPUTER HOME               ║
 ║         GOTHAM ACCESS TERMINAL             ║
╚══════════════════════════════════════════════╝
[/]

[bold #00BCD4]AVAILABLE SERVICES[/]
"""
        )

        self.containers = get_containers()

        MAX_ROWS = 4

        with Horizontal(id="services-container"):

            for start in range(
                0,
                len(self.containers),
                MAX_ROWS
            ):

                with Vertical(
                    classes="service-column"
                ):

                    for i, container in enumerate(
                        self.containers[
                            start:start + MAX_ROWS
                        ]
                    ):

                        yield ServiceCard(
                            container["name"],
                            container["status"],
                            selected=(
                                start + i
                                == self.selected_index
                            ),
                        )

        yield Static(
"""[bold #90A4AE]
══════════════════════════════════════════════
WAYNE MANOR PRIVATE NETWORK
AUTHORIZED ACCESS ONLY
══════════════════════════════════════════════
[/]
""",
            id="homepage-footer"
        )

    def update_selection(self):

        cards = list(
            self.query(ServiceCard)
        )

        for i, card in enumerate(cards):

            card.selected = (
                i == self.selected_index
            )

            card.refresh_card()

    def action_move_up(self):

        if self.selected_index > 0:

            self.selected_index -= 1

        self.update_selection()

    def action_move_down(self):

        if (
            self.selected_index
            < len(self.containers) - 1
        ):

            self.selected_index += 1

        self.update_selection()

    def action_move_left(self):

        if self.selected_index >= 4:

            self.selected_index -= 4

        self.update_selection()

    def action_move_right(self):

        if (
            self.selected_index + 4
            < len(self.containers)
        ):

            self.selected_index += 4

        self.update_selection()

    def action_launch_service(self):


        container = (
            self.containers[
                self.selected_index
            ]
        )

        try:

            output = (
                subprocess.check_output(
                    [
                        "docker",
                        "port",
                        container["name"]
                    ]
                )
                .decode()
                .splitlines()
            )

            if not output:

                self.notify(
                    "No exposed ports"
                )

                return

            first_mapping = output[0]

            port = (
                first_mapping
                .split(":")[-1]
                .strip()
            )

            is_ssh = (
                "SSH_CONNECTION" in os.environ
                or "SSH_CLIENT" in os.environ
            )

            if is_ssh:

                try:

                    server_ip = (
                        socket.gethostbyname(
                            socket.gethostname()
                        )
                    )

                except Exception:

                    server_ip = "SERVER_IP"

                url = (
                    f"http://{server_ip}:{port}"
                )

                self.app.push_screen(
                    UrlPopup(url)
                )

            else:

                url = (
                    f"http://localhost:{port}"
                )

                webbrowser.open(url)

        except Exception as e:

            self.notify(str(e))
