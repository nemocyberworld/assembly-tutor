# lessons/practice_programs/register_swap.py

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
    print(f"\n{BOLD}🔄 Swap Values Between Registers{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn to swap values between registers using multiple methods.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Load one value into `rax` and another into `rbx`.",
        "2️⃣  Swap their contents so that `rax` ends up with the original `rbx` value, and vice versa.",
        "3️⃣  Try two approaches:\n    - With a temporary register (e.g., `rcx`)\n    - Using the `xchg` instruction"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Example with temp register
    slow_print(f"\n{BOLD}🧠 Example 1: Using a Temp Register{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov     rax, 123
    mov     rbx, 456

    mov     rcx, rax
    mov     rax, rbx
    mov     rbx, rcx

    ; rax now = 456
    ; rbx now = 123

    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Example with xchg
    slow_print(f"\n{BOLD}🧠 Example 2: Using `xchg` Instruction{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov     rax, 123
    mov     rbx, 456

    xchg    rax, rbx

    ; rax now = 456
    ; rbx now = 123

    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write both versions of the register swap and inspect the register values after each method.\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ `xchg` is elegant and saves a register, but it can be slower on some CPUs due to implicit locking.")
    slow_print("→ The temp register method is more transparent and safer in certain contexts.\n")

    # Suggested registers
    slow_print(f"{BOLD}📦 Suggested Registers to Use:{RESET} rax, rbx, rcx")

    # Bonus
    slow_print(f"\n{GREEN}✨ Extra Challenge:{RESET}")
    slow_print("→ Try swapping values stored in memory addresses instead of registers.")
    slow_print("→ How would you do this with stack operations (push/pop)? 🤔")

    # Wrap-up
    print(f"\n{BOLD}🚀 Well done! Mastering these techniques gives you fine control over data flow in your programs. 🧠⚙️{RESET}")
