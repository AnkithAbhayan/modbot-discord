import discord
from discord.ext import commands
from bot.utils.constants import constants


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rules")
    async def rules(self, ctx, *args):
        string = constants.json_data["rules"]
        rulesfull = constants.json_data["rulesfull message"]
        rulesfull = rulesfull.split("|")
        array = ctx.message.content.split()
        if len(array) == 1:
            embed = discord.Embed(
                title="Rules of the server:",
                url="https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html",
                description="You can get a copy of the server rules from our website\n [click here](https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html) to view the rules",
                color=constants.colours["blue"],
            )
            embed.set_footer(text="website by Aadi, bot developed by Ankith101")
            await ctx.channel.send(embed=embed)
        elif len(array) == 2:
            if array[1] == "full":
                embed = discord.Embed(
                    title="RULES of AVAMOAGHOS server:",
                    description="\n".join(rulesfull),
                    color=constants.colours["blue"],
                )
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            elif int(array[1]) <= len(string) and int(array[1]) >= 1:
                embed = discord.Embed(
                    title="Rules",
                    description=f"**#{array[1]}.** {string[int(array[1]) - 1]}",
                    color=constants.colours["blue"],
                )
                await ctx.channel.send(embed=embed)
