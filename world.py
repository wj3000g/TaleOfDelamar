import strings

# Modèle de création de zones :

# "NOM_DE_ZONE": {
# DESC: Description de la zone,
# DIALOGENTRY: Entrée dialogue si look() (strings.DIALOG_ENTRY),
# NEEDITEM: Item requis pour accéder à la zone ,
# HASITEM: Item disponible dans la zone (affiché si look()),
# NORTH/SOUTH/EAST/WEST: Nom des zones correspondantes à ces directions,
# }, ...

WORLD_ITEMS = {
    "BLACKBOX": {
        "NAME": "Boîte noire",
        "EDIBLE": False,
        "TAKEABLE": True,
        "DIALOGENTRY": strings.PLAYER_DIALOG_BLACKBOX1
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
        "HASITEM": WORLD_ITEMS["BLACKBOX"],
        "NORTH": None,
        "SOUTH": "MINING2",
        "EAST": None,
        "WEST": None
    },

    "DUNES2": {
        "NAME":
    }

}
