# lessons/basics/bit_flags.py

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
    """Prints the introduction to the Bit Flags lesson."""
    slow_print(f"{BOLD}{MAGENTA}🧠 Welcome to Bit Flags: Control Multiple Settings with Just One Number! 🏁{RESET}")
    slow_print(f"{CYAN}\nImagine having multiple switches (ON/OFF) — instead of separate variables, you can use bits! 🪄")
    slow_print(f"Each bit represents a flag: 1 = ON, 0 = OFF.{RESET}")

def define_flags():
    """Defines and prints common bit flags."""
    slow_print(f"\n{BLUE}🎯 Let’s define our flags using binary positions:{RESET}")
    FLAG_SOUND = 0b0001        # Bit 0
    FLAG_FULLSCREEN = 0b0010   # Bit 1
    FLAG_DEBUG = 0b0100        # Bit 2
    FLAG_VSYNC = 0b1000        # Bit 3

    slow_print(f"{GREEN}FLAG_SOUND       = 0b0001")
    slow_print(f"FLAG_FULLSCREEN  = 0b0010")
    slow_print(f"FLAG_DEBUG       = 0b0100")
    slow_print(f"FLAG_VSYNC       = 0b1000{RESET}")

    return FLAG_SOUND, FLAG_FULLSCREEN, FLAG_DEBUG, FLAG_VSYNC

def demo_flags():
    """Demonstrates setting, toggling, and clearing bit flags."""
    FLAG_SOUND, FLAG_FULLSCREEN, FLAG_DEBUG, FLAG_VSYNC = define_flags()

    settings = 0b0000
    slow_print(f"\n{YELLOW}Current Settings: {settings:04b} (All OFF){RESET}")

    settings |= FLAG_SOUND
    settings |= FLAG_DEBUG
    slow_print(f"{GREEN}Turn ON SOUND and DEBUG → {settings:04b}{RESET}")

    if settings & FLAG_DEBUG:
        slow_print(f"{CYAN}✅ DEBUG mode is ON!{RESET}")

    slow_print(f"{YELLOW}Toggle FULLSCREEN...{RESET}")
    settings ^= FLAG_FULLSCREEN
    slow_print(f"{GREEN}After toggle: {settings:04b}{RESET}")

    settings &= ~FLAG_SOUND
    slow_print(f"{RED}Turn OFF SOUND → {settings:04b}{RESET}")

    slow_print(f"\n{BOLD}{BLUE}🧾 Final Settings Breakdown:{RESET}")
    print_flag_status("SOUND", settings, FLAG_SOUND)
    print_flag_status("FULLSCREEN", settings, FLAG_FULLSCREEN)
    print_flag_status("DEBUG", settings, FLAG_DEBUG)
    print_flag_status("VSYNC", settings, FLAG_VSYNC)

def print_flag_status(name, settings, flag):
    """Prints whether a specific flag is ON or OFF."""
    status = f"{GREEN}ON{RESET}" if settings & flag else f"{RED}OFF{RESET}"
    slow_print(f"{name:<12}: {status}")

def user_test():
    """Allows the user to input flags interactively and shows the resulting settings."""
    slow_print(f"\n{BOLD}{MAGENTA}🎮 Try Setting Flags Yourself!{RESET}")
    slow_print(f"{CYAN}Enter flags you want ON (comma-separated): SOUND, FULLSCREEN, DEBUG, VSYNC{RESET}")
    input_flags = input(f"{YELLOW}Your flags: {RESET}").upper().split(',')

    FLAG_SOUND, FLAG_FULLSCREEN, FLAG_DEBUG, FLAG_VSYNC = define_flags()

    flag_map = {
        "SOUND": FLAG_SOUND,
        "FULLSCREEN": FLAG_FULLSCREEN,
        "DEBUG": FLAG_DEBUG,
        "VSYNC": FLAG_VSYNC
    }

    settings = 0b0000
    for flag in input_flags:
        flag = flag.strip()
        if flag in flag_map:
            settings |= flag_map[flag]
        else:
            slow_print(f"{RED}⚠️ Unknown flag: {flag}{RESET}")

    slow_print(f"\n{GREEN}Your flag byte: {settings:04b}{RESET}")
    slow_print(f"{BOLD}{BLUE}Here’s your configuration status:{RESET}")
    for name, bit in flag_map.items():
        print_flag_status(name, settings, bit)

def summary():
    """Prints a summary of the lesson and reviews bitwise flag operations."""
    slow_print(f"\n{BOLD}{BLUE}🔚 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Use individual bits to store multiple ON/OFF states in a single number.")
    slow_print(f"✔ Use `|` to turn ON, `&` to check, `^` to toggle, and `& ~` to turn OFF flags.")
    slow_print(f"✔ Bit flags are used in games, drivers, settings, and embedded systems!{RESET}")
    slow_print(f"\n{GREEN}Well done, you now wield the power of binary flags! 🧙‍♂️🪄{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    """Runs the Bit Flags lesson."""
    print_intro()
    demo_flags()
    user_test()
    summary()

# Run the lesson
if __name__ == "__main__":
    run()
