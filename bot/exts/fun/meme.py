import discord
from discord.ext import commands
import praw
from dotenv import load_dotenv
import os
from bot.utils.constants import constants

load_dotenv()
my_bot_id = os.getenv("CLIENT_ID")
my_bot_secret = os.getenv("CLIENT_SECRET")
my_user_agent = os.getenv("USER_AGENT")


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meme")
    async def meme(ctx, *args):
        reddit = praw.Reddit(
            client_id=my_bot_id, client_secret=my_bot_secret, user_agent=my_user_agent
        )
        print(reddit.read_only)
        while True:
            sr = reddit.subreddit("programmerhumor").random()
            if not sr.is_self:
                if ctx.channel.id != constants.channels["memes"]:
                    await ctx.channel.send(
                        f"{ctx.author.mention} you can only use `$meme` command in #memes"
                    )
                    break
                else:
                    embed = discord.Embed(
                        title=sr.title,
                        description=(
                            f"posted by u/{sr.author}\n" f"{sr.score} upvotes"
                        ),
                        color=constants.colours["blue"],
                    )
                    embed.set_image(url=str(sr.url))
                    await ctx.channel.send(embed=embed)
                    break
            else:
                continue
