from textual.widgets import Static
from textual.binding import Binding
import time

from batcomputer.services import process_state
from batcomputer.services.processes import (
    get_processes,
    kill_process,
)
from batcomputer.widgets.kill_popup import (
    KillPopup
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
        Binding("k", "kill_process"),
        
        Binding("/", "search"),
        Binding("escape", "clear_search"),
    ]

    def on_mount(self):
    
        self.last_sort = 0

        self.set_interval(
            1,
            self.refresh_list
        )

        self.focus()

    def refresh_list(self):

        current_time = time.time()

        if (
            current_time
            - self.last_sort
            > 5
        ):

            process_state.freeze_sort = False

            self.last_sort = current_time

        else:

            process_state.freeze_sort = True

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
        
        process_state.selected_index = (
            selected_idx
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

        direction = (
            "▼"
            if process_state.sort_reverse
            else "▲"
        )

        title = (
            f"[bold #FF003C]TASKS[/] "
            f"[#888888]({process_state.sort_mode.upper()} {direction})[/]"
        )

        if process_state.search_query:

            title += (
                f" [#00E676]"
                f"SEARCH:"
                f"{process_state.search_query}"
                f"[/]"
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

        if (
            process_state.selected_index
            > 0
        ):

            process_state.selected_index -= 1

            process_state.selected_pid = (
                processes[
                    process_state.selected_index
                ]["pid"]
            )

        self.refresh_list()

    def action_move_down(self):

        processes = get_processes()

        if (
            process_state.selected_index
            < len(processes) - 1
        ):

            process_state.selected_index += 1

            process_state.selected_pid = (
                processes[
                    process_state.selected_index
                ]["pid"]
            )

        self.refresh_list()

    def action_sort_cpu(self):

        if (
            process_state.sort_mode
            == "cpu"
        ):

            process_state.sort_reverse = (
                not process_state.sort_reverse
            )

        else:

            process_state.sort_mode = "cpu"

            process_state.sort_reverse = True

        process_state.freeze_sort = False

        processes = get_processes()

        if processes:

            process_state.selected_index = 0

            process_state.selected_pid = (
                processes[0]["pid"]
            )

        self.last_sort = 0

        self.refresh_list()



    def action_sort_memory(self):

        if (
            process_state.sort_mode
            == "memory"
        ):

            process_state.sort_reverse = (
                not process_state.sort_reverse
            )

        else:

            process_state.sort_mode = "memory"

            process_state.sort_reverse = True

        process_state.freeze_sort = False

        processes = get_processes()

        if processes:

            process_state.selected_index = 0

            process_state.selected_pid = (
                processes[0]["pid"]
            )

        self.last_sort = 0

        self.refresh_list()



    def action_sort_pid(self):

        if (
            process_state.sort_mode
            == "pid"
        ):

            process_state.sort_reverse = (
                not process_state.sort_reverse
            )

        else:

            process_state.sort_mode = "pid"

            process_state.sort_reverse = False

        process_state.freeze_sort = False

        processes = get_processes()

        if processes:

            process_state.selected_index = 0

            process_state.selected_pid = (
                processes[0]["pid"]
            )

        self.last_sort = 0

        self.refresh_list()
        

    def action_sort_name(self):

        if (
            process_state.sort_mode
            == "name"
        ):

            process_state.sort_reverse = (
                not process_state.sort_reverse
            )

        else:

            process_state.sort_mode = "name"

            process_state.sort_reverse = False

        process_state.freeze_sort = False

        processes = get_processes()

        if processes:

            process_state.selected_index = 0

            process_state.selected_pid = (
                processes[0]["pid"]
            )

        self.last_sort = 0

        self.refresh_list()
        
    
    def action_search(self):

        self.app.push_screen(
            SearchPopup()
        )
    
    
    def action_clear_search(self):

        process_state.search_query = ""

        process_state.selected_pid = None

        self.refresh_list()

        self.notify(
            "Search cleared"
        )
    
        
    def action_kill_process(self):

        pid = (
            process_state.selected_pid
        )

        if not pid:
            return

        processes = get_processes()

        proc = next(
            (
                p
                for p in processes
                if p["pid"] == pid
            ),
            None
        )

        if not proc:
            return

        self.app.push_screen(
            KillPopup(
                pid,
                proc["name"]
            )
        )
