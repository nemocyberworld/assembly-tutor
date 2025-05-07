# lessons/practice_programs/call_with_multiple_args.py

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
    print(f"\n{BOLD}📞 Call a Function with Multiple Arguments!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to pass multiple integer values to a function using registers, and receive a result.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use registers to pass arguments (e.g., rdi, rsi, rdx).",
        "2️⃣  Call a function that does some math with the inputs.",
        "3️⃣  Inside the function, use the registers directly or move them to temporary ones.",
        "4️⃣  Return the result in `rax`.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of the registers like delivery trucks 🚚 — each one carries a piece of data to your function. The function processes it and sends the result back in `rax`.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Add 3 numbers together in a function{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov     rdi, 10           ; first number
    mov     rsi, 20           ; second number
    mov     rdx, 30           ; third number
    call    add_three         ; call the function

    ; rax now contains 60
    ; exit
    mov     rax, 60
    xor     rdi, rdi
    syscall

; --------------------------------
; add_three(rdi, rsi, rdx)
; returns sum in rax
add_three:
    mov     rax, rdi          ; rax = first
    add     rax, rsi          ; rax += second
    add     rax, rdx          ; rax += third
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write a function that multiplies 2 integers and then adds a third: result = (a * b) + c")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ System V AMD64 uses: rdi, rsi, rdx, rcx, r8, r9 (in that order) for the first six arguments.")
    slow_print("→ Return values go in `rax`.")
    slow_print("→ Don’t forget to `ret` at the end of your function!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Write a function with 4 arguments: (a + b) * (c - d)")
    slow_print("→ Try calling it from C with inline assembly and passing values that way.")
    slow_print("→ Print the result using a syscall to show off your math magic!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome work! Passing multiple arguments opens the door to real function logic in assembly — you’re officially building reusable low-level tools now! 🔧🧠{RESET}")
