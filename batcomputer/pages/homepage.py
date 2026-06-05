from textual.widgets import Static


class HomepagePage(Static):

    def on_mount(self):
        self.update(
            """
HOMEPAGE

Coming Soon...

This page will become the launcher
for all homelab services.
"""
        )
