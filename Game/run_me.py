from colorama import Fore, Back, Style
print(f"{Fore.YELLOW}Imported colorama.{Style.RESET_ALL}")
import os
print(f"{Fore.YELLOW}Imported os.{Style.RESET_ALL}")
import game
print(f"{Fore.YELLOW}Imported game.{Style.RESET_ALL}")
import time
print(f"{Fore.YELLOW}Imported time.{Style.RESET_ALL}")
from modules import *
print(f"{Fore.YELLOW}Imported modules.{Style.RESET_ALL}")
from modules.combat_sys import clear
print(f"{Fore.YELLOW}Clearing Console{Style.RESET_ALL}")
clear(2)

VERSION = "1.0.0"
state = False

print(f"Version {VERSION}")
if state:
    print(f"This game is in {state}")

# Testing game libary to ensure it is functioning
game.load()

# Preparing User Data
print(f"{Fore.GREEN}Preparing User Data...{Style.RESET_ALL}")
first_time_setup.setup()

# Starting Tutorial
combat_sys.start_tutorial()
