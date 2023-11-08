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
    import levels
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

    def location_request(self):
        solved = False
        while solved == False:
            location = input("Where would you like to go? ")
            if location in self.get_locations():
                solved = True
                print(f"Going to {location}...")
                Game.next()
                Game.console_clear()
                return location
            else:
                print("That location doesn't exist.")
                Game.next()
                Game.console_clear()

    def get_locations():
        locations = ['tavern', 'market', 'town square', 'forest', 'home']
        return locations
# Prints welcome message
Game()
Game.next()
Game.console_clear()

# Begin game
print("Before we begin, we need to setup your character.")
Game.next()
Game.console_clear()
# Get player name
class PlayerProfile:
    name = input("What is your characters name? ")
    age = input("What is your characters age? ")
    sex = input("Is your character male or female? ")
    gold = 0
    inventory = ['map', 'water', 'food']
    health = 100

# Get player class
player = PlayerProfile()
print(f"Hello, {player.name}!")
Game.next()

levels = os.listdir('levels')
for i in levels:
    temp_level = os.join('levels.',i).split('.py')
    import temp_level
    print(temp_level)

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

location = Game.location_request(self=Game)
