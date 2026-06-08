from textual.widgets import Static

from batcomputer.services import docker_state

from batcomputer.services.docker_logs import (
    get_container_logs
)


class DockerLogs(Static):

    def on_mount(self):

        self.set_interval(
            1,
            self.refresh_logs
        )

    def refresh_logs(self):

        selected = (
            docker_state.selected_container
        )

        if not selected:

            return

        try:

            logs = get_container_logs(
                selected
            )

            logs = "\n".join(
                line[:50]
                for line in logs.splitlines()[-20:]
            )

            self.update(
f"""[bold #FF003C]TACTICAL FEED[/]

{logs}
"""
            )

        except Exception as e:

            self.update(
f"""[bold #FF003C]TACTICAL FEED[/]

ERROR

{repr(e)}
"""
            )
