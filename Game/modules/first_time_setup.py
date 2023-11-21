from colorama import Fore, Back, Style
import os
import sys
import time
from combat_sys import clear

save_folder = 'Game/save_games/'
current_save = 'save1.txt'
joined_file = os.path.join(save_folder, current_save)
f = open(joined_file, 'r')
save_time = os.path.getmtime(joined_file)
save_user = f.readline().strip()
save_inventory = f.readline().strip()
f.close()

print(save_time, save_user, save_inventory)
def setup():
    print("test")