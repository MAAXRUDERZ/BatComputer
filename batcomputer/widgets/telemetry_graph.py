from collections import deque


class TelemetryGraph:

    def __init__(
        self,
        width=45,
        height=8,
    ):

        self.width = width
        self.height = height

        self.values = deque(
            [0] * width,
            maxlen=width,
        )

    def add(self, value):

        self.values.append(value)

    def render(self):

        values = list(self.values)

        max_val = max(values) if max(values) > 0 else 1

        canvas = [
            [" "] * self.width
            for _ in range(self.height)
        ]

        points = []

        for x, value in enumerate(values):

            y = int(
                (value / max_val)
                * (self.height - 1)
            )

            y = (
                self.height - 1
            ) - y

            points.append((x, y))

        for x, y in points:

            canvas[y][x] = "•"

        for i in range(len(points) - 1):

            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            dx = x2 - x1
            dy = y2 - y1

            steps = max(
                abs(dx),
                abs(dy),
            )

            for step in range(steps):

                px = int(
                    x1 + dx * step / steps
                )

                py = int(
                    y1 + dy * step / steps
                )

                if canvas[py][px] == " ":
                    canvas[py][px] = "─"

        output = []

        for row in canvas:

            output.append(
                "".join(row)
            )

        return "\n".join(output)
