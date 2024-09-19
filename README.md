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

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- The following Python libraries:
  - `discord.py`
  - `twitchio`
  - `tweepy`
  - `openpyxl`
  - `google-api-python-client`
  - `aiohttp`
  - `python-dotenv`

### Step 1: Clone the Repository

```bash
cd All-In-One-Bot
git pull origin main
/home/pcmartin/startup_script.sh


