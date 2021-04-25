import os
import json
import discord.utils
import discord
from dotenv import load_dotenv
import sys
from discord.ext import commands
from resources.ankith import date_time
from resources.allcommands import *
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_id = 796012940477595689

bot = commands.Bot(command_prefix="$")
bot.remove_command('help')
bot.load_extension('resources.allcommands')

@bot.event
async def on_raw_message_delete(message):
    if str(message.cached_message.author.name) == "$modbot":
        await message.cached_message.channel.send("please stop deleting my messages, you better follow the rules and dont misuse power")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    role = discord.utils.get(message.guild.roles, name="developer")
    await member.add_roles(role)

@bot.event
async def on_message(message):
    print(str(message.author)+" on "+str(message.channel)+": "+str(message.content))
    if message.author == bot.user:
        return
    await filtermessage(message,bot)
    await bot.process_commands(message)
    """
    if message.content.split()[0] in all_commands:
        if "Admin" not in str(message.author.roles):
            if message.content.split()[0] == "$meme" and message.channel.id != 809074960890069022:
                embed = discord.Embed(title="Nope.",description=str(message.author.mention)+", you are not allowed to use that command here.\n goto <#809074960890069022>",color=0x0066ff)
                await message.channel.send(embed=embed)
                return
            elif message.content.split()[0] != "$meme" and message.channel.id != 815490707233701893:
                embed = discord.Embed(title="Nope.",description=str(message.author.mention)+", you are not allowed to use that command here.\n goto <#815490707233701893>",color=0x0066ff)
                await message.channel.send(embed=embed)
                return
        if function:=(command_palette.get(message.content.split()[0])):
            await function(message,client)
    """
keep_alive()
bot.run(TOKEN)
