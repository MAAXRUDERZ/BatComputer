from textual.widgets import Static
from textual.binding import Binding

from batcomputer.services import process_state
from batcomputer.services.processes import (
    get_processes
)


class TaskList(Static):

    can_focus = True

    BINDINGS = [
        Binding("up", "move_up"),
        Binding("down", "move_down"),

        Binding("c", "sort_cpu"),
        Binding("m", "sort_memory"),
        Binding("p", "sort_pid"),
        Binding("n", "sort_name"),
    ]

    def on_mount(self):

        self.set_interval(
            1,
            self.refresh_list
        )

        self.focus()

    def refresh_list(self):

        processes = get_processes()

        if not processes:
            return

        if (
            process_state.selected_pid
            is None
        ):

            process_state.selected_pid = (
                processes[0]["pid"]
            )

        selected_idx = next(
            (
                i
                for i, p in enumerate(processes)
                if p["pid"]
                == process_state.selected_pid
            ),
            0
        )

        VISIBLE_ITEMS = 30

        start = max(
            0,
            selected_idx - 15
        )

        end = min(
            len(processes),
            start + VISIBLE_ITEMS
        )

        if end - start < VISIBLE_ITEMS:

            start = max(
                0,
                end - VISIBLE_ITEMS
            )

        top_count = start

        bottom_count = (
            len(processes)
            - end
        )

        title = (
            f"[bold #FF003C]TASKS[/] "
            f"[#888888]({process_state.sort_mode.upper()})[/]"
        )

        if top_count > 0:

            title += (
                f" [#AA0033]▲{top_count}[/]"
            )

        if bottom_count > 0:

            title += (
                f" [#AA0033]▼{bottom_count}[/]"
            )

        output = (
            title + "\n\n"
        )

        for proc in processes[
            start:end
        ]:

            name = (
                proc["name"]
                or "unknown"
            )

            cpu = (
                proc["cpu_percent"]
                or 0
            )

            mem = (
                proc["memory_percent"]
                or 0
            )

            pid = proc["pid"]

            selected = (
                pid
                == process_state.selected_pid
            )

            if selected:

                output += (
                    f"[bold #FF003C]▶ "
                    f"{name[:18]:18} "
                    f"{cpu:>4.0f}% "
                    f"{mem:>4.1f}% "
                    f"{pid}[/]\n"
                )

            else:

                output += (
                    f"  "
                    f"{name[:18]:18} "
                    f"{cpu:>4.0f}% "
                    f"{mem:>4.1f}% "
                    f"{pid}\n"
                )

        self.update(output)

    def action_move_up(self):

        processes = get_processes()

        current_idx = next(
            (
                i
                for i, p in enumerate(processes)
                if p["pid"]
                == process_state.selected_pid
            ),
            0
        )

        if current_idx > 0:

            process_state.selected_pid = (
                processes[
                    current_idx - 1
                ]["pid"]
            )

        self.refresh_list()

    def action_move_down(self):

        processes = get_processes()

        current_idx = next(
            (
                i
                for i, p in enumerate(processes)
                if p["pid"]
                == process_state.selected_pid
            ),
            0
        )

        if (
            current_idx
            < len(processes) - 1
        ):

            process_state.selected_pid = (
                processes[
                    current_idx + 1
                ]["pid"]
            )

        self.refresh_list()

    def action_sort_cpu(self):

        process_state.sort_mode = "cpu"

        self.refresh_list()

    def action_sort_memory(self):

        process_state.sort_mode = "memory"

        self.refresh_list()

    def action_sort_pid(self):

        process_state.sort_mode = "pid"

        self.refresh_list()

    def action_sort_name(self):

        process_state.sort_mode = "name"

        self.refresh_list()
