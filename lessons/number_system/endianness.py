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
    print(f"{BOLD}{MAGENTA}💡 Welcome to the Endianness Lesson!{RESET}")
    slow_print(f"{CYAN}In computing, endianness refers to the order in which bytes are stored in memory. 🧠")
    slow_print(f"{CYAN}We’ll explore two types of endianness: Big-Endian and Little-Endian.")
    slow_print(f"{CYAN}Let’s dive into how these work and why they matter! 🌟")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def endianness_explanation():
    slow_print(f"\n{BOLD}{BLUE}🔍 What is Endianness?{RESET}")
    slow_print(f"{CYAN}Endianness defines how multi-byte data (like integers) are arranged in memory. 🧑‍💻")
    slow_print(f"{CYAN}Here’s a simple overview:\n1. Big-Endian: The most significant byte comes first.\n2. Little-Endian: The least significant byte comes first.")
    slow_print(f"\nLet’s use a 32-bit number as an example: 0x12345678.")
    slow_print(f"{CYAN}Now let’s break this down into its byte representation.")

def big_endian_vs_little_endian():
    slow_print(f"\n{BOLD}{CYAN}🔄 Big-Endian vs Little-Endian: Visual Example{RESET}")
    slow_print(f"\n{YELLOW}Big-Endian Representation: 0x12 0x34 0x56 0x78{RESET}")
    slow_print(f"{CYAN}In Big-Endian, the most significant byte (0x12) comes first in memory. 🧑‍💻")
    slow_print(f"{CYAN}Memory layout (from lowest address to highest):\n0x12 -> 0x34 -> 0x56 -> 0x78")
    time.sleep(1)

    slow_print(f"\n{YELLOW}Little-Endian Representation: 0x78 0x56 0x34 0x12{RESET}")
    slow_print(f"{CYAN}In Little-Endian, the least significant byte (0x78) comes first in memory. 🧑‍💻")
    slow_print(f"{CYAN}Memory layout (from lowest address to highest):\n0x78 -> 0x56 -> 0x34 -> 0x12")
    time.sleep(1)

def interactive_example():
    slow_print(f"\n{BOLD}{MAGENTA}💡 Let's try an interactive example!{RESET}")
    slow_print(f"{CYAN}Imagine you have a 4-byte integer value that you want to store in memory.")
    input(f"{YELLOW}Press Enter to input your bytes...{RESET}")
    
    byte1 = input(f"Enter the first byte (e.g., 0x12): ").strip()
    byte2 = input(f"Enter the second byte (e.g., 0x34): ").strip()
    byte3 = input(f"Enter the third byte (e.g., 0x56): ").strip()
    byte4 = input(f"Enter the fourth byte (e.g., 0x78): ").strip()

    # Show Big-Endian representation
    print(f"\n{BOLD}{CYAN}Big-Endian Representation: {byte1} {byte2} {byte3} {byte4}{RESET}")
    slow_print(f"{CYAN}In Big-Endian, the most significant byte (0x{byte1[2:]}) comes first in memory.\nMemory layout: {byte1} -> {byte2} -> {byte3} -> {byte4}")
    
    # Show Little-Endian representation
    print(f"\n{BOLD}{CYAN}Little-Endian Representation: {byte4} {byte3} {byte2} {byte1}{RESET}")
    slow_print(f"{CYAN}In Little-Endian, the least significant byte (0x{byte4[2:]}) comes first in memory.\nMemory layout: {byte4} -> {byte3} -> {byte2} -> {byte1}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Endianness Quiz Time!{RESET}")
    score = 0

    for i in range(3):
        print(f"\n{YELLOW}Question {i+1}:{RESET}")
        mode = random.choice(['big_endian', 'little_endian'])

        if mode == 'big_endian':
            correct = 'Big-Endian'
            user = input(f"🧠 In which endianness does the most significant byte come first? ").strip().capitalize()
            if user == correct:
                print(f"{GREEN}✅ Correct! The most significant byte comes first in Big-Endian.{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! It’s Big-Endian, where the most significant byte comes first.{RESET}")

        else:  # little_endian
            correct = 'Little-Endian'
            user = input(f"🧠 In which endianness does the least significant byte come first? ").strip().capitalize()
            if user == correct:
                print(f"{GREEN}✅ Correct! The least significant byte comes first in Little-Endian.{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! It’s Little-Endian, where the least significant byte comes first.{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Amazing! You’re an Endianness Expert!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Great effort! Keep practicing to master endianness!{RESET}")
    else:
        print(f"{RED}💡 No worries! Try again—you’ll get it!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Endianness defines how bytes are ordered in memory (Big-Endian vs Little-Endian).")
    slow_print(f"{CYAN}✔ Big-Endian stores the most significant byte first, while Little-Endian stores the least significant byte first.")
    slow_print(f"{CYAN}✔ This is important for interpreting multi-byte values like integers in memory.")
    print(f"{GREEN}Keep practicing, and soon you’ll be able to handle endianness like a pro! 🧑‍💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    endianness_explanation()
    big_endian_vs_little_endian()
    interactive_example()
    quiz()
    summary()

if __name__ == "__main__":
    run()
