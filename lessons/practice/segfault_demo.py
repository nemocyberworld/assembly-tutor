# lessons/practice_programs/segfault_demo.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}💥 segfault_demo: Cause and Debug a Segmentation Fault!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn what causes segmentation faults and how to use tools like `gdb` to debug them.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Write to an invalid or uninitialized memory address.",
        "2️⃣  Run your program — expect it to crash (with a 'Segmentation fault').",
        "3️⃣  Use `gdb` to find out *where* it crashed and *why*.",
        "4️⃣  Reflect: How would you prevent it from happening in the future?"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} A segfault is like trying to open a door that doesn't exist — your CPU knocks, nobody's home, and it crashes into the wall.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Dereferencing NULL (address 0x0){RESET}")
    slow_print(f"""{DIM}
section .text
    global _start

_start:
    mov     rax, 0           ; rax points to NULL (address 0)
    mov     byte [rax], 42   ; ❌ attempt to write to NULL → segfault!

    ; This line never runs
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Intentionally cause a segmentation fault. Then use `gdb` to run and debug your program:")

    slow_print(f"""{DIM}
    nasm -f elf64 segfault_demo.asm
    ld -o segfault_demo segfault_demo.o
    gdb ./segfault_demo
    (gdb) run
    (gdb) backtrace
{RESET}""")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Writing to address 0, or to a garbage/unallocated pointer will cause a segfault.")
    slow_print("→ `gdb` shows you the *exact instruction* and register state at the crash point.")
    slow_print("→ Reading from [unmapped memory] causes a fault too!")

    # Bonus
    slow_print(f"\n{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Try causing a segfault by reading past the end of an array.")
    slow_print("→ What happens if you jump to an invalid function pointer?")
    slow_print("→ Try running the program *without* gdb — what does the OS report?\n")

    # Wrap-up
    print(f"\n{RED}{BOLD}💣 Boom! Segfaults are scary at first, but now you know how to summon and defeat them. You’re one step closer to systems mastery!{RESET}")
