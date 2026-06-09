import psutil

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

    if (
        process_state.sort_mode
        == "cpu"
    ):

        processes.sort(
            key=lambda p:
            p["cpu_percent"] or 0,
            reverse=True
        )

    elif (
        process_state.sort_mode
        == "memory"
    ):

        processes.sort(
            key=lambda p:
            p["memory_percent"] or 0,
            reverse=True
        )

    elif (
        process_state.sort_mode
        == "pid"
    ):

        processes.sort(
            key=lambda p:
            p["pid"]
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
            ).lower()
        )

    return processes


def get_process_details(pid):

    proc = psutil.Process(pid)

    return {
        "pid": proc.pid,
        "name": proc.name(),
        "status": proc.status(),
        "user": proc.username(),
        "threads": proc.num_threads(),
        "memory": proc.memory_info().rss,
        "cpu": proc.cpu_percent(),
        "cmdline": " ".join(
            proc.cmdline()
        ),
    }


def kill_process(pid):

    psutil.Process(
        pid
    ).kill()
