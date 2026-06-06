from collections import deque


class Graph:

    def __init__(
        self,
        max_points=120,
    ):

        self.values = deque(
            maxlen=max_points
        )

    def add(self, value):

        self.values.append(
            max(0, min(100, value))
        )

    def render(self):

        bars = "⣀⣄⣤⣦⣶⣷⣿"

        graph = ""

        for value in self.values:

            index = int(
                value / 100
                * (len(bars) - 1)
            )

            graph += bars[index]

        return graph
