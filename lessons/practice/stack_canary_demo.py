# lessons/practice_programs/stack_canary_demo.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🛡️ stack_canary_demo: Demonstrate Stack Canary Protection{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how stack canaries help detect buffer overflows and protect against memory corruption attacks.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Set up a local buffer on the stack (like an array or string).",
        "2️⃣  Place a special value (the 'canary') just before the return address.",
        "3️⃣  After your buffer operations, check if the canary is unchanged.",
        "4️⃣  If the canary is altered — 🚨 buffer overflow detected!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of the canary like a 🐤 bird in a coal mine — if it dies (changes), something bad is happening!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Canary-Based Overflow Check (Simulated){RESET}")
    slow_print(f"""{DIM}
section .bss
    buffer resb 32

section .text
global _start

_start:
    ; Simulate a canary
    mov     rbx, 0xDEADBEEFCAFEBABE     ; expected canary value
    push    rbx                         ; save canary on stack

    ; === Dangerous buffer write ===
    ; (in real use, you might overflow here)
    mov     rdi, buffer
    mov     byte [rdi], 'A'             ; pretend user input

    ; === Canary check ===
    pop     rax                         ; retrieve canary
    cmp     rax, 0xDEADBEEFCAFEBABE
    jne     overflow_detected           ; jump if tampered!

    ; Safe exit
    mov     rax, 60
    xor     rdi, rdi
    syscall

overflow_detected:
    ; Canary mismatch!
    mov     rax, 60
    mov     rdi, 1                      ; return error code
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Simulate an unsafe buffer write, guard it with a stack canary, and verify whether an overflow is detected!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `push` to store the canary before your buffer operations.")
    slow_print("→ Use `cmp` to check if it matches afterward.")
    slow_print("→ Simulate a buffer overflow by writing past the end of your array!")

    # Bonus
    slow_print(f"\n{BOLD}🧪 Bonus Experiment:{RESET}")
    slow_print("→ Try deliberately corrupting the stack to see the canary check fail.")
    slow_print("→ Explore how real compilers add canaries with `-fstack-protector`.")

    # Wrap-up
    print(f"\n{BOLD}{GREEN}🎉 Well done! Now you understand how stack canaries act as silent bodyguards for your return addresses! 🛡️{RESET}")
