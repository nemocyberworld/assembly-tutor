# lessons/basics/ascii_table.py

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
    print(f"{BOLD}{MAGENTA}🧮 Welcome to the ASCII Table Explorer!{RESET}")
    slow_print(f"{CYAN}ASCII maps every character — even invisible ones — to numbers!")
    slow_print("There are 128 standard ASCII codes, from 0 to 127.")
    input(f"\n{YELLOW}Press Enter to reveal the table... {RESET}")

def show_control_characters():
    print(f"\n{BOLD}{BLUE}🔒 Control Characters (0–31){RESET}")
    control_names = [
        "NUL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL",
        "BS", "TAB", "LF", "VT", "FF", "CR", "SO", "SI",
        "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB",
        "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US"
    ]
    for i in range(32):
        print(f"{YELLOW}{i:3} {RESET}= {RED}{control_names[i]}{RESET}")
        time.sleep(0.02)

def show_printable_characters():
    print(f"\n{BOLD}{GREEN}🔤 Printable Characters (32–126){RESET}")
    for i in range(32, 127):
        print(f"{CYAN}{i:3} {RESET}= '{GREEN}{chr(i)}{RESET}'", end='   ')
        if (i - 31) % 6 == 0:
            print()
    print()

def ascii_lookup():
    print(f"\n{BOLD}{MAGENTA}🔍 ASCII Lookup Tool{RESET}")
    user_input = input(f"{YELLOW}Enter a character or number (0–127): {RESET}").strip()

    if user_input.isdigit():
        val = int(user_input)
        if 0 <= val <= 127:
            if val < 32:
                print(f"{RED}Code {val} = Control Character (non-printable){RESET}")
            else:
                print(f"{GREEN}Code {val} = '{chr(val)}'{RESET}")
        else:
            print(f"{RED}🚫 Out of ASCII range (0–127){RESET}")
    elif len(user_input) == 1:
        print(f"{GREEN}Character '{user_input}' = ASCII {ord(user_input)}{RESET}")
    else:
        print(f"{RED}❌ Please enter just one character or a number.{RESET}")

def quiz():
    print(f"\n{BOLD}{BLUE}🎮 ASCII Table Quiz!{RESET}")
    score = 0

    for i in range(3):
        mode = random.choice(['char_to_code', 'code_to_char'])

        if mode == 'char_to_code':
            char = random.choice("ABCxyz!?$@")
            correct = ord(char)
            user = input(f"{YELLOW}Q{i+1}: What is the ASCII code for '{char}'? {RESET}")
            if user.strip() == str(correct):
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ It's {correct}{RESET}")

        else:
            code = random.randint(32, 126)
            correct = chr(code)
            user = input(f"{YELLOW}Q{i+1}: What character is ASCII {code}? {RESET}")
            if user.strip() == correct:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ It's '{correct}'{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Final Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 ASCII Master!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👏 Good job! Keep it up!{RESET}")
    else:
        print(f"{RED}📚 No worries—try again! Practice makes perfect.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ASCII covers characters 0 to 127.")
    slow_print("✔ Codes 0–31 are control characters (e.g., newline, tab).")
    slow_print("✔ Codes 32–126 are printable characters.")
    slow_print("✔ Use `ord()` and `chr()` in Python to convert easily.")
    print(f"{GREEN}Now you know what your keyboard is really saying! 😎{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    show_control_characters()
    show_printable_characters()
    ascii_lookup()
    quiz()
    summary()
