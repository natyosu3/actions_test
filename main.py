import discord
import os
from datetime import datetime, timedelta

TOKEN = str(os.environ.get("TOKEN"))
GUILD_ID = 1117469059957665942
CH_ID = 913410359711375410
Echo_ID = 1059820902755344473

bot = discord.Client(intents=discord.Intents.all())

async def update_status():
    echo = bot.get_guild(GUILD_ID).get_member(Echo_ID)
    ch = bot.get_channel(CH_ID)
    status_msg = await ch.fetch_message(1163366925661917234)

    current_time = datetime.now() + timedelta(hours=9)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    if echo.status == discord.Status.online:
        embed = discord.Embed(
            title="Echo BOT Status",
            color=discord.Color.green(),
            description=f"```python\n[{formatted_time}] Online!```"
        )
    else:
        embed = discord.Embed(
            title="Echo BOT Status",
            color=discord.Color.red(),
            description=f"```python\n[{formatted_time}] Offline!\n Echo is downing...```"
        )

    await status_msg.edit(embed=embed)
    await bot.close()

@bot.event
async def on_ready():
    await update_status()

if __name__ == '__main__':
    bot.run(TOKEN)