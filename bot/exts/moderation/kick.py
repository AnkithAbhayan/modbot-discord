import re
import discord
from discord.ext import commands
from bot.utils.constants import constants
from bot.utils.ankith import date_time


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
                color=constants.colours["blue"],
            )
            await ctx.channel.send(embed=embed)
            # sending to #notices
            channel = self.bot.get_channel(constants.channels["notices"])
            embed = discord.Embed(
                title="Notice: **Kick**",
                description=(
                    f"{user.name} has been kicked by {ctx.author}\n",
                    f"**channel**: {ctx.channel}\n",
                    f"**reason**: {' '.join(array[2 : len(array)])}\n",
                    f"**date and time**: {date_time.time()} {date_time.date()}",
                ),
                color=constants.colours["blue"],
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
                color=constants.colours["blue"],
            )
            await user.dm_channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.colours["red"],
            )
            await ctx.channel.send(embed=embed)
