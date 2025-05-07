# lessons/basics/unicode_basics.py

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to Unicode Basics!{RESET}")
    slow_print(f"{CYAN}Ever seen strange characters like “�” or emoji squares?")
    slow_print("That means something went wrong with character encoding!")
    slow_print("Let’s fix that by understanding Unicode 🧠")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def unicode_explained():
    print(f"\n{BOLD}{BLUE}📖 What is Unicode?{RESET}")
    slow_print("✔ Unicode is a universal system for representing text.")
    slow_print("✔ It gives each character a unique number, called a code point.")
    slow_print("✔ Code points look like U+0041 (which is 'A') or U+1F600 (😀).")
    slow_print("✔ Unicode includes letters, numbers, symbols, emojis, and more!")

def show_unicode_examples():
    print(f"\n{BOLD}{CYAN}🔎 Unicode Examples{RESET}")
    examples = ['A', 'ñ', '中', '💡', '🐍', '✔', '€']
    for char in examples:
        code_point = ord(char)
        hex_code = f"U+{code_point:04X}"
        print(f"{YELLOW}{char}{RESET} → {GREEN}{hex_code}{RESET}")
        time.sleep(0.1)

def encode_decode_demo():
    print(f"\n{BOLD}{MAGENTA}🎯 Encode and Decode Demo{RESET}")
    text = input(f"{YELLOW}Enter a character or word: {RESET}")
    encoded = text.encode('utf-8')
    hex_bytes = ' '.join(f"{byte:02X}" for byte in encoded)
    print(f"{CYAN}UTF-8 Encoding (hex): {GREEN}{hex_bytes}{RESET}")
    decoded = encoded.decode('utf-8')
    print(f"{CYAN}Decoded back to text: {GREEN}{decoded}{RESET}")

def quiz():
    print(f"\n{BOLD}{BLUE}🎮 Unicode Quiz Time!{RESET}")
    score = 0
    questions = [
        ("What does Unicode assign to every character?", "code point"),
        ("Can Unicode represent emojis? (yes/no)", "yes"),
        ("What function gives you a character’s code point in Python?", "ord"),
        ("What is the Unicode for 'A'?", "U+0041"),
        ("Is Unicode the same as UTF-8? (yes/no)", "no"),
    ]
    random.shuffle(questions)

    for i, (q, a) in enumerate(questions[:3], 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip().lower()
        if user in a.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ The correct answer is: {a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Over! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 Unicode Champion!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👏 Great work! One step closer to fluency!{RESET}")
    else:
        print(f"{RED}📘 Don’t worry—Unicode has a lot to explore!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Unicode gives each character a code point (like U+0041)")
    slow_print("✔ It supports every language, symbol, and emoji")
    slow_print("✔ Python uses Unicode strings by default")
    print(f"{GREEN}Now you're ready to decode the world's text! 🌍{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    unicode_explained()
    show_unicode_examples()
    encode_decode_demo()
    quiz()
    summary()

if __name__ == "__main__":
    run()
