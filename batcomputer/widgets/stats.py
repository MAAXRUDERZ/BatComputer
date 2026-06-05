from textual.widgets import Static
import psutil


class Stats(Static):
    def on_mount(self):
        self.set_interval(1, self.update_stats)

    def make_bar(self, percent, width=15):
        filled = int(percent / 100 * width)
        empty = width - filled
        return "█" * filled + "░" * empty

    def update_stats(self):
        total_cpu = psutil.cpu_percent()
        cores = psutil.cpu_percent(percpu=True)

        ram = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        output = (
            f"[bold #F7C600]CPU TOTAL[/] "
            f"[#F7C600]{self.make_bar(total_cpu)}[/] "
            f"[white]{total_cpu:.1f}%[/]\n\n"
        )

        output += "[bold #F7C600]CPU THREADS[/]\n\n"

        for i, usage in enumerate(cores):

            if usage < 50:
                color = "#F7C600"
            elif usage < 80:
                color = "#FF9800"
            else:
                color = "#C62828"

            output += (
                f"[#F7C600]T{i:02d}[/] "
                f"[{color}]{self.make_bar(usage)}[/] "
                f"[white]{usage:5.1f}%[/]\n"
            )

        ram_used = ram.used / (1024**3)
        ram_total = ram.total / (1024**3)

        disk_used = disk.used / (1024**3)
        disk_total = disk.total / (1024**3)

        output += "\n"

        output += (
            f"[bold #F7C600]RAM [/]"
            f"[#F7C600]{self.make_bar(ram.percent)}[/] "
            f"[white]{ram_used:.1f}G/{ram_total:.1f}G "
            f"({ram.percent:.1f}%)[/]\n"
        )

        output += (
            f"[bold #F7C600]DSK [/]"
            f"[#F7C600]{self.make_bar(disk.percent)}[/] "
            f"[white]{disk_used:.0f}G/{disk_total:.0f}G "
            f"({disk.percent:.1f}%)[/]\n"
        )

        self.update(output)
