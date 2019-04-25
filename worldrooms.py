import strings

WORLD_ROOMS = {
    "CRASHSITE": {
        "DESC": "Le site du crash, ça sent le brûlé...",
        "DIALOGENTRY": strings.PLAYER_DIALOG_1,
        "NEEDITEM": None,
        "NORTH": "BASE1",
        "SOUTH": None,
        "EAST": "DUNES1",
        "WEST": "DUNES2"
    },
    "BASE1": {
        "DESC": "La base détruite",
        "DIALOGENTRY": strings.PLAYER_DIALOG_BASE1,
        "NEEDITEM": None,
        "NORTH": "DUNES3",
        "SOUTH": "CRASHSITE",
        "EAST": "DUNES1",
        "WEST": "DUNES2"
    }
}
