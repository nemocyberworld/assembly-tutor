# lessons/practice_programs/nested_calls.py

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
    print(f"\n{BOLD}🪆 Nested Function Calls in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Call one function from inside another — just like nesting dolls!\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Write a simple function that doubles a number (e.g., double(x) = x * 2).",
        "2️⃣  Write another function that calls `double`, then adds 10 to the result.",
        "3️⃣  Call the second function from `_start` with your input.",
        "4️⃣  Return the final result in `rax`.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of it like a chef calling their assistant to prepare part of a dish. 🍳🧑‍🍳 The main function delegates a step!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: double_then_add10(7) → 7 * 2 + 10 = 24{RESET}")
    slow_print(f"""{DIM}
global _start
section .text

_start:
    mov     rdi, 7             ; input = 7
    call    double_then_add10  ; result in rax

    ; rax now contains 24

    mov     rax, 60            ; syscall: exit
    xor     rdi, rdi
    syscall

; double_then_add10(x): return double(x) + 10
double_then_add10:
    push    rdi                ; save original input

    call    double             ; rdi = input, rax = double(input)
    mov     rbx, rax           ; store result in rbx

    add     rbx, 10            ; add 10
    mov     rax, rbx           ; final result
    pop     rdi                ; restore original rdi
    ret

; double(x): return x * 2
double:
    shl     rdi, 1             ; rdi * 2 (fast multiply)
    mov     rax, rdi
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write two functions: one should call the other. Try doing `triple_then_square(x)`, or `square_then_add(x)`!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Each function should keep its own logic small and reusable.")
    slow_print("→ Save/restore any registers you change (especially `rdi`, `rbx`, etc.).")
    slow_print("→ Use `call` for delegation — just like in higher-level languages!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Chain 3+ functions together (e.g., double -> square -> add_constant).")
    slow_print("→ Make one function call another *multiple times* (e.g., call `double` twice).")
    slow_print("→ Print intermediate values using syscalls if you're feeling fancy!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome! You've just leveled up into structured assembly programming with nested calls — just like the pros! 🚀🧠{RESET}")
