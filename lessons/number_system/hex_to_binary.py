# lessons/basics/hex_to_binary.py

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
    print(f"{BOLD}{MAGENTA}🔢 Welcome to Hex ↔ Binary Conversion!{RESET}")
    slow_print(f"{CYAN}Did you know every hex digit maps to exactly 4 bits (binary digits)?")
    slow_print("That makes converting between hex and binary super clean and easy! ✨")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def hex_to_bin(hex_str):
    try:
        bin_str = format(int(hex_str, 16), '0{}b'.format(len(hex_str) * 4))
        return bin_str
    except ValueError:
        return None

def bin_to_hex(bin_str):
    try:
        hex_str = format(int(bin_str, 2), 'X')
        return hex_str
    except ValueError:
        return None

def demo_conversions():
    print(f"\n{BOLD}{BLUE}🔍 Demo: Hex → Binary and Binary → Hex{RESET}")
    examples = ['A', '1F', '3C', '7E', 'FF']

    for hex_val in examples:
        bin_val = hex_to_bin(hex_val)
        print(f"{YELLOW}0x{hex_val} = 0b{bin_val}{RESET}")

    print(f"\n{BOLD}{CYAN}🔁 Let's reverse it!{RESET}")
    bin_examples = ['1010', '00011111', '00111100', '01111110', '11111111']
    for bin_val in bin_examples:
        hex_val = bin_to_hex(bin_val)
        print(f"{GREEN}0b{bin_val} = 0x{hex_val}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Conversion Quiz Time!{RESET}")
    score = 0

    for i in range(5):
        print(f"\n{YELLOW}Question {i+1}:{RESET}")
        mode = random.choice(['hex2bin', 'bin2hex'])

        if mode == 'hex2bin':
            hex_val = format(random.randint(0, 255), 'X')
            correct = hex_to_bin(hex_val)
            user = input(f"🧠 What is the binary of 0x{BOLD}{hex_val}{RESET}? ").strip().replace(" ", "")
            if user == correct:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! It's 0b{correct}{RESET}")

        else:  # bin2hex
            bin_val = format(random.randint(0, 255), '08b')
            correct = bin_to_hex(bin_val)
            user = input(f"🧠 What is the hex of 0b{BOLD}{bin_val}{RESET}? ").strip().upper()
            if user == correct:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! It's 0x{correct}{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🎉 Hex Hero! Amazing work!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Solid effort! Keep practicing!{RESET}")
    else:
        print(f"{RED}💡 No worries! Try again—you’ll get it!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Each hex digit equals 4 binary digits (bits)")
    slow_print("✔ Use Python’s `format()` to convert between them")
    slow_print("✔ Hex makes reading binary simpler for humans")
    print(f"{GREEN}Keep practicing—you're decoding the matrix! 🧠{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    demo_conversions()
    quiz()
    summary()
