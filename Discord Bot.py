from twitchio.ext import commands as twitch_commands
from discord.ext import commands as discord_commands
import discord
import asyncio
import aiohttp
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Debugging: print to ensure tokens are loaded
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")

print(f"DISCORD_TOKEN: {DISCORD_TOKEN}")
print(f"TWITCH_TOKEN: {TWITCH_TOKEN}")
print(f"TWITCH_CLIENT_ID: {TWITCH_CLIENT_ID}")

if TWITCH_TOKEN is None:
    raise ValueError("TWITCH_TOKEN is not set! Please check your environment variables.")


# Define Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True
intents.voice_states = True

# Helper function to print messages with a timestamp
def print_with_timestamp(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}')

# Fancy font dictionary
fancy_font = {
    # ... (same as before)
}

# Function to convert a string to fancy font
def to_fancy_font(text):
    return ''.join(fancy_font.get(char, char) for char in text)

# Discord bot instance
discord_bot = discord_commands.Bot(command_prefix='~', intents=intents, case_insensitive=True)
live_notification_messages = []

# Event handler for Discord voice state updates
@discord_bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and after.channel.name == "⌚ 𝔗𝔥𝔢 𝔄𝔫𝔱𝔢𝔠𝔥𝔞𝔪𝔟𝔢𝔯":
        message = f'{member.name} has joined the voice channel: {after.channel.name}'
        print_with_timestamp(message)
        if twitch_bot:
            await twitch_bot.send_twitch_message(f'{member.name} joined {after.channel.name} in Discord')

# Twitch bot class
class TwitchBot(twitch_commands.Bot):
    def __init__(self):
        if TWITCH_TOKEN is None:
            raise ValueError("TWITCH_TOKEN is not set! Please check your .env file or environment variables.")
        
        super().__init__(token=TWITCH_TOKEN, prefix='~', initial_channels=['funkeymantic'])

    async def event_ready(self):
        print_with_timestamp(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.echo:
            return
        print_with_timestamp(message.content)
        await self.handle_commands(message)

        if 'cheese' in message.content.lower():
            await message.channel.send(f'I claim your CHEESE, {message.author.name}!')

    @twitch_commands.command()
    async def hello(self, ctx: twitch_commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    async def send_twitch_message(self, content):
        channel = self.get_channel('funkeymantic')
        if channel:
            await channel.send(content)

# Check if the Twitch stream is live
async def check_twitch_live():
    TWITCH_USER_LOGIN = 'funkeymantic'
    headers = {
        'Client-ID': os.getenv("TWITCH_CLIENT_ID"),
        'Authorization': f'Bearer {TWITCH_TOKEN}'
    }
    async with aiohttp.ClientSession() as session:
        url = f'https://api.twitch.tv/helix/streams?user_login={TWITCH_USER_LOGIN}'
        async with session.get(url, headers=headers) as resp:
            if resp.status == 200:
                data = await resp.json()
                if 'data' in data and len(data['data']) > 0:
                    thumbnail_url = data['data'][0]['thumbnail_url'].replace("{width}", "320").replace("{height}", "180")
                    return True, thumbnail_url
            return False, None

# Discord task to notify when Twitch goes live
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

# Function to start both Discord and Twitch bots
async def run_bots():
    global twitch_bot
    twitch_bot = TwitchBot()

    await asyncio.gather(
        discord_bot.start(DISCORD_TOKEN),
        twitch_bot.start(),
        twitch_live_notifier()
    )

# Start the bots
if __name__ == "__main__":
    asyncio.run(run_bots())
