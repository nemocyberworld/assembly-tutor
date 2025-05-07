# lessons/practice_programs/stack_push_pop.py

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
    print(f"\n{BOLD}📦 Lesson: Push and Pop Values on the Stack{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to use the stack to temporarily store and retrieve data in x86-64 assembly.\n")
    time.sleep(0.5)

    # What is the Stack?
    slow_print(f"{BLUE}💡 What is the Stack?{RESET}")
    slow_print("The stack is like a stack of plates 🍽️ — last in, first out (LIFO).")
    slow_print("Use it to temporarily save values, like registers or function data.\n")

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Load a number into a register like `rax`.",
        "2️⃣  Use `push rax` to place it on the stack (this decreases `rsp`).",
        "3️⃣  Later, use `pop rbx` to retrieve it into `rbx` (this increases `rsp`).",
        "4️⃣  Check that the value is preserved by printing or inspecting it."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}🍰 Analogy:{RESET} You’re holding a cake 🎂 (value in `rax`). You put it down on a plate stack (`push`).")
    slow_print("Then someone else picks it up later (`pop`) — still the same cake!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example Code:{RESET}")
    print(f"""{DIM}
section .text
global _start

_start:
    mov     rax, 1337      ; Load value into rax
    push    rax            ; Push it to the stack

    pop     rbx            ; Pop it back into rbx
    ; rbx now holds 1337

    ; optional: print value to verify

    mov     rax, 60        ; exit syscall
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Try using `push` and `pop` with different values and registers.")
    slow_print("→ Push multiple values and pop them in reverse order — test the LIFO nature!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("  - Only use 64-bit registers with `push`/`pop` (e.g., `rax`, not `eax`).")
    slow_print("  - Be careful not to pop more than you push — the stack gets confused!")
    slow_print("  - The stack pointer `rsp` changes with each push/pop — track it if you’re curious.\n")

    # Bonus Challenge
    slow_print(f"{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("  - Push 3 numbers onto the stack and pop them into 3 different registers.")
    slow_print("  - Print them to verify the correct reverse order.")
    slow_print("  - Try modifying the stack manually using `[rsp]`, `[rsp+8]`, etc. (advanced!)\n")

    # Wrap-up
    print(f"\n{BOLD}🏁 Well done! You’ve now got stacking superpowers 🧙 — one step closer to mastering function calls and recursion!{RESET}")
