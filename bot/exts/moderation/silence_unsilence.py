import discord
import discord.utils
from discord.ext import commands
from bot.utils.constants import constants


class SilenceAndUnsilence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="silence")
    async def silence(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            role = discord.utils.get(ctx.guild.roles, name="everyone")
            await ctx.channel.set_permissions(role, send_messages=False)
            embed = discord.Embed(
                title="Silenced",
                description=f"{ctx.channel.mention} has been silenced by {ctx.author}",
                color=constants.colours["blue"],
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention} you are not allowed to use that command",
                color=constants.colours["red"],
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
                color=constants.colours["blue"],
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Invalid Permissions",
                description=f"{ctx.author.mention}, you are not allowed to use that command",
                color=constants.colours["red"],
            )
            await ctx.channel.send(embed=embed)
