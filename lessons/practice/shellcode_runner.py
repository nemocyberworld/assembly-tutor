# lessons/practice_programs/shellcode_runner.py

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
    print(f"\n{BOLD}💥 shellcode_runner: Load and Run Custom Shellcode Safely!{RESET}\n")
    time.sleep(1)

    # ⚠️ Warning
    slow_print(f"{RED}{BOLD}⚠️  WARNING:{RESET} Running raw shellcode is dangerous if misused.")
    slow_print(f"{RED}Only do this in a virtual machine or controlled environment.{RESET}")
    slow_print(f"{RED}Never run untrusted shellcode from the internet!{RESET}\n")
    time.sleep(0.8)

    # 🎯 Goal
    slow_print(f"{CYAN}🎯 Goal:{RESET} Learn how to load bytes into memory and treat them as code using assembly.")
    slow_print("→ We’ll build a tiny shellcode runner to execute hand-written machine instructions.\n")
    time.sleep(0.5)

    # 🤔 What Is Shellcode?
    slow_print(f"{YELLOW}🤔 What's Shellcode?{RESET}")
    slow_print("→ Shellcode is just binary machine code, often written in hex (\\x48\\x31\\xc0...)")
    slow_print("→ It’s called 'shellcode' because early examples launched a shell (like /bin/sh).")
    slow_print("→ You can write your own to do ANYTHING — print text, add numbers, or exit a program.\n")

    # 🛠️ Instructions
    slow_print(f"{YELLOW}🛠️ Instructions:{RESET}")
    steps = [
        "1️⃣  Allocate memory with read/write/execute permissions (hint: use `mmap`).",
        "2️⃣  Copy your shellcode bytes into that memory.",
        "3️⃣  Create a function pointer to the memory and call it.",
        "4️⃣  Make sure the shellcode is simple and safe — like printing a message or exiting cleanly.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # 💡 Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of memory as a whiteboard. You write some instructions on it, then tell your CPU: “Go read this and follow it!”\n")

    # 🧠 Example in C (with inline shellcode)
    slow_print(f"{BOLD}🧠 Example (C-style Shellcode Runner):{RESET}")
    slow_print(f"""{DIM}
#include <sys/mman.h>
#include <string.h>
#include <stdio.h>

int main() {{
    unsigned char shellcode[] = {{
        0x48, 0x31, 0xc0,             // xor rax, rax
        0xb0, 0x3c,                   // mov al, 60
        0x48, 0x31, 0xff,             // xor rdi, rdi
        0x0f, 0x05                    // syscall (exit(0))
    }};

    void *mem = mmap(0, 4096, PROT_READ|PROT_WRITE|PROT_EXEC,
                     MAP_ANONYMOUS|MAP_PRIVATE, -1, 0);

    memcpy(mem, shellcode, sizeof(shellcode));
    ((void(*)())mem)();  // Run it like a function!
}}
{RESET}""")

    # 📌 Tips
    slow_print(f"\n{BLUE}📌 Tips:{RESET}")
    slow_print("→ Use short, well-understood shellcode (like 'exit(0)' or 'getpid') for safety.")
    slow_print("→ Use `strace ./a.out` to observe syscalls the shellcode makes.")
    slow_print("→ Never pass in external input as shellcode without validating it!")

    # 🎯 Bonus
    slow_print(f"\n{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Write a shellcode that calls `write` to print 'Hello!'.")
    slow_print("→ Modify shellcode to take input from the user.")
    slow_print("→ Add a NOP sled and simulate a jump — it's good exploit practice!\n")

    # ✅ Wrap-up
    slow_print(f"{GREEN}{BOLD}✅ Awesome work! Now you know how the CPU can be told to 'run your bytes'. This is powerful — and must be used with great care! 🔐🧠{RESET}")
