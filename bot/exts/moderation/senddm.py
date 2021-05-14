import discord
import discord.utils
from bot.utils.constants import constants
from discord.ext import commands
import re


class SendDm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="send_dm")
    async def dm(self, ctx, *args):
        admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
        if admin_role in ctx.author.roles:
            array = ctx.message.content.split()
            user = array[1]
            message = array[2]
            if "<@!" in user:
                user = re.search("\d+", user).group()
            user = await ctx.guild.fetch_member(user)
            user.create_dm()
            user.dm_channel.send(message)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.colours["red"],
            )
            await ctx.channel.send(embed=embed)