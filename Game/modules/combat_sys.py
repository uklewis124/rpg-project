from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
from termcolor import colored
import os
import time


#init(autoreset=True)
just_fix_windows_console()


def clear(waiting=0.1):
    if waiting:
        time.sleep(waiting)
        os.system("cls" if os.name == "nt" else "clear")
    else:
        os.system("cls" if os.name == "nt" else "clear")


def color_testing():
    print(f"{Fore.GREEN}Starting tutorial... {Fore.RED}{Back.RED}Red{Style.RESET_ALL} Normal{colored('something after', 'red', 'on_blue')}")
    print(colored('Hello, World!', 'green'))
    print("Hi")


def start_tutorial():
    print(f"{Fore.GREEN}Preparing Console...")
    for _ in range(3):
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} /")
        clear()
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} -")
        clear()
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} \\")
        clear()
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} |")
        clear()
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} /")
        clear()
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} -")
        clear()
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} \\")
        clear()
        print(f"{Fore.GREEN}Preparing Console... {Fore.RED} |")
        clear()
    print(f"{Fore.GREEN}Starting Tutorial...")
