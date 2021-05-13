import discord
import discord.utils
from dotenv import load_dotenv
from discord.ext import commands
import os
import re
import bot.constants
from bot.ankith import date_time

load_dotenv()
my_bot_id = os.getenv("CLIENT_ID")
my_bot_secret = os.getenv("CLIENT_SECRET")
my_user_agent = os.getenv("USER_AGENT")
JsonFile.close()

# discord bot.
class Moderation_toolkit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sendch")
    async def sendch(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            channel = ctx.get_channel(int(array[1]))
            await channel.send(" ".join(array[2 : len(array)]))

    @commands.command(name="kick")
    async def kick(self, ctx, *args):
        array = ctx.message.content.split()
        if "Admin" in str(ctx.author.roles):
            victim = array[1]
            if "<@!" in victim:
                victim = re.search("\d+", victim).group()
            user = await ctx.guild.fetch_member(victim)
            name = user.name
            await user.kick()
            # sending to initial channel
            embed = discord.Embed(
                title="Kicked.",
                description=f"{name} has been kicked from the server",
                color=constants.standard_colour,
            )
            await ctx.channel.send(embed=embed)
            # sending to #notices
            channel = self.bot.get_channel(notice_channel_id)
            embed = discord.Embed(
                title="Notice: **Kick**",
                description=(
                    f"{user.name} has been kicked by {ctx.author}\n",
                    f"**channel**: {ctx.channel}\n",
                    f"**reason**: {' '.join(array[2 : len(array)])}\n",
                    f"**date and time**: {date_time.time()} {date_time.date()}",
                ),
                color=constants.standard_colour,
            )
            await channel.send(embed=embed)
            # sending to dm
            await user.create_dm()
            embed = discord.Embed(
                title="Infraction: Kick",
                description=(
                    f"you just got kicked from {ctx.guild} by {ctx.author}\n"
                    f"**reason:** {' '.join(array[2 : len(array)])}"
                ),
                color=constants.standard_colour,
            )
            await user.dm_channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="remove_role")
    async def remove_role(self, ctx, *args):
        array = ctx.message.content.split()
        if "Owner" in str(ctx.author.roles):
            user = await ctx.guild.fetch_member(int(array[2]))
            role = discord.utils.get(ctx.guild.roles, name=array[1])
            if array[1] not in str(user.roles):
                embed = discord.Embed(
                    title="Doesnt have the role",
                    description=f"{user.mention} doesnt even have the {role.mention} role in the first place",
                    color=constants.error_colour,
                )
                await ctx.channel.send(embed=embed)
            else:
                await user.remove_roles(role)
                embed = discord.Embed(
                    title="Role has been removed",
                    description=f"{role.mention} role has been removed from {user.mention}",
                    color=constants.standard_colour,
                )
                await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="add_role")
    async def add_role(self, ctx, *args):
        array = ctx.message.content.split()
        if "Owner" in str(ctx.author.roles):
            user = await ctx.guild.fetch_member(int(array[2]))
            role = discord.utils.get(ctx.guild.roles, name=array[1])
            if array[1] in str(user.roles):
                embed = discord.Embed(
                    title="Already has the role",
                    description=f"{user.mention} already has the {role.mention} role",
                    color=constants.error_colour,
                )
                await ctx.channel.send(embed=embed)
            else:
                await user.add_roles(role)
                embed = discord.Embed(
                    title="Role has been added",
                    description=f"{user.mention} has been given the {role.name} role",
                    color=constants.standard_colour,
                )
                await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="mute")
    async def mute(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            victim = array[1]
            if "<@!" in victim:
                victim = re.search("\d+", victim).group()
            member = await ctx.guild.fetch_member(victim)
            role = discord.utils.get(ctx.guild.roles, name="muted")
            reason = " ".join(array[2 : len(array)])
            await member.add_roles(role)
            # sending message to initial channel
            embed = discord.Embed(
                title="Muted",
                description=(
                    f"{member.mention} has been muted by {ctx.author}\n"
                    f"**reason**: {reason}"
                ),
                color=constants.standard_colour,
            )
            await ctx.channel.send(embed=embed)
            # sending message to dm
            await member.create_dm()
            embed = discord.Embed(
                title="Infraction: Mute",
                description=(
                    f"you have been muted by {ctx.author}\n" f"**reason**: {reason}"
                ),
                color=constants.standard_colour,
            )
            await member.dm_channel.send(embed=embed)
            # sending message to #notices
            channel = self.bot.get_channel(notice_channel_id)
            embed = discord.Embed(
                title="Notice: **Mute**",
                description=(
                    f"{member.mention} has been muted by {ctx.author}\n"
                    f"**reason**: {reason}\n"
                    f"**channel**: {ctx.channel}\n"
                    f"**date and time**: {date_time.time()} {date_time.date()}"
                ),
                color=constants.standard_colour,
            )
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="unmute")
    async def unmute(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            victim = array[1]
            if "<@!" in victim:
                victim = re.search("\d+", victim).group()
            user = await ctx.guild.fetch_member(victim)
            role = discord.utils.get(ctx.guild.roles, name="muted")
            await user.remove_roles(role)
            embed = discord.Embed(
                title="Unmuted",
                description=f"{user.mention} has been unmuted.",
                color=constants.standard_colour,
            )
            await ctx.channel.send(embed=embed)
            await user.create_dm()
            embed = discord.Embed(
                title="Unmuted",
                description=f"{user.name}, you are now allowed to send messages in the {ctx.guild} server",
                color=constants.standard_colour,
            )
            await user.dm_channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention}, you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="silence")
    async def silence(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            role = discord.utils.get(ctx.guild.roles, name="everyone")
            await ctx.channel.set_permissions(role, send_messages=False)
            embed = discord.Embed(
                title="Silenced",
                description=f"{ctx.channel.mention} has been silenced by {ctx.author}",
                color=constants.standard_colour,
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="unsilence")
    async def unsilence(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            role = discord.utils.get(ctx.guild.roles, name="everyone")
            await ctx.channel.set_permissions(role, send_messages=True)
            embed = discord.Embed(
                title="Unsilenced",
                description=f"{ctx.channel.mention} has been unsilenced by {ctx.author}",
                color=constants.standard_colour,
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention}, you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="warn")
    async def warn(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            victim = array[1]
            if "<@!" in victim:
                victim = re.search("\d+", victim).group()
            reason = " ".join(array[2 : len(array)])
            user = await ctx.guild.fetch_member(victim)
            # sending to initial channel
            embed = discord.Embed(
                title="Warning",
                description=(
                    f"applied warning to {user.name}\n" f"**reason**: {reason}"
                ),
                color=constants.standard_colour,
            )
            await ctx.channel.send(embed=embed)
            await ctx.channel.send(str(user.mention))
            # sending to dms
            await user.create_dm()
            embed = discord.Embed(
                title="Infraction: **Warning**",
                description=(
                    f"you have been warned by {ctx.author}\n" f"**reason**: {reason}"
                ),
                color=constants.standard_colour,
            )
            await user.dm_channel.send(embed=embed)
            # sending to #notices
            channel = self.bot.get_channel(notice_channel_id)
            embed = discord.Embed(
                title="Notice: **Warning**",
                description=(
                    f"{user.mention} has been warned by {ctx.author}\n"
                    f"**reason**: {reason}\n"
                    f"**channel**: {ctx.channel}\n"
                    f"**date and time**: {date_time.time()} {date_time.date()}"
                ),
                color=constants.standard_colour,
            )
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)

    @commands.command(name="dm")
    async def dm(self, ctx, *args):
        admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
        if admin_role in ctx.author.roles:
            array = ctx.message.content.split()
            user = array[1]
            message = array[2]
            if "<@!" in victim:
                user = re.search("\d+", user).group()
            user = await ctx.guild.fetch_member(user)
            user.create_dm()
            user.dm_channel.send(message)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.error_colour,
            )
            await ctx.channel.send(embed=embed)
