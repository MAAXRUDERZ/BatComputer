from textual.widgets import Static

from batcomputer.services import process_state
from batcomputer.services.processes import (
    get_process_details
)


class ProcessDetails(Static):

    def on_mount(self):

        self.set_interval(
            1,
            self.refresh_details
        )

    def refresh_details(self):

        pid = (
            process_state.selected_pid
        )

        if not pid:

            return

        try:

            details = (
                get_process_details(
                    pid
                )
            )

            memory_mb = (
                details["memory"]
                / 1024
                / 1024
            )

            self.update(
f"""[bold #FF003C]PROCESS DETAILS[/]

PID:
{details["pid"]}

USER:
{details["user"]}

STATUS:
{details["status"]}

CPU:
{details["cpu"]:.1f}%

MEMORY:
{memory_mb:.1f} MB

THREADS:
{details["threads"]}

CMDLINE:

{details["cmdline"][:200]}
"""
            )

        except Exception as e:

            self.update(
f"""[bold #FF003C]PROCESS DETAILS[/]

Process exited

{repr(e)}
"""
            )
