from textual.widgets import Static


class DockerProcesses(Static):

    def on_mount(self):

        self.update(
"""[bold #F7C600]PROCESSES[/]

PIDS      : 14
THREADS   : 43
FD COUNT  : 102
"""
        )
