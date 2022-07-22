from colorama import init, Fore, Back, Style
import utils

init()


def about():
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


def start():
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


start()

# total = total // (2**30)

# free = free // (2**30)
# free = round(free / total * 100, 2)
