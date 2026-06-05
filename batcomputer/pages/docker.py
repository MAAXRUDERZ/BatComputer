from textual.widgets import Static


class DockerPage(Static):

    def on_mount(self):
        self.update(
            """
DOCKER

Coming Soon...
"""
        )
