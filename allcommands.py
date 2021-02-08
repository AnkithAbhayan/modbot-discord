import discord
import discord.utils
from ankith import date_time
async def pingedunnecessary(message,client):
    await message.channel.send(str(message.author.mention)+" please dont try to ping everyone")
    channel = client.get_channel(807532505137545217) 
    await channel.send("notice:\n"+str(message.author.mention)+" has tried to ping everyone \n channel: `"+str(message.channel)+"`\n full message: `"+str(message.content)+"`\n time: `"+str(date_time.date())+" "+str(date_time.time())+"`")

async def sendch(message,client):
    if "Admin" in str(message.author.roles):
        array = message.content.split()
        channel = client.get_channel(int(array[1]))
        await channel.send(' '.join(array[2:len(array)]))

async def kick(message,client):
    array = message.content.split()
    if "Admin" in str(message.author.roles):
        user = await message.guild.fetch_member(int(array[1]))
        name = user.name
        await user.kick()
        await message.channel.send(str(name)+" has been kicked from the server")
        channel = client.get_channel(807532505137545217) 
        await channel.send("notice:\n"+str(member.name)+" has been kicked by "+str(message.author)+"\nchannel: "+str(message.channel)+"\nreason: "+" ".join(array[2:len(array)]))
        await user.create_dm()
        await user.dm_channel.send("bruv you just got kicked from teen programming by "+str(message.author)+"\n reason was: "+" ".join(array[2:len(array)]))

async def removerole(message):
    array = message.content.split()
    if "Admin" in str(message.author.roles):
        user = await message.guild.fetch_member(int(array[2]))
        role = discord.utils.get(message.guild.roles, name=array[1])
        if array[1] not in str(user.roles):
            await message.channel.send(str(user.name)+" doesnt even have the "+str(role.name)+" role in the first place")
        else:
            await user.remove_roles(role)
            await message.channel.send(str(user.mention)+" has been deprived of the "+str(role.name)+" role")
    else:
        await message.channel.send(str(message.author.mention)+" you are not allowed to use that command")

async def addrole(message):
    array = message.content.split()
    if "Admin" in str(message.author.roles):
        user = await message.guild.fetch_member(int(array[2]))
        role = discord.utils.get(message.guild.roles, name=array[1])
        if array[1] in str(user.roles):
            await message.channel.send(str(user.name)+" already has the "+str(role.name)+" role")
        else:
            await message.author.add_roles(role)
            await message.channel.send(str(user.mention)+" has been given the "+str(role.name)+" role")
    else:
        await message.channel.send(str(message.author.mention)+" you are not allowed to use that command")

async def mute(message,client):
    if "Admin" in str(message.author.roles):
        array = message.content.split()
        member = await message.guild.fetch_member(int(array[1]))
        role = discord.utils.get(message.guild.roles, name='muted')
        await member.add_roles(role)
        await message.channel.send(str(member.mention)+" has been muted by "+str(message.author)+"\n reason: `"+" ".join(array[2:len(array)])+"`")
        await member.create_dm()
        await member.dm_channel.send("bro you just got muted by "+str(message.author)+"\n reason was: "+" ".join(array[2:len(array)]))
        channel = client.get_channel(807532505137545217) 
        await channel.send("notice:\n"+str(member.name)+" has been muted by "+str(message.author)+"\nchannel: "+str(message.channel)+"\nreason: "+" ".join(array[2:len(array)]))
    else:
        await message.channel.send(str(message.author.mention)+" you are not allowed to use that command")

async def unmute(message,client):
    if "Admin" in str(message.author.roles):
        array = message.content.split()
        user = await message.guild.fetch_member(int(array[1]))
        role = discord.utils.get(message.guild.roles, name='muted')
        await user.remove_roles(role)
        await message.channel.send(str(user.mention)+" has been unmuted by "+str(message.author))
        await user.create_dm()
        await user.dm_channel.send("ok you got unmuted by "+str(message.author)+"\nyou are allowed to send messages now")
    else:
        await message.channel.send(str(message.author.mention)+" you are not allowed to use that command")

async def filtermessage(message,client):
    if "@everyone" in message.content:
        await pingedunnecessary(message,client)
    for item in ["fuck","bitch","cumshot","asshole","wtf"]:
        if item in message.content:
            if "Admin" in str(message.author.roles):
                pass
            else:
                await message.delete()
                await message.channel.send(str(message.author.mention)+" please dont use bad words in this server")
                channel = client.get_channel(807532505137545217) 
                await channel.send("notice:\n"+str(message.author)+" sent a bad word in this server\n textchannel: "+str(message.chanel)+"\n full message: "+str(message.content))

async def showhelp(message):
    embed=discord.Embed(title="$modbot", description="$modbot is a bot for moderators made by the developer team at 'teen programming' here are all commands:", color=0x0066ff)
    embed.add_field(name="$sayhello", value="usage: `$sayhello`\n*sends a message 'hello' with a ping*." , inline=False)
    embed.add_field(name="$sench", value="usage: `$sench <channel_id> <message>`\n*sends the message to the specific channel.*\n", inline=False)
    embed.add_field(name="$kick", value="usage: `$kick <user_id> <reason_for_kick>`\n*kicks the user from the server.*", inline=False)
    embed.add_field(name="$add_role", value="usage: `$add_role <role_name> <user_id>`\n*adds a role to a person*",inline=False)
    embed.add_field(name="$remove_role", value="usage: `$remove_role <role_name> <user_id>`\n*removes a role from a person*",inline=False)
    embed.add_field(name="$mute", value="usage: `$mute <user_id>`\n*mutes a person (they cant send messages)*", inline=False)
    embed.add_field(name="$unmute", value="usage: `$unmute <user_id>`\n*unmutes a person (they are now allowed to send messages*", inline=False)
    await message.channel.send(embed=embed)
