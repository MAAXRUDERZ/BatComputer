from textual.containers import Horizontal, Vertical
from textual.widgets import Static

from batcomputer.widgets.stats import Stats
from batcomputer.widgets.system_info import SystemInfo
from batcomputer.widgets.services import Services


class DashboardPage(Vertical):

    def compose(self):

        stats = Stats()
        stats.styles.width = 55

        info = SystemInfo()
        info.styles.width = 35

        with Horizontal():
            yield stats
            yield info

        yield Services()
