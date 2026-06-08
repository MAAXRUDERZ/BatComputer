from textual.widgets import Static

import psutil
import time
import socket


class DockerSystem(Static):

    def on_mount(self):

        self.boot_time = psutil.boot_time()

        self.refresh_stats()

        self.set_interval(
            2,
            self.refresh_stats
        )

    def make_bar(
        self,
        percent,
        width=15
    ):

        filled = int(
            percent / 100 * width
        )

        empty = width - filled

        return (
            "█" * filled
            + "░" * empty
        )

    def get_uptime(self):

        uptime = int(
            time.time()
            - self.boot_time
        )

        days = uptime // 86400
        hours = (
            uptime % 86400
        ) // 3600

        return (
            f"{days}d {hours}h"
        )

    def get_cpu_temp(self):

        try:

            temps = (
                psutil
                .sensors_temperatures()
            )

            for sensor in temps:

                if temps[sensor]:

                    return (
                        temps[sensor][0]
                        .current
                    )

        except Exception:

            pass

        return None

    def refresh_stats(self):

        cpu_temp = (
            self.get_cpu_temp()
        )

        ram = (
            psutil
            .virtual_memory()
            .percent
        )

        hostname = (
            socket.gethostname()
        )

        if cpu_temp is None:

            cpu_text = "N/A"
            cpu_bar = (
                self.make_bar(0)
            )

        else:

            cpu_text = (
                f"{cpu_temp:.0f}°C"
            )

            cpu_bar = (
                self.make_bar(
                    min(
                        cpu_temp,
                        100
                    )
                )
            )

        self.update(
f"""[bold #FF003C]CORE TELEMETRY[/]

CPU
{cpu_bar}
{cpu_text}

RAM
{self.make_bar(ram)}
{ram:.0f}%

UP
{self.get_uptime()}

HOST
{hostname}
"""
        )
