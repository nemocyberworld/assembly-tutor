# lessons/practice_programs/call_simple.py

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
    print(f"\n{BOLD}🔁 Call a Simple Function in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to define and call a simple function in Assembly using `call` and `ret`.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define a label that acts as your function (e.g., `my_function:`).",
        "2️⃣  Use `call my_function` from your main code to jump to it.",
        "3️⃣  In the function, do something — maybe set a register!",
        "4️⃣  End the function with `ret` to return to the caller.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Calling a function is like sending your friend on a quick errand. When they’re done, they come back and you keep going.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Call a function that sets rax = 42{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    call    set_value       ; jump to the function

    ; rax now contains 42
    mov     rbx, rax        ; save it elsewhere (optional)

    ; exit
    mov     rax, 60
    xor     rdi, rdi
    syscall

set_value:
    mov     rax, 42         ; set a value
    ret                     ; return to the caller
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write a function that sets a register to your favorite number. Call it from `_start` and store the result!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ The `call` instruction saves your return address (where to come back to).")
    slow_print("→ `ret` pulls that address from the stack and jumps back.")
    slow_print("→ You can pass data using registers (like rdi, rsi, etc).")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Write a function that takes a number in `rdi` and returns `rdi * 2` in `rax`.")
    slow_print("→ Chain multiple function calls together.")
    slow_print("→ Print out the result with a syscall for extra flair!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Bravo! You just made your first real Assembly function! Reusable code is clean code, even at the lowest level! 💡🔧{RESET}")
