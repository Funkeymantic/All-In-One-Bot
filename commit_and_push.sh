#!/bin/bash

# Navigate to the project directory
cd /home/pcmartin/All-In-One-Bot/

# Activate the virtual environment (optional)
source /home/pcmartin/All-In-One-Bot/.venv/bin/activate

# Display the current status
echo "Git Status:"
git status

# Add all changes
git add .

# Commit the changes with a message provided as an argument
if [ -z "$1" ]; then
    echo "No commit message provided. Using default message."
    COMMIT_MESSAGE="Auto-commit"
else
    COMMIT_MESSAGE=$1
fi

git commit -m "$COMMIT_MESSAGE"

# Push the changes to GitHub using SSH
echo "Pushing changes to GitHub..."
git push origin main

echo "Changes have been pushed to GitHub."

# Deactivate the virtual environment
deactivate
