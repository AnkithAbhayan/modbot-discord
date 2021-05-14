import discord
import discord.utils
from bot.utils.ankith import date_time
from bot.utils.constants import constants

class filters:
    async def filtermessage(ctx, bot):
        if "@everyone" in ctx.content:
            # ctx.channel.send("are you trying to do something dude?")
            await filters.pingedunnecessary(ctx, bot)
        for item in [
            "fuck",
            "bitch",
            "cumshot",
            "asshole",
            "wtf",
            "retard",
            "cocksucker",
            "nigger",
            "sex",
        ]:
            if item in ctx.content.lower():
                admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
                if admin_role not in ctx.author.roles:
                    channel = bot.get_channel(constants.channel["notices"])
                    link = f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.id}"
                    embed = discord.Embed(
                        title="Notice: **language breach**",
                        description=(
                            f"**User**: {ctx.author.mention}\n"
                            f"**textchannel**: {ctx.channel.mention}\n"
                            f"**full message**:\n"
                            "```"
                            f"{ctx.content}\n"
                            "```\n"
                            f"[goto message]({link})\n"
                            f"**date and time**: {str(date_time.time())} {str(date_time.date())}"
                        ),
                        color=constants.colours["red"],
                    ),
                    await channel.send(embed=embed)

    async def pingedunnecessary(ctx, bot):
        owner_role = discord.utils.get(ctx.guild.roles, name="Admin")
        if owner_role not in ctx.author.roles:
            link = f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.id}"
            embed = discord.Embed(
                title="Dont do it",
                description=f"{ctx.author.mention} please dont try to ping everyone",
                color=constants.colours["red"],
            )
            await ctx.channel.send(embed=embed)
            channel = bot.get_channel(constants.channel["notices"])
            embed = discord.Embed(
                title="Notice: **Pinged Everyone**",
                description=(
                    f"**{ctx.author.mention}** has tried to ping everyone.\n"
                    f"**channel**: {ctx.channel.mention}\n"
                    f"**full message**:\n```{ctx.content}\n"
                    "```\n"
                    f"[goto message]({link})\n"
                    f"**date and time**: {str(date_time.date())} {str(date_time.time())}"
                ),
                color=constants.colours["red"],
            )
            await channel.send(embed=embed)
