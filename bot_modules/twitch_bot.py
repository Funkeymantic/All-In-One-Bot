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

# Function to start the Twitch bot
async def start_twitch_bot():
    twitch_bot = TwitchBot()
    await twitch_bot.start()

