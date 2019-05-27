# Strings.py file --- All strings used in Tale Of Delamar are here
# When a variable starts with "I", it means that the string is a dict,
# and needs to be called to : I_STRING_NAME["EN"] or I_STRING_NAME["FR"]


# These are strings that do not directly relate to the story, they relate to the game/program itself
META_GAMENAME = "Tale Of Delamar"
META_GAMEVERSION = "0.3.0"
META_GAMECREATOR = "Sandai"
META_GAMETITLE = META_GAMENAME + " - version " + META_GAMEVERSION
META_SAVEFILE = "save.dat"
# The config writes here first, then we read the file and encode/compress it, finally we remove the temp file
META_SAVEFILE_TEMP = "save.dat.temp"
META_WAITFRAME = 0.02 # Wait frame between each character appearance
META_CRASHFILE = "CRASHLOG.log"
META_GITHUB_ISSUES_URL = "https://github.com/Sandaidev/TaleOfDelamar/issues"
META_SAVEFILE_COMPLEVEL = 9 # Compression level of the obfuscated save file


# These are a bunch of misc strings
_HELP_COMMANDS = "help quit whereami north/n south/s east/e west/w look inventory map"
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

PLAYER_DIALOG_DUNES3 = {
    "FR": "Encore plus de dunes...",
    "EN": "Even more dunes..."
}


I_PLAYER_DIALOG_CRASHEDSHIP = {
    "FR": "Vous êtes devant vôtre vaisseau à moitié détruit.",
    "EN": "You are in front of your crashed ship."
}

I_PLAYER_DIALOG_MINING1 = {
    "FR": "Vous êtes devant le site de minage 'Kudre'",
    "EN": "You are in front of the mining site 'Kudre'"

}

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

I_PLAYER_DIALOG_CITY1_CENTER = {
    "FR": "Vous êtes au centre ville, vous apercevez des magasins de partout.",
    "EN": "You are in the city centre"
}

I_PLAYER_DIALOG_CITY1_GATES = {
    "FR": "Vous êtes devant des portes, il est écrit sur un panneau 'Ville de Shubin'.",
    "EN": "You are in front of doors, it is written on a sign 'City of Shubin'."
}

I_PLAYER_DIALOG_CITY1_HABS = {
    "FR": "Vous êtes devant un grand bâtiment, il est écrit sur un panneau 'Shubin Habs'.",
    "EN": "You are in front of a big building, it is written on a sign 'Shubin Habs'."
}

I_PLAYER_DIALOG_CITY1_OFFICE = {
    "FR": "Vous êtes devant l'office de tourisme.",
    "EN": "You are in front of the tourism office."
}

I_PLAYER_DIALOG_CITY1_PATH1 = {
    "FR": "Vous êtes dans une ptite ruelle, vous voyez quelques bâtiments par les ouvertures du cache-soleil",
    "EN": "You are in a small alley, you see some buildings through the sunshade openings"
}

I_PLAYER_DIALOG_CITY1_TOOLSMITH = {
    "FR": "Vous êtes devant un magasin d'outillage.",
    "EN": "You are in front of a toolsmith store."
}

I_PLAYER_DIALOG_CITY1_ATLASSTORE = {
    "FR": "Vous êtes devant le magasin Atlas.",
    "EN": "You are in front of the Atlas Store."
}


I_PLAYER_DIALOG_CITY1_EXIT = {
    "FR": "Vous êtes devant la sortie de Shubin.",
    "EN": "You are in front of Shubin's exit."
}


ZONE_I_CRASHSITE = {
    "FR": "Le site du crash",
    "EN": "The crash site"
}

ZONE_I_BASE1 = {
    "FR": "La base abandonnée",
    "EN": "The abandoned base"
}

ZONE_I_DUNES1 = {
    "FR": "Dunes (Est)",
    "EN": "Dunes (Est)"
}

ZONE_I_MINING2 = {
    "FR": "Site de minage 'Kudre Ore'",
    "EN": "'Kudre Ore' mining site"
}

ZONE_I_BLACKBOX1 = {
    "FR": "Emplacement de la boîte noire.",
    "EN": "The blackbox site."
}

ZONE_I_DUNES2 = {
    "FR": "Dunes (Ouest)",
    "EN": "Dunes (West)"
}

ZONE_I_CRASHEDSHIP = {
    "FR": "Le vaisseau écrasé",
    "EN": "The crashed ship"
}

ZONE_I_MINING1 = {
    "FR": "Site de minage 'Shubin'",
    "EN": "'Shubin' mining site"
}

ZONE_I_DUNES3 = {
    "FR": "Dunes (Nord)",
    "EN": "Dunes (North)"
}

ZONE_I_CITY1_GATES = {
    "FR": "Portes d'accès à la ville de Shubin",
    "EN": "Doors to Shubin City"
}

ZONE_I_CITY1_CENTER = {
    "FR": "Centre ville (Shubin)",
    "EN": "City's center (Shubin)"
}

ZONE_I_CITY1_HABS = {
    "FR": "Quartiers d'habitations (Shubin)",
    "EN": "Residential areas (Shubin)"
}

ZONE_I_CITY1_OFFICE = {
    "FR": "Office de tourisme (Shubin)",
    "EN": "Tourism office (Shubin)"
}

ZONE_I_CITY1_TOOLSMITH = {
    "FR": "Magasin d'outillage (Shubin)",
    "EN": "Toolsmith store (Shubin)"
}

ZONE_I_CITY1_ATLAS_STORE = {
    "FR": "Magasin Atlas (Shubin)",
    "EN": "Atlas store (Shubin)"
}

ZONE_I_CITY1_EXIT = {
    "FR": "Sortie de Shubin",
    "EN": "Shubin's exit"
}

ZONE_I_CITY1_PATH1 = {
    "FR": "Petite ruelle (Shubin)",
    "EN": "Small alley (Shubin)"
}

ITEM_I_NAME_BLACKBOX = {
    "FR": "Boîte noire",
    "EN": "Blackbox"
}

ITEM_I_NAME_IDENTITYCARD = {
    "FR": "Carte d'identité",
    "EN": "Identity card"
}

ITEM_I_NAME_TAPEPLAYER = {
    "FR": "Lecteur de cassettes",
    "EN": "Tape player"
}

ITEM_I_NAME_CROWBAR = {
    "FR": "Pied-de-biche",
    "EN": "Crowbar"
}

ITEM_I_NAME_PASSKEY_LEVEL1 = {
    "FR": "Carte d'accès (Niveau 1)",
    "EN": "Passkey (Level 1)"
}