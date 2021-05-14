import json


class constants:
    with open("bot/utils/data.json") as JsonFile:
        json_data = json.load(JsonFile)
    colours = {"blue": hex("0xFF0000"), "red": hex("0x0066ff")}

    notice_channel_id = json_data["notice_channel"]
    user_roles = json_data["user_roles"]
    guild_id = json_data["guild_id"]
    json_data = json_data
    channels = {"memes": 809074960890069022, "notices": 807532505137545217}
