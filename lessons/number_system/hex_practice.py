# lessons/basics/hex_practice.py

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
    print(f"{BOLD}{MAGENTA}🔢 Welcome to Hex Conversion & Debug Reading Practice! 🧠{RESET}")
    slow_print(f"{CYAN}In this lesson, we will practice converting between Hexadecimal, Decimal, and Binary.")
    slow_print(f"Hexadecimal is widely used in debugging, memory addresses, and low-level programming.")
    slow_print(f"Let’s dive into some conversions and debug readings!")
    input(f"\n{YELLOW}Press Enter to begin practicing!{RESET}")

def hex_to_decimal():
    print(f"\n{BOLD}{CYAN}🔄 Hexadecimal to Decimal Conversion:{RESET}")
    slow_print(f"Hexadecimal numbers use a base of 16. Each digit represents powers of 16.")
    hex_num = "0x1F4"  # Example hex value
    decimal_value = int(hex_num, 16)  # Convert hex to decimal
    print(f"{GREEN}Hexadecimal {hex_num} is equal to Decimal {decimal_value}. {RESET}")
    
    # Practice Problem
    slow_print(f"Now it's your turn! Convert the following Hexadecimal number to Decimal:")
    hex_input = input(f"{YELLOW}Enter a Hexadecimal number (e.g., 0x3A): {RESET}").strip()
    try:
        decimal_output = int(hex_input, 16)
        print(f"{GREEN}✅ Correct! {hex_input} is {decimal_output} in Decimal.{RESET}")
    except ValueError:
        print(f"{RED}⚠️ Oops! Invalid Hexadecimal. Please try again using the correct format like 0x1F4.{RESET}")
    
    input(f"\n{YELLOW}Press Enter to continue and practice Decimal to Hex conversion!{RESET}")

def decimal_to_hex():
    print(f"\n{BOLD}{CYAN}🔄 Decimal to Hexadecimal Conversion:{RESET}")
    slow_print(f"Decimal numbers use a base of 10. To convert them to Hexadecimal, we divide by 16.")
    decimal_num = 500  # Example decimal number
    hex_value = hex(decimal_num)  # Convert decimal to hex
    print(f"{GREEN}Decimal {decimal_num} is equal to Hexadecimal {hex_value}. {RESET}")
    
    # Practice Problem
    slow_print(f"Now it's your turn! Convert the following Decimal number to Hexadecimal:")
    decimal_input = input(f"{YELLOW}Enter a Decimal number (e.g., 255): {RESET}").strip()
    try:
        hex_output = hex(int(decimal_input))
        print(f"{GREEN}✅ Correct! {decimal_input} in Decimal is {hex_output} in Hexadecimal.{RESET}")
    except ValueError:
        print(f"{RED}⚠️ Invalid Decimal number! Please try again with a valid number.{RESET}")
    
    input(f"\n{YELLOW}Press Enter to continue and practice Binary to Hex conversion!{RESET}")

def binary_to_hex():
    print(f"\n{BOLD}{CYAN}🔄 Binary to Hexadecimal Conversion:{RESET}")
    slow_print(f"Binary numbers consist of 1s and 0s. We group them in sets of four and convert to Hex.")
    binary_num = "101111110100"  # Example binary value
    hex_value = hex(int(binary_num, 2))  # Convert binary to hex
    print(f"{GREEN}Binary {binary_num} is equal to Hexadecimal {hex_value}. {RESET}")
    
    # Practice Problem
    slow_print(f"Now it's your turn! Convert the following Binary number to Hexadecimal:")
    binary_input = input(f"{YELLOW}Enter a Binary number (e.g., 101010): {RESET}").strip()
    try:
        hex_output = hex(int(binary_input, 2))
        print(f"{GREEN}✅ Correct! {binary_input} in Binary is {hex_output} in Hexadecimal.{RESET}")
    except ValueError:
        print(f"{RED}⚠️ Invalid Binary number! Please try again using only 1s and 0s.{RESET}")
    
    input(f"\n{YELLOW}Press Enter to continue and practice reading Hexadecimal debug values!{RESET}")

def debug_reading():
    print(f"\n{BOLD}{CYAN}🔍 Reading Hexadecimal Debug Values:{RESET}")
    slow_print(f"Debugging often involves interpreting raw memory or register values in Hex.")
    
    # Example debug value
    debug_value = 0xFFEE
    slow_print(f"Debug Output: {YELLOW}0xFFEE{RESET}")
    slow_print(f"This value could represent an address, status register, or data.")
    
    # Let’s say we want to interpret a few bits from this Hex value
    # Convert hex to binary for easier reading
    binary_debug_value = bin(debug_value)[2:].zfill(16)  # Remove '0b' prefix and pad with zeros
    slow_print(f"In binary: {BLUE}{binary_debug_value}{RESET}")
    
    # Practice interpreting a debug value
    slow_print(f"Now it's your turn to read a debug value!")
    debug_input = input(f"{YELLOW}Enter a Hexadecimal debug value (e.g., 0xA4B2): {RESET}").strip()
    try:
        binary_value = bin(int(debug_input, 16))[2:].zfill(16)
        print(f"{GREEN}✅ You entered: {debug_input}. In binary, it's {binary_value}. {RESET}")
    except ValueError:
        print(f"{RED}⚠️ Invalid Hexadecimal value! Please try again.{RESET}")
    
    input(f"\n{YELLOW}Press Enter to finish the lesson and review the key points!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hexadecimal is often used in debugging, especially for interpreting raw memory or register values.")
    slow_print(f"✔ Conversions between Hex, Decimal, and Binary are crucial for understanding how data is represented at low levels.")
    slow_print(f"✔ Mastering these conversions helps you interpret debug values and work with different data formats in programming.")
    print(f"{GREEN}Great job! You’re well on your way to mastering Hexadecimal conversions and debug reading! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    hex_to_decimal()
    decimal_to_hex()
    binary_to_hex()
    debug_reading()
    summary()
