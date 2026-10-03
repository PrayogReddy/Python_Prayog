import psutil
import shutil

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

def check_memory():
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

def check_disk():
    disk = shutil.disk_usage("/")
    usage = disk.used / disk.total * 100
    print(f"Disk Usage: {usage:.2f}%")

def main():
    check_cpu()
    check_memory()
    check_disk()

if __name__ == "__main__":
    main()