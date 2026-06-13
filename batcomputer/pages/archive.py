from textual.widget import Widget
from textual.widgets import Static
from textual.containers import (
    Horizontal,
    Vertical,
)

from batcomputer.widgets.task_list import (
    TaskList
)

from batcomputer.widgets.process_details import (
    ProcessDetails
)


class ArchivePage(Widget):

    def compose(self):

        with Vertical():

            with Horizontal():

                yield TaskList()

                yield ProcessDetails()

            yield Static(
                "[#888888]"
                "\\[C] CPU  "
                "\\[M] MEM  "
                "\\[P] PID  "
                "\\[N] NAME  "
                "\\[K] KILL  "
                "\\[/] SEARCH  "
                "\\[Y] ACCEPT  "
                "\\[ESC] CLEAR"
                "[/]",
                classes="monitor-footer"
            )
