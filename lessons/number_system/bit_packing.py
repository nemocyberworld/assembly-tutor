# lessons/basics/bit_packing.py

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
    slow_print(f"{BOLD}{MAGENTA}🧳 Welcome to Bit Packing! 🧠{RESET}")
    slow_print(f"{CYAN}Sometimes we want to fit multiple values into a single byte (8 bits)...")
    slow_print("It’s like stuffing socks, snacks, and a phone all into one pocket! 🧦🍫📱{RESET}")
    slow_print(f"{BLUE}Let’s pack 3 values into a byte: {RESET}")
    slow_print(f"{YELLOW}- 3 bits for Red (0–7)")
    slow_print("- 3 bits for Green (0–7)")
    slow_print("- 2 bits for Blue (0–3){RESET}")

def pack_color(red, green, blue):
    return ((red & 0b111) << 5) | ((green & 0b111) << 2) | (blue & 0b11)

def unpack_color(byte):
    red = (byte >> 5) & 0b111
    green = (byte >> 2) & 0b111
    blue = byte & 0b11
    return red, green, blue

def demo_packing():
    slow_print(f"\n{MAGENTA}🎨 Let’s Pack Some Colors!{RESET}")
    red = 5   # 101
    green = 3 # 011
    blue = 2  # 10

    slow_print(f"{CYAN}Red={red} (3 bits), Green={green} (3 bits), Blue={blue} (2 bits){RESET}")
    packed = pack_color(red, green, blue)
    slow_print(f"{GREEN}Packed Byte: {packed:08b} (Decimal: {packed}){RESET}")

    unpacked_red, unpacked_green, unpacked_blue = unpack_color(packed)
    slow_print(f"\n{BLUE}Unpacked Values:{RESET}")
    slow_print(f"🔴 Red   = {unpacked_red}")
    slow_print(f"🟢 Green = {unpacked_green}")
    slow_print(f"🔵 Blue  = {unpacked_blue}")

def user_test():
    slow_print(f"\n{BOLD}{MAGENTA}🎮 Try Packing Your Own Color!{RESET}")
    try:
        red = int(input(f"{YELLOW}Enter Red (0–7): {RESET}"))
        green = int(input(f"{YELLOW}Enter Green (0–7): {RESET}"))
        blue = int(input(f"{YELLOW}Enter Blue (0–3): {RESET}"))

        if not (0 <= red <= 7 and 0 <= green <= 7 and 0 <= blue <= 3):
            slow_print(f"{RED}⚠️ One of your values is out of range! Try again.{RESET}")
            return

        packed = pack_color(red, green, blue)
        slow_print(f"{GREEN}Packed Byte: {packed:08b} (Decimal: {packed}){RESET}")

        r, g, b = unpack_color(packed)
        slow_print(f"{BLUE}Unpacked: R={r}, G={g}, B={b}{RESET}")
    except ValueError:
        slow_print(f"{RED}❌ Invalid input. Please enter numbers only.{RESET}")

def summary():
    slow_print(f"\n{BOLD}{BLUE}🔚 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Bit packing saves space by storing multiple small values in one byte.")
    slow_print("✔ Use shifts (<<) and bitwise OR (|) to pack.")
    slow_print("✔ Use shifts (>>) and AND (&) to unpack.")
    slow_print("✔ Widely used in graphics, compression, file formats, and embedded systems!{RESET}")
    slow_print(f"\n{GREEN}Great job learning how to pack bits like a pro! 🎒✨{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

if __name__ == "__main__":
    print_intro()
    demo_packing()
    user_test()
    summary()
