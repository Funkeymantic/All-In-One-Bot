import asyncio
from dotenv import load_dotenv
import os
from bot_modules.discord_bot import start_discord_bot
from bot_modules.twitch_bot import start_twitch_bot, check_twitch_live

# Load environment variables
print("Loading environment variables...")
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")

if DISCORD_TOKEN:
    print("Discord token loaded successfully.")
else:
    print("Failed to load Discord token. Please check your .env file.")
    
if TWITCH_TOKEN:
    print("Twitch token loaded successfully.")
else:
    print("Failed to load Twitch token. Please check your .env file.")

# Define your bot-related functions
async def twitch_live_notifier():
    # Your code for Twitch live notifier
    pass

async def run_bots():
    await asyncio.gather(
        start_discord_bot(DISCORD_TOKEN),
        start_twitch_bot(),
        twitch_live_notifier()
    )
    print("Both bots are running.")

# Run the bots
if __name__
