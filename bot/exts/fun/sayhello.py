from discord.ext import commands


class SayHello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sayhello")
    async def sayhello(self, ctx, *args):
        await ctx.channel.send(f"Hello there!, {ctx.author.mention}")
