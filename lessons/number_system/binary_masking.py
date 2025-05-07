# lessons/basics/binary_masking.py

import time

# 🎨 Color Codes
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

def binary_str(n):
    return f"{n:08b}"

def show_masking_demo(value, mask):
    value_bin = binary_str(value)
    mask_bin = binary_str(mask)
    result = value & mask
    result_bin = binary_str(result)

    print(f"\n{BOLD}{CYAN}🔢 Value:      {value}   →  0b{value_bin}{RESET}")
    print(f"{YELLOW}🛡️  Mask:       {mask}   →  0b{mask_bin}{RESET}")
    print(f"{GREEN}🎯 Result:     {result}   →  0b{result_bin}{RESET}")
    
    slow_print(f"\n{MAGENTA}🧠 What happened?{RESET}")
    slow_print(f"Each bit in the result is ON only if it was ON in both value and mask!")
    slow_print("This is called a bitwise AND (&).")

def intro():
    print(f"{BOLD}{MAGENTA}🎓 Welcome to Binary Masking 101! 🎓{RESET}")
    slow_print(f"{BLUE}We'll use masks to isolate specific bits in a byte (0–255).{RESET}")
    time.sleep(0.5)

def masking_lesson():
    while True:
        try:
            val = int(input(f"\n{YELLOW}Enter a number (0–255) to analyze: {RESET}"))
            if not (0 <= val <= 255):
                print(f"{RED}⚠️ Number must be between 0 and 255!{RESET}")
                continue

            print(f"{CYAN}\nChoose a masking option:{RESET}")
            print(f"{GREEN} 1.{RESET} Mask lower 4 bits (0x0F)")
            print(f"{GREEN} 2.{RESET} Mask upper 4 bits (0xF0)")
            print(f"{GREEN} 3.{RESET} Mask a custom bit pattern")

            choice = input(f"{MAGENTA}Your choice (1/2/3): {RESET}")
            if choice == '1':
                mask = 0x0F
            elif choice == '2':
                mask = 0xF0
            elif choice == '3':
                mask = int(input(f"{YELLOW}Enter your custom mask (0–255): {RESET}"))
                if not (0 <= mask <= 255):
                    print(f"{RED}⚠️ Invalid mask! Must be between 0–255.{RESET}")
                    continue
            else:
                print(f"{RED}❌ Invalid choice! Try again.{RESET}")
                continue

            show_masking_demo(val, mask)

            again = input(f"\n{BLUE}Do you want to try another? (y/n): {RESET}").lower()
            if again != 'y':
                break

        except ValueError:
            print(f"{RED}❌ Please enter valid integers only.{RESET}")

def summary():
    slow_print(f"\n{GREEN}👋 Goodbye! May your bits always align!{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    masking_lesson()
    summary()

if __name__ == "__main__":
    run()
