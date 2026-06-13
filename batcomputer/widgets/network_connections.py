from textual.widgets import Static

import psutil


class NetworkConnections(Static):

    def on_mount(self):

        self.set_interval(
            2,
            self.refresh_data
        )

    def refresh_data(self):

        output = (
            "[bold #39FF14]"
            "ACTIVE CONNECTIONS[/]\n\n"
        )

        try:

            connections = (
                psutil.net_connections()
            )

            count = 0

            for conn in connections:

                if (
                    conn.status
                    != "ESTABLISHED"
                ):

                    continue

                try:

                    pid = conn.pid

                    if not pid:

                        continue

                    process = (
                        psutil.Process(pid)
                    )

                    name = (
                        process.name()
                    )

                except Exception:

                    continue

                remote = "?"

                if conn.raddr:

                    remote = (
                        str(
                            conn.raddr.ip
                        )
                    )

                output += (
                    f"{name[:15]:15} "
                    f"{remote[:20]}\n"
                )

                count += 1

                if count >= 20:

                    break

            if count == 0:

                output += (
                    "No active "
                    "connections"
                )

        except Exception as e:

            output += str(e)

        self.update(output)
