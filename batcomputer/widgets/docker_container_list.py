from textual.widgets import Static
from textual.binding import Binding

from batcomputer.services import docker_state
from batcomputer.services.docker import get_containers


class DockerContainerList(Static):

    can_focus = True

    BINDINGS = [
        Binding("up", "move_up"),
        Binding("down", "move_down"),
    ]

    def on_mount(self):

        self.containers = get_containers()

        if self.containers:

            docker_state.selected_container = (
                self.containers[0]["name"]
            )

        self.refresh_list()

        self.focus()

    def refresh_list(self):

        output = (
            "[bold #F7C600]CONTAINERS[/]\n\n"
        )

        for i, container in enumerate(
            self.containers
        ):

            if i == docker_state.selected_index:

                output += (
                    f"► {container['name']}\n"
                )

                docker_state.selected_container = (
                    container["name"]
                )

            else:

                output += (
                    f"  {container['name']}\n"
                )

        self.update(output)

    def action_move_up(self):

        if docker_state.selected_index > 0:

            docker_state.selected_index -= 1

        self.refresh_list()

    def action_move_down(self):

        if (
            docker_state.selected_index
            < len(self.containers) - 1
        ):

            docker_state.selected_index += 1

        self.refresh_list()
