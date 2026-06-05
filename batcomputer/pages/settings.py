from textual.widgets import Static


class SettingsPage(Static):

    def on_mount(self):
        self.update(
            """
SETTINGS

Coming Soon...
"""
        )
