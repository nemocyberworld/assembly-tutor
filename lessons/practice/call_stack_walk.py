# lessons/practice_programs/call_stack_walk.py

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
    print(f"\n{BOLD}🧵 Walk the Call Stack Like a Pro!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to walk the call stack manually using frame pointers to trace function calls.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Enable stack frames by using `rbp` as the base pointer in each function.",
        "2️⃣  Save the old `rbp` and set up a new one: `push rbp` then `mov rbp, rsp`.",
        "3️⃣  Call several nested functions (e.g., `main → foo → bar`).",
        "4️⃣  Inside the deepest function, follow the saved `rbp` chain to walk up the stack.",
        "5️⃣  Print or examine return addresses or saved `rbp`s to understand the chain."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine the call stack as a stack of sticky notes: each one shows who called who. Walking the stack is like peeling them off, one by one!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Trace Function Calls with Frame Pointers{RESET}")
    slow_print(f"""{DIM}
section .text
    global _start

_start:
    call    func1
    mov     rax, 60
    xor     rdi, rdi
    syscall

func1:
    push    rbp
    mov     rbp, rsp
    call    func2
    pop     rbp
    ret

func2:
    push    rbp
    mov     rbp, rsp

    ; Walk the stack (one level up)
    mov     rax, [rbp]        ; old base pointer (caller’s rbp)
    mov     rbx, [rbp+8]      ; return address to caller

    ; Optionally print or inspect rax and rbx

    pop     rbp
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create 3 nested functions and print the saved `rbp` and return addresses at each level!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ Stack grows down — each `rbp` points to the previous frame.")
    slow_print("→ At `[rbp]` is the old `rbp`, and at `[rbp+8]` is the return address.")
    slow_print("→ You can stop walking when a `NULL` or unusual value is found.\n")

    # Bonus
    slow_print(f"{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Write a loop to walk up 3 frames and dump their return addresses.")
    slow_print("→ Try calling the program from C and walking into the libc or main() frame.")

    # Wrap-up
    print(f"\n{BOLD}🏁 Fantastic! You’ve just peeked behind the curtain of function calls — true wizardry of the stack realm! 🔮🧠{RESET}")
