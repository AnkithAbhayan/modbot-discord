import json
import discord
import discord.utils
from resources.ankith import date_time
with open("resources/data.json","r") as JsonFile:
    data = json.load(JsonFile)
notice_channel_id = data["notice_channel"]
class filters:
    async def filtermessage(ctx,bot):
        if "@everyone" in ctx.content:
            #ctx.channel.send("are you trying to do something dude?")
            await filters.pingedunnecessary(ctx,bot)
        for item in ["fuck","bitch","cumshot","asshole","wtf","retard","cocksucker","nigger","sex"]:
            if item in ctx.content.lower():
                admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
                if admin_role not in ctx.author.roles:
                    channel = bot.get_channel(notice_channel_id)
                    link = f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.id}" 
                    embed=discord.Embed(title="Notice: **language breach**",description=f"**User**: {ctx.author.mention}\n **textchannel**: {ctx.channel.mention}\n **full message**:```\n{ctx.content}\n```\n[goto message]({link})\n**date and time**: {str(date_time.time())} {str(date_time.date())}",color=0x0066ff) 
                    await channel.send(embed=embed)
    async def pingedunnecessary(ctx,bot):
        owner_role = discord.utils.get(ctx.guild.roles, name='Admin')
        if owner_role not in ctx.author.roles:
            link = f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.id}" 
            embed=discord.Embed(title="Dont do it",description=str(ctx.author.mention)+" please dont try to ping everyone",color=0x0066ff)
            await ctx.channel.send(embed=embed)
            channel = bot.get_channel(notice_channel_id)
            embed=discord.Embed(title="Notice: **Pinged Everyone**",description=f"**{ctx.author.mention}** has tried to ping everyone.\n**channel**: {ctx.channel.mention}\n**full message**:\n```{ctx.content}\n```\n[goto message]({link})\n**date and time**: {str(date_time.date())} {str(date_time.time())}" ,color=0x0066ff) 
            await channel.send(embed=embed)