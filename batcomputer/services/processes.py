import psutil
import datetime

from batcomputer.services import (
    process_state
)


def get_processes():

    processes = []

    for proc in psutil.process_iter(
        [
            "pid",
            "name",
            "cpu_percent",
            "memory_percent",
            "username",
        ]
    ):

        try:

            processes.append(
                proc.info
            )

        except Exception:

            pass

    if process_state.search_query:

        query = (
            process_state.search_query
            .lower()
        )

        processes = [

            p

            for p in processes

            if (

                query
                in str(
                    p["pid"]
                )

                or

                query
                in (
                    p["name"]
                    or ""
                ).lower()

            )
        ]

    if not process_state.freeze_sort:

        if (
            process_state.sort_mode
            == "cpu"
        ):

            processes.sort(
                key=lambda p:
                p["cpu_percent"] or 0,
                reverse=process_state.sort_reverse
            )

        elif (
            process_state.sort_mode
            == "memory"
        ):

            processes.sort(
                key=lambda p:
                p["memory_percent"] or 0,
                reverse=process_state.sort_reverse
            )

        elif (
            process_state.sort_mode
            == "pid"
        ):

            processes.sort(
                key=lambda p:
                p["pid"],
                reverse=process_state.sort_reverse
            )

        elif (
            process_state.sort_mode
            == "name"
        ):

            processes.sort(
                key=lambda p:
                (
                    p["name"]
                    or ""
                ).lower(),
                reverse=process_state.sort_reverse
            )

        process_state.cached_processes = (
            processes.copy()
        )

        return processes

    return (
        process_state.cached_processes
    )


def get_process_details(pid):

    proc = psutil.Process(pid)

    try:

        open_files = len(
            proc.open_files()
        )

    except Exception:

        open_files = 0

    try:

        exe = proc.exe()

    except Exception:

        exe = "N/A"

    try:

        cwd = proc.cwd()

    except Exception:

        cwd = "N/A"

    try:

        started = proc.create_time()

    except Exception:

        started = None

    return {

        "pid": proc.pid,

        "ppid": proc.ppid(),

        "name": proc.name(),

        "status": proc.status(),

        "user": proc.username(),

        "threads": proc.num_threads(),

        "memory": proc.memory_info().rss,

        "cpu": proc.cpu_percent(),

        "cmdline": " ".join(
            proc.cmdline()
        ),

        "exe": exe,

        "cwd": cwd,

        "open_files": open_files,

        "started": (
            datetime.datetime
            .fromtimestamp(
                started
            )
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            if started
            else "N/A"
        ),
    }


def kill_process(pid):

    psutil.Process(
        pid
    ).kill()
