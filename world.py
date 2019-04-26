import strings

# Zone creation model :

# "ZONE_NAME_IN_CAPS": {
# "NAME": "Name of the zone",
# "DIALOGENTRY": strings.DIALOG_ENTRY_FOR_THE_ZONE,
# "NEEDITEM": bool, Need an item to go there,
# "HASITEM": There is an item to pickup in this zone,
# "NORTH"/"SOUTH"/"EAST"/"WEST": "NAME_OF_THE_ZONES_THERE",
# }, ...

WORLD_ITEMS = {
    "BLACKBOX": {
        "NAME": "Boîte noire",
        "EDIBLE": False,
        "TAKEABLE": True,
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_BLACKBOX1
    },

    "CROWBAR": {
        "NAME": "Pied-de-biche",
        "EDIBLE": False,
        "TAKEABLE": True,
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_CROWBAR
    },

    "PASSKEY_LEVEL1": {
        "NAME": "Carte d'accès (Niveau 1)",
        "EDIBLE": False,
        "TAKEABLE": True,
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_PASSKEY_LEVEL1
    }
}



WORLD_ROOMS = {
    "CRASHSITE": {
        "NAME": "Site du crash",
        "DIALOGENTRY": strings.PLAYER_DIALOG_1,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BASE1",
        "SOUTH": None,
        "EAST": "DUNES1",
        "WEST": "DUNES2"
    },

    "BASE1": {
        "NAME": "Base abandonnée",
        "DIALOGENTRY": strings.PLAYER_DIALOG_BASE1,
        "NEEDITEM": None,
        "HASITEM": "CROWBAR",
        "NORTH": "DUNES3",
        "SOUTH": "CRASHSITE",
        "EAST": "DUNES1",
        "WEST": "DUNES2"
    },

    "DUNES1": {
        "NAME": "Dunes (Est)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_DUNES1,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BASE1",
        "SOUTH": None,
        "EAST": "MINING2",
        "WEST": "CRASHSITE",
    },

    "MINING2": {
        "NAME": "Site de minage 'Shubin'",
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_MINING2,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BLACKBOX1",
        "SOUTH": None,
        "EAST": None,
        "WEST": "DUNES1"
    },

    "BLACKBOX1": {
        "NAME": "Emplacement de la boîte noire",
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_SITE_BLACKBOX1,
        "NEEDITEM": None,
        "HASITEM": WORLD_ITEMS["BLACKBOX"],
        "NORTH": None,
        "SOUTH": "MINING2",
        "EAST": None,
        "WEST": None
    },

    "DUNES2": {
        "NAME": "Dunes (Ouest)",
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_DUNES2,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BASE1",
        "SOUTH": None,
        "EAST": "CRASHSITE",
        "WEST": "CRASHEDSHIP"
    },

    "CRASHEDSHIP": {
        "NAME": "Vaisseau écrasé",
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_CRASHEDSHIP,
        "NEEDITEM": WORLD_ITEMS["CROWBAR"],
        "HASITEM": WORLD_ITEMS["PASSKEY_LEVEL1"],
        "NORTH": "MINING1",
        "SOUTH": None,
        "EAST": "DUNES2",
        "WEST": None
    },

    "MINING1": {
        "NAME": "Site de minage 'Kudre'",
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_MINING1,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": None,
        "SOUTH": "CRASHEDSHIP",
        "EAST": "DUNES3",
        "WEST": None
    },

    "DUNES3": {
        "NAME": "Dunes (Nord)",
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_DUNES3,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "CITY1_GATES",
        "SOUTH": "BASE1",
        "EAST": None,
        "WEST": "MINING1"
    },

    "CITY1_GATES": {
        "NAME": "Portes d'accès à Shubin",
        #TODO "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_GATES,
        "NEEDITEM": WORLD_ITEMS["PASSKEY_LEVEL1"],
        "HASITEM": None,
        "NORTH": "CITY1_CENTER",
        "SOUTH": "DUNES3",
        "EAST": None,
        "WEST": None
    }

}
