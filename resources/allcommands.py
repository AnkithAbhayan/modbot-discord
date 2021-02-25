import discord
import json
import discord.utils
from ankith import date_time
with open("resources/data.json","r") as JsonFile:
    data = json.load(JsonFile)
notice_channel_id = data["notice_channel"]
print(notice_channel_id)
JsonFile.close()
async def pingedunnecessary(message,client):
    embed=discord.Embed(title="Dont do it",description=str(message.author.mention)+" please dont try to ping everyone",color=0x0066ff)
    await message.channel.send(embed=embed)
    channel = client.get_channel(notice_channel_id)
    embed=discord.Embed(title="Notice: **Pinged Everyone**",description="**"+str(message.author.mention)+"** has tried to ping everyone \n **channel**: "+str(message.channel)+"\n **full message**: "+str(message.content)+"\n **time**: "+str(date_time.date())+" "+str(date_time.time()),color=0x0066ff) 
    await channel.send(embed=embed)

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
        #sending to initial channel
        embed=discord.Embed(title="Kicked.",description=str(name)+" has been kicked from the server",color=0x0066ff)
        await message.channel.send(embed=embed)
        #sending to #notices
        channel = client.get_channel(notice_channel_id) 
        embed=discord.Embed(title="Notice: **Kick**",description=str(user.name)+" has been kicked by "+str(message.author)+"\nchannel: "+str(message.channel)+"\nreason: "+" ".join(array[2:len(array)])+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff)
        await channel.send(embed=embed)
        await user.create_dm()
        embed=discord.Embed(title="Infraction: Kick",description="you just got kicked from "+str(message.guild)+" by "+str(message.author)+"\n reason was: "+" ".join(array[2:len(array)]),color=0x0066ff)
        await user.dm_channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)

async def removerole(message):
    array = message.content.split()
    if "Admin" in str(message.author.roles):
        user = await message.guild.fetch_member(int(array[2]))
        role = discord.utils.get(message.guild.roles, name=array[1])
        if array[1] not in str(user.roles):
            embed=discord.Embed(title="Doesnt have the role",description=str(user.name)+" doesnt even have the `"+str(role.name)+"` role in the first place",color=0x0066ff)
            await message.channel.send(embed=embed)
        else:
            await user.remove_roles(role)
            embed=discord.Embed(title="Role has been removed",description="`"+str(role.name)+"` role has been removed from "+str(user.mention),color=0x0066ff)
            await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)

async def addrole(message):
    array = message.content.split()
    if "Admin" in str(message.author.roles):
        user = await message.guild.fetch_member(int(array[2]))
        role = discord.utils.get(message.guild.roles, name=array[1])
        if array[1] in str(user.roles):
            embed=discord.Embed(title="Already has the role",description=str(user.name)+" already has the "+str(role.name)+" role",color=0x0066ff)
            await message.channel.send(embed=embed)
        else:
            await user.add_roles(role)
            embed=discord.Embed(title="Role has been added",description=str(user.mention)+" has been given the "+str(role.name)+" role",color=0x0066ff)
            await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)

async def mute(message,client):
    if "Admin" in str(message.author.roles):
        array = message.content.split()
        member = await message.guild.fetch_member(int(array[1]))
        role = discord.utils.get(message.guild.roles, name='muted')
        reason = " ".join(array[2:len(array)])
        await member.add_roles(role)
        #sending message to initial channel
        embed=discord.Embed(title="Muted",description=str(member.mention)+" has been muted by "+str(message.author)+"\n**reason**: "+reason,color=0x0066ff)
        await message.channel.send(embed=embed)
        #sending message to dm
        await member.create_dm()
        embed=discord.Embed(title="Infraction: Mute",description="you have been muted by "+str(message.author)+"\n**reason**: "+reason,color=0x0066ff)
        await member.dm_channel.send(embed=embed)
        #sending message to #notices
        channel = client.get_channel(notice_channel_id)
        embed=discord.Embed(title="Notice: **Mute**",description="**"+str(member.name)+"** has been muted by "+str(message.author)+"\n**reason**: "+reason+"\n**channel**: "+str(message.channel)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)

async def unmute(message,client):
    if "Admin" in str(message.author.roles):
        array = message.content.split()
        user = await message.guild.fetch_member(int(array[1]))
        role = discord.utils.get(message.guild.roles, name='muted')
        await user.remove_roles(role)
        embed=discord.Embed(title="Unmuted",description=str(user.name)+" has been unmuted.",color=0x0066ff)
        await message.channel.send(embed=embed)
        await user.create_dm()
        embed=discord.Embed(title="Unmuted",description=str(user.name)+", you are now allowed to send messages in "+str(message.guild),color=0x0066ff)
        await user.dm_channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)

async def filtermessage(message,client):
    if "@everyone" in message.content:
        await pingedunnecessary(message,client)
    for item in ["fuck","bitch","cumshot","asshole","wtf","retard"]:
        if item in message.content:
            if "Admin" in str(message.author.roles):
                pass
            else:
                await message.delete()
                embed=discord.Embed(title="Curse word detected:",description=str(message.author.mention)+" please dont use bad words in this server",color=0x0066ff)
                await message.channel.send(embed=embed)
                channel = client.get_channel(notice_channel_id)
                embed=discord.Embed(title="Notice: **language breach**",description="**"+str(message.author)+"** sent a bad word in this server\n **textchannel**: "+str(message.channel)+"\n **full message**: "+str(message.content)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff) 
                await channel.send(embed=embed)

async def showhelp(message):
    with open("resources/data.json","r") as JsonFile:
        data = json.load(JsonFile)
    all_commands = data["all_commands"]
    all_commands_false = data["all_commands_false"]
    helpinfo = data["helpinfo"]
    JsonFile.close()
    if len(message.content.split()) == 1:
        embed=discord.Embed(title="$modbot", description="$modbot is a bot for moderators made by the developer team at "+str(message.guild)+" here are all commands:", color=0x0066ff)
        for key,value in helpinfo.items():
            embed.add_field(name=key, value=value,inline=False)
        embed.set_footer(text="developed by ankith101.rar")
        await message.channel.send(embed=embed)
    else:
        command = message.content.split()[1]
        if command in all_commands:
            embed=discord.Embed(title=command,description=helpinfo[command],color=0x0066ff)
            embed.set_footer(text="developed by ankith101.rar")
            await message.channel.send(embed=embed)
        elif command in all_commands_false:
            embed=discord.Embed(title="$"+command,description=helpinfo["$"+command],color=0x0066ff)
            embed.set_footer(text="developed by ankith101.rar")
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Unknown command: `"+str(command)+"`",description="idk what you typed, check the spelling",color=0x0066ff)
            await message.channel.send(embed=embed)

async def rules(message):
    with open("resources/data.json","r") as JsonFile:
        data = json.load(JsonFile)
    string = data["rules"]
    JsonFile.close()
    array = message.content.split()
    if len(array) == 1:
        embed=discord.Embed(title="Rules of the server:",url="https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html",description="You can get a copy of the server rules from our website\n [click here](https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html) to view the rules",color=0x0066ff)
        embed.set_footer(text="website by Aadi, bot developed by Ankith101")
        await message.channel.send(embed=embed)
    elif len(array) == 2:
        if int(array[1]) <= len(string) and int(array[1]) >= 1:
            embed=discord.Embed(title="Rules",description="**#"+str(array[1])+".** "+string[int(array[1])-1],color=0x0066ff)

            await message.channel.send(embed=embed)

async def silence(message):
    if "Admin" in str(message.author.roles):
        role = discord.utils.get(message.guild.roles, name="developer")
        await message.channel.set_permissions(role, send_messages=False)
        embed=discord.Embed(title="Silenced",description="`"+str(message.channel)+"` has been silenced by "+str(message.author),color=0x0066ff)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)

async def unsilence(message):
    if "Admin" in str(message.author.roles):
        role = discord.utils.get(message.guild.roles, name="developer")
        await message.channel.set_permissions(role, send_messages=True)
        embed=discord.Embed(title="Unsilenced",description="`"+str(message.channel)+"` has been unsilenced by "+str(message.author),color=0x0066ff)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)
async def warn(message,client):
    if "Admin" in str(message.author.roles):
        array = message.content.split()
        user_id = array[1]
        reason = " ".join(array[2:len(array)])
        user = await message.guild.fetch_member(int(array[1]))
        #sending to initial channel
        embed=discord.Embed(title="Warning",description="applied warning to "+str(user.name)+"\n**reason**: "+reason,color=0x0066ff)
        await message.channel.send(embed=embed)
        await message.channel.send(str(user.mention))
        #sending to dms
        await user.create_dm()
        embed=discord.Embed(title="Infraction: **Warning**",description="you have been warned by "+str(message.author)+"\n**reason**: "+reason,color=0x0066ff)
        await user.dm_channel.send(embed=embed)
        #sending to #notices
        channel = client.get_channel(notice_channel_id)
        embed=discord.Embed(title="Notice: **Warning**",description="**"+str(user.name)+"** has been warned by "+str(message.author)+"\n**reason**: "+reason+"\n**channel**: "+str(message.channel)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(message.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await message.channel.send(embed=embed)
