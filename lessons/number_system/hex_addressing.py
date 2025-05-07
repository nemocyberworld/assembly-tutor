# lessons/basics/hex_addressing.py

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
    print(f"{BOLD}{MAGENTA}🔍 Welcome to Hex Addressing in Memory! 🧠{RESET}")
    slow_print(f"{CYAN}When programming, computers use memory addresses to store data.")
    slow_print("But instead of using long binary numbers, we use hex (hexadecimal) to represent them—it's much shorter and easier to work with!")
    slow_print(f"Hexadecimal numbers represent addresses in the memory space, and each hex digit corresponds to 4 bits (binary).")
    input(f"\n{YELLOW}Press Enter to continue and see how it works in action! {RESET}")

def explain_memory():
    print(f"\n{BOLD}{CYAN}🔢 Memory Addressing with Hexadecimal{RESET}")
    slow_print("Let's say we want to represent some memory addresses. These addresses are locations where the CPU stores data or instructions.")
    slow_print(f"Memory is typically divided into blocks, and each block has a unique address. Here's a small part of the memory addressed using hexadecimal:")

    # Show some example addresses
    example_addresses = ['0x00400000', '0x00400004', '0x00400008', '0x0040000C', '0x00400010']
    for addr in example_addresses:
        print(f"{BLUE}{addr}{RESET} : {YELLOW}Memory Address{RESET}")

def memory_address_demo():
    print(f"\n{BOLD}{BLUE}🎯 Memory Addressing Example:{RESET}")
    # Demonstrate converting an address to binary (8-bit simulation)
    hex_addr = random.choice(['0x00400000', '0x00400004', '0x00400008', '0x0040000C', '0x00400010'])
    bin_addr = bin(int(hex_addr, 16))[2:].zfill(32)
    print(f"{YELLOW}Memory Address: {RESET}{BOLD}{hex_addr}{RESET}")
    print(f"{CYAN}In Binary:  {RESET}{bin_addr}")
    print(f"{GREEN}This is how the memory is accessed by the CPU!{RESET}")

def explain_offset():
    print(f"\n{BOLD}{CYAN}🎯 Understanding Offsets{RESET}")
    slow_print("Often, memory is organized into chunks called blocks or words. These blocks have fixed sizes (like 4 bytes or 8 bytes).")
    slow_print("An offset refers to the number of bytes from the beginning of the block to the specific address you're looking at.")
    slow_print(f"For example, if a memory block starts at address 0x00400000, the next byte in the block might be at address 0x00400004.")
    input(f"\n{YELLOW}Press Enter to see how offsets work in action!{RESET}")

def demo_offsets():
    print(f"{BOLD}{CYAN}🔄 Address with Offsets{RESET}")
    start_addr = 0x00400000
    for offset in range(0, 16, 4):  # Increments of 4 bytes (simulated 4-byte blocks)
        addr = start_addr + offset
        print(f"{MAGENTA}Start Address: 0x{start_addr:08X}  →  Offset: {offset} bytes  →  Address with Offset: 0x{addr:08X}{RESET}")
        time.sleep(0.5)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Hex Addressing Quiz!{RESET}")
    score = 0

    for i in range(3):
        print(f"\n{YELLOW}Question {i+1}:{RESET}")
        hex_addr = format(random.randint(0x400000, 0x500000), 'X')
        user_answer = input(f"🧠 What is the binary equivalent of 0x{BOLD}{hex_addr}{RESET}? ").strip()

        correct_answer = bin(int(hex_addr, 16))[2:].zfill(32)
        if user_answer == correct_answer:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is {correct_answer}{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Perfect! You understand memory addressing in hexadecimal!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Great job! Keep practicing to solidify your understanding!{RESET}")
    else:
        print(f"{RED}💡 Don't worry! Try again and keep learning!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hexadecimal is used to simplify memory addressing.")
    slow_print("✔ Each hex digit represents 4 binary digits, making it a more compact way to express addresses.")
    slow_print("✔ Offsets allow us to refer to specific locations within a memory block or array.")
    print(f"{GREEN}You're on your way to mastering memory management with hex! 🧠💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_memory()
    memory_address_demo()
    explain_offset()
    demo_offsets()
    quiz()
    summary()
