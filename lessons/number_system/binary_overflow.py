# lessons/basics/binary_overflow.py

import sys
import time

# 🎨 Terminal color styling
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
    print()  # for newline

def show_binary(num, bits=8):
    """Format number as signed binary with fixed width."""
    return format(num & ((1 << bits) - 1), f'0{bits}b')

def intro():
    slow_print(f"{BOLD}{MAGENTA}💥 Binary Overflow & Two’s Complement Basics 💥{RESET}")
    slow_print(f"{CYAN}\nHave you ever added 1 to 255 in an 8-bit system and got... 0? That's overflow! ⚠️")
    slow_print(f"Let's explore how computers represent negative numbers and what overflow really means.{RESET}")

def overflow_demo():
    slow_print(f"\n{YELLOW}➡️  8-bit unsigned max value is 255 (0b11111111){RESET}")
    slow_print(f"{BLUE}Let's add 1 to it:{RESET}")
    result = (255 + 1) & 0xFF  # Simulate 8-bit wrap-around
    slow_print(f"  255 + 1 = {result} (Binary: {show_binary(result)})")
    slow_print(f"{RED}⚠️ This is overflow! We've wrapped back to 0!{RESET}")

def twos_complement_basics():
    slow_print(f"\n{YELLOW}➡️ Representing Negative Numbers in Binary (Two’s Complement):{RESET}")
    slow_print(f"{CYAN}In an 8-bit signed system, range is -128 to 127:{RESET}")
    slow_print(f"{GREEN}  +1   = {show_binary(1)}")
    slow_print(f"  -1   = {show_binary(-1)} (Two's complement)")
    slow_print(f"  -128 = {show_binary(-128)}")
    slow_print(f"  127  = {show_binary(127)}{RESET}")
    
    slow_print(f"\n{BLUE}🔄 Two's Complement Trick:{RESET}")
    slow_print("To get -N:")
    slow_print("  1. Convert N to binary")
    slow_print("  2. Invert all bits")
    slow_print("  3. Add 1")

def try_it_yourself():
    slow_print(f"\n{BOLD}{MAGENTA}🧪 Try It Yourself!{RESET}")
    num = int(input(f"{YELLOW}Enter a number between -128 and 127: {RESET}"))
    bits = 8
    bin_result = show_binary(num, bits)
    slow_print(f"{CYAN}Binary ({bits}-bit two's complement): {BOLD}{bin_result}{RESET}")
    
    # Reverse the conversion
    if bin_result[0] == '1':
        slow_print(f"{RED}Note: This starts with '1', so it's negative in two’s complement!{RESET}")
        true_val = int(bin_result, 2) - (1 << bits)
    else:
        true_val = int(bin_result, 2)
    slow_print(f"{GREEN}That’s equal to: {true_val}{RESET}")

def summary():
    slow_print(f"\n{BOLD}{BLUE}🧠 Summary:{RESET}")
    slow_print(f"{CYAN}• Binary overflow happens when a number exceeds the max for a bit-width.")
    slow_print(f"• Two’s complement allows representation of negatives without special bits.")
    slow_print(f"• Always be careful with fixed-width binary math — bugs love overflow! 🐛{RESET}")
    slow_print(f"\n{BOLD}{GREEN}Well done! You just unlocked the mystery of binary negatives. 💡{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    overflow_demo()
    twos_complement_basics()
    try_it_yourself()
    summary()

if __name__ == "__main__":
    run()
