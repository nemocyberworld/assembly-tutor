# lessons/practice_programs/recursive_factorial.py

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
    print(f"\n{BOLD}🌀 Recursive Factorial in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to write a recursive function in Assembly that computes the factorial of a number (n!).\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Pass the number `n` in a register (e.g. `rdi`).",
        "2️⃣  Check if `n <= 1`, and if so, return 1 (base case).",
        "3️⃣  Otherwise, recursively call `factorial(n - 1)`.",
        "4️⃣  Multiply the result by `n` and return it.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of recursion like stacking dinner plates 🍽️. Each call adds a plate to the stack, and once you're done, you clean (return) them in reverse order!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Recursive factorial function for rdi = 5{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov     rdi, 5          ; input: 5
    call    factorial       ; call function
    mov     rbx, rax        ; store result (120)

    ; exit
    mov     rax, 60
    xor     rdi, rdi
    syscall

factorial:
    push    rbp             ; save base pointer
    mov     rbp, rsp

    cmp     rdi, 1
    jbe     .base_case      ; if n <= 1, return 1

    push    rdi             ; save current n
    dec     rdi             ; n = n - 1
    call    factorial       ; recursive call
    pop     rdi             ; restore n
    imul    rax, rdi        ; rax = n * factorial(n - 1)
    jmp     .done

.base_case:
    mov     rax, 1

.done:
    mov     rsp, rbp
    pop     rbp
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Modify the code to compute factorials of different numbers (e.g., 3, 7, 10) and verify the results!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ The return value goes in `rax`.")
    slow_print("→ Use `push` and `pop` to save/restore registers during recursive calls.")
    slow_print("→ Always end functions with `ret` and restore `rbp` and `rsp` if modified.")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Add a print syscall to show the result on the console.")
    slow_print("→ Track how many times the function is called (like a counter in memory).")
    slow_print("→ Try tracing the stack manually to visualize how recursion works.")

    # Wrap-up
    print(f"\n{BOLD}🏁 Amazing! You just built a recursive function in pure assembly! Welcome to the realm of stack frames, call stacks, and infinite depth! 🧠🔁{RESET}")
