# lessons/basics/char_encoding_diff.py

import time
import random

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to the Differences: ASCII vs UTF-8 vs Unicode!{RESET}")
    slow_print(f"{CYAN}Let’s break down the major character encodings: ASCII, UTF-8, and Unicode.")
    slow_print("They’re all used to represent text, but they have key differences. Let's explore! 🔍")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_ascii():
    print(f"\n{BOLD}{BLUE}📖 What is ASCII?{RESET}")
    slow_print(f"{CYAN}✔ ASCII (American Standard Code for Information Interchange) is a 7-bit encoding system.")
    slow_print("✔ It supports 128 characters, including letters, digits, punctuation, and control characters.")
    slow_print("✔ ASCII only covers English characters (A-Z, a-z), digits (0-9), and some symbols.")
    slow_print(f"{CYAN}Example: 'A' = {GREEN}0x41{RESET} in ASCII (which is 65 in decimal).")
    slow_print(f"{RED}Limitations: ASCII cannot handle characters like ‘ñ’ or ‘中’. 🛑{RESET}")

def explain_utf8():
    print(f"\n{BOLD}{BLUE}📖 What is UTF-8?{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 is a variable-length encoding using 1 to 4 bytes per character.")
    slow_print("✔ It's backward compatible with ASCII (1 byte for ASCII characters).")
    slow_print("✔ UTF-8 can encode any Unicode character — including emojis and global scripts.")
    slow_print(f"{CYAN}Example: 'A' = {GREEN}0x41{RESET} in UTF-8 (same as ASCII).")
    slow_print(f"{CYAN}'🌍' is encoded as: {GREEN}0xF0 0x9F 0x8C 0x8D{RESET} in UTF-8 (4 bytes).")
    slow_print("✔ UTF-8 is the most common encoding used on the web. 🌐")

def explain_unicode():
    print(f"\n{BOLD}{BLUE}📖 What is Unicode?{RESET}")
    slow_print(f"{CYAN}✔ Unicode is a universal character set that includes almost every symbol in every language.")
    slow_print("✔ Each character has a unique code point written as U+ followed by its hex value.")
    slow_print(f"✔ Unicode includes alphabets, scripts, emojis, and more.")
    slow_print(f"{CYAN}Example: 'A' = {GREEN}U+0041{RESET}, same as ASCII and UTF-8 for this character.")
    slow_print("✔ Unicode defines over 143,000 characters. 📚")

def compare_encodings():
    print(f"\n{BOLD}{CYAN}🔍 Comparing ASCII, UTF-8, and Unicode{RESET}")
    slow_print(f"{CYAN}✔ ASCII: Limited to 128 characters, good for plain English text.")
    slow_print("✔ UTF-8: Efficient and flexible, supports all Unicode characters.")
    slow_print("✔ Unicode: The full character set; UTF-8 is one way of encoding it.")
    slow_print("\nLet’s see the difference in action with some examples!")

    slow_print(f"{CYAN}ASCII supports: {GREEN}'A', 'B', '1', '@'{RESET}")
    slow_print(f"{CYAN}Unicode includes: {GREEN}'A', 'B', '1', '@', '中', '💡', '🌍'{RESET}")

def interactive_encoding():
    print(f"\n{BOLD}{MAGENTA}🎯 Try Encoding Different Characters!{RESET}")
    char_input = input(f"{YELLOW}Enter a character or emoji to see its encoding in ASCII, UTF-8, and Unicode: {RESET}").strip()

    # ASCII encoding (only valid if in ASCII range)
    if len(char_input) == 1 and ord(char_input) < 128:
        ascii_encoding = f"0x{ord(char_input):02X}"
    else:
        ascii_encoding = f"{RED}Not Supported{RESET}"

    # UTF-8 encoding
    utf8_encoded = char_input.encode('utf-8')
    utf8_hex = ' '.join(f"0x{byte:02X}" for byte in utf8_encoded)

    # Unicode code point
    unicode_code_point = f"U+{ord(char_input):04X}"

    print(f"\n{CYAN}Encoding Results:{RESET}")
    print(f"{GREEN}ASCII: {ascii_encoding}")
    print(f"{GREEN}UTF-8: {utf8_hex}")
    print(f"{GREEN}Unicode: {unicode_code_point}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Encoding Quiz Time!{RESET}")
    score = 0
    questions = [
        ("What’s the maximum number of bytes UTF-8 can use?", "4"),
        ("Does ASCII support non-English characters? (yes/no)", "no"),
        ("Can UTF-8 encode emojis? (yes/no)", "yes"),
        ("What is the Unicode for 'A'?", "U+0041"),
        ("Is Unicode a character set or an encoding system?", "character set"),
    ]
    random.shuffle(questions)

    for i, (q, a) in enumerate(questions[:3], 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip().lower()
        if user == a.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ The correct answer is: {GREEN}{a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 Encoding Expert! Well done!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👏 Great job! Keep practicing!{RESET}")
    else:
        print(f"{RED}📘 Keep going! Practice makes perfect!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ASCII is a 7-bit encoding for basic English characters.")
    slow_print("✔ UTF-8 is a versatile encoding that supports all Unicode characters using 1 to 4 bytes.")
    slow_print("✔ Unicode is a massive character set, including global scripts, symbols, and emojis.")
    print(f"{GREEN}Now you understand the differences between ASCII, UTF-8, and Unicode! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explain_ascii()
    explain_utf8()
    explain_unicode()
    compare_encodings()
    interactive_encoding()
    quiz()
    summary()

if __name__ == "__main__":
    run()
