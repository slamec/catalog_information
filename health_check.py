# !/usr/bin/env python3

import psutil
import shutil
import email

# check cpu usage
def cpu_usage():
    cpu = psutil.cpu_percent(60)

    return cpu

print(cpu_usage())