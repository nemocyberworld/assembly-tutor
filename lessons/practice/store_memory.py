# lessons/practice_programs/store_memory.py

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
    print(f"\n{BOLD}📦 Store a Value in Memory & Retrieve It{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to save data into memory and bring it back using assembly instructions.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Reserve memory space using `.bss` or use the stack.",
        "2️⃣  Use `mov` to copy a value from a register (like `rax`) into memory.",
        "3️⃣  Then use `mov` again to copy the value *back* into another register (like `rbx`).",
        "4️⃣  (Optional) Print the value using a syscall to confirm it's still correct."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Memory analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of memory like a tiny notepad. You write a number down (store it), walk away, and come back later to read it (load it).\n")

    # Example
    slow_print(f"{BOLD}🧠 Example Using `.bss` and Labels:{RESET}")
    slow_print(f"""{DIM}
section .bss
    temp    resq 1         ; reserve 8 bytes (1 quadword) of space

section .text
global _start

_start:
    mov     rax, 123       ; put 123 into rax
    mov     [temp], rax    ; write rax's value into memory at [temp]

    mov     rbx, [temp]    ; read the value back into rbx

    ; rbx now contains 123

    mov     rax, 60        ; syscall: exit
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Store your favorite number in memory, retrieve it, and (optionally) print it to the console!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `.bss` to reserve uninitialized memory. Perfect for storing variables!")
    slow_print("→ Want to be fancy? Use the stack: `push` a value, then `pop` it back later.")
    slow_print("→ You can also use `[rsp+offset]` to access local variables like in C.\n")

    # Bonus
    slow_print(f"{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("→ Try storing two or more values (e.g., [temp], [temp+8]) and load them back in reverse order.")
    slow_print("→ What happens if you change the value in memory before loading it? 🤔")

    # Wrap-up
    print(f"\n{BOLD}🏁 Great job! Mastering memory access gives you real power in low-level programming! 🔥{RESET}")
