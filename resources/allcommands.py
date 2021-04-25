import discord
import praw
import json
import discord.utils
from dotenv import load_dotenv
from discord.ext import commands
import os
from resources.ankith import date_time
load_dotenv()
my_bot_id = os.getenv("CLIENT_ID")
my_bot_secret = os.getenv("CLIENT_SECRET")
my_user_agent = os.getenv("USER_AGENT")
with open("resources/data.json","r") as JsonFile:
    data = json.load(JsonFile)
notice_channel_id = data["notice_channel"]
JsonFile.close()

@commands.command(name='sayhello')
async def sayhello(ctx,*args):
    await ctx.channel.send(f"Hello there!, {ctx.author.mention}")

async def pingedunnecessary(client,message):
    if not message.author.has_role("Owner"):
        embed=discord.Embed(title="Dont do it",description=str(ctx.author.mention)+" please dont try to ping everyone",color=0x0066ff)
        await message.channel.send(embed=embed)
        channel = client.get_channel(notice_channel_id)
        embed=discord.Embed(title="Notice: **Pinged Everyone**",description="**"+str(message.author.mention)+"** has tried to ping everyone \n **channel**: "+str(message.channel)+"\n **full ctx**: "+str(message.content)+"\n **time**: "+str(date_time.date())+" "+str(date_time.time()),color=0x0066ff) 
        await channel.send(embed=embed)

@commands.command(name='sendch')
async def sendch(ctx,*args):
    if "Admin" in str(ctx.author.roles):
        array = ctx.content.split()
        channel = ctx.get_channel(int(array[1]))
        await channel.send(' '.join(array[2:len(array)]))

@commands.command(name='kick')
async def kick(ctx,*args):
    array = ctx.content.split()
    if "Admin" in str(ctx.author.roles):
        victim = array[1]
        if '<@!' in victim:
            victim = re.search('\d+',victim).group()
        user = await ctx.guild.fetch_member(victim)
        name = user.name
        await user.kick()
        #sending to initial channel
        embed=discord.Embed(title="Kicked.",description=str(name)+" has been kicked from the server",color=0x0066ff)
        await ctx.channel.send(embed=embed)
        #sending to #notices
        channel = bot.get_channel(notice_channel_id) 
        embed=discord.Embed(title="Notice: **Kick**",description=str(user.name)+" has been kicked by "+str(ctx.author)+"\nchannel: "+str(ctx.channel)+"\nreason: "+" ".join(array[2:len(array)])+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff)
        await channel.send(embed=embed)
        await user.create_dm()
        embed=discord.Embed(title="Infraction: Kick",description="you just got kicked from "+str(ctx.guild)+" by "+str(ctx.author)+"\n reason was: "+" ".join(array[2:len(array)]),color=0x0066ff)
        await user.dm_channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

@commands.command(name='remove_role')
async def remove_role(ctx,*args):
    array = ctx.content.split()
    if "Owner" in str(ctx.author.roles):
        user = await ctx.guild.fetch_member(int(array[2]))
        role = discord.utils.get(ctx.guild.roles, name=array[1])
        if array[1] not in str(user.roles):
            embed=discord.Embed(title="Doesnt have the role",description=str(user.name)+" doesnt even have the `"+str(role.name)+"` role in the first place",color=0x0066ff)
            await ctx.channel.send(embed=embed)
        else:
            await user.remove_roles(role)
            embed=discord.Embed(title="Role has been removed",description="`"+str(role.name)+"` role has been removed from "+str(user.mention),color=0x0066ff)
            await ctx.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

@commands.command(name='add_role')
async def add_role(ctx,*args):
    array = ctx.content.split()
    if "Owner" in str(ctx.author.roles):
        user = await ctx.guild.fetch_member(int(array[2]))
        role = discord.utils.get(ctx.guild.roles, name=array[1])
        if array[1] in str(user.roles):
            embed=discord.Embed(title="Already has the role",description=str(user.name)+" already has the `"+str(role.name)+"` role",color=0x0066ff)
            await ctx.channel.send(embed=embed)
        else:
            await user.add_roles(role)
            embed=discord.Embed(title="Role has been added",description=str(user.mention)+" has been given the `"+str(role.name)+"` role",color=0x0066ff)
            await ctx.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

@commands.command(name='mute')
async def mute(ctx,*args):
    if "Admin" in str(ctx.author.roles):
        array = ctx.content.split()
        victim = array[1]
        if '<@!' in victim:
            victim = re.search('\d+',victim).group()
        member = await ctx.guild.fetch_member(victim)
        role = discord.utils.get(ctx.guild.roles, name='muted')
        reason = " ".join(array[2:len(array)])
        await member.add_roles(role)
        #sending ctx to initial channel
        embed=discord.Embed(title="Muted",description=str(member.mention)+" has been muted by "+str(ctx.author)+"\n**reason**: "+reason,color=0x0066ff)
        await ctx.channel.send(embed=embed)
        #sending ctx to dm
        await member.create_dm()
        embed=discord.Embedi(title="Infraction: Mute",description="you have been muted by "+str(ctx.author)+"\n**reason**: "+reason,color=0x0066ff)
        await member.dm_channel.send(embed=embed)
        #sending ctx to #notices
        channel = bot.get_channel(notice_channel_id)
        embed=discord.Embed(title="Notice: **Mute**",description="**"+str(member.name)+"** has been muted by "+str(ctx.author)+"\n**reason**: "+reason+"\n**channel**: "+str(ctx.channel)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

@commands.command(name='unmute')
async def unmute(ctx,*args):
    if "Admin" in str(ctx.author.roles):
        array = ctx.content.split()
        victim = array[1]
        if '<@!' in victim:
            victim = re.search('\d+',victim).group()
        user = await ctx.guild.fetch_member(int(array[1]))
        role = discord.utils.get(ctx.guild.roles, name='muted')
        await user.remove_roles(role)
        embed=discord.Embed(title="Unmuted",description=str(user.name)+" has been unmuted.",color=0x0066ff)
        await ctx.channel.send(embed=embed)
        await user.create_dm()
        embed=discord.Embed(title="Unmuted",description=str(user.name)+", you are now allowed to send ctxs in "+str(ctx.guild),color=0x0066ff)
        await user.dm_channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

async def filterctx(ctx,bot):
    if "@everyone" in ctx.content:
        await pingedunnecessary(ctx,bot)
    for item in ["fuck","bitch","cumshot","asshole","wtf","retard","cocksucker","nigger","sex"]:
        if item in ctx.content:
            if "Admin" in str(ctx.author.roles):
                pass
            else:
                channel = bot.get_channel(notice_channel_id)
                embed=discord.Embed(title="Notice: **language breach**",description="**"+str(ctx.author)+"** sent a bad word in this server\n **textchannel**: "+str(ctx.channel)+"\n **full ctx**: "+str(ctx.content)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff) 
                await channel.send(embed=embed)

@commands.command(name='help')
async def showhelp(ctx,*args):
    with open("resources/data.json","r") as JsonFile:
        data = json.load(JsonFile)
    all_commands = data["all_commands"]
    all_commands_false = data["all_commands_false"]
    helpinfo = data["helpinfo"]
    JsonFile.close()
    if len(ctx.content.split()) == 1:
        embed=discord.Embed(title="$modbot", description="$modbot is a bot for moderators made by the developer team at "+str(ctx.guild)+" here are all commands:", color=0x0066ff)
        for key,value in helpinfo.items():
            embed.add_field(name=key, value=value,inline=False)
        embed.set_footer(text="developed by ankith101.rar")
        await ctx.channel.send(embed=embed)
    else:
        command = ctx.content.split()[1]
        if command in all_commands:
            embed=discord.Embed(title=command,description=helpinfo[command],color=0x0066ff)
            embed.set_footer(text="developed by ankith101.rar")
            await ctx.channel.send(embed=embed)
        elif command in all_commands_false:
            embed=discord.Embed(title="$"+command,description=helpinfo["$"+command],color=0x0066ff)
            embed.set_footer(text="developed by ankith101.rar")
            await ctx.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Unknown command: `"+str(command)+"`",description="idk what you typed, check the spelling",color=0x0066ff)
            await ctx.channel.send(embed=embed)

@commands.command(name='rules')
async def rules(ctx,*args):
    with open("resources/data.json","r") as JsonFile:
        data = json.load(JsonFile)
    string = data["rules"]
    rulesfull = data["rulesfull"]
    rulesfull = rulesfull.split("|")
    print(rulesfull)
    JsonFile.close()
    array = ctx.content.split()
    if len(array) == 1:
        embed=discord.Embed(title="Rules of the server:",url="https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html",description="You can get a copy of the server rules from our website\n [click here](https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html) to view the rules",color=0x0066ff)
        embed.set_footer(text="website by Aadi, bot developed by Ankith101")
        await ctx.channel.send(embed=embed)
    elif len(array) == 2:
        if array[1] == "full":
            embed=discord.Embed(title="RULES of AVAMOAGHOS server:",description="\n".join(rulesfull),color=0x0066ff)
            embed.set_footer(text="developed by ankith101.rar")
            await ctx.channel.send(embed=embed)
        elif int(array[1]) <= len(string) and int(array[1]) >= 1:
            embed=discord.Embed(title="Rules",description="**#"+str(array[1])+".** "+string[int(array[1])-1],color=0x0066ff)
            await ctx.channel.send(embed=embed)

@commands.command(name='silence')
async def silence(ctx,*args):
    if "Admin" in str(ctx.author.roles):
        role = discord.utils.get(ctx.guild.roles, name="developer")
        await ctx.channel.set_permissions(role, send_ctxs=False)
        embed=discord.Embed(title="Silenced",description="`"+str(ctx.channel)+"` has been silenced by "+str(ctx.author),color=0x0066ff)
        await ctx.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

@commands.command(name='unsilence')
async def unsilence(ctx,*args):
    if "Admin" in str(ctx.author.roles):
        role = discord.utils.get(ctx.guild.roles, name="developer")
        await ctx.channel.set_permissions(role, send_ctxs=True)
        embed=discord.Embed(title="Unsilenced",description="`"+str(ctx.channel)+"` has been unsilenced by "+str(ctx.author),color=0x0066ff)
        await ctx.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

@commands.command(name='warn')
async def warn(ctx,*args):
    if "Admin" in str(ctx.author.roles):
        array = ctx.content.split()
        user_id = array[1]
        reason = " ".join(array[2:len(array)])
        user = await ctx.guild.fetch_member(int(array[1]))
        #sending to initial channel
        embed=discord.Embed(title="Warning",description="applied warning to "+str(user.name)+"\n**reason**: "+reason,color=0x0066ff)
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(str(user.mention))
        #sending to dms
        await user.create_dm()
        embed=discord.Embed(title="Infraction: **Warning**",description="you have been warned by "+str(ctx.author)+"\n**reason**: "+reason,color=0x0066ff)
        await user.dm_channel.send(embed=embed)
        #sending to #notices
        channel = bot.get_channel(notice_channel_id)
        embed=discord.Embed(title="Notice: **Warning**",description="**"+str(user.name)+"** has been warned by "+str(ctx.author)+"\n**reason**: "+reason+"\n**channel**: "+str(ctx.channel)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=0x0066ff)
        await ctx.channel.send(embed=embed)

@commands.command(name='meme')
async def meme(ctx,*args):
    reddit = praw.Reddit(
        client_id=my_bot_id,
        client_secret=my_bot_secret,
        user_agent=my_user_agent,
    )
    print(reddit.read_only)
    while True:
        sr = reddit.subreddit("programmerhumor").random()
        if not sr.is_self:
            slink = sr.url
            if ctx.channel.id != 809074960890069022:
                await ctx.channel.send(str(ctx.author.mention)+" you can only use `$meme` command in #memes")
                break
            else:
                embed=discord.Embed(title=str(sr.title),description="posted by u/"+str(sr.author)+"\n"+str(sr.score)+" upvotes",color=0x0066ff)
                embed.set_image(url=str(sr.url))
                await ctx.channel.send(embed=embed)
                break
        else:
            continue

def setup(bot):
    bot.add_command(sayhello)
    bot.add_command(rules)
    bot.add_command(sendch)
    bot.add_command(add_role)
    bot.add_command(remove_role)
    bot.add_command(kick)
    bot.add_command(mute)
    bot.add_command(unmute)
    bot.add_command(silence)
    bot.add_command(unsilence)
    bot.add_command(warn)
