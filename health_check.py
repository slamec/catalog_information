# !/usr/bin/env python3

from turtle import st
import psutil
import shutil
import email

# check cpu usage if higher than 80% return actual usage
def cpu_usage():
    cpu = psutil.cpu_percent(5)

    if cpu >= 80:
        pass
    else:
        return "CPU usage is lower than 80%"
    
print(cpu_usage())

# checl disk usage
def disk_space():
    total, used, free = shutil.disk_usage(__file__)

    usage_perc = float(used)/float(total) * 100

    if usage_perc <= 20:

        free_space = "{:.2f}{}".format(usage_perc, '%')
        pass
    else:
        return "Disk space is less than 20%"

print(disk_space())

# check available memory 
def ram_usage():
    ram = psutil.virtual_memory().available  / (1024.0 ** 2)

    if ram <= 500:
        pass
    else:
        return "Available memory is less than 500MB"

print(ram_usage())
