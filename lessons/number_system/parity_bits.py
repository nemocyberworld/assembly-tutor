# lessons/basics/parity_bits.py

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

def print_intro():
    print(f"{BOLD}{MAGENTA}✨ Welcome to Parity Bits: Catching Errors with a Single Bit! 🧠{RESET}")
    slow_print(f"{CYAN}\nImagine sending binary data across space 🚀...")
    slow_print("...but one bit flips by accident! 😱")
    slow_print("Enter the hero: the Parity Bit! 🦸")
    print(f"{CYAN}It helps detect single-bit errors with minimal effort.{RESET}")

def explain_parity():
    print(f"\n{BLUE}📘 What is a Parity Bit?{RESET}")
    slow_print(f"{YELLOW}- It's an extra bit added to binary data to help detect errors.")
    slow_print("- Even parity: total 1s (including parity bit) is EVEN.")
    slow_print("- Odd parity: total 1s (including parity bit) is ODD.{RESET}")

def add_parity(data_bits, mode="even"):
    ones = data_bits.count('1')
    if mode == "even":
        parity = '0' if ones % 2 == 0 else '1'
    else:
        parity = '1' if ones % 2 == 0 else '0'
    return data_bits + parity

def check_parity(data_with_parity, mode="even"):
    ones = data_with_parity.count('1')
    if mode == "even":
        return ones % 2 == 0
    else:
        return ones % 2 == 1

def demo_parity():
    print(f"\n{MAGENTA}💡 Let’s add a parity bit!{RESET}")
    original = format(random.randint(0, 255), '08b')
    mode = random.choice(["even", "odd"])
    with_parity = add_parity(original, mode)

    print(f"Original data: {BOLD}{original}{RESET}")
    print(f"Parity mode: {BOLD}{mode.upper()}{RESET}")
    print(f"Data with parity bit: {GREEN}{with_parity}{RESET}")

    print(f"\n{BLUE}🔍 Let’s check the data...{RESET}")
    is_valid = check_parity(with_parity, mode)
    if is_valid:
        print(f"{GREEN}✅ All good! No errors detected.{RESET}")
    else:
        print(f"{RED}❌ Error! Parity check failed.{RESET}")

    # Let's simulate an error
    index_to_flip = random.randint(0, 8)
    corrupted = list(with_parity)
    corrupted[index_to_flip] = '1' if corrupted[index_to_flip] == '0' else '0'
    corrupted = ''.join(corrupted)

    print(f"\n{YELLOW}😈 Simulating error by flipping bit {index_to_flip}...{RESET}")
    print(f"Corrupted data: {RED}{corrupted}{RESET}")

    is_valid = check_parity(corrupted, mode)
    if not is_valid:
        print(f"{GREEN}✅ Parity bit caught the error!{RESET}")
    else:
        print(f"{RED}⚠️ Parity bit failed to detect the error.{RESET}")

def user_challenge():
    print(f"\n{BOLD}{MAGENTA}🎮 Time to Try It Yourself!{RESET}")
    mode = input(f"{CYAN}Choose parity mode (even/odd): {RESET}").strip().lower()
    while mode not in ["even", "odd"]:
        mode = input(f"{RED}Invalid. Please choose 'even' or 'odd': {RESET}").strip().lower()

    user_data = input(f"{YELLOW}Enter an 8-bit binary number: {RESET}").strip()
    if len(user_data) != 8 or any(c not in "01" for c in user_data):
        print(f"{RED}⚠️ Invalid input. Must be 8 bits of 0s and 1s.{RESET}")
        return

    full_data = add_parity(user_data, mode)
    print(f"{GREEN}With parity bit: {full_data}{RESET}")

    check = check_parity(full_data, mode)
    if check:
        print(f"{CYAN}✅ Your data is valid!{RESET}")
    else:
        print(f"{RED}❌ Oops! Parity check failed.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}🔚 Summary:{RESET}")
    print(f"{CYAN}✔ Parity bits add simple error detection to binary data.")
    print("✔ EVEN parity = total 1s are even.")
    print("✔ ODD parity = total 1s are odd.")
    print("✔ Used in memory, communications, and networks to detect transmission errors.{RESET}")
    print(f"\n{GREEN}You’ve mastered parity bits! 🎉👾{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    print_intro()
    explain_parity()
    demo_parity()
    user_challenge()
    summary()
