# lessons/basics/signed_vs_unsigned.py

import time
import sys

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
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_intro():
    slow_print(f"{BOLD}{MAGENTA}🔄 Signed vs Unsigned Numbers in Binary 🧠{RESET}")
    slow_print(f"\n{CYAN}Did you know the same 8 bits can mean very different things depending on context?")
    slow_print(f"Let’s explore how numbers can be interpreted as {GREEN}unsigned{CYAN} (only positive) or {RED}signed{CYAN} (positive AND negative)!{RESET}")

def show_example():
    slow_print(f"\n{BLUE}🎯 Example: What does 0b11111111 (255) mean?{RESET}")

    unsigned = int('11111111', 2)
    signed = unsigned if unsigned < 128 else unsigned - 256

    slow_print(f"{YELLOW}Unsigned interpretation: {GREEN}{unsigned} (0 to 255 range){RESET}")
    slow_print(f"{YELLOW}Signed interpretation:   {RED}{signed} (-128 to 127 range){RESET}")

def convert_and_show(value):
    slow_print(f"\n{BOLD}{CYAN}🔎 Converting {value} to binary...{RESET}")

    if value < 0:
        binary = format((value + 256) % 256, '08b')
    else:
        binary = format(value, '08b')

    print(f"{YELLOW}Binary (8-bit): {BOLD}{binary}{RESET}")

    unsigned = int(binary, 2)
    signed = unsigned if unsigned < 128 else unsigned - 256

    print(f"{GREEN}As Unsigned: {unsigned}{RESET}")
    print(f"{RED}As Signed:   {signed}{RESET}")

def user_test():
    slow_print(f"\n{MAGENTA}🎮 Try it Yourself! Enter a value between 0–255 (we’ll decode both ways):{RESET}")
    try:
        raw = int(input(f"{YELLOW}Enter an 8-bit value (0–255): {RESET}"))

        if 0 <= raw <= 255:
            convert_and_show(raw)
        else:
            slow_print(f"{RED}⚠️ Must be between 0 and 255!{RESET}")
    except ValueError:
        slow_print(f"{RED}❌ Invalid input. Please enter a number only.{RESET}")

def summary():
    slow_print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Unsigned numbers go from {BOLD}0 to 255{RESET}")
    slow_print("✔ Signed numbers (two's complement) go from {BOLD}-128 to 127{RESET}")
    slow_print("✔ The most significant bit (MSB) is used for sign in signed numbers")
    slow_print("✔ Same bits ➡️ Different meaning based on interpretation! 🧩{RESET}")
    slow_print(f"\n{GREEN}Now you understand the secret double life of binary numbers! 🕵️‍♂️{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    print_intro()
    show_example()
    user_test()
    summary()

if __name__ == "__main__":
    run()
