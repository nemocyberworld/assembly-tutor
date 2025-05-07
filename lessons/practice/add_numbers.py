# lessons/practice_programs/add_numbers.py

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
    print(f"\n{BOLD}➕ Add Two Numbers and Print the Result (x86-64, Linux){RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}📢 Let's add two numbers in assembly and print the result!{RESET}")
    slow_print(f"{CYAN}We'll use basic arithmetic, a tiny ASCII conversion, and Linux syscalls.{RESET}")
    time.sleep(1)

    # Setup
    slow_print(f"\n{BOLD}🧰 What You'll Use:{RESET}")
    setup_info = [
        "✔ Constants defined in `.data` section",
        "✔ `mov` and `add` for arithmetic",
        "✔ Simple loop/div for ASCII conversion",
        "✔ `write` syscall to print result"
    ]
    for item in setup_info:
        slow_print(f"{MAGENTA}{item}{RESET}")
        time.sleep(0.4)

    # Code
    slow_print(f"\n{BOLD}💡 Program Skeleton (NASM syntax):{RESET}")
    slow_print(f"""{DIM}section .data
    num1    dq 5
    num2    dq 7
    buffer  times 20 db 0

section .text
    global _start

_start:
    mov     rax, [num1]
    add     rax, [num2]

    ; TODO: Convert to ASCII and store in buffer
    ; TODO: Write buffer to stdout using syscall

    mov     rax, 60        ; exit
    xor     rdi, rdi
    syscall{RESET}""")
    time.sleep(1)

    # Breakdown
    slow_print(f"\n{BOLD}🔍 Breakdown:{RESET}")
    breakdown = [
        "✔ Load numbers from memory with `mov rax, [num1]`",
        "✔ Add values using `add`",
        "✔ Convert number in `rax` to ASCII (manual conversion)",
        "✔ Store digits in reverse, then write with `syscall 1`"
    ]
    for line in breakdown:
        slow_print(f"{CYAN}{line}{RESET}")
        time.sleep(0.4)

    # Build
    slow_print(f"\n{BOLD}⚙️ Build and Run:{RESET}")
    slow_print(f"{MAGENTA}1. Save as `add_numbers.asm`")
    slow_print(f"2. Assemble: nasm -f elf64 add_numbers.asm -o add_numbers.o")
    slow_print(f"3. Link: ld add_numbers.o -o add_numbers")
    slow_print(f"4. Run: ./add_numbers{RESET}")
    time.sleep(1)

    # Challenge
    slow_print(f"\n{BOLD}{BLUE}🎯 Optional Challenge:{RESET}")
    slow_print(f"{MAGENTA}→ Format the result as '5 + 7 = 12'")
    slow_print("→ Try using signed 64-bit numbers")
    slow_print("→ Try reading numbers from user input with syscall 0 (read){RESET}")
    time.sleep(1)

    # Wrap-up
    print(f"\n{BOLD}✅ Lesson complete! Try it yourself and tweak the numbers or output style!{RESET}")
