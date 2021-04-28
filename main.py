import os
import json
import discord.utils
import discord
from dotenv import load_dotenv
import sys
from discord.ext import commands
from resources.ankith import date_time
from resources.allcommands import Moderation_toolkit,self_assign_roles
from resources.filters import filters
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_id = 796012940477595689

bot = commands.Bot(command_prefix="$")
bot.remove_command('help')
bot.add_cog(Moderation_toolkit(bot))
bot.add_cog(self_assign_roles(bot))

@bot.event
async def on_raw_message_delete(message):
    if str(message.cached_message.author.name) == "$modbot":
        await message.cached_message.channel.send("please stop deleting my messages, you better follow the rules and dont misuse power")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    print(str(message.author)+" on "+str(message.channel)+": "+str(message.content))
    if message.author == bot.user:
        return
    await filters.filtermessage(message,bot)
    await bot.process_commands(message)
keep_alive()
bot.run(TOKEN)
