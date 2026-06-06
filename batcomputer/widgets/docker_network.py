from textual.widgets import Static


class DockerNetwork(Static):

    def on_mount(self):

        self.update(
"""[bold #F7C600]NETWORK[/]

RX 1.2MB/s
TX 0.4MB/s
"""
        )
