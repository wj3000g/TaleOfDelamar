import strings

# Zone creation model :
# "ZONE_NAME_IN_CAPS": {
    # "NAME": "Name of the zone",
    # "DIALOGENTRY": strings.DIALOG_ENTRY_FOR_THE_ZONE,
    # "NEEDITEM": bool, does the player need an item to go there, ?
    # "HASITEM": There is an item to pickup in this zone, ?
    # "NORTH"/"SOUTH"/"EAST"/"WEST": "NAME_OF_THE_ZONES_THERE",
# }, ...

# Item creation model :
# "ITEM_NAME_IN_CAPS": {
    # "NAME": "Name of the item",
    # "EDIBLE": bool, can the item be eaten ?
    # "TAKEABLE": bool, can the item be stored in the player's inventory ?
    # "NEEDITEM": "ITEM_NAME" or None, does the item requires another to be used ?
    # "DIALOGENTRY": string.DIALOG_ENTRY_FOR_THE_ITEM
# }, ...


WORLD_ITEMS = {
    "BLACKBOX": {
        "ID": "BLACKBOX",
        "NAME": "Boîte noire",
        "NEEDITEM": "TAPE_PLAYER",
        "DIALOGENTRY": strings.I_PLAYER_DIALOG_BLACKBOX1
    },

    "IDENTITYCARD": {
        "ID": "IDENTITYCARD",
        "NAME": "Carte d'identité",
        "NEEDITEM": None,
        "DIALOGENTRY": strings.I_PLAYER_DIALOG_IDENTITYCARD
    },

    "TAPE_PLAYER": {
        "ID": "TAPE_PLAYER",
        "NAME": "Lecteur de cassettes",
        "NEEDITEM": None,
        "DIALOGENTRY": strings.I_PLAYER_DIALOG_TAPE_PLAYER
    },

    "CROWBAR": {
        "ID": "CROWBAR",
        "NAME": "Pied-de-biche",
        "NEEDITEM": None,
        "DIALOGENTRY": strings.I_PLAYER_DIALOG_CROWBAR
    },

    "PASSKEY_LEVEL1": {
        "ID": "PASSKEY_LEVEL1",
        "NAME": "Carte d'accès (Niveau 1)",
        "NEEDITEM": None,
        "DIALOGENTRY": strings.I_PLAYER_DIALOG_PASSKEY_LEVEL1
    }
}



WORLD_ROOMS = {
    "CRASHSITE": {
        "NAME": strings.ZONE_I_CRASHSITE,
        "DIALOGENTRY": strings.I_PLAYER_DIALOG_1,
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
        "DIALOGENTRY": strings.PLAYER_DIALOG_MINING2,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BLACKBOX1",
        "SOUTH": None,
        "EAST": None,
        "WEST": "DUNES1"
    },

    "BLACKBOX1": {
        "NAME": "Emplacement de la boîte noire",
        "DIALOGENTRY": strings.PLAYER_DIALOG_SITE_BLACKBOX1,
        "NEEDITEM": None,
        "HASITEM": "BLACKBOX",
        "NORTH": None,
        "SOUTH": "MINING2",
        "EAST": None,
        "WEST": None
    },

    "DUNES2": {
        "NAME": "Dunes (Ouest)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_DUNES2,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BASE1",
        "SOUTH": None,
        "EAST": "CRASHSITE",
        "WEST": "CRASHEDSHIP"
    },

    "CRASHEDSHIP": {
        "NAME": "Vaisseau écrasé",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CRASHEDSHIP,
        "NEEDITEM": "CROWBAR",
        "HASITEM": "PASSKEY_LEVEL1",
        "NORTH": "MINING1",
        "SOUTH": None,
        "EAST": "DUNES2",
        "WEST": None
    },

    "MINING1": {
        "NAME": "Site de minage 'Kudre'",
        "DIALOGENTRY": strings.PLAYER_DIALOG_MINING1,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": None,
        "SOUTH": "CRASHEDSHIP",
        "EAST": "DUNES3",
        "WEST": None
    },

    "DUNES3": {
        "NAME": "Dunes (Nord)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_DUNES3,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "CITY1_GATES",
        "SOUTH": "BASE1",
        "EAST": None,
        "WEST": "MINING1"
    },

    "CITY1_GATES": {
        "NAME": "Portes d'accès à Shubin",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_GATES,
        "NEEDITEM": "PASSKEY_LEVEL1",              
        "HASITEM": None,
        "NORTH": "CITY1_CENTER",
        "SOUTH": "DUNES3",
        "EAST": None,
        "WEST": None
    },

    "CITY1_CENTER": {
        "NAME": "Centre ville (Shubin)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_CENTER,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "CITY1_PATH1",
        "SOUTH": "CITY1_GATES",
        "EAST": "CITY1_HABS",
        "WEST": "CITY1_ATLAS_STORE",
    },

    "CITY1_HABS": {
        "NAME": "Quartier d'habitations (Shubin)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_HABS,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "CITY1_OFFICE",
        "SOUTH": None,
        "EAST": None,
        "WEST": "CITY1_CENTER"
    },
    
    "CITY1_OFFICE": {
        "NAME": "Bureau d'administration (Shubin)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_OFFICE,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "CITY1_EXIT",
        "SOUTH": "CITY1_HABS",
        "EAST": None,
        "WEST": "CITY1_PATH1"
    },

    "CITY1_PATH1": {
        "NAME": "Intersection nord (Shubin)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_PATH1,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "CITY1_EXIT",
        "SOUTH": "CITY1_CENTER",
        "EAST": "CITY1_OFFICE",
        "WEST": "CITY1_TOOLSMITH"
    },

    "CITY1_TOOLSMITH": {
        "NAME": "Atelier d'outillage (Shubin)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_TOOLSMITH,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "CITY1_EXIT",
        "SOUTH": "CITY1_ATLAS_STORE",
        "EAST": "CITY1_PATH1",
        "WEST": None
    },

    "CITY1_ATLAS_STORE": {
        "NAME": "Magasin 'Atlas Store'",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_ATLASSTORE,
        "NEEDITEM": None,
        "HASITEM": WORLD_ITEMS["TAPE_PLAYER"],
        "NORTH": "CITY1_TOOLSMITH",
        "SOUTH": None,
        "EAST": "CITY1_CENTER",
        "WEST": None
    },

    "CITY1_EXIT": {
        "NAME": "Sortie de la ville (Shubin)",
        "DIALOGENTRY": strings.PLAYER_DIALOG_CITY1_EXIT,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": None,
        "SOUTH": "CITY1_PATH1",
        "EAST": "CITY1_OFFICE",
        "WEST": "CITY1_TOOLSMITH"
    }

}
