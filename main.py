# Adventure Game using Python
try:
    import time
    import random
    import sys
    import os
    import pandas as pd # Not sure if I'll use this yet
    import datetime
    import asyncio # Not sure if I'll use this yet
except ImportError as e:
    print("Imports failed")
    print("In particular, the following imports failed:")
    print(e)
    sys.exit()

print("Imports successful")
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    def console_clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def __init__(self):
        print("Welcome to the game!")
Game()
time.sleep(5)
Game.console_clear(self=Game)
