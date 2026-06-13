from textual.screen import ModalScreen
from textual.widgets import Input

from batcomputer.services import (
    process_state
)


class SearchPopup(
    ModalScreen
):

    def compose(self):

        yield Input(
            placeholder=
            "Search PID or process..."
        )

    def on_input_submitted(
        self,
        event
    ):

        process_state.search_query = (
            event.value
        )

        self.dismiss()

    def on_mount(self):

        self.query_one(
            Input
        ).focus()
