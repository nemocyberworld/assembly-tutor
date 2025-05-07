# lessons/encoding/encoding_quiz.py

import random
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
    print(f"{BOLD}{MAGENTA}🧪 Welcome to the Encoding Challenge!{RESET}")
    slow_print(f"{CYAN}Can you guess the character just by looking at its UTF-8 byte sequence?")
    slow_print("This quiz will sharpen your encoding skills and train your byte-eye! 👀")
    input(f"\n{YELLOW}Press Enter to begin the quiz... {RESET}")

def get_random_utf8_character():
    examples = [
        ('A', 'A'.encode('utf-8')),
        ('é', 'é'.encode('utf-8')),
        ('€', '€'.encode('utf-8')),
        ('你', '你'.encode('utf-8')),
        ('🚀', '🚀'.encode('utf-8')),
        ('💡', '💡'.encode('utf-8')),
        ('ñ', 'ñ'.encode('utf-8')),
        ('Ω', 'Ω'.encode('utf-8')),
        ('🌍', '🌍'.encode('utf-8')),
        ('ß', 'ß'.encode('utf-8'))
    ]
    return random.choice(examples)

def byte_to_hex(byte_seq):
    return ' '.join(f"{b:02X}" for b in byte_seq)

def quiz():
    score = 0
    print(f"\n{BOLD}{BLUE}🎯 Let’s Play: Name That Character!{RESET}")

    for i in range(5):
        print(f"\n{YELLOW}Question {i + 1}:{RESET}")
        char, byte_seq = get_random_utf8_character()
        hex_bytes = byte_to_hex(byte_seq)
        print(f"{CYAN}UTF-8 Bytes: {GREEN}{hex_bytes}{RESET}")
        answer = input(f"{BOLD}What character is this? {RESET}").strip()

        if answer == char:
            print(f"{GREEN}✅ Correct! It's {char}{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! It was {char}{RESET}")

    print(f"\n{BOLD}{MAGENTA}🏁 Quiz Complete! Your Score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🌟 Encoding Master! Incredible memory!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Good job! You're learning fast!{RESET}")
    else:
        print(f"{RED}📚 No worries—review UTF-8 and try again!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 encodes characters using 1–4 bytes.")
    slow_print("✔ Each byte is represented in hexadecimal when viewed at the byte level.")
    slow_print("✔ You can recognize patterns (like 0xC3 or 0xF0) in multibyte characters.")
    print(f"{GREEN}Keep practicing and soon you’ll be reading bytes like books! 📘{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    quiz()
    summary()

if __name__ == "__main__":
    run()
