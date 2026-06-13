from textual.widgets import Static

import psutil
import socket


class NetworkInterfaces(Static):

    def on_mount(self):

        self.set_interval(
            2,
            self.refresh_data
        )

    def refresh_data(self):

        output = (
            "[bold #39FF14]CLUES[/]\n\n"
            "[bold #7CFC00]"
            f"{'IFACE':<12}"
            f"{'IP':<18}"
            f"{'STATE':<8}"
            "[/]\n"
            "────────────────────────────────────\n"
        )

        interfaces = (
            psutil.net_if_addrs()
        )

        stats = (
            psutil.net_if_stats()
        )

        for name, addresses in interfaces.items():

            ip = "N/A"

            for addr in addresses:

                if (
                    addr.family
                    == socket.AF_INET
                ):

                    ip = (
                        addr.address
                    )

                    break

            is_up = False

            if name in stats:

                is_up = (
                    stats[name].isup
                )

            status = (
                "[#39FF14]UP[/]"
                if is_up
                else "[#006400]DOWN[/]"
            )

            output += (
                f"{name[:11]:<12}"
                f"{ip[:17]:<18}"
                f"{status}\n"
            )

        self.update(output)
