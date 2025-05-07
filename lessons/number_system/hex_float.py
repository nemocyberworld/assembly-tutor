# lessons/basics/hex_float.py

import struct
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
    print(f"{BOLD}{MAGENTA}🌊 Welcome to Hex ↔ Float Conversion!{RESET}")
    slow_print(f"{CYAN}Did you know floating-point numbers can be represented in hex?")
    slow_print("This uses a standard called IEEE 754 — and it's how your computer stores decimals! 💻")
    input(f"\n{YELLOW}Press Enter to dive into floating-point hex decoding... {RESET}")

def float_to_hex(f):
    """Convert float to IEEE 754 hex representation"""
    packed = struct.pack('!f', f)
    return packed.hex().upper()

def hex_to_float(h):
    """Convert IEEE 754 hex to float"""
    try:
        bytes_obj = bytes.fromhex(h)
        return struct.unpack('!f', bytes_obj)[0]
    except:
        return None

def demo_conversions():
    print(f"\n{BOLD}{BLUE}🔍 Demo: Float ↔ Hex (IEEE 754){RESET}")
    floats = [1.0, -2.5, 3.14, 0.0, 10.75]

    for f in floats:
        hex_val = float_to_hex(f)
        print(f"{YELLOW}{f:<6} = 0x{hex_val}{RESET}")
    
    print(f"\n{BOLD}{CYAN}🔁 Let's reverse it!{RESET}")
    hexes = ["3F800000", "C0200000", "4048F5C3", "00000000", "412B0000"]

    for h in hexes:
        f_val = hex_to_float(h)
        print(f"{GREEN}0x{h} = {f_val}{RESET}")

def explain_ieee754():
    print(f"\n{BOLD}{MAGENTA}📘 What is IEEE 754?{RESET}")
    slow_print(f"{CYAN}IEEE 754 is a format that breaks a float into 3 parts:")
    slow_print("✔ Sign bit (1 bit) — positive or negative")
    slow_print("✔ Exponent (8 bits) — scaled power of 2")
    slow_print("✔ Mantissa/Fraction (23 bits) — precision bits")
    slow_print("Together, they store decimal numbers efficiently in binary!")

def interactive_decoder():
    print(f"\n{BOLD}{BLUE}🔧 Float ↔ Hex Playground{RESET}")
    mode = input(f"{YELLOW}Choose mode (float2hex / hex2float): {RESET}").strip().lower()

    if mode == "float2hex":
        try:
            val = float(input("🔢 Enter a float (e.g., 5.5): "))
            result = float_to_hex(val)
            print(f"{GREEN}✅ IEEE 754 Hex: 0x{result}{RESET}")
        except:
            print(f"{RED}❌ Invalid float!{RESET}")
    elif mode == "hex2float":
        h = input("🔢 Enter 8-digit hex (e.g., 40B00000): ").strip()
        result = hex_to_float(h)
        if result is not None:
            print(f"{GREEN}✅ Float: {result}{RESET}")
        else:
            print(f"{RED}❌ Invalid hex input! Must be 8 hex digits.{RESET}")
    else:
        print(f"{RED}❌ Unknown mode. Try again.{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 IEEE 754 Hex Quiz Time!{RESET}")
    questions = [
        ("What is 1.0 in IEEE 754 hex?", "3F800000"),
        ("What is -2.5 in hex?", "C0200000"),
        ("What float is 4048F5C3?", "3.14"),
        ("What float is 412B0000?", "10.75")
    ]
    random.shuffle(questions)
    score = 0

    for i, (q, correct) in enumerate(questions[:3], 1):
        user = input(f"\n{YELLOW}Q{i}: {q} {RESET}\nYour Answer: ").strip().upper()
        if correct in user or user in correct:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! Correct answer: {correct}{RESET}")
    
    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Floating-Point Genius! Well done!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👍 Solid work! You’re getting it!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing — floats are tricky but powerful!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Floats are stored using the IEEE 754 format")
    slow_print("✔ You can convert floats to hex (and back!) with Python's struct module")
    slow_print("✔ Each float = sign + exponent + mantissa (all packed into 32 bits)")
    print(f"{GREEN}Now you can decode floating point numbers like a pro! 🧠{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_ieee754()
    demo_conversions()
    interactive_decoder()
    quiz()
    summary()
