import os
import json
import discord.utils
import discord
from dotenv import load_dotenv
import sys
from allcommands import *
from ankith import date_time
with open("file.json","r") as JsonFile:
    data = json.load(JsonFile)

def savetojson(message,channel,author,data):
    if channel not in data["all_channels"]:
        data["channels"].update({channel:[]})
        data["all_channels"].append(channel)
    data["channels"][channel].append({"message":message,"author":author})
    with open("file.json","w") as JsonFile:
        json.dump(data,JsonFile,indent=4)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_id = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
all_commands = ["$sayhello","$sendch","$kick","$remove_role","$add_role","$kick","$mute","$unmute","$help"]
@client.event
async def on_message(message):
    savetojson(str(message.content),str(message.channel),str(message.author),data)
    print(str(message.author)+" on "+str(message.channel)+": "+str(message.content))
    if message.author == client.user:
        return
    await filtermessage(message,client)
    if message.channel.id == 807532505137545217:
        await message.delete()
    if message.content.split()[0] in all_commands:
        if message.channel.id != 796562613412560936 and "Admin" not in str(message.author.roles):
            await message.channel.send(str(message.author.mention)+" you cant use that command here.\n goto #bots")
            return
        if message.content == '$sayhello':
            await message.channel.send("hello! "+str(message.author.mention))
        elif message.content.split()[0] == "$sendch":
            await sendch(message,client)
        elif message.content.split()[0] == "$kick":
            await kick(message,client)
        elif message.content.split()[0] == "$remove_role":
            await removerole(message)
        elif message.content.split()[0] == "$add_role":            
            await addrole(message)
        elif message.content.split()[0] == "$mute":
            await mute(message,client)
        elif message.content.split()[0] == "$unmute":
            await unmute(message,client)
        elif message.content.split()[0] == "$help":
            await showhelp(message)
client.run(TOKEN)