import strings

# Modèle de création de zones :

# DESC: Description de la zone
# DIALOGENTRY: Entrée dialogue si look() (strings.DIALOG_ENTRY)
# NEEDITEM: Item requis pour accéder à la zone 
# HASITEM: Item disponible dans la zone (affiché si look())
# NORTH/SOUTH/EAST/WEST: Nom des zones correspondantes à ces directions


WORLD_ROOMS = {
    "CRASHSITE": {
        "DESC": "Le site du crash, ça sent le brûlé...",
        "DIALOGENTRY": strings.PLAYER_DIALOG_1,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BASE1",
        "SOUTH": None,
        "EAST": "DUNES1",
        "WEST": "DUNES2"
    },

    "BASE1": {
        "DESC": "La base détruite",
        "DIALOGENTRY": strings.PLAYER_DIALOG_BASE1,
        "NEEDITEM": None,
        "HASITEM": "CROWBAR",
        "NORTH": "DUNES3",
        "SOUTH": "CRASHSITE",
        "EAST": "DUNES1",
        "WEST": "DUNES2"
    }

    "DUNES1": {
        "DESC": "Des dunes de sable orangées à perte de vue",
        "DIALOGENTRY": strings.PLAYER_DIALOG_DUNES1,
        "NEEDITEM": None,
        "HASITEM": None,
        "NORTH": "BASE1",
        "SOUTH": 
    }

}
