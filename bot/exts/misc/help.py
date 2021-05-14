import discord
from bot.utils.constants import constants
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def showhelp(self, ctx, *args):
        all_commands = constants.json_data["all_commands"]
        all_commands_false = constants.json_data["all_commands_false"]
        helpinfo = constants.json_data["helpinfo"]
        if len(ctx.message.content.split()) == 1:
            embed = discord.Embed(
                title="$modbot",
                description=f"$modbot is a bot for moderators made by the developer team at {ctx.guild} here are all commands:",
                color=constants.colours["blue"],
            )
            for key, value in helpinfo.items():
                embed.add_field(name=key, value=value, inline=False)
            embed.set_footer(text="developed by ankith101.rar")
            await ctx.channel.send(embed=embed)
        else:
            command = ctx.message.content.split()[1]
            if command in all_commands:
                embed = discord.Embed(
                    title=command,
                    description=helpinfo[command],
                    color=constants.colours["blue"],
                )
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            elif command in all_commands_false:
                embed = discord.Embed(
                    title="$" + command,
                    description=helpinfo["$" + command],
                    color=constants.colours["blue"],
                )
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=f"Unknown command: `{command}`",
                    description="idk what you typed, check the spelling",
                    color=constants.colours["red"],
                )
                await ctx.channel.send(embed=embed)
