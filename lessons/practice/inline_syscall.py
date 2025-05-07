# lessons/practice_programs/inline_syscall.py

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
    print(f"\n{BOLD}💻 inline_syscall: Perform a Syscall Using Inline Assembly in C{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to directly invoke Linux system calls using inline assembly inside a C program.\n")
    time.sleep(0.5)

    # Why It Matters
    slow_print(f"{BLUE}💡 Why Learn This?{RESET}")
    slow_print("→ Inline syscalls give you direct control over the OS without needing libc.")
    slow_print("→ Great for bare-metal systems, debugging, or writing tiny, fast programs.\n")

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Write a C function that uses `__asm__` or `asm` keyword.",
        "2️⃣  Load syscall number and arguments into registers (rax, rdi, rsi, etc.).",
        "3️⃣  Use `syscall` instruction to make the call.",
        "4️⃣  Store the result or error code from rax.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}🔌 Analogy:{RESET} It's like speaking *directly* to the kernel using secret hand signals (registers). No middlemen!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Inline Assembly to Call write(1, msg, len){RESET}")
    slow_print(f"""{DIM}
#include <stdio.h>

int main() {
    const char* msg = "Hello from inline syscall!\\n";
    long len = 27;

    asm volatile (
        "mov $1, %%rax\\n"        // syscall: write
        "mov $1, %%rdi\\n"        // fd: stdout
        "mov %[msg], %%rsi\\n"    // buffer
        "mov %[len], %%rdx\\n"    // length
        "syscall\\n"
        :
        : [msg] "r" (msg), [len] "r" (len)
        : "rax", "rdi", "rsi", "rdx"
    );

    return 0;
}
{RESET}""")

    # Tips
    slow_print(f"\n{BLUE}🛠️ Tips:{RESET}")
    slow_print("→ Be careful: clobbering the wrong registers can cause strange bugs.")
    slow_print("→ You must follow the syscall calling convention: rax, rdi, rsi, rdx, r10, r8, r9.")
    slow_print("→ Avoid calling stdlib functions after raw syscalls unless you know what you're doing.")

    # Bonus Challenge
    slow_print(f"\n{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Try calling `exit(42)` using inline assembly (hint: syscall number 60).")
    slow_print("→ Can you implement `getpid()` or `open()` this way?\n")

    # Wrap-up
    print(f"\n{GREEN}{BOLD}🏁 Boom! You're talking directly to the Linux kernel like a boss. Inline syscalls are fast, raw, and powerful. ⚙️🐧{RESET}")
