# Adventure Game using Python
try:
    import time
    import random
    import sys
    import os
    import pandas as pd # Not sure if I'll use this yet
    import datetime
    import asyncio # Not sure if I'll use this yet
    import resources.tutorial as tutorial
except ImportError as e:
    print("Imports failed")
    print("In particular, the following imports failed:")
    print(e)
    sys.exit()
print("Imports successful")
class Game:
    def console_clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        print("Welcome to the game!")

    def next():
        time.sleep(1)

    def wait_prompt():
        input("Press enter to continue... ")
    def print(self, msg):
        print(msg)
        self.next()
        
    item_values = {
        'map': 1,
        'water': 1,
        'food': 1,
        'sword': 5,
        'shield': 5,
        'armor': 5
    }
# Prints welcome message
Game.wait_prompt()
Game()
Game.next()
Game.console_clear()
Game.print("Test")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          131721]


# Begin game
print("Before we begin, we need to setup your character.")
Game.next()

class PlayerProfile:
    """
    This class represents the player's profile.
    """
    name = input("What is your character's name? ")
    age = input("What is your character's age? ")
    sex = input("Is your character male or female? ")
    gold = 0
    inventory = ['map', 'water', 'food']
    health = 100

    def check_net_worth(self):
        """
        This method calculates the net worth of the player's inventory.
        """
        net_worth = 0
        for item in self.inventory:
            net_worth += Game.item_values[item]
        return net_worth

# Get player class
player = PlayerProfile()
print(f"Hello, {player.name}!")

Game.next()

CITY_NAME = "City of Isso"

print(f"Hello traveler, welcome to {CITY_NAME} city!")
print(f"Here you will find many adventures and quests to complete.")
print(f"You will also find many dangers and enemies.")
print(f"To get a head start, you should visit the local tavern and get some supplies.")
print(f"Good luck!")

# Countdown & beginning
time.sleep(5)
Game.console_clear()

# Entering the city
print(f"You are entering the city of {CITY_NAME}")
Game.next()
print("Here you will be faced with many chalenges and quests.")
print("You will also find many dangers and enemies.")
print("To start, let's get you some supplies.")

# Ask if player wants to go through tutorial
tutorial_ask = input("Would you like to go through the tutorial? (y/n) ")
if str(tutorial_ask.lower()) in ['y', 'yes','ye']:
    tutorial.run_tutorial(player)
else:
    pass

# DEBUG print("DEBUG: Player inventory: " + str(player.inventory))
# DEBUG print("DEBUG: Player net worth: " + str(player.check_net_worth()))
# DEBUG print("The game now starts loading levels...")

class levels:
    def __init__(__self__):
        self = __self__
    def level_1(self, Game):
        Game.console_clear()

levels.level_1(Game)
