# lessons/practice_programs/subtract_numbers.py

import time

# ANSI Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}➖ Lesson: Subtract One Number from Another{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to subtract one number from another using x86-64 assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Put your starting number (minuend) in `rax`.",
        "2️⃣  Put the number you want to subtract (subtrahend) in `rbx`.",
        "3️⃣  Use `sub rax, rbx` to perform the subtraction.",
        "4️⃣  After that, `rax` will hold the result!",
        "5️⃣  (Optional) Print the result using a syscall or helper function."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine `rax` is your wallet with 💵 $100, and `rbx` is a bill for 💳 $35.")
    slow_print("→ When you subtract, you're paying the bill. What’s left in your wallet is the result.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example Code:{RESET}")
    slow_print(f"""{DIM}
    mov     rax, 100       ; rax = 100 (wallet)
    mov     rbx, 35        ; rbx = 35  (bill)
    sub     rax, rbx       ; rax = rax - rbx → rax = 65
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Try changing the values. What happens if you subtract a *bigger* number from a smaller one?")
    slow_print("→ For example: `rax = 10`, `rbx = 50` — this will result in a negative number (two’s complement form).\n")

    # Tip
    slow_print(f"{BLUE}💡 Tip:{RESET} The `sub` instruction updates CPU flags like:")
    slow_print("  - Zero Flag (ZF) if result is 0")
    slow_print("  - Sign Flag (SF) if result is negative")
    slow_print("These flags help you later in `if`-like conditions using `je`, `jl`, etc.\n")

    # Bonus
    slow_print(f"{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("→ Subtract a number from itself. What value do you expect?")
    slow_print("→ Store the result in memory using something like:")
    slow_print(f"""{DIM}
    section .bss
    result  resq 1

    ; after doing the subtraction:
    mov     [result], rax
{RESET}""")

    # Wrap-up
    print(f"\n{BOLD}🏁 Nice work! Subtraction is just the beginning — get ready for comparisons, branching, and math battles! ⚔️{RESET}")
