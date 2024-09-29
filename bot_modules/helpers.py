from datetime import datetime

# Helper function to print messages with a timestamp
def print_with_timestamp(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}')

# Fancy font dictionary
fancy_font = {
    'A': '𝔸', 'a': '𝕒', 'B': '𝔹', 'b': '𝕓', 'C': 'ℂ', 'c': '𝕔',
    'D': '𝔻', 'd': '𝕕', 'E': '𝔼', 'e': '𝕖', 'F': '𝔽', 'f': '𝕗',
    'G': '𝔾', 'g': '𝕘', 'H': 'ℍ', 'h': '𝕙', 'I': '𝕀', 'i': '𝕚',
    'J': '𝕁', 'j': '𝕛', 'K': '𝕂', 'k': '𝕜', 'L': '𝕃', 'l': '𝕝',
    'M': '𝕄', 'm': '𝕞', 'N': 'ℕ', 'n': '𝕟', 'O': '𝕆', 'o': '𝕠',
    'P': 'ℙ', 'p': '𝕡', 'Q': 'ℚ', 'q': '𝕢', 'R': 'ℝ', 'r': '𝕣',
    'S': '𝕊', 's': '𝕤', 'T': '𝕋', 't': '𝕥', 'U': '𝕌', 'u': '𝕦',
    'V': '𝕍', 'v': '𝕧', 'W': '𝕎', 'w': '𝕨', 'X': '𝕏', 'x': '𝕩',
    'Y': '𝕐', 'y': '𝕪', 'Z': 'ℤ', 'z': '𝕫'
}

# Function to convert a string to fancy font
def to_fancy_font(text):
    return ''.join(fancy_font.get(char, char) for char in text)
