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
    slow_print("✔ ASCII (American Standard Code for Information Interchange) is a 7-bit encoding system.")
    slow_print("✔ It supports 128 characters, including letters, digits, punctuation, and control characters.")
    slow_print("✔ ASCII only covers English characters (A-Z, a-z), digits (0-9), and some symbols.")
    slow_print(f"{CYAN}Example: 'A' = {GREEN}0x41{RESET} in ASCII (which is 65 in decimal).")
    slow_print(f"{CYAN}Limitations: It cannot handle non-English characters like ‘ñ’ or ‘中’. 🛑")

def explain_utf8():
    print(f"\n{BOLD}{BLUE}📖 What is UTF-8?{RESET}")
    slow_print("✔ UTF-8 is a variable-length encoding that can use 1 to 4 bytes per character.")
    slow_print("✔ It’s backward compatible with ASCII (1 byte for ASCII characters).")
    slow_print("✔ UTF-8 can encode any Unicode character, including emojis, and characters from multiple languages.")
    slow_print(f"{CYAN}Example: 'A' = {GREEN}0x41{RESET} in UTF-8 (same as ASCII).")
    slow_print(f"{CYAN}But a character like '🌍' is encoded as {GREEN}0xF0 0x9F 0x8C 0x8D{RESET} in UTF-8 (4 bytes).")
    slow_print(f"{CYAN}UTF-8 is widely used on the web due to its efficiency and versatility. 🌐")

def explain_unicode():
    print(f"\n{BOLD}{BLUE}📖 What is Unicode?{RESET}")
    slow_print("✔ Unicode is a universal character encoding standard that aims to cover all languages and symbols.")
    slow_print("✔ It includes characters from virtually every writing system on earth, along with special symbols and emojis.")
    slow_print("✔ Unicode code points are written as U+ followed by the code (e.g., U+0041 for 'A').")
    slow_print(f"{CYAN}Example: 'A' = {GREEN}U+0041{RESET} in Unicode, no different from UTF-8 or ASCII for this character.")
    slow_print(f"{CYAN}Unicode defines over 143,000 characters, which is much larger than ASCII or UTF-8 alone. 📚")

def compare_encodings():
    print(f"\n{BOLD}{CYAN}🔍 Comparing ASCII, UTF-8, and Unicode{RESET}")
    slow_print(f"✔ ASCII is limited to 128 characters and is mostly used for English text.")
    slow_print(f"✔ UTF-8 is flexible and can encode all Unicode characters using 1 to 4 bytes.")
    slow_print(f"✔ Unicode provides a universal character set, but UTF-8 is one of its encoding forms.")
    slow_print(f"\nLet’s see the difference in action with some examples!")
    slow_print(f"\nASCII only supports these characters: {GREEN}'A', 'B', '1', '@'{RESET}")
    slow_print(f"\nUnicode includes all of these (and many more!): {GREEN}'A', 'B', '1', '@', '中', '💡', '🌍'{RESET}")
    
def interactive_encoding():
    print(f"\n{BOLD}{MAGENTA}🎯 Try Encoding Different Characters!{RESET}")
    char_input = input(f"{YELLOW}Enter a character or emoji to see its encoding in ASCII, UTF-8, and Unicode: {RESET}")
    
    # ASCII encoding (only for ASCII characters)
    if ord(char_input) < 128:
        ascii_encoding = f"ASCII: {hex(ord(char_input))}"
    else:
        ascii_encoding = f"ASCII: {RED}Not Supported{RESET}"
    
    # UTF-8 encoding
    utf8_encoded = char_input.encode('utf-8')
    utf8_hex = ' '.join(f"{byte:02X}" for byte in utf8_encoded)
    
    # Unicode code point
    unicode_code_point = f"U+{ord(char_input):04X}"
    
    print(f"{CYAN}Encoding Results:{RESET}")
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
        if user == a:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ The correct answer is: {a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 Encoding Expert! Well done!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👏 Great job! Keep practicing!{RESET}")
    else:
        print(f"{RED}📘 Keep going! Practice makes perfect!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ASCII is a 7-bit encoding supporting only 128 characters, mainly for English.")
    slow_print(f"✔ UTF-8 is flexible, using 1 to 4 bytes, and is backward compatible with ASCII.")
    slow_print(f"✔ Unicode is a universal character set that includes almost every character from every language.")
    print(f"{GREEN}You now understand the differences between ASCII, UTF-8, and Unicode! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_ascii()
    explain_utf8()
    explain_unicode()
    compare_encodings()
    interactive_encoding()
    quiz()
    summary()
