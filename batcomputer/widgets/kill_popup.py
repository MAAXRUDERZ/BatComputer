from textual.screen import ModalScreen
from textual.widgets import Static
from textual.binding import Binding

from batcomputer.services.processes import (
    kill_process
)


class KillPopup(ModalScreen):

    BINDINGS = [
        Binding("y", "confirm"),
        Binding("n", "cancel"),
        Binding("escape", "cancel"),
    ]

    def __init__(
        self,
        pid,
        process_name,
    ):

        super().__init__()

        self.pid = pid

        self.process_name = (
            process_name
        )

    def compose(self):

        yield Static(
f"""
[bold #7B1FA2]END TASK[/]

Name:
{self.process_name}

PID:
{self.pid}

[Y] Confirm
[N] Cancel
"""
        )

    def action_confirm(self):

        try:

            kill_process(
                self.pid
            )

        except Exception:

            pass

        self.dismiss(True)

    def action_cancel(self):

        self.dismiss(False)
