# lessons/basics/hex_intro.py

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
    print(f"{BOLD}{MAGENTA}💡 Welcome to the Wonderful World of Hexadecimal!{RESET}")
    slow_print(f"{CYAN}Hexadecimal (or just 'hex') is a base-16 number system.")
    slow_print("It uses the digits 0-9 and the letters A-F.")
    slow_print("This makes it super useful for representing binary in a compact form.\n")
    input(f"{YELLOW}Press Enter to begin the lesson! {RESET}")

def explain_hex():
    print(f"{BLUE}{BOLD}\n🔍 Why Hexadecimal?{RESET}")
    print(f"{CYAN}- 1 hex digit = 4 binary digits (bits)")
    print("- Easier for humans to read than binary")
    print("- Used in color codes (#FF5733), memory addresses, and debugging\n")

    print(f"{GREEN}Decimal to Hex Examples:{RESET}")
    for num in [10, 15, 31, 255]:
        print(f"{YELLOW}{num} => 0x{format(num, 'X')}{RESET}")

    print(f"\n{MAGENTA}Binary to Hex Example:{RESET}")
    binary = '11110000'
    decimal = int(binary, 2)
    hex_val = format(decimal, 'X')
    print(f"{CYAN}Binary: {binary} => Decimal: {decimal} => Hex: 0x{hex_val}{RESET}")

def hex_quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 HEX PRACTICE TIME!{RESET}")
    score = 0

    for i in range(5):
        mode = random.choice(["dec2hex", "hex2dec"])
        print(f"\n{YELLOW}Question {i+1}/5:{RESET}")

        if mode == "dec2hex":
            num = random.randint(0, 255)
            answer = format(num, 'X')
            user = input(f"🔢 What is the hex value of {BOLD}{num}{RESET}? (Use uppercase A-F): ").strip()
            if user.upper() == answer:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! It’s 0x{answer}.{RESET}")

        else:
            num = random.randint(0, 255)
            hex_val = format(num, 'X')
            user = input(f"🧠 What is the decimal value of 0x{BOLD}{hex_val}{RESET}? ").strip()
            if user.isdigit() and int(user) == num:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Incorrect. It's {num}.{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Done! Your Score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🎉 Hex Hero! You nailed it!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Great job! A bit more practice and you’re there!{RESET}")
    else:
        print(f"{RED}💡 Keep learning — it gets easier!{RESET}")

def review():
    print(f"\n{BOLD}{CYAN}📘 Quick Recap:{RESET}")
    print(f"{CYAN}✔ Hex uses 0-9 and A-F (base-16)")
    print("✔ 1 hex digit = 4 binary bits")
    print("✔ Use format(n, 'X') to get uppercase hex in Python")
    print("✔ Hex is cleaner than binary for large numbers{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_hex()
    hex_quiz()
    review()
