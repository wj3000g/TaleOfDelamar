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
import datetime
import zlib
init()


config = configparser.ConfigParser()
PLAYER_INVENTORY = None # Initialize the inventory for future use. (List)
__DEBUG_FLAG = True


class GameCrash(Exception): # Exception for manually initiated crashes
    pass


def print_centered(text, opt_fillchar=" "):
	term_columns = os.get_terminal_size()[0] 
	print(text.center(term_columns, opt_fillchar))


def tprint(text, sleep_frame=strings.META_WAITFRAME):
	if os.name == "nt":
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
	
	else:
		if type(text) is list:
			for multipart in text:
				for letter in multipart:
					print(letter, end='')
					sys.stdout.flush()
					time.sleep(sleep_frame)
				print("")
		
		else:
			for letter in text:
				print(letter, end='')
				sys.stdout.flush()
				time.sleep(sleep_frame)
	
	print("") # Prints a new line


def getstring(string_var):
	return string_var[config.get("GAMEDATA", "LANGUAGE")]


def clear_screen():
	if os.name == 'nt': # If OS is Windows
		os.system("cls")
	
	else:
		os.system("clear")


def debug(text):
	if __DEBUG_FLAG == True:
		cprint("DEBUG: " + str(text), "yellow")

	else:
		pass


def ret_save_data():
	"""
	Automatically de-obfuscate the obfuscated save file, and return its contents
	"""

	with open(strings.META_SAVEFILE, "rb") as obfuscated_save_file:
		obfuscated_save_data = obfuscated_save_file.read()

	deobfuscated_save_data = zlib.decompress(obfuscated_save_data).decode()
	return deobfuscated_save_data

def add_achievement(achievement_id):
	"""
	Adds the achievement ID to the game's save
	"""

	current_unlocked_achievements = str(config.get("GAMEDATA", "ACHIEVEMENTS")) # Get str from memory
	current_unlocked_achievements = current_unlocked_achievements.split(", ") # Converts str to list

	# We check if the player already have the achievement
	for achievement in current_unlocked_achievements:
		if achievement_id == achievement: # If the player already have the achievement...
			return
	
	# If we're here, this means that the player doesn't have the achievement yet, so we append it to the save.

	current_unlocked_achievements.append(achievement_id) # Add item to list
	current_unlocked_achievements = ', '.join(current_unlocked_achievements) # Convert list to str

	achievement_name = getstring(world.WORLD_ACHIEVEMENTS[achievement_id]["NAME"])
	cprint("You unlocked the achievement '" + achievement_name + "' !", "green")


def list_achievements():
	# TODO: this.
	pass


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
				"INVENTORY": "IDENTITYCARD",
				"LANGUAGE": game_language,
				"ACHIEVEMENTS": "",
				}

				save_game()
				clear_screen()
				return
			
			else:
				continue
		
		elif user_choice == "2" and game_save_exists == True:
			try:
				config.read_string(ret_save_data()) # Read de-obfuscated save data
				return
		
			except Exception as error: # The save file is unreadable or corrupted
				cprint("ERROR! The save file '"+strings.META_SAVEFILE+"' is unreadable or corrupted !", "red")
				cprint("Try to restore it to an earlier version or start a new game,", "red")
				cprint("Error message: " + str(error), "yellow")
				input()
				continue
		
		elif user_choice == "99":
			sys.exit()
		
		else:
			print("Incorrect choice!")
			input("Press [ENTER] to continue...")
			continue


def save_game():

	with open(strings.META_SAVEFILE_TEMP, "w") as temp_save_file_write:
		config.write(temp_save_file_write)

	with open(strings.META_SAVEFILE_TEMP, "r") as temp_save_file_read:
		temp_savefile_contents = temp_save_file_read.read() # Read the un-obfuscated data

	try:
		os.remove(strings.META_SAVEFILE_TEMP)
	
	except:
		pass # An error has occured while removing the temp save file, assuming it has been manually deleted
	
	obfuscated_save_data = zlib.compress(temp_savefile_contents.encode(), strings.META_SAVEFILE_COMPLEVEL)

	with open(strings.META_SAVEFILE, "wb") as obfuscated_save_file:
		obfuscated_save_file.write(obfuscated_save_data)


def welcome():
	"""
	Displays the welcome message at the start of the game
	"""

	print(colored("Tale of Delamar", "cyan") + " - version " + strings.META_GAMEVERSION)
	print("By " + colored(strings.META_GAMECREATOR, "magenta"))
	cprint(":: Type 'help' to get a list of all commands.", "green")

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

	EDIT: Implemented for v0.3.0
	"""

	print_centered(colored("= Showing map =", "magenta"), "-")

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
	
	MAP_MIDDLEBLOCK_HEADER += "====" # Dirty workaround to show "box-like"
	MAP_MIDDLEBLOCK_FOOTER += "===="

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


def look():
	location_id = config["GAMEDATA"]["CURRENTZONE"]
	location_name = getstring(world.WORLD_ROOMS[location_id]["NAME"])
	item_in_zone_id = world.WORLD_ROOMS[location_id]["HASITEM"]
	current_inventory = config["GAMEDATA"]["INVENTORY"]

	north_id = world.WORLD_ROOMS[location_id]["NORTH"]
	south_id = world.WORLD_ROOMS[location_id]["SOUTH"]
	east_id = world.WORLD_ROOMS[location_id]["EAST"]
	west_id = world.WORLD_ROOMS[location_id]["WEST"]

	tprint("You are at " + colored(location_name, "cyan"))
	tprint("-----------" + "-"*len(location_name)) # Automatically adjusts the size of the separator
	tprint(getstring(world.WORLD_ROOMS[location_id]["DIALOGENTRY"]))
	tprint("-----------" + "-"*len(location_name))
	tprint("Your surroundings --")

	if north_id == None:
		tprint("North: Nothing")
	else:
		tprint("North: " + colored(getstring(world.WORLD_ROOMS[north_id]["NAME"]), "cyan"))
	
	if south_id == None:
		tprint("South: Nothing")
	else:
		tprint("South: " + colored(getstring(world.WORLD_ROOMS[south_id]["NAME"]), "cyan"))

	if east_id == None:
		tprint("East: Nothing")
	else:
		tprint("East: " + colored(getstring(world.WORLD_ROOMS[east_id]["NAME"]), "cyan"))

	if west_id == None:
		tprint("West: Nothing")
	else:
		tprint("West: " + colored(getstring(world.WORLD_ROOMS[west_id]["NAME"]), "cyan"))
	
	tprint("-----------" + "-"*len(location_name))

	if item_in_zone_id == None:
		return
		
	else: # If there is an item in the current zone
		for item_id in current_inventory:
			if item_id == item_in_zone_id: # If the player already have the item...		
				return # Exits the function
					
		# The player doesn't have the item in the zone yet. We pick it up.
		tprint("You picked up an item !")
		
		new_item_name = getstring(world.WORLD_ITEMS[item_in_zone_id]["NAME"])
		print("You got '" + colored(new_item_name, "cyan") + "' !")

		try: 	# Workaround, not all "UNLOCKS" metadata has been written, so if we catch an error,
				# this means that there is no achievement to unlock.
			achievement_in_zone = world.WORLD_ITEMS[item_in_zone_id]["UNLOCKS"]
			
			if achievement_in_zone != None: # If there is an achievement
				add_achievement(achievement_in_zone)
		
		except:
			pass

		current_inventory = str(config.get("GAMEDATA", "INVENTORY")) # Get str from memory
		current_inventory = current_inventory.split(", ") # Converts str to list
		current_inventory.append(item_in_zone_id) # Add item to list
		current_inventory = ', '.join(current_inventory) # Convert list to str

		# Since config.set() only accepts str, we cast the list to an str just for this,
		# We use ast.literal_eval() to cast it back to a list
		config.set("GAMEDATA", "INVENTORY", str(current_inventory))
		
		return


def whereami():
	game_language = config.get("GAMEDATA", "LANGUAGE")
	current_location_name = world.WORLD_ROOMS[config["GAMEDATA"]["CURRENTZONE"]]["NAME"][game_language]
	tprint("You are at : " + colored(current_location_name, "cyan"))


def print_inventory():
	tprint("Inventory content : ")
	
	# Even older method (broken) : current_inventory = json.loads(config["GAMEDATA"]["INVENTORY"])
	# old method (broken) : current_inventory = json.loads(config.get("GAMEDATA", "INVENTORY"))
	
	# This is a "viking-type" workaround, it converts litteraly the save contents to a list
	# current_inventory = ast.literal_eval(config.get("GAMEDATA", "INVENTORY"))

	# New method : split inventory content to make a list

	current_inventory = str(config.get("GAMEDATA", "INVENTORY"))
	current_inventory = current_inventory.split(", ")

	for item_id in current_inventory:
		debug("item_id : " + str(item_id))
		item_name = getstring(world.WORLD_ITEMS[item_id]["NAME"])
		print(" - " + item_name)
	tprint("------------------")


def spawn_screen_transition():
	if os.name == "nt":
		os.system("color 80")
		time.sleep(0.3)
		os.system("cls")
		os.system("color 70")
		time.sleep(0.3)
		os.system("color 80")
		time.sleep(0.3)
		os.system("color 0F")
		time.sleep(0.3)
		os.system("cls")
	
	else:
		clear_screen()


def game_loop():
	while True:
		user_choice = input("> ").lower()

		if __DEBUG_FLAG == True:
			if user_choice == "debug":
				cprint("==- Debug menu -==", "yellow")
				cprint("1/ Add an item to inventory (by ID)", "yellow")
				cprint("2/ Travel to a specific location (by ID)", "yellow")
				cprint("3/ Crash the game", "magenta")

				debug_input = input("debug-menu/")

				if debug_input == "1":

					new_item_id = input("Item to add (ID, in caps) : ")
					current_inventory = str(config.get("GAMEDATA", "INVENTORY")) # Get str from memory
					current_inventory = current_inventory.split(", ") # Converts str to list
					current_inventory.append(new_item_id) # Add item to list
					current_inventory = ', '.join(current_inventory) # Convert list to str

					# Since config.set() only accepts str, we cast the list to an str just for this,
					# We use ast.literal_eval() to cast it back to a list
					config.set("GAMEDATA", "INVENTORY", str(current_inventory))
					print("Added item to inventory !")					
					continue

				elif debug_input == "2":
					zone_to_travel = input("Zone to travel (ID, in caps) : ")
					config.set("GAMEDATA", "CURRENTZONE", zone_to_travel)
					continue
				
				elif debug_input == "3":
					# This command is useful to get the current stacktrace, and to get the un-obfuscated save file
					cprint("Initiating game crash...", "yellow")
					raise GameCrash("Manually initiated game crash.")
				
				else:
					continue

		else:
			pass

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
		
		elif user_choice == "map":
			draw_map()
			continue
		
		elif user_choice == "save":
			print("Saving game...")
			save_game()
			cprint("Game saved !", "green")
			continue
		
		elif user_choice == "": # If the user enters a new line, do nothing
			continue
		
		else:
			print("Invalid command, type 'help' to get a list of all commands.")
			continue

try:
	GAME_INIT()
	spawn_screen_transition()
	welcome()
	game_loop()

except KeyboardInterrupt:
	# We save the game, then quit it.
	cprint("You pressed CTRL+C !", "yellow") 
	print("Saving game...")
	save_game()
	cprint("Game saved.", "green")
	input("Press [ENTER] to quit the game.")
	sys.exit()
	       
except Exception as game_error:

	with open(strings.META_SAVEFILE_TEMP, "w") as temp_save_file_write:
		config.write(temp_save_file_write)
	
	with open(strings.META_SAVEFILE_TEMP, "r") as temp_save_file_read:
		temp_save_data = temp_save_file_read.read()
	
	try:
		os.remove(strings.META_SAVEFILE_TEMP)
	
	except:
		pass

	with open(strings.META_CRASHFILE, "w") as crash_file:
		today = datetime.date.today()
		formatted_time = str(today.strftime('%d, %b %Y'))

		crash_file.write("===== Tale of Delamar =====\n")
		crash_file.write("Game version : " + strings.META_GAMEVERSION + "\n")
		crash_file.write("Date : " + formatted_time + "\n")
		crash_file.write("Base error : " + str(game_error) + "\n")
		crash_file.write("===== Traceback =====\n")
		crash_file.write(str(traceback.format_exc()) + "\n")
		crash_file.write("===== Memory save data =====\n")
		crash_file.write(temp_save_data + "\n")
		crash_file.write("===== End of File =====\n")
	
	cprint("The game crashed ! Please make a new GitHub issue at : " + strings.META_GITHUB_ISSUES_URL, "red")
	cprint("And embed the file named '" + strings.META_CRASHFILE + "'", "red")
	input("Press [ENTER] to exit the game.")
	sys.exit()
