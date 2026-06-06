from textual.widgets import Static
import subprocess


class Services(Static):

    def on_mount(self):
        self.update_services()
        self.set_interval(5, self.update_services)

    def update_services(self):

        try:
            output = subprocess.check_output(
                [
                    "docker",
                    "ps",
                    "-a",
                    "--format",
                    "{{.Names}}|{{.Status}}"
                ]
            ).decode()

            containers = output.splitlines()

        except Exception:
            self.update(
                "[bold #F7C600]SERVICES[/]\n\n[red]Docker unavailable[/]"
            )
            return

        text = "[bold #F7C600]SERVICES[/]\n\n"

        if not containers:
            text += "[yellow]No containers found[/]"

        else:

            rows = ["", "", ""]

            for i, container in enumerate(containers):

                name, status = container.split("|", 1)

                if status.startswith("Up"):
                    icon = "[green]●[/]"
                else:
                    icon = "[red]●[/]"

                row = i % 3

                rows[row] += f"{icon} {name:<11}"

            text += "\n".join(rows)

        self.update(text)
