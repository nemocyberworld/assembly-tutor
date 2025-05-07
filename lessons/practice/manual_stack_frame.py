# lessons/practice_programs/manual_stack_frame.py

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
    print(f"\n{BOLD}📦 manual_stack_frame: Build and Destroy Your Own Stack Frame{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to create and tear down your own stack frame using `push`, `pop`, and base/frame pointers.\n")
    time.sleep(0.5)

    # Why
    slow_print(f"{BLUE}💡 Why Learn This?{RESET}")
    slow_print("→ Most programming languages manage stack frames for you.")
    slow_print("→ But *you* are learning assembly, so you get to do it yourself!")
    slow_print("→ Understanding stack frames is key to mastering function calls, recursion, and debugging.\n")

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Push the old `rbp` to save the caller's frame pointer.",
        "2️⃣  Set `rbp` to the current `rsp` (new base of this frame).",
        "3️⃣  Allocate space on the stack for local variables (e.g., `sub rsp, 16`).",
        "4️⃣  Do some operations, like saving a value into [rbp-8].",
        "5️⃣  Restore the old frame with `mov rsp, rbp` and `pop rbp`.",
        "6️⃣  Return with `ret`!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}🧠 Analogy:{RESET} Think of a stack frame like a temporary workbench. You set it up, do your work, clean it up, and move on.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Manual Stack Frame{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    call my_function

    ; exit
    mov rax, 60
    xor rdi, rdi
    syscall

my_function:
    push rbp            ; save caller's base pointer
    mov rbp, rsp        ; set up new base pointer

    sub rsp, 16         ; allocate 16 bytes for locals
    mov qword [rbp-8], 123  ; store 123 as a "local variable"

    ; (Imagine doing something cool here)

    mov rsp, rbp        ; clean up local stack space
    pop rbp             ; restore old base pointer
    ret                 ; return to caller
{RESET}""")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Always restore the stack before returning!")
    slow_print("→ Use `gdb` or `objdump` to inspect your frames.")
    slow_print("→ Stack grows downward — lower memory addresses!")

    # Bonus
    slow_print(f"\n{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Add a second local variable at [rbp-16] and store a second value.")
    slow_print("→ Try nesting function calls — can you trace the stack frames? 🔍")

    # Wrap-up
    print(f"\n{GREEN}{BOLD}🏁 Awesome! You've now built and destroyed your own stack frame — like a true assembly architect! 🏗️🧠{RESET}")
