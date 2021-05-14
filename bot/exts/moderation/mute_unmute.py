import discord
import re
import discord.utils
from discord.ext import commands
from bot.utils.constants import constants
from bot.utils.ankith import date_time


class MuteAndUnmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
                color=constants.colours["blue"],
            )
            await ctx.channel.send(embed=embed)
            # sending message to dm
            await member.create_dm()
            embed = discord.Embed(
                title="Infraction: Mute",
                description=(
                    f"you have been muted by {ctx.author}\n" f"**reason**: {reason}"
                ),
                color=constants.colours["blue"],
            )
            await member.dm_channel.send(embed=embed)
            # sending message to #notices
            channel = self.bot.get_channel(constants.channels["notices"])
            embed = discord.Embed(
                title="Notice: **Mute**",
                description=(
                    f"{member.mention} has been muted by {ctx.author}\n"
                    f"**reason**: {reason}\n"
                    f"**channel**: {ctx.channel}\n"
                    f"**date and time**: {date_time.time()} {date_time.date()}"
                ),
                color=constants.colours["blue"],
            )
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.colours["red"],
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
                color=constants.colours["blue"],
            )
            await ctx.channel.send(embed=embed)
            await user.create_dm()
            embed = discord.Embed(
                title="Unmuted",
                description=f"{user.name}, you are now allowed to send messages in the {ctx.guild} server",
                color=constants.colours["blue"],
            )
            await user.dm_channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention}, you are not allowed to use that command",
                color=constants.colours["red"],
            )
            await ctx.channel.send(embed=embed)
