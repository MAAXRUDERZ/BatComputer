from textual.widget import Widget
from textual.containers import (
    Horizontal,
    Vertical,
)

from textual.widgets import Static

from batcomputer.widgets.network_interfaces import (
    NetworkInterfaces
)

from batcomputer.widgets.network_connections import (
    NetworkConnections
)


class NetworkPage(Widget):

    def compose(self):

        with Vertical():

            yield Static(
                "[bold #39FF14]RIDDLER GRID[/]",
                classes="network-title"
            )

            with Horizontal():

                yield NetworkInterfaces(
                    classes="network-panel"
                )

                yield NetworkConnections(
                    classes="network-panel"
                )

            yield Static(
                "[bold #39FF14]THE GRID[/]",
                classes="network-wide-panel"
            )

            yield Static(
                "[#FFD700]"
                "\\[R\\] Refresh   "
                "\\[P\\] Ping   "
                "\\[T\\] Trace Route   "
                "\\[S\\] Scan"
                "[/]",
                classes="network-footer"
            )
