from textual.widgets import Static


class ServiceCard(Static):

    def __init__(
        self,
        service_name,
        service_status,
        selected=False,
    ):
        super().__init__()

        self.service_name = service_name
        self.service_status = service_status
        self.selected = selected

    def on_mount(self):
        self.refresh_card()

    def refresh_card(self):

        status_color = (
            "green"
            if self.service_status == "running"
            else "red"
        )

        if self.selected:

            self.update(
f"""[#F7C600]╔════════════════════════════════════╗[/]
 [#F7C600]║[/] [bold #F7C600]► {self.service_name[:29]:<29}[/] [#F7C600] ║[/]
 [#F7C600]║[/] STATUS : [{status_color}]● {self.service_status.upper()}[/]               [#F7C600]║[/]
[#F7C600]╚════════════════════════════════════╝[/]"""
            )

        else:

            self.update(
f"""╔════════════════════════════════════╗
 ║   {self.service_name[:30]:<30} ║
 ║ STATUS : [{status_color}]● {self.service_status.upper()}[/]               ║
╚════════════════════════════════════╝"""
            )
