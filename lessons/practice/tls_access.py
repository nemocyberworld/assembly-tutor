# lessons/practice_programs/tls_access.py

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
    print(f"\n{BOLD}🌐 tls_access: Access Thread-Local Storage Manually{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to manually access thread-local storage (TLS) — where each thread keeps its private variables.\n")
    time.sleep(0.5)

    # Concept
    slow_print(f"{BLUE}💡 What is TLS?{RESET}")
    slow_print("→ TLS gives each thread its own copy of some data (like errno or thread ID).")
    slow_print("→ Useful in multi-threaded programs where threads must not share state.")
    slow_print("→ On x86_64 Linux, TLS is often accessed using the `fs:` segment register.\n")

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Assume a known offset within the TLS block (e.g., `fs:0x28` for `errno` in glibc).",
        "2️⃣  Use the `mov` instruction with segment override prefix `fs:`.",
        "3️⃣  Print or modify the value, or simulate thread switching.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Example
    slow_print(f"\n{BOLD}🧠 Example: Read Thread ID from TLS (Linux/glibc){RESET}")
    slow_print(f"""{DIM}
; Access thread ID stored by glibc at offset 0x28 in the TLS block
section .text
global _start

_start:
    mov     rax, qword fs:[0x28]   ; read thread ID
    ; use rax or print it

    mov     rax, 60                ; syscall: exit
    xor     rdi, rdi
    syscall
{RESET}""")

    # Analogy
    slow_print(f"\n{BLUE}🗂️ Analogy:{RESET} Imagine each thread has a private locker (TLS block). You can access your own locker using a special key (`fs:`), but no one else can touch it.\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ Try printing the value you load from TLS to see if it changes between threads.")
    slow_print("→ You can simulate thread context by manually changing the base of `fs:` in an advanced setup (e.g., via `arch_prctl`).")
    slow_print("→ Use `gettid` syscall or inspect `/proc/self/task` to compare with the value at `fs:0x28`.\n")

    # Bonus
    slow_print(f"{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Use a C program to spawn threads and access TLS in each via inline assembly.")
    slow_print("→ Try changing the TLS offset and observing how values differ (or cause segfaults!).")

    # Wrap-up
    print(f"\n{GREEN}{BOLD}🏁 TLS gives you private memory for every thread — it’s like a secret desk drawer in a shared office! Master it, and you're threading like a pro! 🔧🧵{RESET}")
