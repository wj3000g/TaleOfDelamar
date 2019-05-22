import strings
import world
from colorama import init
from termcolor import cprint, colored
import configparser
import os
import sys
import time
import ast
import traceback
init()

config = configparser.ConfigParser()
PLAYER_INVENTORY = None # Initialize the inventory for future use. (List)
__DEBUG_FLAG = True

def print_centered(text, opt_fillchar=" "):
	term_columns = os.get_terminal_size()[0]
	print(text.center(term_columns, opt_fillchar))

def getstring(string_var):
	return string_var[config.get("GAMEDATA", "LANGUAGE")]

def clear_screen():
	if os.name == 'nt': # If OS is Windows
		os.system("cls")
	
	else:
		os.system("clear")

def debug(text):
	cprint("DEBUG: " + str(text), "yellow")

def GAME_INIT():
	print("loading...")

	if os.name == 'nt': # If OS is Windows or Windows-based...
		os.system("title " + strings.META_GAMETITLE)

	else:
		# While it is possible to set a custom title on Linux, I need to focus on Windows users first.
		# Thus this feature is currently disabled on Linux.
		pass


	while True: # Title screen
		clear_screen()
		print(colored(strings.META_GAMENAME, "cyan") + " -- by " + strings.META_GAMECREATOR)
		cprint("Version " + strings.META_GAMEVERSION)
		print("-----------\n")
		
		print("1/ Start a new game")

		if os.path.isfile(strings.META_SAVEFILE) == True: # If the save file exists...
			game_save_exists = True
			print("2/ " + colored("Load your save", "green"))
		
		else:
			game_save_exists = False
		
		print("99/ Exit the game")
			
		user_choice = input("Menu> ")

		if user_choice == "1":
			cprint("Are you sure you want to start a new game ?", "yellow")
			cprint("Doing this will erase all existing progress you may have made", "yellow")
			print("enter 'start' without quotes to start a new game.")
			user_verify = input("Menu/confirm> ").lower()
			
			if user_verify == "start":
			
				print("Select your language : ")
				print("1/ Français")
				print("2/ English")

				language_choice = input("Menu/confirm/language> ")

				if language_choice == "1":
					game_language = "FR"
				
				elif language_choice == "2":
					game_language = "EN"

				else:
					cprint("Incorrect entry !", "yellow")
					input()
					continue


				config["GAMEDATA"] = {
				"CURRENTZONE": "CRASHSITE", # The starting point of the game
				"INVENTORY": ["IDENTITYCARD"],
				"LANGUAGE": game_language
				}

				save_game()
				clear_screen()
				return
			
			else:
				continue
		
		elif user_choice == "2" and game_save_exists == True:
			try:
				config.read(strings.META_SAVEFILE)
				return
		
			except Exception as error: # The save file is unreadable or corrupted
				cprint("ERROR! The save file '"+strings.META_SAVEFILE+"' is unreadable or corrupted !", "red")
				cprint("Try to restore it to an earlier version or or start a new game,", "red")
				cprint("DEBUG INFOS: " + str(error), "yellow")
				input()
				continue
		
		elif user_choice == "99":
			sys.exit()
		
		else:
			print("Incorrect choice!")
			input("Press [ENTER] to continue...")
			continue


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

	if __DEBUG_FLAG == True:
		cprint("Debug flag enabled !", "yellow")
		cprint("Traceback and exception printing enabled !", "yellow")


def draw_map():
	"""
	okay so this one is a little tricky and experimental, let me explain:
	We draw a map of the player's surroundings, sounds easy right ? Wrong.
	Because we're on a command line, we're drawing stuff up to down.
	So we need to know if we're drawing the room on the player's north, if yes, draw it.
	The size of the "boxes" of the rooms will be determined by the length of the name of the room +2, 
	so it's nicely centered and stuff.
	Then we need to know if we're drawing the room at the left, if yes, 
	we need to move the room to the north first, etc, etc...

	See why it's complicated ?

	I plan to (try to) implement this in the v0.4.0, but not before.
	"""

	print_centered("= Showing map =", "-")

	location_id = config.get("GAMEDATA", "CURRENTZONE")

	north_id = world.WORLD_ROOMS[location_id]["NORTH"]
	south_id = world.WORLD_ROOMS[location_id]["SOUTH"]
	east_id = world.WORLD_ROOMS[location_id]["EAST"]
	west_id = world.WORLD_ROOMS[location_id]["WEST"]

	if north_id != None:
		# We get the length of the room name, with the current language
		north_room_name = getstring(world.WORLD_ROOMS[north_id]["NAME"])
		north_room_name_len = len(north_room_name)
		# debug("ROOM LEN: " + str(north_room_name_len))

		map_north_data_header = "=" * (north_room_name_len + 2) # Header + 2 add. spaces
		map_north_data_body_direction = "| " + "- North -".center(north_room_name_len) + " |" 
		map_north_data_body = "| " + north_room_name + " |"
		map_north_data_footer = "=" * (north_room_name_len + 2) # Footer + 2 add. spaces

		print_centered(map_north_data_header)
		print_centered(map_north_data_body_direction)
		print_centered(map_north_data_body)
		print_centered(map_north_data_footer)
	
	# This one is a little trickier, we draw West, Here, and East at once.
	
	MAP_MIDDLEBLOCK_HEADER = ""
	MAP_MIDDLEBLOCK_BODY_DIRECTION = ""
	MAP_MIDDLEBLOCK_BODY = ""
	MAP_MIDDLEBLOCK_FOOTER = ""

	if west_id != None:
		# We get the length of the room name, with the current language
		west_room_name = getstring(world.WORLD_ROOMS[west_id]["NAME"])
		west_room_name_len = len(west_room_name)

		MAP_MIDDLEBLOCK_HEADER += "=" * (west_room_name_len + 2)
		MAP_MIDDLEBLOCK_BODY_DIRECTION += "| " + "- West -".center(west_room_name_len) + " |"
		MAP_MIDDLEBLOCK_BODY += "| " + west_room_name + " |"
		MAP_MIDDLEBLOCK_FOOTER += "=" * (west_room_name_len + 2)

	# then, we draw the current position of the player.

	current_room_name = getstring(world.WORLD_ROOMS[config.get("GAMEDATA", "CURRENTZONE")]["NAME"])
	current_room_name_len = len(current_room_name)

	MAP_MIDDLEBLOCK_HEADER += "=" * (current_room_name_len + 2)
	MAP_MIDDLEBLOCK_BODY_DIRECTION += "| " + "- Here -".center(current_room_name_len) + " |"
	MAP_MIDDLEBLOCK_BODY += "| " + current_room_name + " |"
	MAP_MIDDLEBLOCK_FOOTER += "=" * (current_room_name_len + 2)

	if east_id != None:
		# We get the length of the room name, with the current language
		east_room_name = getstring(world.WORLD_ROOMS[east_id]["NAME"])
		east_room_name_len = len(east_room_name)

		MAP_MIDDLEBLOCK_HEADER += "=" * (east_room_name_len + 2)
		MAP_MIDDLEBLOCK_BODY_DIRECTION += "| " + "- East -".center(east_room_name_len) + " |"
		MAP_MIDDLEBLOCK_BODY += "| " + east_room_name + " |"
		MAP_MIDDLEBLOCK_FOOTER += "=" * (east_room_name_len + 2)
	
	print_centered(MAP_MIDDLEBLOCK_HEADER)
	print_centered(MAP_MIDDLEBLOCK_BODY_DIRECTION)
	print_centered(MAP_MIDDLEBLOCK_BODY)
	print_centered(MAP_MIDDLEBLOCK_FOOTER)

	if south_id != None:
		south_room_name = getstring(world.WORLD_ROOMS[south_id]["NAME"])
		south_room_name_len = len(south_room_name)

		map_south_data_header = "=" * (south_room_name_len + 2) # Header + 2 add. spaces
		map_south_data_body_direction = "| " + "- South -".center(south_room_name_len) + " |" 
		map_south_data_body = "| " + south_room_name + " |"
		map_south_data_footer = "=" * (south_room_name_len + 2) # Footer + 2 add. spaces
	
		print_centered(map_south_data_header)
		print_centered(map_south_data_body_direction)
		print_centered(map_south_data_body)
		print_centered(map_south_data_footer)
	
	print("") # New line


def move_to_location(cardinal_point):
	"""
	cardinal point should be "NORTH", "SOUTH", "EAST" or "WEST"
	"""

	try:

		old_room = config["GAMEDATA"]["CURRENTZONE"]
		new_room = world.WORLD_ROOMS[old_room][cardinal_point]
		
		if new_room == None:
			tprint("You cannot go there.")
			return

		
		new_room_name = getstring(world.WORLD_ROOMS[new_room]["NAME"])
		
		debug("new_room = " + str(new_room))
		debug("new_room_name = " + str(new_room_name))

		if world.WORLD_ROOMS[new_room]["NEEDITEM"] != None: # If an item is required to go there...
			current_inventory = config["GAMEDATA"]["INVENTORY"]
			needed_item_id = world.WORLD_ITEMS[world.WORLD_ROOMS[new_room]["NEEDITEM"]]["ID"]
			needed_item_name = world.WORLD_ITEMS[world.WORLD_ROOMS[new_room]["NEEDITEM"]]["NAME"]
			
			if current_inventory == None:
				tprint("You do not have the required item in your inventory,")
				tprint("You need to have '" + needed_item_name + "'")
				return
				
			else: # Inventory isn't blank
				for item_id in current_inventory:
					if item_id == needed_item_id: # If the player have the needed item in his inventory...
						tprint("You entered by using " + needed_item_name)
						tprint("you are now at : " + new_room_name)
						config["GAMEDATA"]["CURRENTZONE"] = new_room
						return # Exits the function
					
				# If we arrive here, this means that the player doesn't have the needed item.
				tprint("You do not have the required item in your inventory,")
				tprint("You need to have '" + needed_item_name + "'")
				return
			
		else: # The room doesn't requires an item...
			config["GAMEDATA"]["CURRENTZONE"] = new_room
			tprint("You are now at : " + new_room_name)
			return
	
	except Exception as error: # If we arrive here, this means that there is a bug in there, oops.
		print("ERROR! in function move_to_location() try block raised an exception !")
		print(str(error))
		traceback.print_exc()
		return


def tprint(text, sleep_frame=strings.META_WAITFRAME):
	if type(text) is list:
		for multipart in text:
			for letter in multipart:
				print(letter, end='')
				time.sleep(sleep_frame)
			print("")
	
	else:
		for letter in text:
			print(letter, end='')
			time.sleep(sleep_frame)
	
	print("") # Prints a new line


def look():
	location_id = config["GAMEDATA"]["CURRENTZONE"]
	location_name = getstring(world.WORLD_ROOMS[location_id]["NAME"])
	item_in_zone_id = world.WORLD_ROOMS[location_id]["HASITEM"]
	current_inventory = config["GAMEDATA"]["INVENTORY"]

	north_id = world.WORLD_ROOMS[location_id]["NORTH"]
	south_id = world.WORLD_ROOMS[location_id]["SOUTH"]
	east_id = world.WORLD_ROOMS[location_id]["EAST"]
	west_id = world.WORLD_ROOMS[location_id]["WEST"]

	tprint("You are at " + location_name)
	tprint("-----------" + "-"*len(location_name)) # Automatically adjusts the size of the separator
	tprint(getstring(world.WORLD_ROOMS[location_id]["DIALOGENTRY"]))
	tprint("-----------" + "-"*len(location_name))
	tprint("Your surroundings --")

	if north_id == None:
		tprint("North: Nothing")
	else:
		tprint("North: " + getstring(world.WORLD_ROOMS[north_id]["NAME"]))
	
	if south_id == None:
		tprint("South: Nothing")
	else:
		tprint("South: " + getstring(world.WORLD_ROOMS[south_id]["NAME"]))

	if east_id == None:
		tprint("East: Nothing")
	else:
		tprint("East: " + getstring(world.WORLD_ROOMS[east_id]["NAME"]))

	if west_id == None:
		tprint("West: Nothing")
	else:
		tprint("West: " + getstring(world.WORLD_ROOMS[west_id]["NAME"]))
	
	tprint("-----------" + "-"*len(location_name))

	if item_in_zone_id == None:
		return
		
	else: # If there is an item in the current zone
		for item_id in current_inventory:
			if item_id == item_in_zone_id: # If the player already have the item...		
				return # Exits the function
					
		# The player doesn't have the item in the zone yet. We pick it up.
		tprint("You picked up an item !")
		
		new_item_name = getstring(item_in_zone_id["NAME"])
		print("You got '" + new_item_name + "'")
		config.set("GAMEDATA", "INVENTORY", item_in_zone_id["ID"])
		# Adds the item to the inventory
		return


def whereami():
	game_language = config.get("GAMEDATA", "LANGUAGE")
	current_location_name = world.WORLD_ROOMS[config["GAMEDATA"]["CURRENTZONE"]]["NAME"][game_language]
	tprint("You are at : " + current_location_name)


def print_inventory():
	tprint("Inventory content : ")
	
	# Even older method (broken) : current_inventory = json.loads(config["GAMEDATA"]["INVENTORY"])
	# old method (broken) : current_inventory = json.loads(config.get("GAMEDATA", "INVENTORY"))
	
	# This is a "viking-type" workaround, it converts litteraly the save contents to a list
	current_inventory = ast.literal_eval(config.get("GAMEDATA", "INVENTORY"))

	for item_id in current_inventory:
		item_name = world.WORLD_ITEMS[item_id]["NAME"]
		print(str(current_inventory.index(item_id) + 1) + " - " + item_name)
	tprint("------------------")


def game_loop():
	while True:
		user_choice = input("> ").lower()

		if user_choice == "help":
			print(getstring(strings._T_HELP_MESSAGE))
			continue
		
		elif user_choice == "quit":
			print("Saving game...")
			save_game()
			print("Quitting game...")
			sys.exit(0)
		
		elif user_choice == "whereami":
			whereami()
			continue
		
		elif user_choice == "north" or user_choice == "n":
			move_to_location("NORTH")
			continue
		
		elif user_choice == "south" or user_choice == "s":
			move_to_location("SOUTH")
			continue
		
		elif user_choice == "east" or user_choice == "e":
			move_to_location("EAST")
			continue
		
		elif user_choice == "west" or user_choice == "w":
			move_to_location("WEST")
			continue

		elif user_choice == "look":
			look()
			continue

		elif user_choice == "inventory":
			print_inventory()
			continue
		
		elif user_choice == "drop":
			print_inventory()
			print("-----------")
			
			try:
				item_to_drop_number = int(("What would you like to drop ? [ID] : ")) + 1
			
			except:
				print("You must enter a number !")
				continue
			
			current_inventory = ast.literal_eval(config.get("GAMEDATA", "INVENTORY"))

			for item_id in current_inventory:
				if current_inventory.index(item_id) + 1 == item_to_drop_number:
					item_to_drop_id = item_id
					break
			
			item_to_drop_name = getstring(world.WORLD_ITEMS[item_id]["NAME"])

			user_confirm = input("Are tou sure you want to drop " + item_to_drop_name + " ? [y/n] : ").lower()

			if user_confirm == "y":


		
		elif user_choice == "map":
			draw_map()
			continue
		
		elif user_choice == "": # If the user enters a new line, do nothing
			continue
		
		else:
			print("Invalid command, type 'help' to get a list of all commands.")
			continue


GAME_INIT()
clear_screen()
welcome()
game_loop()
