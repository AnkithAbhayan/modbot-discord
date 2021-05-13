import praw
import discord
import discord.utils
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sayhello")
    async def sayhello(self, ctx, *args):
        await ctx.channel.send(f"Hello there!, {ctx.author.mention}")

    @commands.command(name="meme")
    async def meme(ctx, *args):
        reddit = praw.Reddit(
            client_id=my_bot_id,
            client_secret=my_bot_secret,
            user_agent=my_user_agent,
        )
        print(reddit.read_only)
        while True:
            sr = reddit.subreddit("programmerhumor").random()
            if not sr.is_self:
                slink = sr.url
                if ctx.channel.id != 809074960890069022:
                    await ctx.channel.send(
                        str(ctx.author.mention)
                        + " you can only use `$meme` command in #memes"
                    )
                    break
                else:
                    embed = discord.Embed(
                        title=str(sr.title),
                        description="posted by u/"
                        + str(sr.author)
                        + "\n"
                        + str(sr.score)
                        + " upvotes",
                        color=constants.standard_colour,
                    )
                    embed.set_image(url=str(sr.url))
                    await ctx.channel.send(embed=embed)
                    break
            else:
                continue

    @commands.command(name="rules")
    async def rules(self, ctx, *args):
        string = self.my_bot.json_data["rules"]
        rulesfull = self.my_bot.json_data["rulesfull message"]
        rulesfull = rulesfull.split("|")
        print(rulesfull)
        JsonFile.close()
        array = ctx.message.content.split()
        if len(array) == 1:
            embed = discord.Embed(
                title="Rules of the server:",
                url="https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html",
                description="You can get a copy of the server rules from our website\n [click here](https://htmlpreview.github.io/?https://github.com/AnkithAbhayan/modbot-discord/blob/main/docs/rules.html) to view the rules",
                color=constants.standard_colour,
            )
            embed.set_footer(text="website by Aadi, bot developed by Ankith101")
            await ctx.channel.send(embed=embed)
        elif len(array) == 2:
            if array[1] == "full":
                embed = discord.Embed(
                    title="RULES of AVAMOAGHOS server:",
                    description="\n".join(rulesfull),
                    color=constants.standard_colour,
                )
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            elif int(array[1]) <= len(string) and int(array[1]) >= 1:
                embed = discord.Embed(
                    title="Rules",
                    description="**#"
                    + str(array[1])
                    + ".** "
                    + string[int(array[1]) - 1],
                    color=constants.standard_colour,
                )
                await ctx.channel.send(embed=embed)

    @commands.command(name="help")
    async def showhelp(self, ctx, *args):
        all_commands = self.my_bot.json_data["all_commands"]
        all_commands_false = self.my_bot.json_data["all_commands_false"]
        helpinfo = self.my_bot.json_data["helpinfo"]
        JsonFile.close()
        if len(ctx.message.content.split()) == 1:
            embed = discord.Embed(
                title="$modbot",
                description="$modbot is a bot for moderators made by the developer team at "
                + str(ctx.guild)
                + " here are all commands:",
                color=constants.standard_colour,
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
                    color=constants.standard_colour,
                )
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            elif command in all_commands_false:
                embed = discord.Embed(
                    title="$" + command,
                    description=helpinfo["$" + command],
                    color=constants.standard_colour,
                )
                embed.set_footer(text="developed by ankith101.rar")
                await ctx.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Unknown command: `" + str(command) + "`",
                    description="idk what you typed, check the spelling",
                    color=constants.error_colour,
                )
                await ctx.channel.send(embed=embed)
