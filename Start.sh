#!/bin/bash

# Directory where the repository is located
REPO_DIR="/home/pcmartin/All-In-One-Bot"

# GitHub repository URL
REPO_URL="git@github.com:Funkeymantic/All-In-One-Bot.git"

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

# Function to pull the latest changes and handle divergent branches
function update_repository {
    echo "Checking for updates..."
    cd "$REPO_DIR" || exit
    git fetch origin

    # Handle divergent branches by merging
    git config pull.rebase false

    if git pull origin $(git rev-parse --abbrev-ref HEAD); then
        echo "Repository updated."
        return 1
    else
        echo "Pull failed, conflicts might be present."
        return 0
    fi
}

# Check for updates and stop the bot if there were changes
if update_repository; then
    echo "Stopping the bot if it's running..."
    pkill -f "python3 $REPO_DIR/main.py"

    # Run the bot
    echo "Starting the bot..."
    nohup python3 "$REPO_DIR/main.py" > "$REPO_DIR/bot.log" 2>&1 &
    echo "Bot started with PID $!"
else
    echo "Conflicts detected or pull failed. Please resolve them manually."
    exit 1
fi

# Stage, commit, and push any local changes to the remote repository
echo "Staging local changes..."
git add .
echo "Committing changes..."
git commit -m "Automated commit and push from script."

# Get the current branch name
BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

# Push to the correct branch
echo "Pushing to GitHub..."
git push origin "$BRANCH_NAME"
echo "Push complete."

