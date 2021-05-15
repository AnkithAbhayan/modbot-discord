import json


class constants:
    with open("bot/utils/data.json") as JsonFile:
        json_data = json.load(JsonFile)
    colours = {"red": 0xFF0000, "blue": 0x0066FF}

    user_roles = json_data["user_roles"]
    guild_id = json_data["guild_id"]
    json_data = json_data
    channels = {"memes": 809074960890069022, "notices": 807532505137545217, "bot-testing":807239459933782037}
