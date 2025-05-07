# lessons/practice_programs/exit_code.py

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
    print(f"\n{BOLD}🛑 Returning a Specific Exit Code (x86-64, Linux){RESET}\n")
    time.sleep(1)

    # Intro
    slow_print(f"{YELLOW}Did you know your program can leave a message for the shell? Let's learn about exit codes!{RESET}")
    slow_print(f"{CYAN}This is useful for scripting, automation, and just looking cool 😎{RESET}")
    time.sleep(1)

    # Objective
    slow_print(f"\n{BOLD}🎯 Objective:{RESET} Write a program that returns an exit code of 42 to the shell.")

    # Explanation
    slow_print(f"\n{BOLD}🔍 About Syscalls:{RESET}")
    slow_print("The `exit` syscall on x86-64 Linux is syscall number 60.")
    slow_print("To use it:")
    slow_print(" - Put the exit code in `rdi`.")
    slow_print(" - Put 60 in `rax`.")
    slow_print(" - Call `syscall`.")
    time.sleep(1)

    # Instructions
    slow_print(f"\n{BOLD}🔧 Instructions:{RESET}")
    instructions = [
        "1️⃣  Place the desired exit code (e.g., 42) into RDI.",
        "2️⃣  Place 60 (the syscall number for exit) into RAX.",
        "3️⃣  Execute the syscall instruction to exit."
    ]
    for line in instructions:
        slow_print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)

    # Hint
    slow_print(f"\n{BOLD}{GREEN}💡 Hint:{RESET} Exit codes are passed via RDI. The shell reads it with `$?`.")

    # Example
    slow_print(f"\n{BOLD}🧠 Example Code:{RESET}")
    slow_print(f"""{DIM}
section .text
    global _start

_start:
    mov     rdi, 42        ; exit code
    mov     rax, 60        ; syscall number for exit
    syscall
{RESET}""")
    time.sleep(1)

    # Check exit code
    slow_print(f"\n{BOLD}{BLUE}🔎 Checking the Exit Code:{RESET}")
    slow_print("Run this in your terminal after building the program:")
    slow_print(f"{BOLD}  $ ./exit_code; echo $?{RESET}")
    time.sleep(0.5)

    # Task
    slow_print(f"\n{BOLD}{GREEN}🎯 Your Task:{RESET}")
    slow_print("→ Change the exit code to different values and observe the output of `echo $?`.")
    slow_print("→ Try values like 0, 1, 100, 255. See what changes!")

    # Bonus
    slow_print(f"\n{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("→ Create a loop that exits with 0 if a value is even, or 1 if it's odd.")
    slow_print("→ Return a code based on user input (advanced).")
    time.sleep(1)

    # Wrap-up
    print(f"\n{BOLD}✅ Boom! You’ve returned your first custom exit code. Let the scripts rejoice! 🧙‍♀️✨{RESET}")
