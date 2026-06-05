from textual.widgets import Static
import psutil
import socket
import platform
import time
import subprocess


class SystemInfo(Static):
    def on_mount(self):
        self.boot_time = psutil.boot_time()
        self.set_interval(1, self.update_info)

    def make_bar(self, percent, width=20):
        filled = int(percent / 100 * width)
        empty = width - filled
        return "█" * filled + "░" * empty

    def get_uptime(self):
        uptime_seconds = int(time.time() - self.boot_time)

        days = uptime_seconds // 86400
        hours = (uptime_seconds % 86400) // 3600
        minutes = (uptime_seconds % 3600) // 60

        return f"{days}d {hours}h {minutes}m"

    def get_cpu_temp(self):
        try:
            temps = psutil.sensors_temperatures()

            for sensor_name in temps:
                if temps[sensor_name]:
                    return temps[sensor_name][0].current

            return None

        except Exception:
            return None

    def get_gpu_info(self):
        try:
            output = subprocess.check_output(
                [
                    "nvidia-smi",
                    "--query-gpu=temperature.gpu,utilization.gpu,memory.used,memory.total",
                    "--format=csv,noheader,nounits"
                ]
            ).decode().strip()

            temp, util, mem_used, mem_total = output.split(",")

            return {
                "temp": float(temp.strip()),
                "util": float(util.strip()),
                "mem_used": float(mem_used.strip()),
                "mem_total": float(mem_total.strip())
            }

        except Exception:
            return None

    def temp_color(self, temp):
        if temp is None:
            return "#888888"

        if temp < 50:
            return "#00FF88"
        elif temp < 70:
            return "#F7C600"
        elif temp < 85:
            return "#FF9800"
        else:
            return "#FF3333"

    def update_info(self):
        hostname = socket.gethostname()

        cpu_temp = self.get_cpu_temp()

        if cpu_temp is None:
            cpu_temp_text = "N/A"
            cpu_temp_bar = self.make_bar(0)
            cpu_temp_color = "#888888"
        else:
            cpu_temp_text = f"{cpu_temp:.1f}°C"
            cpu_temp_bar = self.make_bar(cpu_temp)
            cpu_temp_color = self.temp_color(cpu_temp)

        gpu = self.get_gpu_info()

        if gpu:
            gpu_temp_bar = self.make_bar(gpu["temp"])
            gpu_temp_color = self.temp_color(gpu["temp"])

            gpu_util_bar = self.make_bar(gpu["util"])

            gpu_temp_text = f'{gpu["temp"]:.0f}°C'
            gpu_util_text = f'{gpu["util"]:.0f}%'

            vram_percent = (
                gpu["mem_used"] / gpu["mem_total"]
            ) * 100

            vram_bar = self.make_bar(vram_percent)

            vram_text = (
                f'{gpu["mem_used"]:.0f}M/'
                f'{gpu["mem_total"]:.0f}M'
            )

        else:
            gpu_temp_bar = self.make_bar(0)
            gpu_util_bar = self.make_bar(0)
            vram_bar = self.make_bar(0)

            gpu_temp_color = "#888888"

            gpu_temp_text = "N/A"
            gpu_util_text = "N/A"
            vram_text = "N/A"

        self.update(
f"""[bold #F7C600]SYSTEM[/]

[#F7C600]CPU TEMP[/]
[{cpu_temp_color}]{cpu_temp_bar}[/]
[{cpu_temp_color}]{cpu_temp_text}[/]

[#F7C600]GPU TEMP[/]
[{gpu_temp_color}]{gpu_temp_bar}[/]
[{gpu_temp_color}]{gpu_temp_text}[/]

[#F7C600]GPU USAGE[/]
[#F7C600]{gpu_util_bar}[/]
[white]{gpu_util_text}[/]

[#F7C600]VRAM[/]
[#F7C600]{vram_bar}[/]
[white]{vram_text}[/]

[#F7C600]UPTIME[/]
[white]{self.get_uptime()}[/]

[#F7C600]HOST[/]            [#F7C600]OS[/]
[white]{hostname}[/]        [white]{platform.system()}[/]
"""
        )
