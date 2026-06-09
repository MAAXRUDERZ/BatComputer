from textual.widget import Widget
from textual.containers import Horizontal

from batcomputer.widgets.task_list import (
    TaskList
)

from batcomputer.widgets.process_details import (
    ProcessDetails
)


class MonitorPage(Widget):

    def compose(self):

        with Horizontal():

            yield TaskList()

            yield ProcessDetails()
