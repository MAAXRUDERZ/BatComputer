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

            if memory_mb > 1024:

                memory_text = (
                    f"{memory_mb / 1024:.2f} GB"
                )

            else:

                memory_text = (
                    f"{memory_mb:.1f} MB"
                )

            self.update(
f"""[bold #FF003C]PROCESS DETAILS[/]

PID         : {details["pid"]}
PPID        : {details.get("ppid", "N/A")}
USER        : {details["user"]}
STATUS      : {details["status"]}

CPU         : {details["cpu"]:.1f}%
MEMORY      : {memory_text}
THREADS     : {details["threads"]}

OPEN FILES  : {details.get("open_files", 0)}

STARTED
{details.get("started", "N/A")}

EXECUTABLE
{details.get("exe", "N/A")[:300]}

WORKING DIR
{details.get("cwd", "N/A")[:300]}

CMDLINE
{details["cmdline"][:500]}
"""
            )

        except Exception as e:

            self.update(
f"""[bold #FF003C]PROCESS DETAILS[/]

PROCESS EXITED

{repr(e)}
"""
            )
