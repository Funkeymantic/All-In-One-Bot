#!/bin/bash

# Directory where the repository is located
REPO_DIR="/home/pcmartin/All-In-One-Bot"

# GitHub repository URL
REPO_URL="git@github.com:Funkeymantic/All-In-One-Bot.git"

# Function to pull the latest changes
function update_repository {
    echo "Checking for updates..."
    cd "$REPO_DIR" || exit
    git fetch origin main
    LOCAL=$(git rev-parse @)
    REMOTE=$(git rev-parse @{u})

    if [ "$LOCAL" = "$REMOTE" ]; then
        echo "Already up to date."
        return 0
    else
        echo "Updating repository..."
        git pull origin main
        echo "Repository updated."
        return 1
    fi
}

# Check if the repository directory exists and is a git repository
if [ -d "$REPO_DIR/.git" ]; then
    echo "Repository found."
else
    echo "Cloning the repository..."
    git clone "$REPO_URL" "$REPO_DIR"
fi

# Activate the virtual environment
source "$REPO_DIR/.venv/bin/activate"

# Check for updates and restart the bot if there were changes
if update_repository; then
    echo "No updates found. Running the bot as usual."
else
    echo "Repository was updated. Restarting the bot..."
    pkill -f "python3 $REPO_DIR/main.py"  # Stop the bot if it's running
fi

# Run the bot
nohup python3 "$REPO_DIR/main.py" > "$REPO_DIR/bot.log" 2>&1 &
echo "Bot started with PID $!"
