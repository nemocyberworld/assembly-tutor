# lessons/basics/binary_intro.py

import time

# 🎨 Color codes for visual excitement!
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"\n{BOLD}🤖 Welcome to Binary Land!{RESET}")
    time.sleep(1)
    slow_print(f"{CYAN}🌟 What if I told you computers can't count past 1?{RESET}")
    slow_print("😲 It's true! Computers only know two things:")
    slow_print(f"{GREEN}1 = ON 🔆{RESET} and {YELLOW}0 = OFF 🌑{RESET}")
    print()

def main_lesson():
    # 🎯 Goal
    slow_print(f"{MAGENTA}🎯 Your Mission:{RESET}")
    slow_print("Learn how to read, write, and think in binary — the secret language of machines!\n")

    time.sleep(0.5)
    slow_print(f"{BLUE}📊 Decimal vs Binary:{RESET}")
    slow_print("You (a human) count like this: 0, 1, 2, 3, 4, 5...")
    slow_print("A computer counts: 0, 1... then what?")
    slow_print("Answer: 1 0 → that's binary for 2!\n")

    time.sleep(0.5)
    # 🧠 Explain Binary Powers
    slow_print(f"{YELLOW}🧠 Binary is just powers of 2:{RESET}")
    slow_print("Decimal:     1 × 10⁰ + 2 × 10¹ = 21")
    slow_print("Binary:      1 × 2⁰ + 0 × 2¹ + 1 × 2² = 5 (0b101)")
    print()

    # 🔢 Live Binary Table
    slow_print(f"{CYAN}🔢 Let's See Binary in Action:{RESET}")
    slow_print(f"{BOLD}Number  Binary{RESET}")
    for i in range(16):
        slow_print(f"{i:<8} {GREEN}{format(i, '04b')}{RESET}")
    print()

    # 🧪 Decimal → Binary
    slow_print(f"{MAGENTA}🧪 Convert Decimal to Binary with Python:{RESET}")
    num = 13
    slow_print(f"{YELLOW}Decimal {num}{RESET} → Binary: {GREEN}{bin(num)}{RESET}\n")

    # 🔁 Binary → Decimal
    binary = "1101"
    slow_print(f"{BLUE}🔁 Convert Binary to Decimal:{RESET}")
    slow_print(f"{YELLOW}Binary {binary}{RESET} → Decimal: {GREEN}{int(binary, 2)}{RESET}\n")

    # 👨‍💻 Try it Yourself!
    slow_print(f"{CYAN}🎮 Time to Play!{RESET}")
    favorite = 42
    slow_print(f"What is the binary of {favorite}? It's {GREEN}{bin(favorite)}{RESET}")
    binary_input = "101010"
    slow_print(f"What is {binary_input} in decimal? It's {GREEN}{int(binary_input, 2)}{RESET}\n")

    # 💥 Binary Tricks
    slow_print(f"{MAGENTA}💥 Bonus: Bitwise Powers!{RESET}")
    a = 0b1010  # 10
    b = 0b0110  # 6
    slow_print(f"a = 0b1010 ({a}), b = 0b0110 ({b})")
    slow_print(f"{BOLD}a & b = {a & b}{RESET}  → AND")
    slow_print(f"{BOLD}a | b = {a | b}{RESET}  → OR")
    slow_print(f"{BOLD}a ^ b = {a ^ b}{RESET}  → XOR\n")

def summary():
    slow_print(f"{BLUE}📚 What You Learned:{RESET}")
    slow_print("✅ Computers use binary (just 0s and 1s) to do *everything*.")
    slow_print("✅ You can convert with `bin()` and `int(x, 2)`.")
    slow_print("✅ Binary is like magic for programmers ✨\n")

    slow_print(f"{GREEN}{BOLD}🎉 You just took your first step into the matrix! 🧩{RESET}")
    slow_print(f"{CYAN}Next up: Learn how to do math and logic in binary! 🧠💡{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    main_lesson()
    summary()

# Run this when the file is executed
if __name__ == "__main__":
    run()
