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
        await channel.send("notice:\n"+str(user.name)+" has been kicked by "+str(message.author)+"\nchannel: "+str(message.channel)+"\nreason: "+" ".join(array[2:len(array)]))
        await user.create_dm()
        await user.dm_channel.send("bruv you just got kicked from teen programming by "+str(message.author)+"\n reason was: "+" ".join(array[2:len(array)]))
    else:
        await message.channel.send(str(message.author.mention)+" you are not allowed to use that command")

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
    if "Admin" in str(message.author.roles) or "ankith101.rar" in str(user.name):
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
    all_commands = ["$sayhello","$sendch","$kick","$remove_role","$add_role","$kick","$mute","$unmute","$help","$rules"]
    all_commands_false = ["sayhello","sendch","kick","remove_role","add_role","kick","mute","unmute","help","rules"]
    helpinfo = {
        "$help":"usage: `$help` or `$help <specific_command>`\n*former shows all commands and info. latter shows info about specific command*",
        "$sayhello":"usage: `$sayhello`\n*sends a message 'hello' with a ping*.",
        "$sendch":"usage: `$sench <channel_id> <message>`\n*sends the message to the specific channel.*",
        "$kick":"usage: `$kick <user_id> <reason_for_kick>`\n*kicks the user from the server.*",
        "$add_role":"usage: `$add_role <role_name> <user_id>`\n*adds a role to a person*",
        "$remove_role":"usage: `$remove_role <role_name> <user_id>`\n*removes a role from a person*",
        "$mute":"usage: `$mute <user_id>`\n*mutes a person (they cant send messages)*",
        "$unmute":"usage: `$unmute <user_id>`\n*unmutes a person (they are now allowed to send messages)*",
        "$rules":"usage: `$rules` or `$rules <rule_no>`\n*prints all the rules or individually*"
    }
    if len(message.content.split()) == 1:
        embed=discord.Embed(title="$modbot", description="$modbot is a bot for moderators made by the developer team at 'teen programming' here are all commands:", color=0x0066ff)
        for key,value in helpinfo.items():
            embed.add_field(name=key, value=value,inline=False)
        await message.channel.send(embed=embed)
    else:
        command = message.content.split()[1]
        if command in all_commands:
            embed=discord.Embed(title=command,description=helpinfo[command],color=0x0066ff)
            embed.set_footer(text="Developed by Ankith101.rar")
            await message.channel.send(embed=embed)
        elif command in all_commands_false:
            embed=discord.Embed(title="$"+command,description=helpinfo["$"+command],color=0x0066ff)
            embed.set_footer(text="Developed by Ankith101.rar")
            await message.channel.send(embed=embed)
        else:
            if command[0] == "$":
                embed=discord.Embed(title="Unknown command: `"+str(command)+"`",description="idk what you typed, check the spelling",color=0x0066ff)
                await message.channel.send(embed=embed)

async def rules(message):
    string = [
        "Be nice to one another, respect each other's opinions",
        "Don't send hateful messages",
        "No nsfw or inappropriate messages should be sent",
        "If anyone encounters any issue, Ping the @Admin they will address the issue",
        "No spamming please or pinging of @everyone",
        "No racist or homophobic messages, photos ,videos etc",
        "This is an English speaking server so speak in English to the best of your ability",
        "Bot commands must be used only in #bots",
        "People who do not abide with these rules will be banned or muted from the server"
        ]
    array = message.content.split()
    if len(array) == 1:
        embed=discord.Embed(title="Rules of the server:",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",description="everyone is supposed to follow these:",color=0x0066ff)
        for i in range(len(string)):
            embed.add_field(name="**#"+str(i+1)+"**",value=string[i],inline=True)
        embed.set_footer(text="Developed by Ankith101.rar")
        await message.channel.send(embed=embed)
    elif len(array) == 2:
        if int(array[1]) <= len(string) and int(array[1]) >= 1:
            embed=discord.Embed(title="Rules",description="**#"+str(array[1])+".** "+string[int(array[1])-1],color=0x0066ff)
            embed.set_footer(text="Developed by Ankith101.rar")
            await message.channel.send(embed=embed)