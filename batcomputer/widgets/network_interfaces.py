from textual.widgets import Static

import psutil


class NetworkInterfaces(Static):

    def on_mount(self):

        self.set_interval(
            2,
            self.refresh_data
        )

    def refresh_data(self):

        output = (
            "[bold #39FF14]CLUES[/]\n\n"
        )

        interfaces = (
            psutil.net_if_addrs()
        )

        stats = (
            psutil.net_if_stats()
        )

        for name in interfaces:

            is_up = False

            if name in stats:

                is_up = (
                    stats[name].isup
                )

            status = (
                "UP"
                if is_up
                else "DOWN"
            )

            output += (
                f"{name}\n"
                f"Status: {status}\n\n"
            )

        self.update(output)
