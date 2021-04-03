import os
import json
import discord.utils
import discord
from dotenv import load_dotenv
import sys
from resources.ankith import date_time
from resources.allcommands import *
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_id = 796012940477595689

client = discord.Client()

@client.event
async def on_raw_message_delete(message):
    if str(message.cached_message.author.name) == "$modbot":
        await message.cached_message.channel.send("please stop deleting my messages, you better follow the rules and dont misuse power")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    role = discord.utils.get(message.guild.roles, name="developer")
    await member.add_roles(role)
with open("resources/data.json","r") as JsonFile:
    data = json.load(JsonFile)
all_commands = data["all_commands"]
command_palette = {"$sayhello":sayhello,"$sendch":sendch,"$remove_role":removerole,"$add_role":addrole,"$mute":mute,"$unmute":unmute,"$warn":warn,"$kick":kick,"$help":showhelp,"$rules":rules,"$silence":silence,"$unsilence":unsilence,"$meme":meme}
JsonFile.close()
@client.event
async def on_message(message):
    print(str(message.author)+" on "+str(message.channel)+": "+str(message.content))
    if message.author == client.user:
        return
    await filtermessage(message,client)
    if message.content.split()[0] in all_commands:
        if message.channel.id != 815490707233701893: 
            if "Admin" not in str(message.author.roles) and message.content.split()[0] != "$meme":
                await message.channel.send(str(message.author.mention)+" you cant use that command here.\n goto #bots or #memes")
                return
        if function:=(command_palette.get(message.content.split()[0])):
            await function(message,client)
keep_alive()
client.run(TOKEN)