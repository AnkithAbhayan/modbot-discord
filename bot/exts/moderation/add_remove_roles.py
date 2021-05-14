import discord
from discord.ext import commands
from bot.utils.constants import constants
import discord.utils


class RemoveRoleAndAddRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
                    color=constants.colours["red"],
                )
                await ctx.channel.send(embed=embed)
            else:
                await user.remove_roles(role)
                embed = discord.Embed(
                    title="Role has been removed",
                    description=f"{role.mention} role has been removed from {user.mention}",
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
                    color=constants.colours["red"],
                )
                await ctx.channel.send(embed=embed)
            else:
                await user.add_roles(role)
                embed = discord.Embed(
                    title="Role has been added",
                    description=f"{user.mention} has been given the {role.name} role",
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
