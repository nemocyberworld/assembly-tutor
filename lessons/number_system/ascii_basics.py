# lessons/basics/ascii_basics.py

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
    print(f"{BOLD}{MAGENTA}🔤 Welcome to ASCII Basics!{RESET}")
    slow_print(f"{CYAN}Ever wonder how text is stored in computers?")
    slow_print("It all starts with ASCII — a system where each character has a number!")
    input(f"\n{YELLOW}Press Enter to dive into ASCII... {RESET}")

def show_ascii_table():
    print(f"\n{BOLD}{BLUE}📊 ASCII Table Highlights (A–Z, a–z, 0–9){RESET}")
    slow_print(f"{CYAN}Here's how characters map to numbers in ASCII:")
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
        print(f"{YELLOW}'{ch}'{RESET} = {GREEN}{ord(ch)}{RESET}")
        time.sleep(0.01)

def char_to_ascii():
    print(f"\n{BOLD}{MAGENTA}🔡 Convert Characters to ASCII{RESET}")
    text = input(f"{YELLOW}Enter some text: {RESET}").strip()
    print(f"{CYAN}ASCII Codes:{RESET}")
    for ch in text:
        print(f"'{ch}' → {GREEN}{ord(ch)}{RESET}")

def ascii_to_char():
    print(f"\n{BOLD}{CYAN}🔢 Convert ASCII to Characters{RESET}")
    codes = input(f"{YELLOW}Enter space-separated ASCII values (e.g., 72 105): {RESET}").strip().split()
    print(f"{GREEN}Characters: ", end='')
    for code in codes:
        try:
            num = int(code)
            if 0 <= num <= 127:
                print(chr(num), end='')
            else:
                print(f"{RED} ? {RESET}", end='')
        except:
            print(f"{RED} ? {RESET}", end='')
    print(RESET)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 ASCII Quiz Time!{RESET}")
    score = 0
    for i in range(3):
        mode = random.choice(['char_to_ascii', 'ascii_to_char'])

        if mode == 'char_to_ascii':
            ch = random.choice("ABCxyz!?")
            answer = ord(ch)
            user = input(f"\n{YELLOW}Q{i+1}: What is the ASCII code for '{ch}'? {RESET}")
            if user.strip() == str(answer):
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ It's {answer}{RESET}")

        else:
            num = random.choice([65, 66, 97, 98, 33, 63])
            answer = chr(num)
            user = input(f"\n{YELLOW}Q{i+1}: What character is ASCII {num}? {RESET}")
            if user.strip() == answer:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ It's '{answer}'{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 ASCII Ace! Well done!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Nice! Just one mistake!{RESET}")
    else:
        print(f"{RED}📚 Keep practicing! You’ll get it!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ASCII stands for American Standard Code for Information Interchange")
    slow_print("✔ Each character is stored as a number from 0 to 127")
    slow_print("✔ Use `ord()` to convert characters to numbers")
    slow_print("✔ Use `chr()` to convert numbers back to characters")
    print(f"{GREEN}ASCII is the ABC of digital text — now you know how to speak computer! 🤖{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_ascii_table()
    char_to_ascii()
    ascii_to_char()
    quiz()
    summary()

if __name__ == "__main__":
    run()
