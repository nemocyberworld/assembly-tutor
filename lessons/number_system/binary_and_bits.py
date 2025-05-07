# lessons/basics/binary_and_bits.py

import time

# 🎨 Terminal Color Constants
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"
DIM = "\033[2m"

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}💡 Welcome to the Binary and Bits Explorer!{RESET}")
    slow_print(f"{CYAN}Everything in a computer breaks down into 1s and 0s—binary!")
    slow_print("Let's understand how bits represent numbers and how we can manipulate them.")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def print_bit_table(number):
    binary = format(number, '08b')
    slow_print(f"\n{BOLD}{CYAN}🔍 Bit Breakdown for {number} (Decimal):{RESET}")
    slow_print(f"{YELLOW}Binary: 0b{binary}{RESET}")

    print(f"\n{BOLD}{MAGENTA}Bit Position → Power of 2:{RESET}")
    for i in range(7, -1, -1):
        print(f"{BOLD}{i:^5}{RESET}", end=' ')
    print()
    for i in range(7, -1, -1):
        print(f"{BLUE}{2**i:^5}{RESET}", end=' ')
    print()

    print(f"\n{BOLD}{GREEN}Active Bits (1s):{RESET}")
    total = 0
    for i, bit in enumerate(binary):
        power = 2**(7 - i)
        if bit == '1':
            slow_print(f"{GREEN}Bit {7 - i} ON → Adds {power}{RESET}")
            total += power
        else:
            slow_print(f"{DIM}Bit {7 - i} OFF → Adds 0{RESET}")
    slow_print(f"\n{CYAN}✅ Total: {total} (as expected!){RESET}\n")

def bit_toggle_demo():
    print(f"\n{BOLD}{MAGENTA}✨ Bit Toggling Fun ✨{RESET}")
    try:
        num = int(input(f"{YELLOW}Enter a number (0–255): {RESET}"))
        if not (0 <= num <= 255):
            raise ValueError
        print_bit_table(num)
        pos = int(input(f"{CYAN}Which bit would you like to toggle? (0–7): {RESET}"))
        if not (0 <= pos <= 7):
            raise ValueError
        mask = 1 << pos
        toggled = num ^ mask
        slow_print(f"\n{BLUE}Toggling bit {pos} with XOR mask {mask} (0b{mask:08b})...{RESET}")
        slow_print(f"{YELLOW}New number: {toggled} (Binary: 0b{toggled:08b}){RESET}")
        print_bit_table(toggled)
    except ValueError:
        print(f"{RED}❌ Invalid input. Please enter numbers in range.{RESET}")

def interactive_bits():
    while True:
        print(f"\n{BOLD}Choose an option:{RESET}")
        print("1. View bit positions of a number")
        print("2. Toggle a bit (ON ↔ OFF)")
        print("3. Exit")
        choice = input(f"{CYAN}Enter choice (1/2/3): {RESET}")

        if choice == "1":
            try:
                n = int(input(f"{YELLOW}Enter a number (0–255): {RESET}"))
                if not (0 <= n <= 255):
                    raise ValueError
                print_bit_table(n)
            except ValueError:
                print(f"{RED}❌ Please enter a valid number from 0 to 255.{RESET}")
        elif choice == "2":
            bit_toggle_demo()
        elif choice == "3":
            print(f"{GREEN}👋 See you next time, Bit Wizard!{RESET}")
            break
        else:
            print(f"{RED}❌ Invalid choice! Please try again.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Binary uses just 0 and 1 to represent all numbers and data.")
    slow_print("✔ Each bit represents a power of 2, from 2⁰ to 2⁷ in a byte.")
    slow_print("✔ You can toggle bits using XOR and bit masks.")
    print(f"{GREEN}Now you can see the magic in every byte! 🧙‍♂️{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    interactive_bits()
    summary()

if __name__ == "__main__":
    run()
