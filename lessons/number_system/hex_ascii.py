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
    print(f"{BOLD}{MAGENTA}🔡 Welcome to Hex & ASCII!{RESET}")
    slow_print(f"{CYAN}Every letter, number, and symbol on your keyboard has a number behind it.")
    slow_print("That number is part of a system called ASCII (American Standard Code for Information Interchange).")
    slow_print("We often represent these codes using hexadecimal for readability.\n")
    input(f"{YELLOW}Press Enter to begin! {RESET}")

def show_ascii_table():
    print(f"\n{BOLD}{BLUE}📘 Sample ASCII Table (Decimal, Hex, Character):{RESET}")
    print(f"{MAGENTA}{'Char':<6}{'Dec':<6}{'Hex':<6}{RESET}")
    for code in range(32, 48):  # Printable characters
        char = chr(code)
        dec = code
        hex_val = format(code, '02X')
        print(f"{GREEN}{char:<6}{dec:<6}{hex_val:<6}{RESET}")

def convert_demo():
    print(f"\n{BOLD}{CYAN}🔄 Let's Try Some Conversions!{RESET}")
    examples = ['A', 'z', '0', '?', ' ']

    for char in examples:
        dec = ord(char)
        hex_val = format(dec, '02X')
        print(f"{YELLOW}'{char}' -> Decimal: {dec}, Hex: 0x{hex_val}{RESET}")

def ascii_quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 ASCII & HEX PRACTICE!{RESET}")
    score = 0

    for i in range(5):
        mode = random.choice(["char2hex", "hex2char"])
        print(f"\n{YELLOW}Question {i+1}/5:{RESET}")

        if mode == "char2hex":
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?$@")
            answer = format(ord(char), '02X')
            user = input(f"🔠 What is the hex value of '{BOLD}{char}{RESET}'? ").strip().upper()
            if user == answer:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! It's 0x{answer}.{RESET}")

        else:  # hex2char
            char = random.choice("abcdefghijklmnopqrstuvwxyz.,:;'!?")
            hex_val = format(ord(char), '02X')
            user = input(f"🔡 What character is 0x{BOLD}{hex_val}{RESET}? ").strip()
            if user == char:
                print(f"{GREEN}✅ Spot on!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ It's '{char}'.{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Finished! Your Score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🎉 ASCII Ace! You crushed it!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Nice work! You're on your way!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing, future coder!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}🔚 Summary:{RESET}")
    print(f"{CYAN}✔ ASCII assigns numbers to characters (like 'A' = 65)")
    print("✔ We often use hexadecimal (like 'A' = 0x41) for compactness")
    print("✔ Python’s `ord()` and `chr()` let you switch between them")
    print("✔ `format(n, 'X')` shows the hex value of a number{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_ascii_table()
    convert_demo()
    ascii_quiz()
    summary()

if __name__ == "__main__":
    run()
