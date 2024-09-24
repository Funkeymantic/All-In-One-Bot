# bot_modules/discord_bot.py

from discord.ext import commands
import discord
from .helpers import print_with_timestamp
import os

# Define Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True
intents.voice_states = True

# Discord bot instance
discord_bot = commands.Bot(command_prefix='~', intents=intents, case_insensitive=True)
live_notification_messages = []

# Event handler for Discord voice state updates
@discord_bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and after.channel.name == "⌚ 𝔗𝔥𝔢 𝔄𝔫𝔱𝔢𝔠𝔥𝔞𝔪𝔟𝔢𝔯":
        message = f'{member.name} has joined the voice channel: {after.channel.name}'
        print_with_timestamp(message)
        if 'twitch_bot' in globals():
            await twitch_bot.send_twitch_message(f'{member.name} joined {after.channel.name} in Discord')

# Function to start the Discord bot
async def start_discord_bot(discord_token):
    await discord_bot.start(discord_token)
