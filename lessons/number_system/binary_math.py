# lessons/basics/binary_math.py

import time

# 🎨 Terminal Color Palette
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
    print(f"\n{BOLD}{CYAN}🧠 Welcome to Binary Math Basics!{RESET}\n")
    time.sleep(0.5)
    slow_print(f"{YELLOW}Why learn binary math?{RESET}")
    slow_print("👉 Because computers do math with just 1s and 0s!\n")

def lesson():
    # Binary addition
    print(f"{BOLD}{GREEN}➕ Binary Addition:{RESET}")
    slow_print("  0 + 0 = 0")
    slow_print("  0 + 1 = 1")
    slow_print("  1 + 0 = 1")
    slow_print("  1 + 1 = 10 (carry the 1!) 🪄\n")

    a = 0b1010  # 10
    b = 0b0101  # 5
    slow_print(f"Let's add {a} (0b{a:04b}) + {b} (0b{b:04b})")
    result = a + b
    slow_print(f"Decimal result: {GREEN}{result}{RESET}")
    slow_print(f"Binary result: {GREEN}0b{result:04b}{RESET}\n")

    # Binary subtraction
    print(f"{BOLD}{RED}➖ Binary Subtraction:{RESET}")
    x = 0b1101  # 13
    y = 0b0011  # 3
    slow_print(f"Let's subtract {x} (0b{x:04b}) - {y} (0b{y:04b})")
    result = x - y
    slow_print(f"Decimal result: {GREEN}{result}{RESET}")
    slow_print(f"Binary result: {GREEN}0b{result:04b}{RESET}\n")

    # Binary multiplication
    print(f"{BOLD}{BLUE}✖️ Binary Multiplication:{RESET}")
    a = 0b0011  # 3
    b = 0b0100  # 4
    result = a * b
    slow_print(f"{a} × {b} = {result}")
    slow_print(f"Binary: 0b{a:04b} × 0b{b:04b} = 0b{result:08b}\n")

    # Binary division
    print(f"{BOLD}{MAGENTA}➗ Binary Division:{RESET}")
    a = 0b1100  # 12
    b = 0b0011  # 3
    result = a // b
    slow_print(f"{a} ÷ {b} = {result}")
    slow_print(f"Binary: 0b{a:04b} ÷ 0b{b:04b} = 0b{result:04b}\n")

    # Bit shifting
    print(f"{BOLD}{CYAN}🔄 Bit Shifting Magic:{RESET}")
    n = 0b0001  # 1
    slow_print(f"{n} << 2 = {n << 2}  → 0b{n:04b} becomes 0b{n << 2:04b} (×4)")
    slow_print(f"{n << 2} >> 1 = {(n << 2) >> 1} → divide by 2\n")

    # Final interactive play
    print(f"{BOLD}{YELLOW}🧪 Try it Yourself!{RESET}")
    num = 7
    shift_left = num << 1
    shift_right = num >> 1
    slow_print(f"{num} << 1 = {shift_left} (binary: {bin(shift_left)})")
    slow_print(f"{num} >> 1 = {shift_right} (binary: {bin(shift_right)})\n")

def summary():
    print(f"{BOLD}{GREEN}🎉 Summary:{RESET}")
    slow_print("✅ You learned how to add, subtract, multiply, and divide in binary.")
    slow_print("✅ You saw the magic of bit shifting (fast math!).")
    slow_print("✅ Now you're thinking like a CPU 🧠💻!\n")
    slow_print(f"{BOLD}{MAGENTA}Next Stop: Bitwise Logic Operators! 🚀{RESET}\n")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    lesson()
    summary()

if __name__ == "__main__":
    run()
