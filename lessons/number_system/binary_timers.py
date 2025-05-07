# lessons/basics/binary_timers.py

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
    """Prints text slowly with a delay between each character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_intro():
    """Prints the introductory message for the Binary Timers lesson."""
    slow_print(f"{BOLD}{MAGENTA}⏱️ Welcome to Binary Timers!{RESET}")
    slow_print(f"{CYAN}In electronics, timers often count in {YELLOW}binary{CYAN} using bits like switches flipping on/off.")
    slow_print(f"Let's simulate how a 4-bit binary timer counts up over time, just like in real hardware!{RESET}\n")

def binary_timer(bits=4, delay=0.5, max_count=None):
    """Simulates a binary timer counting up in binary with a given bit size."""
    slow_print(f"{BOLD}{BLUE}🚀 Starting {bits}-bit Binary Timer...{RESET}")
    max_value = (1 << bits)
    count_limit = max_value if max_count is None else min(max_count, max_value)

    for i in range(count_limit):
        binary = format(i, f'0{bits}b')
        decorated = decorate_bits(binary)
        slow_print(f"{YELLOW}Count {i:2}: {decorated}{RESET}", delay=delay)

    slow_print(f"\n{GREEN}✅ Timer Complete! Reached {count_limit} steps.{RESET}")

def decorate_bits(binary_str):
    """Adds color to bits for fun visual effect."""
    result = ""
    for bit in binary_str:
        if bit == "1":
            result += f"{GREEN}{bit}{RESET}"
        else:
            result += f"{RED}{bit}{RESET}"
    return result

def explain_use_cases():
    """Explains real-world use cases of binary timers."""
    slow_print(f"\n{BOLD}{BLUE}🔍 Real-World Use Cases:{RESET}")
    slow_print(f"{CYAN}✔ Digital watches and clocks count in binary under the hood.")
    slow_print(f"✔ Microcontrollers use binary timers to control LEDs, motors, or delays.")
    slow_print(f"✔ Traffic lights, alarms, and even game logic often use binary counters.{RESET}")

def user_demo():
    """Allows the user to try out the binary timer with custom inputs."""
    slow_print(f"\n{BOLD}{MAGENTA}🎮 Try It Yourself!{RESET}")
    slow_print(f"{CYAN}Choose how many bits (2–8) and how fast the counter should run!{RESET}")

    try:
        bits = int(input(f"{YELLOW}How many bits? (2-8): {RESET}"))
        if not (2 <= bits <= 8):
            raise ValueError("Out of range")
        speed = float(input(f"{YELLOW}Delay per count (seconds)? (e.g., 0.2): {RESET}"))
        max_steps = int(input(f"{YELLOW}How many steps to count (or 0 for full range)? {RESET}"))
        binary_timer(bits=bits, delay=speed, max_count=max_steps if max_steps > 0 else None)
    except ValueError:
        slow_print(f"{RED}⚠️ Invalid input. Please try again with proper numbers!{RESET}")

def summary():
    """Summarizes the key takeaways from the Binary Timers lesson."""
    slow_print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Binary timers count up using bits that toggle ON (1) and OFF (0).")
    slow_print(f"✔ Useful in {YELLOW}hardware timing, LED control, state machines, and more.{RESET}")
    slow_print(f"{GREEN}Now you understand how devices count time in pure binary! 🔢💡{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    """Runs the complete binary timer lesson."""
    print_intro()
    binary_timer(bits=4, delay=0.4)  # Default 4-bit binary timer with a delay of 0.4s
    explain_use_cases()
    user_demo()
    summary()

if __name__ == "__main__":
    run()
