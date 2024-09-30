#!/bin/bash

# Directory where the repository is located
REPO_DIR="/home/pcmartin/All-In-One-Bot"
LOG_DIR="$REPO_DIR/logs"  # Directory to store and push logs

# GitHub repository URL
REPO_URL="git@github.com:Funkeymantic/All-In-One-Bot.git"

# Ensure logs directory exists
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Function to check if the repository directory exists and pull latest changes
function update_repository {
    echo "Checking for updates..."
    cd "$REPO_DIR" || exit

    # Fetch and pull changes from GitHub
    git fetch origin
    if git pull origin $(git rev-parse --abbrev-ref HEAD); then
        echo "Repository updated."
    else
        echo "Failed to update the repository. Check for conflicts or issues."
        return 0
    fi

    return 1
}

# Function to push log files to GitHub
function push_logs {
    echo "Pushing log files to GitHub..."
    cd "$REPO_DIR" || exit

    # Check for any changes to log files and commit them
    git add "$LOG_DIR"/*.log 2>/dev/null
    if git commit -m "Updated log files"; then
        git push origin $(git rev-parse --abbrev-ref HEAD)
        echo "Logs pushed to GitHub."
    else
        echo "No changes to log files or commit failed."
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
if [ ! -d "$REPO_DIR/.venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv "$REPO_DIR/.venv"
fi

echo "Activating virtual environment..."
source "$REPO_DIR/.venv/bin/activate"

# Pull updates (but always restart the bot regardless of updates)
update_repository

echo "Stopping the bot if it's running..."
pkill -f "python3 $REPO_DIR/main.py"

# Run the bot
echo "Starting the bot..."
nohup python3 "$REPO_DIR/main.py" > "$LOG_DIR/bot.log" 2>&1 &
BOT_PID=$!
echo "Bot started with PID $BOT_PID"

# Push log files to GitHub
push_logs

echo "Resync and restart completed."
