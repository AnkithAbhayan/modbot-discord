from discord.ext import commands
from random import randint


class RandomCase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="randomcase")
    async def randomcase(self, ctx, *args):
        array = ctx.message.content.split()
        arg = list(" ".join(array[1 : len(array)]))
        for index, value in enumerate(arg):
            if randint(1, 2) == 2:
                arg[index] = arg[index].upper()
        await ctx.channel.send("".join(arg))
