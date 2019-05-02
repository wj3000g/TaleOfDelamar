# Strings.py file --- All strings used in Tale Of Delamar are here
# When a variable starts with "I", it means that the string is a dict,
# and needs to be called to : I_STRING_NAME["EN"] or I_STRING_NAME["FR"]


# These are strings that do not directly relate to the story, they relate to the game/program itself
META_GAMENAME = "Tale Of Delamar"
META_GAMEVERSION = "0.2.0"
META_GAMECREATOR = "Sandai"
META_GAMETITLE = META_GAMENAME + " - version " + META_GAMEVERSION
META_SAVEFILE = "SAVE.ini"
META_WAITFRAME = 0.02 # Wait frame between each character appearance


# These are a bunch of misc strings
_HELP_COMMANDS = "help quit whereami north/n south/s east/e west/w look inventory"
_T_HELP_MESSAGE = {
    "EN": "Available commands : " + _HELP_COMMANDS,
    "FR": "Commandes disponibles: " + _HELP_COMMANDS
}
_PLACEHOLDER = "__DEBUG_PLACEHOLDER"

# These are strings said by the in-game player
I_PLAYER_DIALOG_1 = {
    "FR": [
        "[Vous] - ugh... j'suis où ? y'a pas de lumière, juste un bouton qui est allumé en vert...",
        "Bon, qui ne tente rien n'a rien...",
        "*click*",
        "[voix faible, robotique] - Démarrage...",
        "Bienvenue dans AtlasOS !",
        "Système de survie... OK!",
        "Ouverture de la visière...",
        "(La lumière éteincellante du soleil illumine votre visage, vous êtes allongé sur le sable rouge.)"
    ],

    "EN": [
        "[You] - ugh... where am I ? there's no light, only a green button...",
        "right, nothing ventured, nothing gained...",
        "*click*",
        "[quiet voice, robotic] - Starting...",
        "Welcome to AtlasOS !",
        "Life support system... Online!",
        "Opening visor...",
        "(The bright light illuminates your face, you are laying down on the red sand.)"
    ]
}

ZONE_I_CRASHSITE = {
    "EN": "The crash site",
    "FR": "Le site du crash"
}

PLAYER_DIALOG_BASE1 = {
    "FR": [
        "(vous passez par ce qui s'apparente à un SAS détruit...)",
        "(des fissures sont présentes sur les vitres des couloirs de la base abandonnée.)"
    ],

    "EN": [
        "(you go through what looks like a destroyed SAS...)"
        "(There are cracks on the windows of the abandoned bases corridors.)"
    ]
}


PLAYER_DIALOG_DUNES1 = {
    "FR": "Des étendues de dunes de sable à perte de vue",
    "EN": "Sand dunes as far as the eye can see"
}

PLAYER_DIALOG_MINING2 = {
    "FR": "(vous vous approchez du site de minage 'Shubin')",
    "EN": "(you are approaching the 'Shubin' mining site)"
}

PLAYER_DIALOG_SITE_BLACKBOX1 = {
    "FR": "Vous vous trouvez devant une boîte noire semi-enfouie dans le sable.",
    "EN": "You are in front of a semi-buried black box in the sand."
}

PLAYER_DIALOG_DUNES2 = {
    "FR": "Encore plus de dunes...",
    "EN": "Even more dunes..."
}

PLAYER_DIALOG_CRASHEDSHIP = "Vous êtes devant vôtre vaisseau à moitié détruit."

PLAYER_DIALOG_MINING1 = "Vous êtes devant le site de minage 'Kudre'"

I_PLAYER_DIALOG_BLACKBOX1 = {
    "FR": "Une boîte noire, une lecteur de cassettes est requis pour le lire.",
    "EN": "A black box, a tape player is required to read it."
}

I_PLAYER_DIALOG_TAPE_PLAYER = {
    "FR": "Un lecteur de cassettes.",
    "EN": "A tape player."
}

I_PLAYER_DIALOG_CROWBAR = {
    "FR": "Un pied-de-biche.",
    "EN": "A crowbar."
}

I_PLAYER_DIALOG_PASSKEY_LEVEL1 = {
    "FR": "Une carte d'accès (niveau 1).",
    "EN": "An access card (level 1)."
}

I_PLAYER_DIALOG_IDENTITYCARD = {
    "FR": "Une carte d'idendité",
    "EN": "An identity card"
}

PLAYER_DIALOG_CITY1_CENTER = _PLACEHOLDER
PLAYER_DIALOG_CITY1_GATES = _PLACEHOLDER
PLAYER_DIALOG_DUNES3 = _PLACEHOLDER
PLAYER_DIALOG_CITY1_HABS = _PLACEHOLDER
PLAYER_DIALOG_CITY1_OFFICE = _PLACEHOLDER
PLAYER_DIALOG_CITY1_PATH1 = _PLACEHOLDER
PLAYER_DIALOG_CITY1_TOOLSMITH = _PLACEHOLDER
PLAYER_DIALOG_CITY1_ATLASSTORE = _PLACEHOLDER
PLAYER_DIALOG_CITY1_EXIT = _PLACEHOLDER
