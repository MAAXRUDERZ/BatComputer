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

    current_page = "Dashboard"

    THEMES = {
        "Dashboard": {
            "primary": "#FFD700",
            "accent": "#F7C600",
            "name": "Adam West",
        },
        "Homepage": {
            "primary": "#90A4AE",
            "accent": "#00BCD4",
            "name": "BTAS",
        },
        "Docker": {
            "primary": "#B71C1C",
            "accent": "#FF1744",
            "name": "Batman Beyond",
        },
        "Network": {
            "primary": "#2E7D32",
            "accent": "#00E676",
            "name": "WayneTech",
        },
        "Archive": {
            "primary": "#6A1B9A",
            "accent": "#FF1744",
            "name": "Batman Who Laughs",
        },
        "Settings": {
            "primary": "#78909C",
            "accent": "#ECEFF1",
            "name": "Arkham",
        },
    }
    
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
[/bold #FFD700]""",
    id="logo"
        )

        yield Container(
            DashboardPage(),
            id="page-container"
        )
        
        yield Static(
            "",
            id="footer"
        )

    def update_footer(self):

        footer = self.query_one("#footer")

        pages = [
            ("Dashboard", "F1"),
            ("Homepage", "F2"),
            ("Docker", "F3"),
            ("Network", "F4"),
            ("Archive", "F5"),
            ("Settings", "F6"),
        ]

        text = ""

        for page, key in pages:

            theme_color = self.THEMES[self.current_page]["accent"]

            if page == self.current_page:
                text += (
                    f"[bold {theme_color}]\\[{key}] {page}[/]  "
                )
            else:
                text += (
                    f"[white]\\[{key}] {page}[/]  "
                )

        footer.update(text)


    def update_logo(self):

        logo = self.query_one("#logo")

        color = self.THEMES[self.current_page]["primary"]

        logo.update(
    f"""[bold {color}]
    ██████╗  █████╗ ████████╗ ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗
    ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
    ██████╔╝███████║   ██║   ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
    ██╔══██╗██╔══██║   ██║   ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗
    ██████╔╝██║  ██║   ██║   ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
    [/bold {color}]"""
        )

    def on_mount(self):
        self.update_footer()
        self.update_logo()

    def switch_page(self, page):

        container = self.query_one("#page-container")

        container.remove_children()

        container.mount(page)

    def action_show_dashboard(self):
        self.bell()
    
        self.current_page = "Dashboard"    
        
        self.switch_page(
            DashboardPage()
        )
        self.update_footer()
        self.update_logo()

    def action_show_homepage(self):
        self.bell()
    
        self.current_page = "Homepage"
        
        self.switch_page(
            HomepagePage()
        )
        self.update_footer()
        self.update_logo()
        
    def action_show_docker(self):
        self.bell()
        
        self.current_page = "Docker"
    
        self.switch_page(
            DockerPage()
        )
        self.update_footer()
        self.update_logo()
        
    def action_show_network(self):
        self.bell()
    
        self.current_page = "Network"
    
        self.switch_page(
            NetworkPage()
        )
        self.update_footer()
        self.update_logo()
    
    def action_show_archive(self):
        self.bell()
    
        self.current_page = "Archive"
    
        self.switch_page(
            ArchivePage()
        )
        self.update_footer()
        self.update_logo()

    def action_show_settings(self):
        self.bell()
    
        self.current_page = "Settings"
        self.switch_page(
            SettingsPage()
        )
        self.update_footer()
        self.update_logo()
        
if __name__ == "__main__":
    BatComputer().run()
