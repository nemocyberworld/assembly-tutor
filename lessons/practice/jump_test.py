# lessons/practice_programs/jump_test.py

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
    print(f"\n{BOLD}🪂 Jump Based on Comparison (x86-64 Assembly){RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn to compare values using `cmp` and take different actions with conditional jumps.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Load two values into registers (like rax and rbx).",
        "2️⃣  Use `cmp` to compare them — like a subtraction test.",
        "3️⃣  Choose a conditional jump (`je`, `jne`, `jl`, `jg`, etc.).",
        "4️⃣  Exit with 0 or 1 depending on the comparison result."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Code Example
    slow_print(f"\n{BOLD}🧠 Example Skeleton:{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov rax, 10       ; First number
    mov rbx, 20       ; Second number

    cmp rax, rbx      ; Compare rax vs rbx
    jl less_than      ; Jump if rax < rbx

greater_or_equal:
    mov rdi, 1        ; Exit code 1: rax >= rbx
    jmp exit

less_than:
    mov rdi, 0        ; Exit code 0: rax < rbx

exit:
    mov rax, 60       ; syscall: exit
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET}")
    slow_print("→ Write a program that compares two values and exits with 0 if one is less than the other, or 1 otherwise.")

    # Tip
    slow_print(f"\n{BLUE}💡 Tip:{RESET} `cmp a, b` acts like `a - b`, but without modifying the original values. Just flags!")

    # Bonus
    slow_print(f"\n{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("→ Try using other conditions like:")
    slow_print("   🔸 `je` (equal)")
    slow_print("   🔸 `jne` (not equal)")
    slow_print("   🔸 `jg` (greater than)")
    slow_print("→ Change exit codes based on these branches!")

    # Wrap-up
    print(f"\n{BOLD}🧠 Nice! You now have basic conditional logic in raw assembly. Use it to build smarter flows! 🛠️✨{RESET}")
