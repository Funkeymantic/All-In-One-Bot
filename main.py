<<<<<<< HEAD
# main.py

import asyncio
from dotenv import load_dotenv
import os
from bot_modules.discord_bot import start_discord_bot
from bot_modules.twitch_bot import start_twitch_bot, check_twitch_live

# Load environment variables from .env file
print("Loading environment variables...")
load_dotenv()

# Retrieve tokens from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")

# Check if tokens are loaded properly
if DISCORD_TOKEN:
    print("Discord token loaded successfully.")
else:
    print("Failed to load Discord token. Please check your .env file.")
    
if TWITCH_TOKEN:
    print("Twitch token loaded successfully.")
else:
    print("Failed to load Twitch token. Please check your .env file.")

# Function to notify when Twitch goes live
async def twitch_live_notifier():
    live_notification_sent = False
    print("Starting Twitch live notifier...")
    
    while True:
        print("Checking if the Twitch stream is live...")
        is_live, thumbnail_url = await check_twitch_live()
        
        if is_live and not live_notification_sent:
            print("Stream is live! Sending notification to Discord...")
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
            print("Live notification sent to Discord.")
        elif not is_live and live_notification_sent:
            print("Stream is no longer live. Removing previous notifications...")
            for msg in live_notification_messages:
                try:
                    await msg.delete()
                except discord.NotFound:
                    pass
            live_notification_messages.clear()
            live_notification_sent = False
            print("Notifications removed.")
        else:
            print("Stream status unchanged.")

        # Sleep for 5 minutes before checking again
        await asyncio.sleep(300)

# Function to start both the Discord and Twitch bots
async def run_bots():
    print("Starting Discord and Twitch bots...")
    await asyncio.gather(
        start_discord_bot(DISCORD_TOKEN),
        start_twitch_bot(),
        twitch_live_notifier()
    )
    print("Both bots are running.")

# Entry point for the script
if __name__ == "__main__":
    try:
        print("Running bots...")
        asyncio.run(run_bots())
        print("Bots are now running.")
    except Exception as e:
        print(f"An error occurred: {e}")
        with open("/home/pcmartin/All-In-One-Bot/error.log", "a") as error_file:
            error_file.write(f"{str(e)}\n")


=======
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
>>>>>>> 77bd72ff1578f6a3677e3bc7dd362f658b53cbba
