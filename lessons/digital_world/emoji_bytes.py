# lessons/unicode/emoji_bytes.py

import time

# 🎨 Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}😀 Welcome to Emoji Bytes!{RESET}")
    slow_print(f"{CYAN}Did you know emojis aren't just characters?")
    slow_print("They're multi-byte Unicode symbols stored in UTF-8.")
    slow_print("Let's peek behind the curtain to see their raw byte form! 🧵")
    input(f"\n{YELLOW}Press Enter to begin the emoji byte adventure... {RESET}")

def emoji_to_bytes(emoji):
    utf8_bytes = emoji.encode("utf-8")
    hex_view = ' '.join(f"{b:02X}" for b in utf8_bytes)
    bin_view = ' '.join(f"{b:08b}" for b in utf8_bytes)
    return utf8_bytes, hex_view, bin_view

def show_emojis():
    emojis = ["😀", "🔥", "🎉", "🚀", "❤️", "👨‍💻", "🇺🇳"]
    print(f"\n{BOLD}{BLUE}🔍 Emoji UTF-8 Breakdown:{RESET}")
    for emoji in emojis:
        utf8, hex_code, bin_code = emoji_to_bytes(emoji)
        print(f"{GREEN}{emoji}{RESET} → {CYAN}{hex_code:<30}{RESET} → {MAGENTA}{bin_code}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Emoji Byte Quiz!{RESET}")
    emoji = "🎯"
    expected = list(emoji.encode("utf-8"))
    user = input(f"{YELLOW}What are the decimal UTF-8 bytes of {emoji}? (space-separated): {RESET}")
    try:
        user_bytes = list(map(int, user.strip().split()))
        if user_bytes == expected:
            print(f"{GREEN}✅ Correct! UTF-8 wins again!{RESET}")
        else:
            print(f"{RED}❌ Oops! Actual bytes: {expected}{RESET}")
    except:
        print(f"{RED}⚠️ Invalid input. Enter space-separated numbers like: 240 159 142 175{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Emojis are part of Unicode and use multiple bytes")
    slow_print("✔ UTF-8 encodes them into 2 to 6 bytes")
    slow_print("✔ You can inspect emoji bytes just like any text character")
    print(f"{GREEN}Now you can read the secret byte-language of emojis! 🎊{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_emojis()
    quiz()
    summary()
