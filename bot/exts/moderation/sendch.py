from discord.ext import commands


class SendCh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sendch")
    async def sendch(self, ctx, *args):
        if "Admin" in str(ctx.author.roles):
            array = ctx.message.content.split()
            channel = ctx.get_channel(int(array[1]))
            await channel.send(" ".join(array[2 : len(array)]))
