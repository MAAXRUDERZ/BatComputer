from textual.widgets import Static


class DockerActions(Static):

    def on_mount(self):

        self.update(
"""[bold #F7C600]
[ENTER] OPEN
[S] START
[T] STOP
[R] RESTART
[X] SHELL
[/]
"""
        )
