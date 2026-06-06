from textual.widgets import Static


class DockerLogs(Static):

    def on_mount(self):

        self.update(
"""[bold #F7C600]LIVE LOGS[/]

Container logs will appear here...
"""
        )
