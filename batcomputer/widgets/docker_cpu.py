from textual.widgets import Static


class DockerCPU(Static):

    def on_mount(self):

        self.update(
"""[bold #F7C600]CPU[/]

▁▁▂▃▄▅▆▇▆▅▄▃▂▁

14.2%
"""
        )
