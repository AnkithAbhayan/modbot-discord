from discord.ext import commands
import discord
import discord.utils
from bot.utils.constants import constants


class SelfAssignRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="get_role")
    async def get_role(self, ctx, *args):
        array = ctx.message.content.split()
        if len(array) == 1:
            help_get_role = discord.Embed(
                title="Command help: `$get_role`",
                description=(
                    f"This command lets you self assign roles to your user so that you can access the full benefits!\n"
                    f"**Usage**:\n"
                    "```\n"
                    "$get_role <role_name>\n"
                    "```\n"
                    "**Example**: `$get_role developer` gives you access to all programming related channels!\n"
                    f"**All self-assignable roles**: `{', '.join(constants.json_data['user_roles'])}`"
                ),
                color=constants.colours["blue"],
            )
            await ctx.channel.send(embed=help_get_role)
            await ctx.send(ctx.author.mention)
            return

        developer_role = discord.utils.get(ctx.guild.roles, name="developer")
        if developer_role not in ctx.author.roles:
            if array[1] == "developer":
                await ctx.author.add_roles(developer_role)
                got_the_role_embed = discord.Embed(
                    title=":white_check_mark: role added!",
                    description=f"You have now got the {developer_role.mention} role! :tada:\nEnjoy access to all the programming related channels!",
                    color=constants.colours["blue"],
                )
                got_the_role_embed.set_footer(text="Happy coding.")
                await ctx.channel.send(embed=got_the_role_embed)
            else:
                get_dev_role_embed = discord.Embed(
                    title=":x: No @developer role.",
                    description=f"Hi! If you require specific language roles, you have to get the {developer_role.mention} role first.\nThis role gives you access to channels related to programming.",
                    color=constants.colours["red"],
                )
                get_dev_role_embed.add_field(
                    name="How to get the @developer role?",
                    value="Enter the following command. \n ```\n$get_role developer```",
                    inline=False,
                )
                get_dev_role_embed.set_footer(text="Happy coding.")
                await ctx.channel.send(embed=get_dev_role_embed)
            await ctx.send(ctx.author.mention)
            return

        if array[1] in constants.json_data["user_roles"]:
            role = discord.utils.get(ctx.guild.roles, name=array[1])
            if role in ctx.author.roles:
                already_have_the_role = discord.Embed(
                    title=":x: You Already have the role.",
                    description=f"It looks like you already have the {role.mention} role.",
                    color=constants.colours["red"],
                )
                await ctx.channel.send(embed=already_have_the_role)
                await ctx.send(ctx.author.mention)
                return
            await ctx.author.add_roles(role)
            got_the_role_embed = discord.Embed(
                title=":white_check_mark: role added!",
                description=f"You have now got the {role.mention} role! :tada:",
                color=constants.colours["blue"],
            )
            got_the_role_embed.set_footer(text="Happy coding.")
            await ctx.channel.send(embed=got_the_role_embed)
        else:
            error_in_role_name = discord.Embed(
                title=":x: Invalid role.",
                description=f"The role name you entered is incorrect!\n Correct usage:\n ```\n$get_role <role_name>\n```\n**All self-assignable roles**: `{', '.join(constants.json_data['user_roles'])}`",
                color=constants.colours["red"],
            )
            await ctx.channel.send(embed=error_in_role_name)
        await ctx.send(ctx.author.mention)
