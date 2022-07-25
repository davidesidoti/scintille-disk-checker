from colorama import init, Fore, Back, Style
import utils
import signal
import sys

init()
signal.signal(signal.SIGINT, utils.quit_handler)


def about():
    """
    ANCHOR: About
    It prints out a header, then prints out some text, then prints out a menu with two options, then
    waits for the user to enter a number, then if the user enters 00, it calls the start() function, and
    if the user enters 99, it calls the exit() function
    """
    utils.clear()

    utils.header()

    print(Fore.GREEN + "Autore      " + Fore.RED +
          ":   " + Fore.YELLOW + "Scintille Web Agency")
    print(Fore.GREEN + "Sito Web    " + Fore.RED +
          ":   " + Fore.YELLOW + "https://scintille.net\n")

    print(Fore.RED + "[" + Fore.RESET + "00" + Fore.RED + "]" + " Indietro          " +
          Fore.RED + "[" + Fore.RESET + "99" + Fore.RED + "]" + " Esci\n")

    option = input(Fore.RED + "[" + Fore.RESET + "-" + Fore.RED + "]" +
                   Fore.GREEN + " Seleziona una opzione: " + Fore.CYAN)

    if option == "00":
        start()
    elif option == "99":
        exit()


def disk_usage():
    """
    ANCHOR: Disk Usage
    It prints out the total, used, and free disk space on the system
    """
    utils.clear()

    utils.header()

    total = utils.get_total()
    used = utils.get_used()
    free = utils.get_free()

    print(Fore.RED + "[" + Fore.RESET + "-" +
          Fore.RED + "]" + Fore.GREEN + " Ecco le informazioni sul tuo disco:\n")

    print(Fore.RED + "[" + Fore.RESET + "-" +
          Fore.RED + "]" + Fore.CYAN + " Spazio Totale: " + Fore.YELLOW + str(total))
    print(Fore.RED + "[" + Fore.RESET + "-" +
          Fore.RED + "]" + Fore.CYAN + " Spazio Utilizzato: " + Fore.YELLOW + str(used))
    print(Fore.RED + "[" + Fore.RESET + "-" +
          Fore.RED + "]" + Fore.CYAN + " Spazio Disponibile: " + Fore.YELLOW + str(free) + "\n")

    print(Fore.RED + "[" + Fore.RESET + "00" + Fore.RED + "]" + " Indietro          " +
          Fore.RED + "[" + Fore.RESET + "99" + Fore.RED + "]" + " Esci\n")

    option = input(Fore.RED + "[" + Fore.RESET + "-" + Fore.RED + "]" +
                   Fore.GREEN + " Seleziona una opzione: " + Fore.CYAN)

    if option == "00":
        start()
    elif option == "99":
        exit()


def start():
    """
    ANCHOR: Start
    It prints a menu, asks the user to select an option, and then calls the appropriate function
    """
    utils.clear()

    utils.header()

    print(Fore.RED + "[" + Fore.RESET + "::" + Fore.RED + "]" + Fore.YELLOW +
          " Seleziona uno dei tool di controllo qui sotto " + Fore.RED + "[" + Fore.RESET + "::" + Fore.RED + "]\n")

    print(Fore.RED + "[" + Fore.RESET + "1" +
          Fore.RED + "]" + " Utilizzo del disco\n")

    print(Fore.RED + "[" + Fore.RESET + "99" + Fore.RED + "]" + " Informazioni          " +
          Fore.RED + "[" + Fore.RESET + "00" + Fore.RED + "]" + " Esci\n")

    option = input(Fore.RED + "[" + Fore.RESET + "-" + Fore.RED + "]" +
                   Fore.GREEN + " Seleziona una opzione: " + Fore.CYAN)

    if option == "99":
        about()
    elif option == "00":
        exit()
    elif option == "1":
        disk_usage()


if len(sys.argv) == 1:
    start()
else:
    if sys.argv[1] == "disk":
        print(utils.get_total() + "\n" +
              utils.get_used() + "\n" + utils.get_free())
