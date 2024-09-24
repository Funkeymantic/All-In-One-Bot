# bot_modules/helpers.py

from datetime import datetime

# Helper function to print messages with a timestamp
def print_with_timestamp(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}')

# Fancy font dictionary
fancy_font = {
    # (fill in the details from your existing dictionary)
}

# Function to convert a string to fancy font
def to_fancy_font(text):
    return ''.join(fancy_font.get(char, char) for char in text)