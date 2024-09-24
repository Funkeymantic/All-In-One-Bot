# main.py

import asyncio
from dotenv import load_dotenv
import os
from bot_modules.discord_bot import start_discord_bot
from bot_modules.twitch_bot import start_twitch_bot, check_twitch_live

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")

async def twitch_live_notifier():
    live_notification_sent = False
    while True:
        is_live, thumbnail_url = await check_twitch_live()
        if is_live and not live_notification_sent:
            live_channel = discord_bot.get_channel(705560543964037161)
            embed = discord.Embed(
                title="We're LIVE on Twitch!",
                description="Check it out at https://twitch.tv/funkeymantic",
                color=discord.Color.purple()
            )
            embed.set_image(url=thumbnail_url)
            message = await live_channel.send(embed=embed)
            live_notification_messages.append(message)
            live_notification_sent = True
        elif not is_live and live_notification_sent:
            for msg in live_notification_messages:
                try:
                    await msg.delete()
                except discord.NotFound:
                    pass
            live_notification_messages.clear()
            live_notification_sent = False
        await asyncio.sleep(300)

async def run_bots():
    await asyncio.gather(
        start_discord_bot(DISCORD_TOKEN),
        start_twitch_bot(),
        twitch_live_notifier()
    )

if __name__ == "__main__":
    asyncio.run(run_bots())