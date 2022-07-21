import shutil
import os

total, used, free = shutil.disk_usage("/")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_total():
    global total
    total = str(total // (2**30)) + " GB"
    return total
