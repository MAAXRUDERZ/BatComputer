from textual.widgets import Static


class DockerIO(Static):

    def on_mount(self):

        self.update(
"""[bold #F7C600]BLOCK IO[/]

READ  8MB/s
WRITE 2MB/s
"""
        )
