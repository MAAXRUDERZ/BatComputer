from textual.app import App
from textual.widgets import Static
from textual.containers import Container

from batcomputer.pages.dashboard import DashboardPage
from batcomputer.pages.homepage import HomepagePage
from batcomputer.pages.docker import DockerPage
from batcomputer.pages.network import NetworkPage
from batcomputer.pages.archive import ArchivePage
from batcomputer.pages.settings import SettingsPage


class BatComputer(App):

    CSS_PATH = "batcomputer.tcss"

    BINDINGS = [
        ("f1", "show_dashboard", "Dashboard"),
        ("f2", "show_homepage", "Homepage"),
        ("f3", "show_docker", "Docker"),
        ("f4", "show_network", "Network"),
        ("f5", "show_archive", "Archive"),
        ("f6", "show_settings", "Settings"),
    ]

    def compose(self):

        yield Static(
"""[bold #FFD700]
██████╗  █████╗ ████████╗ ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║   ██║   ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
██╔══██╗██╔══██║   ██║   ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝██║  ██║   ██║   ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
[/bold #FFD700]"""
        )

        yield Container(
            DashboardPage(),
            id="page-container"
        )

    def switch_page(self, page):

        container = self.query_one("#page-container")

        container.remove_children()

        container.mount(page)

    def action_show_dashboard(self):

        self.switch_page(
            DashboardPage()
        )

    def action_show_homepage(self):

        self.switch_page(
            HomepagePage()
        )
    def action_show_docker(self):
        self.switch_page(
            DockerPage()
        )
        
    def action_show_network(self):
        self.switch_page(
            NetworkPage()
        )
    
    def action_show_archive(self):
        self.switch_page(
            ArchivePage()
        )

    def action_show_settings(self):
        self.switch_page(
            SettingsPage()
        )
        
if __name__ == "__main__":
    BatComputer().run()
