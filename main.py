import discord
import os


TOKEN = str(os.environ.get("TOKEN"))
GUILD_ID = 1117469059957665942
Echo_ID = 1059820902755344473
bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("pingを確認")
    echo: discord.Member = bot.get_guild(GUILD_ID).get_member(Echo_ID)


    print(echo.status)
    await bot.close()


if __name__ == '__main__':
    bot.run(TOKEN)