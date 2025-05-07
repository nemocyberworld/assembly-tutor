# lessons/basics/hex_checksum.py

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
    print(f"{BOLD}{MAGENTA}🧮 Welcome to Hex Checksum Basics!{RESET}")
    slow_print(f"{CYAN}Checksums help verify data integrity — like spell-check for computers! ✉️")
    slow_print("A checksum is often a simple math formula applied to bytes or hex values.")
    input(f"\n{YELLOW}Press Enter to learn how to make your own checksums... {RESET}")

def calculate_checksum(hex_values):
    """Calculate a simple checksum: sum of bytes mod 256"""
    try:
        total = sum(int(byte, 16) for byte in hex_values)
        checksum = total % 256
        return format(checksum, '02X')
    except ValueError:
        return None

def demo_checksums():
    print(f"\n{BOLD}{BLUE}🔍 Demo: Simple Hex Checksum Calculation{RESET}")
    datasets = [
        ["1A", "2B", "3C"],
        ["10", "20", "30", "40"],
        ["FF", "01"],
        ["12", "34", "56", "78"],
    ]

    for data in datasets:
        checksum = calculate_checksum(data)
        joined = ' '.join(data)
        print(f"{YELLOW}Data: {joined:<15} → Checksum: 0x{checksum}{RESET}")

def explain_checksum():
    print(f"\n{BOLD}{CYAN}🧠 How It Works:{RESET}")
    slow_print(f"{CYAN}✔ Convert each hex byte to decimal")
    slow_print("✔ Add them all together")
    slow_print("✔ Take the total modulo 256 (keep it 1 byte!)")
    slow_print("✔ Convert the result back to hex — that’s your checksum!")

def interactive_calculator():
    print(f"\n{BOLD}{MAGENTA}🧪 Try It Yourself!{RESET}")
    raw = input(f"{YELLOW}Enter hex bytes separated by spaces (e.g., '1A 2B 3C'): {RESET}")
    data = raw.strip().upper().split()

    result = calculate_checksum(data)
    if result:
        print(f"{GREEN}✅ Checksum: 0x{result}{RESET}")
    else:
        print(f"{RED}❌ Invalid input — make sure to use valid hex bytes!{RESET}")

def quiz():
    print(f"\n{BOLD}{BLUE}🎮 Hex Checksum Quiz!{RESET}")
    score = 0
    questions = [
        (["1A", "2B", "3C"], "91"),
        (["FF", "01"], "00"),
        (["10", "20", "30", "40"], "A0"),
        (["12", "34", "56", "78"], "1A"),
    ]
    random.shuffle(questions)

    for i, (hex_list, correct) in enumerate(questions[:3], 1):
        data_str = ' '.join(hex_list)
        user = input(f"\n{YELLOW}Q{i}: What is the checksum of {data_str}? {RESET}\nYour Answer (hex): ").strip().upper()
        if user == correct:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! It's 0x{correct}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Finished! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Checksum Champion! You nailed it!{RESET}")
    elif score == 2:
        print(f"{YELLOW}💪 Nice job! You’re getting the hang of it.{RESET}")
    else:
        print(f"{RED}🔁 Give it another go — practice makes perfect!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ A checksum verifies data hasn't been corrupted")
    slow_print("✔ It's calculated using simple math on hex bytes")
    slow_print("✔ Many protocols use checksums to keep data reliable")
    print(f"{GREEN}Now you can create your own checksums — data protector unlocked! 🛡️{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_checksum()
    demo_checksums()
    interactive_calculator()
    quiz()
    summary()
