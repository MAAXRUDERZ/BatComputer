from textual.widgets import Static


class ArchivePage(Static):

    def on_mount(self):
        self.update(
            """
BAT ARCHIVE

Coming Soon...
"""
        )
        
