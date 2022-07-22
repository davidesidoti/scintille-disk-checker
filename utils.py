import shutil
from colorama import Fore
import os

total, used, free = shutil.disk_usage("/")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header():
    print(Fore.YELLOW +
          "███████╗ ██████╗██╗███╗   ██╗████████╗██╗██╗     ██╗     ███████╗")
    print("██╔════╝██╔════╝██║████╗  ██║╚══██╔══╝██║██║     ██║     ██╔════╝")
    print("███████╗██║     ██║██╔██╗ ██║   ██║   ██║██║     ██║     █████╗  ")
    print("╚════██║██║     ██║██║╚██╗██║   ██║   ██║██║     ██║     ██╔══╝  ")
    print("███████║╚██████╗██║██║ ╚████║   ██║   ██║███████╗███████╗███████╗")
    print(
        "╚══════╝ ╚═════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚══════╝╚══════╝╚══════╝"
        + Fore.RED
        + "                             Version : 1.0\n\n"
    )

    print(Fore.GREEN + "[-]" + Fore.CYAN +
          " Creato da : Scintille Web Agency\n")


def get_total():
    global total
    total = str(total // (2**30)) + " GB"
    return total
