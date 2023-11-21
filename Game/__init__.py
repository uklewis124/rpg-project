import colorama as c
from colorama import Fore, Back, Style
c.init(autoreset=True)
c.just_fix_windows_console()

print(Fore.RED,"[FATAL] error goes here")
print(Back.GREEN,"Green back")
print(Style.DIM,"Dim style")
print(Style.RESET_ALL,"Reset style")
print("back to normal")