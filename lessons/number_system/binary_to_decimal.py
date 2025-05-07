# lessons/basics/binary_to_decimal.py

import time

# 🌈 Terminal Color Constants
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def binary_to_decimal(binary_str):
    slow_print(f"{CYAN}🔍 Converting binary to decimal...{RESET}")
    total = 0
    for i, digit in enumerate(reversed(binary_str)):
        if digit not in "01":
            print(f"{RED}❌ Invalid binary digit: {digit}{RESET}")
            return None
        value = int(digit) * (2 ** i)
        slow_print(f"{YELLOW}{digit} × 2^{i} = {value}{RESET}")
        total += value
    slow_print(f"\n{GREEN}✅ Decimal value: {total}{RESET}\n")
    return total

def decimal_to_binary(decimal_num):
    slow_print(f"{CYAN}🔁 Converting decimal to binary...{RESET}")
    if decimal_num == 0:
        slow_print(f"{GREEN}✅ Binary: 0b0{RESET}")
        return "0"

    bits = []
    while decimal_num > 0:
        bit = decimal_num % 2
        bits.append(str(bit))
        slow_print(f"{BLUE}{decimal_num} ÷ 2 = {decimal_num // 2}, remainder = {bit}{RESET}")
        decimal_num //= 2
    binary_str = ''.join(reversed(bits))
    slow_print(f"\n{GREEN}✅ Binary: 0b{binary_str}{RESET}\n")
    return binary_str

def interactive_demo():
    print(f"{BOLD}{MAGENTA}\n✨ Welcome to Binary ↔ Decimal Converter! ✨{RESET}\n")
    while True:
        print(f"{BOLD}Choose an option:{RESET}")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Exit")
        choice = input(f"{CYAN}Enter choice (1/2/3): {RESET}")

        if choice == "1":
            binary_input = input(f"{YELLOW}Enter a binary number (e.g. 1011): {RESET}")
            binary_to_decimal(binary_input.strip())
        elif choice == "2":
            try:
                decimal_input = int(input(f"{YELLOW}Enter a decimal number (e.g. 13): {RESET}"))
                decimal_to_binary(decimal_input)
            except ValueError:
                print(f"{RED}❌ Please enter a valid integer!{RESET}")
        elif choice == "3":
            print(f"{GREEN}👋 Goodbye! Keep coding in binary!{RESET}")
            break
        else:
            print(f"{RED}❌ Invalid choice, try again!{RESET}")
        print()
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
# Run the lesson
if __name__ == "__main__":
    interactive_demo()
