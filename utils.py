import shutil
from colorama import Fore
import os
import sys


def quit_handler(sig, frame):
    """
    It prints a message to the screen and exits the program

    :param sig: The signal that was received
    :param frame: the current stack frame
    """
    print(Fore.RED + "\n\n[" + Fore.RESET + "!" +
          Fore.RED + "] Programma interrotto.")
    sys.exit(0)


def clear():
    """
    If the operating system is Windows, clear the screen using the cls command, otherwise clear the
    screen using the clear command
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def header():
    """
    It prints a header
    """
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
    total, used, free = shutil.disk_usage("/")
    total = str(total // (2**30)) + " GB"
    return total


def get_used():
    total, used, free = shutil.disk_usage("/")
    used = str(used // (2**30)) + " GB (" + str(round(used // (2**30) / total * 100, 2)) + "%)"
    return used


def get_free():
    total, used, free = shutil.disk_usage("/")
    free = str(free // (2**30)) + " GB (" + str(round(free // (2**30) / total * 100, 2)) + "%)"
    return free
