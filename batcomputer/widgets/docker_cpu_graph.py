from textual.widgets import Static
from random import randint

from batcomputer.widgets.graph import Graph


class DockerCPUGraph(Static):

    def on_mount(self):

        self.graph = Graph(
            max_points=120
        )

        for _ in range(120):

            self.graph.add(0)

        self.set_interval(
            0.1,
            self.update_graph
        )

    def update_graph(self):

        value = randint(
            0,
            100
        )

        self.graph.add(value)

        if value < 40:

            color = "#00FF88"

        elif value < 75:

            color = "#F7C600"

        else:

            color = "#FF4444"

        self.update(
f"""[bold {color}]CPU[/] [white]{value:.1f}%[/]

[{color}]{self.graph.render()}[/]
"""
        )
