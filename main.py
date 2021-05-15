import os
import json
from datetime import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot.exts.fun.meme import Meme
from bot.exts.fun.sayhello import SayHello
from bot.exts.fun.randomcase import RandomCase

from bot.exts.misc.self_assign_roles import SelfAssignRoles
from bot.exts.misc.help import Help
from bot.exts.misc.rules import Rules

from bot.exts.moderation.warn import Warn
from bot.exts.moderation.mute_unmute import MuteAndUnmute
from bot.exts.moderation.kick import Kick
from bot.exts.moderation.sendch import SendCh
from bot.exts.moderation.senddm import SendDm
from bot.exts.moderation.silence_unsilence import SilenceAndUnsilence
from bot.exts.moderation.add_remove_roles import RemoveRoleAndAddRole

from bot.utils.filters import filters
from bot.utils.constants import constants
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$")
bot.remove_command("help")

bot.add_cog(SayHello(bot))
bot.add_cog(Meme(bot))
bot.add_cog(RandomCase(bot))

bot.add_cog(SelfAssignRoles(bot))
bot.add_cog(Help(bot))
bot.add_cog(Rules(bot))

bot.add_cog(Warn(bot))
bot.add_cog(MuteAndUnmute(bot))
bot.add_cog(Kick(bot))
bot.add_cog(SendCh(bot))
bot.add_cog(SendDm(bot))
bot.add_cog(SilenceAndUnsilence(bot))
bot.add_cog(RemoveRoleAndAddRole(bot))


@bot.event
async def on_raw_message_delete(message):
    if str(message.cached_message.author.name) == "$modbot":
        await message.cached_message.channel.send(
            "please stop deleting my messages, you better follow the rules and dont misuse power"
        )


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_message(message):
    print(f"{message.author} on {message.channel}: {message.content}")
    if message.guild is None:
        channel = bot.get_channel(constants.channels["bot-testing"])
        dm_embed = discord.Embed(
            title=f"Dm from `{message.author}`:",
            description=(
                f"`time`:`{datetime.now()}`\n"
                f"`content:`\n"
                "```\n"
                f"{message.content}\n"
                "```"
            ),
            color=constants.colours["blue"]
        )
        await channel.send(embed=dm_embed)
    if message.author == bot.user:
        return

    await filters.filtermessage(message, bot)
    await bot.process_commands(message)


keep_alive()
bot.run(TOKEN)
