import strings
import world
from colorama import init
from termcolor import cprint, colored
import configparser
import os
import sys
init()

config = configparser.ConfigParser()
PLAYER_INVENTORY = None # Initialize the inventory for future use.

def clear_screen():
    if os.name == 'nt': # If OS is Windows
        os.system("cls")
    
    else:
        os.system("clear")


def GAME_INIT():
    print("loading...")

    if os.name == 'nt': # If OS is Windows or Windows-based...
        os.system("title " + strings.META_GAMETITLE)

    else:
        # While it is possible to set a custom title on Linux, I need to focus on Windows users first.
        # Thus this feature is currently disabled on Linux.
        pass

    if os.path.isfile(strings.META_SAVEFILE) == True: # If the save file exists...
        try:
            config.read(strings.META_SAVEFILE)

            PLAYER_INVENTORY = config["DATA"]["INVENTORY"] # Loads the inventory from the save file

        
        except Exception as error: # The save file is unreadable or corrupted
            cprint("ERROR! The save file '"+strings.META_SAVEFILE+"' is unreadable or corrupted !", "red")
            cprint("Try to restore it to an earlier version or to remove it,", "red")
            cprint("-to allow the game to start from a new one.", "red")
            cprint("DEBUG INFOS: " + str(error), "yellow")
            input()
            sys.exit(0)
    
    else:
        with open(strings.META_SAVEFILE, "w") as config_file:
            config["GAMEDATA"] = {
                "CURRENTZONE": "CRASHEDSHIP", # The starting point of the game
                "INVENTORY": None
            }

    while True: # Title screen
        pass






def welcome():
    """
    Displays the welcome message at the start of the game
    """

    print("Tale of Delamar - version " + strings.META_GAMEVERSION)
    print("By " + strings.META_GAMECREATOR)
    print(":: Type 'help' to get a list of all commands.")


def teleport_to_destination(destination_id):
    PLAYER_LOCATION = destination_id

def move_to_location(cardinal_point):
    pass
    

while True:
    user_choice = input("> ").lower()

    if user_choice == "help":
        print(strings._HELP_MESSAGE)
        continue
    
    elif user_choice == "quit":
        print("Saving game...")
        config["DATA"]["INVENTORY"] = PLAYER_INVENTORY
        print("Quitting game...")
        sys.exit(0)
    
    elif user_choice == "whereami":
        whereami()
        continue
    
    elif user_choice == "north" or "n":
        move_to_location("N")
        continue
    
    elif user_choice == "south" or "s":
        move_to_location("S")
        continue
    
    elif user_choice == "east" or "e":
        move_to_location("E")
        continue
    
    elif user_choice == "west" or "w":
        move_to_location("W")
        continue

    elif user_choice == "look":
        look()
        continue

    elif user_choice == "inventory":
        inventory()
        continue
    
    else:
        print("Invalid command, type 'help' to get a list of all commands.")
        continue
