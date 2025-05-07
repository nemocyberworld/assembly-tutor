# lessons/practice_programs/syscall_bruteforce.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RED = "\033[91m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🚨 syscall_bruteforce: Brute Force Syscall Numbers (For Education Only){RESET}\n")
    time.sleep(1)

    # WARNING
    slow_print(f"{RED}{BOLD}⚠️  WARNING:{RESET} This lesson is for educational purposes only.")
    slow_print(f"{RED}Running unknown syscalls can crash your program or system. Use inside a VM or safe environment!{RESET}\n")
    time.sleep(0.8)

    # Goal
    slow_print(f"{CYAN}🎯 Goal:{RESET} Learn how system calls are made using syscall numbers and explore what happens when you try unknown ones.\n")
    time.sleep(0.5)

    # What Is a Syscall?
    slow_print(f"{YELLOW}🔍 What's a Syscall?{RESET}")
    slow_print("→ A syscall is a direct request to the Linux kernel to perform something low-level, like reading files, printing text, or exiting a program.")
    slow_print("→ Each syscall has a number (e.g., 1 = write, 60 = exit).\n")

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Start with a known syscall number like 0 (usually `read`).",
        "2️⃣  Place the syscall number in `rax`.",
        "3️⃣  Fill `rdi`, `rsi`, `rdx` with dummy (safe) values.",
        "4️⃣  Call `syscall`, observe what happens.",
        "5️⃣  Increment `rax`, try the next number.",
        "6️⃣  Print or log results, note which return values are errors (like -1, -38 for ENOSYS)."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}🧠 Analogy:{RESET} Imagine trying every button on a remote to see what it does — most do nothing, some do something cool, and others... reset your TV. 😅\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Brute Force Loop{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov rbx, 0          ; syscall number starts at 0

.loop:
    mov rax, rbx        ; syscall number
    xor rdi, rdi        ; dummy args
    xor rsi, rsi
    xor rdx, rdx
    syscall

    inc rbx             ; try next syscall number
    cmp rbx, 200        ; limit how far you brute force!
    jl .loop

    ; exit cleanly
    mov rax, 60
    xor rdi, rdi
    syscall
{RESET}""")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use a debugger like `strace` to watch which syscalls are invoked.")
    slow_print("→ Watch out for invalid syscalls (you’ll get ENOSYS or a crash).")
    slow_print("→ Print return values to learn what each syscall returns (or if it fails).")

    # Bonus
    slow_print(f"\n{BOLD}🎯 Bonus Exploration:{RESET}")
    slow_print("→ Compare your findings with `/usr/include/asm/unistd_64.h`.")
    slow_print("→ Try calling valid syscalls with bad parameters — what happens?")
    slow_print("→ Can you find syscall 39 (`getpid`) or 60 (`exit`) just by observing?\n")

    # Wrap-up
    slow_print(f"{GREEN}{BOLD}🏁 You’ve peeked behind the curtain of the OS! Just remember: with great power comes great caution. 👨‍💻🧠{RESET}")

    # Final Note
    slow_print(f"\n{RED}⚠️  Always experiment responsibly. This is a *learning* exercise, not a hacking tool!{RESET}")

