import json
import discord
import discord.utils
with open("resources/data.json","r") as JsonFile:
    data = json.load(JsonFile)
notice_channel_id = data["notice_channel"]
class filters:
    async def filtermessage(ctx,bot):
        if "@everyone" in ctx.content:
            #ctx.channel.send("are you trying to do something dude?")
            await pingedunnecessary(ctx,bot)
        for item in ["fuck","bitch","cumshot","asshole","wtf","retard","cocksucker","nigger","sex"]:
            if item in ctx.content:
                if "Admin" in str(ctx.author.roles):
                    pass
                else:
                    channel = bot.get_channel(notice_channel_id)
                    embed=discord.Embed(title="Notice: **language breach**",description="**"+str(ctx.author)+"** sent a bad word in this server\n **textchannel**: "+str(ctx.channel)+"\n **full message**: "+str(ctx.content)+"\n**date and time**: "+str(date_time.time())+" "+str(date_time.date()),color=0x0066ff) 
                    await channel.send(embed=embed)
    async def pingedunnecessary(client,message):
        if not message.author.has_role("Owner"):
            embed=discord.Embed(title="Dont do it",description=str(message.author.mention)+" please dont try to ping everyone",color=0x0066ff)
            await message.channel.send(embed=embed)
            channel = client.get_channel(notice_channel_id)
            embed=discord.Embed(title="Notice: **Pinged Everyone**",description="**"+str(message.author.mention)+"** has tried to ping everyone \n **channel**: "+str(message.channel)+"\n **full message**: "+str(message.content)+"\n **time**: "+str(date_time.date())+" "+str(date_time.time()),color=0x0066ff) 
            await channel.send(embed=embed)