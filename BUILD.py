# TODO Create two version of the game at build, it creates one FR and EN

print("Starting: Loading modules...")
import os
import sys
import shutil
from termcolor import cprint
from colorama import init
from time import time
import datetime
import configparser
init()

_LOGFILE_NAME = "BUILDLOG.log"
now = datetime.datetime.now()

logfile = open(_LOGFILE_NAME, "a", 1)
logfile.write("\n\n================\n")
logfile.write(now.strftime("%Y-%m-%d %H:%M") + "  --  New task\n")


def info(text):
	cprint(text, "grey", "on_white")
	logfile.write(text + "\n")

info("** STARTED LOGGING")

def recursive_copy(src, dest): # From https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python
	"""
	Copy each file from src dir to dest dir, including sub-directories.
	"""
	list_dir = os.listdir(src)

	for item in list_dir:
		info("** [" + str(list_dir.index(item) + 1) + "/" + str(len(list_dir)) + "]: COPYING '" + item + "'...")
		
		file_path = os.path.join(src, item)

		# if item is a file, copy it
		if os.path.isfile(file_path):
			shutil.copy(file_path, dest)

		# else if item is a folder, recurse 
		elif os.path.isdir(file_path):
			new_dest = os.path.join(dest, item)
			
			shutil.copytree(file_path, new_dest)


start_time = time()

CONFIGFILE = "BUILDCONFIG.ini"

info("** LOADING CONFIG FILE '" + CONFIGFILE + "'...")
config = configparser.ConfigParser()

if os.path.isfile(CONFIGFILE):
	config.read(CONFIGFILE)


else:
	info("[WARN]: Your config file is empty, running interactive mode...")
	script_name = input("Name of the script to build : ")
	version_number_file = input("Name of the file containing the version number : ")
	modules_to_include = input("Modules to include (Cx_Freeze-style) : ")
	project_name = input("Name of the project (spaces not allowed) : ")

	choice_embed_other_files = input("Embed additional files in a folder ? [Y/n] : ")

	if choice_embed_other_files == "Y":
		folder_to_embed = input("Additional folder name : ")

		config["DATA"] = {
		"SCRIPT_NAME": script_name,
		"VERSION_NUMBER_FILE": version_number_file,
		"MODULES_TO_INCLUDE":  modules_to_include,
		"PROJECT_NAME":  project_name,
		"EMBED_ADD_FILES": choice_embed_other_files,
		"FOLDER_TO_EMBED": folder_to_embed
		}

	else:
		config["DATA"] = {
		"SCRIPT_NAME": script_name,
		"VERSION_NUMBER_FILE": version_number_file,
		"MODULES_TO_INCLUDE":  modules_to_include,
		"PROJECT_NAME":  project_name,
		"EMBED_ADD_FILES": choice_embed_other_files,
		"FOLDER_TO_EMBED": "None"
		}


	info("[INFO]: Writing to the config file...")
	with open(CONFIGFILE, "w") as config_file:
		config.write(config_file)

	info("** PROGRAM WILL NOW EXIT")
	input("Press any key to continue...")
	sys.exit()

info("** READING FILE '" + config["DATA"]["VERSION_NUMBER_FILE"] + "'...")
try:
	with open(config["DATA"]["VERSION_NUMBER_FILE"], "r") as version_file:
		SCRIPTVERSION = version_file.read()

except (FileNotFoundError, IOError) as error:
	info("[WARN]: File '" + config["DATA"]["VERSION_NUMBER_FILE"] + "' was not found, passing...")


NEW_DIST_FOLDER = config["DATA"]["PROJECT_NAME"] + "_" + SCRIPTVERSION + "_Win32"
info("** NEW DIST FOLDER = " + NEW_DIST_FOLDER)

info("** BUILD STARTING")

# Actually building the script
info("** RUNNING CX_FREEZE...")
os.system("python cxfreeze.py -c -OO -s --target-name=TaleOfDelamar.exe --include-modules=" + config["DATA"]["MODULES_TO_INCLUDE"] + " " + config["DATA"]["SCRIPT_NAME"])


# Checking if we embed an additionnal folder...
if config["DATA"]["EMBED_ADD_FILES"] == "Y":
	folder_to_embed = config["DATA"]["FOLDER_TO_EMBED"]

	recursive_copy(folder_to_embed, "dist/")


# Renaming "dist" into the correct folder name
info("** RENAMING THE DIST FOLDER...")
try:
	os.rename("dist/", NEW_DIST_FOLDER)

except FileExistsError:
	info("** NEW DIST FOLDER ALREADY EXISTS")


info("** EMBEDDING FILE '" + config["DATA"]["VERSION_NUMBER_FILE"] + "'...")
shutil.copy(config["DATA"]["VERSION_NUMBER_FILE"], NEW_DIST_FOLDER)


# Zipping the folder
# make archive explaination : the first argument is the name of the end file,
# wich is the name of the new dist folder, the function auto-adds a '.zip', so the name is the same.
info("** ZIPPING THE NEW DIST FOLDER...")
shutil.make_archive(NEW_DIST_FOLDER, 'zip', NEW_DIST_FOLDER)


info("** CLEANING UP... (RECURSIVE METHOD)")
info("** [1/2] REMOVING FOLDER 'dist'... (may not exist)")
if os.path.isdir("dist"): # if the "dist" dir exists...
	try:
		shutil.rmtree('dist', ignore_errors=False) # Recursively removes the "dist" directory

	except Exception as error:
		info("[ERROR]: " + str(error))


info("** [2/2] REMOVING FOLDER '" + NEW_DIST_FOLDER + "'...")
if os.path.isdir(NEW_DIST_FOLDER):
	try:
		shutil.rmtree(NEW_DIST_FOLDER, ignore_errors=False)

	except Exception as error:
		info("[ERROR]: " + str(error))

total_time_seconds = round(time() - start_time, 2)


info("** BUILD COMPLETE!")
info("** BUILD TIME : " + str(total_time_seconds) + " SECONDS")
info("** END LOGGING")
info("================")
input("[Press ENTER to quit]")
logfile.close()
sys.exit()
