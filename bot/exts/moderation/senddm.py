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
            message = " ".join(array[2:len(array)])
            if "<@!" in user:
                user = re.search("\d+", user).group()
            user = await ctx.guild.fetch_member(user)
            await user.create_dm()
            dm_message = discord.Embed(
                description=f"{message}",
                color=constants.colours["blue"]
            )
            dm_message.set_author(
                name=ctx.author.name, 
                url=discord.Embed.Empty, 
                icon_url=ctx.author.avatar_url
            )
            roles = ctx.author.roles #list of roles, lowest role first
            roles.reverse() #list of roles, highest role first
            top_role = roles[0]
            dm_message.set_footer(text=top_role.name)
            await user.dm_channel.send(embed=dm_message)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.colours["red"],
            )
            await ctx.channel.send(embed=embed)
