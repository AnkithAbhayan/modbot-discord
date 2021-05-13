import json


class constants:
    with open("bot/data.json") as JsonFile:
        json_data = json.load(JsonFile)
    standard_colour = hex(json_data["standard_colour"])
    error_colour = hex(json_data["error_colour"])
    notice_channel_id = json_data["notice_channel"]
    user_roles = json_data["user_roles"]
    guild_id = json_data["guild_id"]
    json_data = json_data
