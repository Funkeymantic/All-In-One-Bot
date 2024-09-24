# All-In-One Bot

## Overview

The All-In-One Bot is a versatile bot designed to integrate with Twitch, Discord, and more. It supports live notifications, command handling, and interactive features across multiple platforms. The bot is built using Python and utilizes several libraries, including `discord.py`, `twitchio`, and more.

## Features and Capabilities

### 1. **Discord Integration**
- **Event Handling**: The bot can handle various Discord events, such as voice state updates (e.g., when a user joins a specific voice channel).
- **Message Commands**: The bot can respond to specific commands sent by users in Discord, such as greeting users with custom messages.

### 2. **Twitch Integration**
- **Live Stream Notifications**: The bot monitors a specified Twitch channel and notifies a designated Discord channel when the stream goes live. It sends a custom embed with the stream’s details.
- **Twitch Chat Commands**: The bot responds to specific commands in Twitch chat, enabling interaction with viewers.

### 3. **Environment Variable Management**
- The bot uses a `.env` file to securely manage tokens and API keys, ensuring sensitive information is not hard-coded into the source code.

## Project Structure

    /All-In-One-Bot
        /bot_modules
            __init__.py
            discord_bot.py
            twitch_bot.py
            helpers.py
        .env (not included in the repository)
        main.py


- **bot_modules**: Contains the modularized code for Discord and Twitch bots, as well as helper functions.
- **main.py**: The entry point to start the bots and manage their lifecycle.
- **.env**: Environment file to store sensitive information like API keys and tokens.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- The following Python libraries:
  - `discord.py`
  - `twitchio`
  - `aiohttp`
  - `python-dotenv`

Install the required libraries using pip:

```bash
pip install discord.py twitchio aiohttp python-dotenv
```

## Step 1: Clone the Repository

```bash

git clone https://github.com/YourUsername/All-In-One-Bot.git
cd All-In-One-Bot
```

## Step 2: Set Up Environment Variables

Create a .env file in the root directory of the project with the following content:

```env

DISCORD_TOKEN=your_discord_token
TWITCH_TOKEN=your_twitch_token
TWITCH_CLIENT_ID=your_twitch_client_id
```

## Step 3: Run the Bot

To start the bot, run the following command:

```bash
cd All-In-One-Bot
./commit_an_push.sh
```

This will start both the Discord and Twitch bots concurrently.

## Usage

### Discord Commands

- `~hello`: The bot will greet the user in Discord.
- **Voice State Updates**: The bot will notify when a user joins the specified voice channel.

### Twitch Commands

- `~hello`: The bot will greet the user in Twitch chat.
- **Live Notifications**: The bot will notify a specific Discord channel when the Twitch stream goes live.

## Contributing

To contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.


