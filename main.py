import os
import json
import sys

import discord.utils
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot.ankith import date_time

from bot.exts.moderation_toolkit import Moderation_toolkit
from bot.exts.self_assign_roles import self_assign_roles
from bot.exts.fun import Fun

from bot.filters import filters
from keep_alive import keep_alive
from bot.constants import constants

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
with open("bot/data.json") as JsonFile:
    json_data = json.load(JsonFile)

bot = commands.Bot(command_prefix="$")
bot.remove_command("help")
bot.add_cog(Fun(bot))
bot.add_cog(Moderation_toolkit(bot))
bot.add_cog(self_assign_roles(bot))


@bot.event
async def on_raw_message_delete(message):
    if str(message.cached_message.author.name) == "$modbot":
        await message.cached_message.channel.send(
            "please stop deleting my messages, you better follow the rules and dont misuse power"
        )


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_message(message):
    print(f"{message.author} on {message.channel}: {message.content}")
    if message.author == bot.user:
        return
    await filters.filtermessage(message, bot)
    await bot.process_commands(message)


keep_alive()
bot.run(TOKEN)
