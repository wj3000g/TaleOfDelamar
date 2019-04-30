import strings
import world
from colorama import init
from termcolor import cprint, colored
import configparser
import os
import sys
import time
init()

config = configparser.ConfigParser()
PLAYER_INVENTORY = None # Initialize the inventory for future use.
__DEBUG_FLAG = True


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


def save_game():
	with open(strings.META_SAVEFILE, "w") as save_file:
		config.write(save_file)

def welcome():
    """
    Displays the welcome message at the start of the game
    """

    print("Tale of Delamar - version " + strings.META_GAMEVERSION)
    print("By " + strings.META_GAMECREATOR)
    print(":: Type 'help' to get a list of all commands.")



def move_to_location(cardinal_point):
    try:
		if cardinal_point == "N":

			old_room = config["DATA"]["CURRENTZONE"]
			new_room = world.WORLD_ROOMS[old_room]["NORTH"]
			
			if world.WORLD_ROOMS[new_room]["NEEDITEM"] != None: # If an item is required to go there...
				current_inventory = config["DATA"]["INVENTORY"]
				needed_item_name = world.WORLD_ITEMS[world.WORLD_ROOMS[new_room]["NEEDITEM"]]["NAME"]
				
				if current_inventory == None:
					tprint("You do not have the required item in your inventory,")
					tprint("You need to have '" + needed_item_name + "'")
				
				else: # Inventory isn't blank
					for item in inventory:
						# TODO this
						pass
			

			
			config["DATA"]["CURRENTZONE"] = new_room
		
		elif cardinal_point == "S":
			old_room = config["DATA"]["CURRENTZONE"]
			new_room = world.WORLD_ROOMS[old_room]["SOUTH"]
			
			config["DATA"]["CURRENTZONE"] = new_room
		
		elif cardinal_point == "E":
			old_room = config["DATA"]["CURRENTZONE"]
			new_room = world.WORLD_ROOMS[old_room]["EAST"]
			
			config["DATA"]["CURRENTZONE"] = new_room
		
		elif cardinal_point == "W":
			old_room = config["DATA"]["CURRENTZONE"]
			new_room = world.WORLD_ROOMS[old_room]["WEST"]
			
			config["DATA"]["CURRENTZONE"] = new_room
	
	except Exception as error:
		print("You cannot go there.")
		
		if __DEBUG_FLAG == True:
			print("[DEBUG]: In function move_to_location(), Exception returned :")
			print(str(error))


def tprint(text, sleep_frame=strings.META_WAITFRAME): # TODO support multiparts (string lists)
	for letter in text:
		print(letter, end="")
		time.sleep(sleep_frame)
	
	print("") # Prints a new line
	

def look():
	location_id = config["DATA"]["CURRENTZONE"]
	location_name = world.WORLD_ROOMS[location_id]["NAME"]
	is_item_in_zone = world.WORLD_ROOMS[location_id]["HASITEM"]
	
	north_name = world.WORLD_ROOMS[world.WORLD_ROOMS[location_id]["NORTH"]]["NAME"]
	south_name = world.WORLD_ROOMS[world.WORLD_ROOMS[location_id]["SOUTH"]]["NAME"]
	east_name = world.WORLD_ROOMS[world.WORLD_ROOMS[location_id]["EAST"]]["NAME"]
	west_name =world.WORLD_ROOMS[world.WORLD_ROOMS[location_id]["WEST"]]["NAME"]
	
	tprint("You are at " + location_name)
	tprint("-----------" + "-"*len(location_name)) # Automatically adjusts the size of the separator
	tprint(world.WORLD_ROOMS[location_id]["DIALOGENTRY"]) # TODO test this, hopefully it prints the dialog entry associated to the zone
	tprint("-----------" + "-"*len(location_name))
	
	if 
	
		

def game_loop():
	while True:
		user_choice = input("> ").lower()

		if user_choice == "help":
			print(strings._HELP_MESSAGE)
			continue
		
		elif user_choice == "quit":
			print("Saving game...")
			save_game()
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


