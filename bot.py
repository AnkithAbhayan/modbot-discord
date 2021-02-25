import os
import json
import discord.utils
import discord
from dotenv import load_dotenv
import sys
from resources.allcommands import *
from resources.ankith import date_time
from resources.ankith import cryptography

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
JsonFile.close()
@client.event
async def on_message(message):
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
        elif message.content.split()[0] == "$rules":
            await rules(message)
        elif message.content.split()[0] == "$silence":
            await silence(message)
        elif message.content.split()[0] == "$unsilence":
            await unsilence(message)
        elif message.content.split()[0] == "$warn":
            await warn(message,client)
client.run(TOKEN)