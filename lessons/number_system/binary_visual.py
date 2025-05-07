# lessons/basics/binary_visual.py

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
    slow_print(f"{BOLD}{MAGENTA}💡 Welcome to Binary Visualizer: LEDs and Switches Simulation!{RESET}")
    slow_print(f"{CYAN}In real electronics, bits control things like {YELLOW}LEDs{CYAN} and {YELLOW}switches{CYAN}.")
    slow_print(f"This simulation helps you *see* what binary values look like in action!{RESET}\n")

def render_binary_as_leds(value, bits=8):
    binary = format(value, f'0{bits}b')
    visual = ""
    for bit in binary:
        if bit == '1':
            visual += f"{GREEN}[●]{RESET} "  # LED ON
        else:
            visual += f"{RED}[○]{RESET} "   # LED OFF
    return visual.strip()

def simulate_leds():
    slow_print(f"\n{BOLD}{BLUE}🔦 LED Simulation (8-bit counter):{RESET}")
    for i in range(16):  # 0 to 15
        leds = render_binary_as_leds(i, bits=4)
        slow_print(f"{YELLOW}Decimal {i:2} → Binary {format(i, '04b')} → {leds}{RESET}", delay=0.4)

def simulate_switches():
    slow_print(f"\n{BOLD}{MAGENTA}🎮 Switch Simulation: Flip Bits Yourself!{RESET}")
    slow_print(f"{CYAN}Enter an 8-bit binary value (e.g., 10101010) to see the switch state.{RESET}")

    user_input = input(f"{YELLOW}Enter 8 bits: {RESET}")
    if len(user_input) != 8 or not all(c in '01' for c in user_input):
        slow_print(f"{RED}⚠️ Invalid input. Please enter exactly 8 binary digits.{RESET}")
        return
    
    slow_print(f"\n{GREEN}🕹️ Switch State:{RESET}")
    print(render_binary_as_switches(user_input))

def render_binary_as_switches(binary):
    visual = ""
    for i, bit in enumerate(binary):
        label = f"S{i}"
        if bit == '1':
            visual += f"{GREEN}{label}: ON  {RESET}"
        else:
            visual += f"{RED}{label}: OFF {RESET}"
        if i % 4 == 3:
            visual += "\n"
    return visual.strip()

def summary():
    slow_print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Each bit in binary can control a physical device like an LED or switch.")
    slow_print(f"✔ 1 = ON (🟢), 0 = OFF (🔴).")
    slow_print(f"✔ Useful in microcontrollers, robotics, embedded systems, and digital circuits.{RESET}")
    slow_print(f"\n{GREEN}Now you can see how binary controls the real world! 🧠🔌{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

if __name__ == "__main__":
    print_intro()
    simulate_leds()
    simulate_switches()
    summary()
