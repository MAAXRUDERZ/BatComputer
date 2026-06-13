from textual.widgets import Static

import psutil
import time


class NetworkStats(Static):

    def on_mount(self):

        io = psutil.net_io_counters()

        self.last_recv = io.bytes_recv
        self.last_sent = io.bytes_sent

        self.last_time = time.time()

        self.set_interval(
            1,
            self.refresh_data
        )

    def refresh_data(self):

        io = psutil.net_io_counters()

        now = time.time()

        elapsed = now - self.last_time

        recv_speed = (
            io.bytes_recv
            - self.last_recv
        ) / elapsed

        sent_speed = (
            io.bytes_sent
            - self.last_sent
        ) / elapsed

        self.last_recv = (
            io.bytes_recv
        )

        self.last_sent = (
            io.bytes_sent
        )

        self.last_time = now

        self.update(
f"""[bold #39FF14]THE GRID[/]

[bold #7CFC00]DOWNLOAD SPEED[/]          [bold #ADFF2F]TOTAL DOWNLOAD[/]

{recv_speed / 1024 / 1024:>7.2f} MB/s          {io.bytes_recv / 1024 / 1024:>10.1f} MB

[bold #00FF7F]UPLOAD SPEED[/]            [bold #98FB98]TOTAL UPLOAD[/]

{sent_speed / 1024 / 1024:>7.2f} MB/s          {io.bytes_sent / 1024 / 1024:>10.1f} MB

[bold #39FF14]PACKETS SENT[/]            [bold #66FF66]PACKETS RECEIVED[/]

{io.packets_sent:>10}              {io.packets_recv:>10}

[bold #228B22]ERRORS IN[/]               [bold #006400]ERRORS OUT[/]

{io.errin:>10}          {io.errout:>10}
"""
)
