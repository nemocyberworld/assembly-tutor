# lessons/practice_programs/exec_ls.py

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
    print(f"\n{BOLD}🚀 Execute a Program: `/bin/ls` with `execve`!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to execute another program (like `/bin/ls`) directly from your assembly program using the `execve` syscall.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Set up the path to the program you want to run (`/bin/ls`).",
        "2️⃣  Create an array of arguments (argv), ending with NULL.",
        "3️⃣  Set envp to NULL (we’ll skip environment variables for now).",
        "4️⃣  Use `execve` syscall to replace your program with `/bin/ls`!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine you're stepping out of your house, and another person steps in with their own script — that's `execve`! It replaces *you* with *them*!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Launch `/bin/ls` from Assembly{RESET}")
    slow_print(f"""{DIM}
section .data
    path    db "/bin/ls", 0
    arg0    db "/bin/ls", 0
    argv    dq arg0, 0      ; argv = [pointer to arg0, NULL]
    envp    dq 0            ; no environment variables

section .text
    global _start

_start:
    mov     rax, 59         ; syscall: execve
    lea     rdi, [rel path] ; filename
    lea     rsi, [rel argv] ; argv
    lea     rdx, [rel envp] ; envp
    syscall

    ; If execve fails, exit gracefully
    mov     rax, 60
    mov     rdi, 1          ; error code
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Try modifying the program to launch `/bin/date` or `/usr/bin/env` instead!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ `execve` completely replaces your running process — no code after it runs.")
    slow_print("→ Make sure your strings are null-terminated!")
    slow_print("→ `argv` must end in a NULL pointer — just like in C!")

    # Bonus
    slow_print(f"{BOLD}🌟 Bonus Challenge:{RESET}")
    slow_print("→ Pass extra arguments to `ls` like `-l` or `-a` by extending the `argv` array.")
    slow_print("→ Try launching a program you write yourself!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Boom! You just made your program *morph* into another one! `execve` is the foundation of how shells launch commands. 🔧💥{RESET}")
