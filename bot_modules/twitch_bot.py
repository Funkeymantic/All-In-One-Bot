# bot_modules/twitch_bot.py

from twitchio.ext import commands as twitch_commands
from .helpers import print_with_timestamp
import os
import aiohttp

# Twitch bot class
class TwitchBot(twitch_commands.Bot):
    def __init__(self):
        if os.getenv("TWITCH_TOKEN") is None:
            raise ValueError("TWITCH_TOKEN is not set! Please check your .env file or environment variables.")
        
        super().__init__(token=os.getenv("TWITCH_TOKEN"), prefix='~', initial_channels=['funkeymantic'])

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

# Function to check if the Twitch stream is live
async def check_twitch_live():
    TWITCH_USER_LOGIN = 'funkeymantic'
    headers = {
        'Client-ID': os.getenv("TWITCH_CLIENT_ID"),
        'Authorization': f'Bearer {os.getenv("TWITCH_TOKEN")}'
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

# Function to start the Twitch bot
async def start_twitch_bot():
    twitch_bot = TwitchBot()
    await twitch_bot.start()
