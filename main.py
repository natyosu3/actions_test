import discord
import os


TOKEN = str(os.environ.get("TOKEN"))
GUILD_ID = 1117469059957665942

CH_ID = 913410359711375410

Echo_ID = 1059820902755344473
bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    echo: discord.Member = bot.get_guild(GUILD_ID).get_member(Echo_ID)
    ch: discord.TextChannel = bot.get_channel(CH_ID)

    status_msg: discord.Message = await ch.fetch_message(1163366925661917234)

    if str(echo.status) == "online" and status_msg != None:
        await status_msg.edit(embed=discord.Embed(
            title="Echo BOT Status",
            color=discord.Color.green(),
            description="```python\nOnline!```"
        ))
    else:
        await status_msg.edit(embed=discord.Embed(
            title="Echo BOT Status",
            color=discord.Color.red(),
            description="```python\nOffline!\n Echo is downing...```"
        ))

    if status_msg == None:
        if str(echo.status) == "online":
            await status_msg.edit(embed=discord.Embed(
                title="Echo BOT Status",
                color=discord.Color.green(),
                description="```python\nOnline!```"
            ))
        else:
            await status_msg.edit(embed=discord.Embed(
                title="Echo BOT Status",
                color=discord.Color.red(),
                description="```python\nOffline!\n Echo is downing...```"
            ))

    await bot.close()


if __name__ == '__main__':
    bot.run(TOKEN)