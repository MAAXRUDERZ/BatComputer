from textual.screen import ModalScreen
from textual.widgets import Static

from batcomputer.services.docker_logs import (
    get_container_logs
)


class LogPopup(ModalScreen):

    def __init__(self, container_name):

        super().__init__()

        self.container_name = container_name

    def compose(self):

        logs = get_container_logs(
            self.container_name,
            tail=200
        )

        yield Static(
            f"FULL LOGS - {self.container_name}\n\n"
            f"{logs}\n\n"
            f"ESC to close"
        )

    def on_key(self, event):

        if event.key == "escape":

            self.dismiss()
