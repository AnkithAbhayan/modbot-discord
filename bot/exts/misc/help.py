import discord
from bot.utils.constants import constants
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def showhelp(self, ctx, *args):
        helpinfo = constants.json_data["helpinfo"]
        if len(ctx.message.content.split()) == 1:
            categories = [category for category in helpinfo]
            embed = discord.Embed(
                title="Command Help.",
                description=(
                    f"$modbot is a bot for moderators made by the developer team at {ctx.guild}\n"
                    "If you'd like to view command help for a different category:\n"
                    "```\n"
                    "$help <category>\n"
                    "```\n\n"
                    f"**All the categories**: `{', '.join(categories)}`\n"
                    f"If you're just looking for help info on a specific command:\n"
                    "```\n"
                    "$help <command>\n"
                    "```"
                ),
                color=constants.colours["blue"],
            )
            embed.set_footer(text="developed by ankith101.rar")
            await ctx.channel.send(embed=embed)
        else:
            second_arg = ctx.message.content.split()[1]
            if helpinfo.get(second_arg):
                embed = discord.Embed(
                    title=f"Command help. Category: {second_arg}",
                    description=f"Here are all the commands of the `{second_arg}` category.",
                    color=constants.colours["blue"],
                )
                for commandname, info in helpinfo[second_arg].items():
                    embed.add_field(name=f"${commandname}", value=info, inline=False)
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            else:
                for category, commands in helpinfo.items():
                    if commands.get(second_arg):
                        embed = discord.Embed(
                            title=f"Command Help: `${command}`",
                            description=helpinfo[category][second_arg],
                            color=constants.colours["blue"],
                        )
                        await ctx.channel.send(embed=embed)
                        return
                embed = discord.Embed(
                    title=f"Unknown command or Category: `{command}`",
                    description=f"`{command}` is not a valid command name or a category.",
                    color=constants.colours["red"],
                )
                await ctx.channel.send(embed=embed)
