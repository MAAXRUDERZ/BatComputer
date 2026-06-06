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
            selector = "[bold #F7C600]►[/]"
        else:
            selector = " "

        self.update(
    f"""╔════════════════════════════════════╗
 ║  {selector} {self.service_name[:29]:<29}║
 ║  STATUS : [{status_color}]● {self.service_status.upper()}[/]              ║
╚════════════════════════════════════╝"""
        )
