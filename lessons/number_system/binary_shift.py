# lessons/basics/binary_shift.py

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
    """Prints text slowly with a delay between each character."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def show_shift_demo(number, shift_by):
    """Show the result of left and right binary shifts on a number."""
    binary_original = format(number, '08b')
    
    # Left Shift
    left_shifted = number << shift_by
    binary_left = format(left_shifted, '08b')
    
    # Right Shift
    right_shifted = number >> shift_by
    binary_right = format(right_shifted, '08b')

    slow_print(f"\n{BOLD}{CYAN}📌 Original Number: {number}{RESET}")
    slow_print(f"{YELLOW}Binary: 0b{binary_original}{RESET}")

    slow_print(f"\n{GREEN}👉 LEFT SHIFT by {shift_by}:{RESET}")
    slow_print(f"Binary: 0b{binary_left}")
    slow_print(f"Decimal: {left_shifted}")
    slow_print(f"Effect: Multiplies by 2^{shift_by} = {2 ** shift_by}")

    slow_print(f"\n{MAGENTA}👈 RIGHT SHIFT by {shift_by}:{RESET}")
    slow_print(f"Binary: 0b{binary_right}")
    slow_print(f"Decimal: {right_shifted}")
    slow_print(f"Effect: Divides by 2^{shift_by} = {2 ** shift_by} (ignores remainders!)")

def intro():
    """Introduction to the Bit Shift lesson."""
    print(f"{BOLD}{MAGENTA}🔮 Welcome to Bit Shift Magic! 🔮{RESET}")
    slow_print(f"{BLUE}In this lesson, you'll learn how to shift bits left and right to multiply or divide numbers!{RESET}")
    time.sleep(0.5)

def shift_lesson():
    """Interactive lesson for understanding bit shifts."""
    while True:
        try:
            # User input for number and shift amount
            num = int(input(f"\n{YELLOW}Enter an integer (0–255): {RESET}"))
            shift = int(input(f"{CYAN}How many bits would you like to shift? (1–4): {RESET}"))

            # Input validation
            if not (0 <= num <= 255):
                print(f"{RED}⚠️ Please enter a number between 0 and 255.{RESET}")
                continue
            if not (1 <= shift <= 4):
                print(f"{RED}⚠️ Shift amount must be between 1 and 4.{RESET}")
                continue

            # Display shift demo
            show_shift_demo(num, shift)

            # Ask if the user wants to try again
            again = input(f"\n{BLUE}Try another? (y/n): {RESET}").lower()
            if again != 'y':
                print(f"{GREEN}👋 Bye! Keep shifting your perspective!{RESET}")
                break

        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter integers only!{RESET}")

def summary():
    """Wrap-up the lesson and give a summary."""
    slow_print(f"\n{GREEN}👋 Thanks for learning bit shifts with us!{RESET}")
    slow_print(f"{CYAN}Now you know how shifting bits can multiply and divide numbers efficiently!{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    """Run the entire lesson."""
    intro()
    shift_lesson()
    summary()

if __name__ == "__main__":
    run()
