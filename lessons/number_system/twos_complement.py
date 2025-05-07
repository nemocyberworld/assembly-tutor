# lessons/basics/twos_complement.py

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
    slow_print(f"{BOLD}{MAGENTA}➖ Two's Complement: How Computers Understand Negative Numbers! 🧠{RESET}")
    slow_print(f"\n{CYAN}Positive numbers in binary are easy... but what about negatives?")
    slow_print(f"With {YELLOW}Two's Complement{CYAN}, computers can represent {RED}negative{CYAN} numbers using only 1s and 0s!{RESET}\n")

def explain_twos_complement():
    slow_print(f"{BLUE}🎯 Let's break it down with an example: Represent -5 in 8-bit binary{RESET}")
    slow_print(f"\n{BOLD}Step 1: Write +5 in binary →{RESET} {GREEN}00000101{RESET}")
    slow_print(f"{BOLD}Step 2: Invert the bits      →{RESET} {YELLOW}11111010{RESET}")
    slow_print(f"{BOLD}Step 3: Add 1                →{RESET} {RED}11111011{RESET}")
    slow_print(f"\n✅ So, -5 in 8-bit two's complement is: {BOLD}{RED}11111011{RESET}")

def to_twos_complement(n, bits=8):
    """Convert an integer n to a two's complement binary string"""
    if n < 0:
        n = (1 << bits) + n
    return format(n, f'0{bits}b')

def from_twos_complement(bin_str):
    """Convert a binary string in two's complement to a signed int"""
    val = int(bin_str, 2)
    if bin_str[0] == '1':
        val -= (1 << len(bin_str))
    return val

def user_try():
    slow_print(f"\n{BOLD}{MAGENTA}🎮 Try it Yourself!{RESET}")
    slow_print(f"{CYAN}Enter a number between -128 and 127 to see its two's complement form.{RESET}")
    try:
        num = int(input(f"{YELLOW}Your number: {RESET}"))
        if -128 <= num <= 127:
            bin_form = to_twos_complement(num)
            print(f"\n{GREEN}{num} in two's complement (8-bit) → {BOLD}{bin_form}{RESET}")
            slow_print(f"{CYAN}Let’s decode it back...{RESET}")
            back_to_decimal = from_twos_complement(bin_form)
            print(f"{BLUE}Binary {bin_form} = Decimal {back_to_decimal}{RESET}")
        else:
            slow_print(f"{RED}⚠️ Please enter a number between -128 and 127!{RESET}")
    except ValueError:
        slow_print(f"{RED}❌ Invalid input. Please enter a whole number.{RESET}")

def summary():
    slow_print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Two's complement lets us store both {GREEN}positive{CYAN} and {RED}negative{CYAN} integers in binary.")
    slow_print(f"✔ Invert + add 1 = two's complement method.")
    slow_print(f"✔ MSB (leftmost bit) tells us if it’s negative (1) or positive (0).")
    slow_print(f"✔ Used in nearly every computer system today!{RESET}")
    slow_print(f"\n{GREEN}Now you're fluent in the language of computer negativity! 😄{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

if __name__ == "__main__":
    print_intro()
    explain_twos_complement()
    user_try()
    summary()
