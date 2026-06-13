from textual.widgets import Static

import psutil


class NetworkStats(Static):

    def on_mount(self):

        self.set_interval(
            2,
            self.refresh_data
        )

    def refresh_data(self):

        io = (
            psutil.net_io_counters()
        )

        self.update(
f"""[bold #39FF14]THE GRID[/]

DOWNLOAD
{io.bytes_recv / 1024 / 1024:.1f} MB

UPLOAD
{io.bytes_sent / 1024 / 1024:.1f} MB

PACKETS SENT
{io.packets_sent}

PACKETS RECEIVED
{io.packets_recv}

ERRORS IN
{io.errin}

ERRORS OUT
{io.errout}
"""
        )
