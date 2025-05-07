# lessons/practice_programs/multiply_loop.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🧮 Multiply Using a Loop (No `mul` Instruction!){RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Multiply two numbers by using a loop and repeated addition.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Store your two numbers: one in `rax` (multiplicand), one in `rbx` (multiplier).",
        "2️⃣  Zero out `rcx` — it will hold the result.",
        "3️⃣  In a loop, add `rax` to `rcx`, and decrement `rbx`.",
        "4️⃣  Loop until `rbx` is zero.",
        "5️⃣  `rcx` will now contain rax × rbx!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Code Example
    slow_print(f"\n{BOLD}🧠 Example Logic:{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov     rax, 6        ; multiplicand
    mov     rbx, 4        ; multiplier
    xor     rcx, rcx      ; result = 0

multiply_loop:
    add     rcx, rax      ; result += multiplicand
    dec     rbx           ; multiplier--
    jnz     multiply_loop ; loop until multiplier is zero

    ; rcx now contains 24
    ; (optional: convert to string and print it)

    mov     rax, 60       ; syscall: exit
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET}")
    slow_print("→ Change the inputs (multiplicand and multiplier) and observe how the loop behaves.")
    slow_print("→ Test edge cases like 0 and 1.")

    # Tip
    slow_print(f"\n{BLUE}💡 Tip:{RESET} This is how multiplication was done before fancy `mul` instructions — essential in low-level bootloaders or minimal environments!")

    # Bonus
    slow_print(f"\n{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("→ What if one input is 0? Does your loop still behave?")
    slow_print("→ Handle negative numbers using two's complement. Can you detect and fix the sign of the result?")

    # Wrap-up
    print(f"\n{BOLD}🚀 Nice work! You're manually implementing arithmetic at the metal level. Great for understanding how CPUs really operate! 🧠🔥{RESET}")
