import discord
import praw
import json
import discord.utils
from dotenv import load_dotenv
from discord.ext import commands
import os
import re
from resources.ankith import date_time
load_dotenv()
my_bot_id = os.getenv("CLIENT_ID")
my_bot_secret = os.getenv("CLIENT_SECRET")
my_user_agent = os.getenv("USER_AGENT")
error_colour = 0xFF0000
standard_colour = 0x0066ff
with open("resources/data.json","r") as JsonFile:
    data = json.load(JsonFile)
notice_channel_id = data["notice_channel"]
JsonFile.close()

class Moderation_toolkit(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='sayhello')
    async def sayhello(self,ctx,*args):
        await ctx.channel.send(f"Hello there!, {ctx.author.mention}")

    @commands.command(name='sendch')
    async def sendch(self,ctx,*args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            channel = ctx.get_channel(int(array[1]))
            await channel.send(' '.join(array[2:len(array)]))

    @commands.command(name='kick')
    async def kick(self,ctx,*args):
        array = ctx.message.content.split()
        if "Admin" in str(ctx.author.roles):
            victim = array[1]
            if '<@!' in victim:
                victim = re.search('\d+',victim).group()
            user = await ctx.guild.fetch_member(victim)
            name = user.name
            await user.kick()
            #sending to initial channel
            embed=discord.Embed(title="Kicked.",description=str(name)+" has been kicked from the server",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)
            #sending to #notices
            channel = self.bot.get_channel(notice_channel_id) 
            embed=discord.Embed(title="Notice: **Kick**",description=str(user.name)+" has been kicked by "+str(ctx.author)+"\nchannel: "+str(ctx.channel)+"\nreason: "+" ".join(array[2:len(array)])+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=data["standard_colour"])
            await channel.send(embed=embed)
            await user.create_dm()
            embed=discord.Embed(title="Infraction: Kick",description="you just got kicked from "+str(ctx.guild)+" by "+str(ctx.author)+"\n reason was: "+" ".join(array[2:len(array)]),color=data["standard_colour"])
            await user.dm_channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)

    @commands.command(name='remove_role')
    async def remove_role(self,ctx,*args):
        array = ctx.message.content.split()
        if "Owner" in str(ctx.author.roles):
            user = await ctx.guild.fetch_member(int(array[2]))
            role = discord.utils.get(ctx.guild.roles, name=array[1])
            if array[1] not in str(user.roles):
                embed=discord.Embed(title="Doesnt have the role",description=str(user.name)+" doesnt even have the `"+str(role.name)+"` role in the first place",color=data["standard_colour"])
                await ctx.channel.send(embed=embed)
            else:
                await user.remove_roles(role)
                embed=discord.Embed(title="Role has been removed",description="`"+str(role.name)+"` role has been removed from "+str(user.mention),color=data["standard_colour"])
                await ctx.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)

    @commands.command(name='add_role')
    async def add_role(self,ctx,*args):
        array = ctx.message.content.split()
        if "Owner" in str(ctx.author.roles):
            user = await ctx.guild.fetch_member(int(array[2]))
            role = discord.utils.get(ctx.guild.roles, name=array[1])
            if array[1] in str(user.roles):
                embed=discord.Embed(title="Already has the role",description=str(user.name)+" already has the `"+str(role.name)+"` role",color=data["standard_colour"])
                await ctx.channel.send(embed=embed)
            else:
                await user.add_roles(role)
                embed=discord.Embed(title="Role has been added",description=str(user.mention)+" has been given the `"+str(role.name)+"` role",color=data["standard_colour"])
                await ctx.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)

    @commands.command(name='mute')
    async def mute(self,ctx,*args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            victim = array[1]
            if '<@!' in victim:
                victim = re.search('\d+',victim).group()
            member = await ctx.guild.fetch_member(victim)
            role = discord.utils.get(ctx.guild.roles, name='muted')
            reason = " ".join(array[2:len(array)])
            await member.add_roles(role)
            #sending message to initial channel
            embed=discord.Embed(title="Muted",description=str(member.mention)+" has been muted by "+str(ctx.author)+"\n**reason**: "+reason,color=data["standard_colour"])
            await ctx.channel.send(embed=embed)
            #sending message to dm
            await member.create_dm()
            embed=discord.Embed(title="Infraction: Mute",description="you have been muted by "+str(ctx.author)+"\n**reason**: "+reason,color=data["standard_colour"])
            await member.dm_channel.send(embed=embed)
            #sending message to #notices
            channel = self.bot.get_channel(notice_channel_id)
            embed=discord.Embed(title="Notice: **Mute**",description="**"+str(member.name)+"** has been muted by "+str(ctx.author)+"\n**reason**: "+reason+"\n**channel**: "+str(ctx.channel)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=data["standard_colour"])
            await channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)

    @commands.command(name='unmute')
    async def unmute(self,ctx,*args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            victim = array[1]
            if '<@!' in victim:
                victim = re.search('\d+',victim).group()
            user = await ctx.guild.fetch_member(victim)
            role = discord.utils.get(ctx.guild.roles, name='muted')
            await user.remove_roles(role)
            embed=discord.Embed(title="Unmuted",description=str(user.name)+" has been unmuted.",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)
            await user.create_dm()
            embed=discord.Embed(title="Unmuted",description=str(user.name)+", you are now allowed to send messages in "+str(ctx.guild),color=data["standard_colour"])
            await user.dm_channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)

    @commands.command(name='help')
    async def showhelp(self,ctx,*args):
        with open("resources/data.json","r") as JsonFile:
            data = json.load(JsonFile)
        all_commands = data["all_commands"]
        all_commands_false = data["all_commands_false"]
        helpinfo = data["helpinfo"]
        JsonFile.close()
        if len(ctx.message.content.split()) == 1:
            embed=discord.Embed(title="$modbot", description="$modbot is a bot for moderators made by the developer team at "+str(ctx.guild)+" here are all commands:", color=data["standard_colour"])
            for key,value in helpinfo.items():
                embed.add_field(name=key, value=value,inline=False)
            embed.set_footer(text="developed by ankith101.rar")
            await ctx.channel.send(embed=embed)
        else:
            command = ctx.message.content.split()[1]
            if command in all_commands:
                embed=discord.Embed(title=command,description=helpinfo[command],color=data["standard_colour"])
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            elif command in all_commands_false:
                embed=discord.Embed(title="$"+command,description=helpinfo["$"+command],color=data["standard_colour"])
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            else:
                embed=discord.Embed(title="Unknown command: `"+str(command)+"`",description="idk what you typed, check the spelling",color=data["standard_colour"])
                await ctx.channel.send(embed=embed)

    @commands.command(name='rules')
    async def rules(self,ctx,*args):
        with open("resources/data.json","r") as JsonFile:
            data = json.load(JsonFile)
        string = data["rules"]
        rulesfull = data["rulesfull message"]
        rulesfull = rulesfull.split("|")
        print(rulesfull)
        JsonFile.close()
        array = ctx.message.content.split()
        if len(array) == 1:
            embed=discord.Embed(title="Rules of the server:",url="https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html",description="You can get a copy of the server rules from our website\n [click here](https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html) to view the rules",color=data["standard_colour"])
            embed.set_footer(text="website by Aadi, bot developed by Ankith101")
            await ctx.channel.send(embed=embed)
        elif len(array) == 2:
            if array[1] == "full":
                embed=discord.Embed(title="RULES of AVAMOAGHOS server:",description="\n".join(rulesfull),color=data["standard_colour"])
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            elif int(array[1]) <= len(string) and int(array[1]) >= 1:
                embed=discord.Embed(title="Rules",description="**#"+str(array[1])+".** "+string[int(array[1])-1],color=data["standard_colour"])
                await ctx.channel.send(embed=embed)

    @commands.command(name='silence')
    async def silence(self,ctx,*args):
        if "Admin" in str(ctx.author.roles):
            role = discord.utils.get(ctx.guild.roles, name="everyone")
            await ctx.channel.set_permissions(role, send_messages=False)
            embed=discord.Embed(title="Silenced",description="`"+str(ctx.channel)+"` has been silenced by "+str(ctx.author),color=data["standard_colour"])
            await ctx.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)

    @commands.command(name='unsilence')
    async def unsilence(self,ctx,*args):
        if "Admin" in str(ctx.author.roles):
            role = discord.utils.get(ctx.guild.roles, name="everyone")
            await ctx.channel.set_permissions(role, send_messages=True)
            embed=discord.Embed(title="Unsilenced",description="`"+str(ctx.channel)+"` has been unsilenced by "+str(ctx.author),color=data["standard_colour"])
            await ctx.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
            await ctx.channel.send(embed=embed)

    @commands.command(name='warn')
    async def warn(self,ctx,*args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            victim = array[1]
            if '<@!' in victim:
                victim = re.search('\d+',victim).group()
            reason = " ".join(array[2:len(array)])
            user = await ctx.guild.fetch_member(victim)
            #sending to initial channel
            embed=discord.Embed(title="Warning",description="applied warning to "+str(user.name)+"\n**reason**: "+reason,color=data["standard_colour"])
            await ctx.channel.send(embed=embed)
            await ctx.channel.send(str(user.mention))
            #sending to dms
            await user.create_dm()
            embed=discord.Embed(title="Infraction: **Warning**",description="you have been warned by "+str(ctx.author)+"\n**reason**: "+reason,color=data["standard_colour"])
            await user.dm_channel.send(embed=embed)
            #sending to #notices
            channel = self.bot.get_channel(notice_channel_id)
            embed=discord.Embed(title="Notice: **Warning**",description="**"+str(user.name)+"** has been warned by "+str(ctx.author)+"\n**reason**: "+reason+"\n**channel**: "+str(ctx.channel)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=data["standard_colour"])
            await channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Invalid Permissions",description=str(ctx.author.mention)+" you are not allowed to use that command",color=data["standard_colour"])
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
                    embed=discord.Embed(title=str(sr.title),description="posted by u/"+str(sr.author)+"\n"+str(sr.score)+" upvotes",color=data["standard_colour"])
                    embed.set_image(url=str(sr.url))
                    await ctx.channel.send(embed=embed)
                    break
            else:
                continue

class self_assign_roles(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="get_role")
    async def get_role(self,ctx,*args):
        array = ctx.message.content.split()
        if len(array) == 1:
            help_get_role = discord.Embed(title="Command help: `$get_role`",description=f"This command lets you self assign roles to your user so that you can access the full benefits!\nUsage:\n```\n$get_role <role_name>```\n\n Example: `$get_role developer` gives you access to all programming related channels!\n All self-assignable roles: `{', '.join(data['user_roles'])}`",color=standard_colour)
            await ctx.channel.send(embed=help_get_role)
            return
        developer_role = discord.utils.get(ctx.guild.roles, name="developer")
        if developer_role not in ctx.author.roles:
            get_dev_role_embed = discord.Embed(title="No {developer_role.mention} role.",description="Hi! If you require specific language roles, you have to get the @developer role first. This role gives you access to channels related to programming.",color=error_colour)
            get_dev_role_embed.add_field(name="How to get the {developer_role.mention} role?", value="Enter the following command. \n ```\n$get_role developer```",inline=False)
            get_dev_role_embed.set_footer(text="Happy coding.")
            await ctx.channel.send(embed=embed)
            return
        if array[1] in data["user_roles"]:
            role = discord.utils.get(ctx.guild.roles, name=array[1])
            if role in ctx.author.roles:
                already_have_the_role = discord.Embed(title=":x: You Already have the role.",description=f"It looks like you already have the {role.mention} role.",color=error_colour)
                await ctx.channel.send(embed=already_have_the_role)
                return
            await ctx.author.add_roles(role)
            got_the_role_embed = discord.Embed(title=f":white_check_mark: role added!",description=f"You have now got the {role.mention} role! :tada:",color=standard_colour)
            get_dev_role_embed.set_footer(text="Happy coding.")
            await ctx.channel.send(embed=got_the_role_embed)
        else:
            error_in_role_name = discord.Embed(title=":x: Invalid role.",description=f"The role name you entered is incorrect!\n Correct usage:\n ```\n$get_role <role_name>\n```\nHere are all the valid role names: `{', '.join(data['user_roles'])}`",color=error_colour)
            await ctx.channel.send(embed=error_in_role_name)
