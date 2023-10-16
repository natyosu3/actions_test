import discord
import os


TOKEN = str(os.environ.get("TOKEN"))
GUILD_ID = 1117469059957665942

CH_ID = 913410359711375410

Echo_ID = 1059820902755344473
bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("pingを確認")
    echo: discord.Member = bot.get_guild(GUILD_ID).get_member(Echo_ID)

    ch: discord.TextChannel = bot.get_channel(CH_ID)

    if str(echo.status) == "online":
        await ch.send(embed=discord.Embed(
            title="Echo BOT Status",
            color=discord.Color.green(),
            description="```python online!```"
        ))
    else:
        await ch.send(embed=discord.Embed(
            title="Echo BOT Status",
            color=discord.Color.red(),
            description="```python offline!\n Echo is downing...```"
        ))

    await bot.close()


if __name__ == '__main__':
    bot.run(TOKEN)