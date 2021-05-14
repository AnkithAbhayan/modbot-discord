import discord
import re
from bot.utilsconstants import constants
from bot.utils.ankith import date_time
from discord.ext import commands


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
                color=constants.colours["blue"],
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
                color=constants.colours["blue"],
            )
            await user.dm_channel.send(embed=embed)
            # sending to #notices
            channel = self.bot.get_channel(constants.channels["notices"])
            embed = discord.Embed(
                title="Notice: **Warning**",
                description=(
                    f"{user.mention} has been warned by {ctx.author}\n"
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
