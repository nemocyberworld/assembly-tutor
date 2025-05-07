# lessons/practice_programs/countdown.py

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
    print(f"\n{BOLD}⏳ Countdown from a Number to Zero (x86-64, Linux){RESET}\n")
    time.sleep(1)

    # Intro
    slow_print(f"{YELLOW}Ready to build a simple loop? Let’s count down!{RESET}")
    slow_print(f"{CYAN}This will teach you loops, conditionals, and a bit of control flow magic! 🧙‍♂️{RESET}")
    time.sleep(1)

    # Objective
    slow_print(f"\n{BOLD}🎯 Objective:{RESET} Create a countdown program using a loop that stops at zero.\n")
    
    # Step-by-step
    slow_print(f"{BOLD}🔧 Steps:{RESET}")
    steps = [
        "1️⃣  Set a register (like `rcx`) with the starting number.",
        "2️⃣  Print or keep track of the current value (optional).",
        "3️⃣  Use `dec` to subtract 1 each time.",
        "4️⃣  Loop using `jnz` (jump if not zero).",
        "5️⃣  Exit cleanly when the counter hits zero."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.4)

    # Example code
    slow_print(f"\n{BOLD}💡 Code Skeleton:{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov rcx, 5        ; starting countdown value

.loop:
    ; Optionally: print rcx here
    dec rcx           ; decrement the counter
    jnz .loop         ; loop if rcx != 0

    ; done counting down
    mov rax, 60       ; syscall: exit
    xor rdi, rdi
    syscall
{RESET}""")
    time.sleep(1)

    # Explanation
    slow_print(f"\n{BOLD}🔍 How It Works:{RESET}")
    explanations = [
        "✔ `mov rcx, 5` — sets up your loop counter.",
        "✔ `dec rcx` — subtracts 1 from `rcx`.",
        "✔ `jnz .loop` — loops back if `rcx` isn't zero.",
        "✔ `syscall` with `rax=60` exits cleanly."
    ]
    for line in explanations:
        slow_print(f"{CYAN}{line}{RESET}")
        time.sleep(0.4)

    # Build instructions
    slow_print(f"\n{BOLD}🛠️ Build & Run:{RESET}")
    slow_print(f"{MAGENTA}1. Save as `countdown.asm`")
    slow_print("2. Assemble: nasm -f elf64 countdown.asm -o countdown.o")
    slow_print("3. Link: ld countdown.o -o countdown")
    slow_print("4. Run: ./countdown{RESET}")
    time.sleep(1)

    # Challenge
    slow_print(f"\n{BOLD}{GREEN}🎯 Your Task:{RESET}")
    slow_print("→ Make a countdown from 10 to 0.")
    slow_print("→ Print each number as it counts down (for extra practice).")

    # Tip & bonus
    slow_print(f"\n{BOLD}{BLUE}💡 Tip:{RESET} If printing, make sure you don’t skip printing 0. Check value *before* or *after* `dec` accordingly.")

    slow_print(f"\n{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print(f"{MAGENTA}→ Add a sound (like ASCII bell: '\\a') or newline after each number.")
    slow_print("→ Add user input to choose the countdown start value!{RESET}")
    time.sleep(1)

    # Wrap-up
    print(f"\n{BOLD}✅ Mission accomplished! You’ve built your first countdown loop in Assembly! 🚀{RESET}")
