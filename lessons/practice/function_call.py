# lessons/practice_programs/function_call.py

import time

# ANSI Colors
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
    print(f"\n{BOLD}🔧 Lesson: Use `call` and `ret` to Simulate a Function{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}🎯 Goal:{RESET} Learn how to use `call` and `ret` in x86-64 assembly to simulate basic function calls.\n")
    time.sleep(0.5)

    # Intro
    slow_print(f"{BLUE}📞 What's a Function Call?{RESET}")
    slow_print("In high-level languages, functions are like helpers you can summon to do work.")
    slow_print("In assembly, you simulate this by jumping to code with `call`, then coming back with `ret`.\n")

    # Instructions
    slow_print(f"{YELLOW}📘 Instructions:{RESET}")
    instructions = [
        "1️⃣  Define a function label (e.g., `my_function:`).",
        "2️⃣  Use `call my_function` to jump to it.",
        "3️⃣  In the function, do some work (e.g., print or add).",
        "4️⃣  End the function with `ret` to return to where `call` was made.",
        "5️⃣  Observe that execution resumes right after the `call`."
    ]
    for i in instructions:
        slow_print(f"{MAGENTA}{i}{RESET}")
        time.sleep(0.3)

    # Visual
    slow_print(f"\n{BLUE}📦 Analogy:{RESET} Think of `call` as 📞 dialing a helper. When they’re done, they hang up with `ret`, and you continue your day!")

    # Example Code
    slow_print(f"\n{BOLD}🧠 Example Code:{RESET}")
    print(f"""{DIM}
section .text
global _start

_start:
    call    my_function       ; Call the function

    mov     rax, 60           ; Exit syscall
    xor     rdi, rdi
    syscall

my_function:
    mov     rax, 42           ; Do something
    ; (You could print this value with a syscall)
    ret                       ; Return to where we called from
{RESET}""")

    # Your Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write a function that adds two numbers and stores the result.")
    slow_print("→ Then return to the main code and print or inspect the result.\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("  - `call` pushes the return address onto the stack.")
    slow_print("  - `ret` pops that return address and jumps to it.")
    slow_print("  - Don't forget to `ret` or you might crash into unknown territory! 💥\n")

    # Bonus Challenge
    slow_print(f"{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("  - Pass values to your function using registers (e.g., `rdi`, `rsi`).")
    slow_print("  - Write a function that multiplies two numbers passed in registers.")
    slow_print("  - Call it multiple times with different arguments!\n")

    # Wrap-up
    slow_print(f"{BOLD}🏁 Congrats! You've just summoned your first assembly function like a wizard 🧙‍♂️ — with `call` and `ret` as your magic words!{RESET}")
