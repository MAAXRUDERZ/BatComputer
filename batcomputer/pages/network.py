from textual.widgets import Static


class NetworkPage(Static):

    def on_mount(self):
        self.update(
            """
NETWORK

Coming Soon...
"""
        )
