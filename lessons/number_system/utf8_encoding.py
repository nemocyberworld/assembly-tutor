# lessons/basics/utf8_encoding.py

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
    print(f"{BOLD}{MAGENTA}🌍 Welcome to UTF-8 Multi-byte Encoding!{RESET}")
    slow_print(f"{CYAN}UTF-8 is capable of encoding all characters from all languages!")
    slow_print("But how does it handle characters that need more than one byte? 🤔 Let’s find out!")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_multi_byte_encoding():
    print(f"\n{BOLD}{BLUE}📖 How UTF-8 Encodes Multi-byte Characters{RESET}")
    slow_print("✔ UTF-8 can encode characters with 1 to 4 bytes.")
    slow_print("✔ ASCII characters (like 'A') fit in 1 byte. But what about characters like ‘ñ’ or ‘🌍’? 🌐")
    slow_print("✔ These require 2, 3, or even 4 bytes.")
    slow_print("✔ UTF-8 uses a special bit pattern to determine how many bytes a character needs.")
    slow_print("Let’s break it down step by step...")

def multi_byte_examples():
    print(f"\n{BOLD}{CYAN}🔍 Multi-byte Examples{RESET}")
    examples = ['ñ', '🌍', '€', '中', '👾']
    
    for char in examples:
        encoded = char.encode('utf-8')
        hex_repr = ' '.join(f"{byte:02X}" for byte in encoded)
        byte_count = len(encoded)
        print(f"{YELLOW}{char}{RESET} → UTF-8 bytes: {GREEN}{hex_repr}{RESET} ({byte_count} byte{'s' if byte_count > 1 else ''})")
        time.sleep(0.1)

def byte_explanation():
    print(f"\n{BOLD}{MAGENTA}🧑‍💻 Understanding the UTF-8 Encoding{RESET}")
    slow_print("Let’s take a deeper look at a few characters.")
    slow_print(f"{CYAN}Character 'ñ' (Unicode U+00F1) uses 2 bytes in UTF-8.")
    slow_print("In binary: 11000011 10110001 (C3 B1).")
    slow_print("The first byte starts with ‘110’ (meaning 2-byte character) and the second byte starts with '10'.")
    slow_print("This pattern helps UTF-8 figure out how many bytes to use for any given character.")
    input(f"\n{YELLOW}Press Enter to continue... {RESET}")

def interactive_encoding():
    print(f"\n{BOLD}{BLUE}🎯 Try Encoding Some Characters!{RESET}")
    char_input = input(f"{YELLOW}Enter a character or emoji to see its UTF-8 encoding: {RESET}")
    encoded = char_input.encode('utf-8')
    hex_bytes = ' '.join(f"{byte:02X}" for byte in encoded)
    byte_count = len(encoded)
    print(f"{CYAN}UTF-8 Encoding (hex): {GREEN}{hex_bytes}{RESET}")
    print(f"{CYAN}This character uses {byte_count} byte{'s' if byte_count > 1 else ''}. {RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 UTF-8 Multi-byte Quiz!{RESET}")
    score = 0
    questions = [
        ("How many bytes does 'ñ' (U+00F1) use in UTF-8?", "2"),
        ("How many bytes does '🌍' (U+1F30D) use in UTF-8?", "4"),
        ("What is the first byte pattern for characters that use 3 bytes in UTF-8?", "1110"),
        ("Can UTF-8 encode emojis? (yes/no)", "yes"),
        ("What is the maximum number of bytes a character can use in UTF-8?", "4"),
    ]
    random.shuffle(questions)

    for i, (q, a) in enumerate(questions[:3], 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip()
        if user == a:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ The correct answer is: {a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 UTF-8 Expert! Great job!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👏 Nice work! Keep practicing!{RESET}")
    else:
        print(f"{RED}📚 Keep going! Practice makes perfect!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 encodes characters from 1 to 4 bytes.")
    slow_print("✔ ASCII characters fit in 1 byte, while complex ones like emojis use 3 or 4 bytes.")
    slow_print("✔ The first few bits in the byte pattern determine how many bytes are needed.")
    print(f"{GREEN}You now have a solid understanding of how UTF-8 handles multi-byte characters! 🌟{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_multi_byte_encoding()
    multi_byte_examples()
    byte_explanation()
    interactive_encoding()
    quiz()
    summary()
