from twitchio.ext import commands as twitch_commands
from .helpers import print_with_timestamp
import os
import aiohttp
import time

class TwitchBot(twitch_commands.Bot):
    def __init__(self):
        if os.getenv("TWITCH_TOKEN") is None:
            raise ValueError("TWITCH_TOKEN is not set! Please check your .env file or environment variables.")
        
        super().__init__(token=os.getenv("TWITCH_TOKEN"), prefix='!', initial_channels=['funkeymantic'])
        self.last_cheese_response_time = 0
        self.cheese_cooldown = 30  # 30 seconds cooldown

    async def event_ready(self):
        print_with_timestamp(f'Logged in as | {self.nick}')
        print_with_timestamp(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Ensure the bot does not respond to its own messages
        if message.author.name == self.nick:
            return

        print_with_timestamp(message.content)

        # Handle commands
        await self.handle_commands(message)

        # Respond to "cheese" with a cooldown
        if 'cheese' in message.content.lower():
            current_time = time.time()
            if current_time - self.last_cheese_response_time >= self.cheese_cooldown:
                await message.channel.send(f'I claim your CHEESE, {message.author.name}!')
                self.last_cheese_response_time = current_time

    @twitch_commands.command(name='hello')
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
