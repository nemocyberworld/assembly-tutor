# lessons/practice_programs/increment_loop.py

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
    print(f"\n{BOLD}🔁 Increment a Register in a Loop (x86-64 Assembly){RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Build a loop that increments a register until a certain limit is reached.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Initialize a register (like rcx) to 0.",
        "2️⃣  Set another register (like rbx) as the loop counter.",
        "3️⃣  In the loop, increment rcx and decrement rbx.",
        "4️⃣  When rbx reaches 0, stop the loop.",
        "5️⃣  Optionally: convert and print the final value of rcx!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Code Example
    slow_print(f"\n{BOLD}🧠 Example Code:{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov rcx, 0         ; register to increment
    mov rbx, 10        ; loop counter

.loop:
    inc rcx            ; add 1 to rcx
    dec rbx            ; subtract 1 from rbx
    jnz .loop          ; loop if rbx != 0

    ; rcx now holds 10

    mov rax, 60        ; syscall: exit
    xor rdi, rdi
    syscall
{RESET}""")
    time.sleep(1)

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET}")
    slow_print("→ Write a loop that increments a register 20 times.")
    slow_print("→ (Optional) Print the final value to verify it!")

    # Tip
    slow_print(f"\n{BLUE}💡 Tip:{RESET} You can also use the `loop` instruction (only works with `ecx`).")

    # Bonus
    slow_print(f"\n{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("→ Make the step size variable (e.g., add 2 instead of 1).")
    slow_print("→ Use a nested loop to simulate counting in two dimensions.")

    # Wrap-up
    print(f"\n{BOLD}🚀 Done! You just built a low-level loop. Feels powerful, right? 🔧💥{RESET}")
