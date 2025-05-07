# lessons/basics/utf8_intro.py

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
    print(f"{BOLD}{MAGENTA}🌍 Welcome to UTF-8 Basics!{RESET}")
    slow_print(f"{CYAN}ASCII is great for English... but what about emojis, accents, or other languages?")
    slow_print("That’s where UTF-8 shines! It's the world’s most popular text encoding.")
    input(f"\n{YELLOW}Press Enter to explore UTF-8... {RESET}")

def utf8_demo():
    print(f"\n{BOLD}{BLUE}🔍 UTF-8 in Action{RESET}")
    examples = ['A', 'é', 'ñ', '€', '✓', '😄']

    for char in examples:
        encoded = char.encode('utf-8')
        hex_repr = ' '.join(f"{byte:02X}" for byte in encoded)
        print(f"{YELLOW}'{char}'{RESET} → UTF-8 bytes: {GREEN}{hex_repr}{RESET}")
        time.sleep(0.1)

def utf8_explain():
    print(f"\n{BOLD}{CYAN}💡 How UTF-8 Works{RESET}")
    slow_print("✔ ASCII characters use 1 byte (same as ASCII)")
    slow_print("✔ Characters beyond ASCII use 2–4 bytes")
    slow_print("✔ All languages, emojis, and symbols can be encoded!")
    slow_print("✔ It's backward compatible with ASCII 🎉")

def interactive_encode():
    print(f"\n{BOLD}{MAGENTA}🎯 Try It Yourself: Encode Text to UTF-8 Hex{RESET}")
    user_input = input(f"{YELLOW}Enter a word or emoji: {RESET}")
    encoded = user_input.encode('utf-8')
    hex_bytes = ' '.join(f"{byte:02X}" for byte in encoded)
    print(f"{GREEN}UTF-8 bytes: {hex_bytes}{RESET}")

def quiz():
    print(f"\n{BOLD}{BLUE}🎮 UTF-8 Quiz!{RESET}")
    score = 0
    questions = [
        ("How many bytes does 'A' take in UTF-8?", "1"),
        ("Is UTF-8 compatible with ASCII? (yes/no)", "yes"),
        ("Can UTF-8 represent emojis? (yes/no)", "yes"),
        ("What does 'UTF' stand for in UTF-8?", "Unicode Transformation Format"),
        ("How many bytes can a UTF-8 character use at most?", "4"),
    ]
    random.shuffle(questions)

    for i, (q, a) in enumerate(questions[:3], 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip().lower()
        if user in a.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Oops! The answer is: {a}{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 UTF-8 Genius! Well done!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👏 Great job! Keep going!{RESET}")
    else:
        print(f"{RED}💡 Don’t worry—UTF-8 takes time to master!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 encodes all characters in all languages using 1 to 4 bytes")
    slow_print("✔ ASCII is fully included in UTF-8")
    slow_print("✔ Python uses UTF-8 by default, so you’re already using it!")
    print(f"{GREEN}Keep exploring the world of characters — from A to 😄!{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    utf8_demo()
    utf8_explain()
    interactive_encode()
    quiz()
    summary()
