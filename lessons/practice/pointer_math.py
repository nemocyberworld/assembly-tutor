# lessons/practice_programs/pointer_math.py

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
    print(f"\n{BOLD}🧭 Pointer Math: Walk Through Memory with Style!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to use pointer arithmetic to access and manipulate memory addresses in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Reserve memory for multiple values (like an array).",
        "2️⃣  Use a register (e.g. `rsi`) as a pointer to the start of the array.",
        "3️⃣  Use pointer arithmetic: add/subtract from the pointer to access other elements.",
        "4️⃣  (Optional) Use a loop to walk through memory automatically!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of a pointer like a 🧍walking person with a flashlight. The flashlight shows the memory spot they're at. Move forward or backward to visit other spots!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Walking Through an Array Using a Pointer{RESET}")
    slow_print(f"""{DIM}
section .bss
    values  resq 3              ; reserve space for 3 integers (24 bytes)

section .text
global _start

_start:
    ; Store some values
    mov     rax, 100
    mov     [values], rax

    mov     rax, 200
    mov     [values + 8], rax

    mov     rax, 300
    mov     [values + 16], rax

    ; Set pointer to start of the array
    lea     rsi, [values]       ; rsi now points to values[0]

    ; Load first value
    mov     rax, [rsi]          ; rax = 100

    ; Move pointer forward (to values[1])
    add     rsi, 8
    mov     rbx, [rsi]          ; rbx = 200

    ; Move pointer forward again (to values[2])
    add     rsi, 8
    mov     rcx, [rsi]          ; rcx = 300

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Store 3–5 values in memory. Use a pointer (like `rsi`) to walk through the values, one by one, and load them into registers!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `lea` to load the address of the array into a register (acts like a pointer).")
    slow_print("→ Use `add` or `sub` to move your pointer around (just like indexing).")
    slow_print("→ 64-bit values need 8-byte steps: add 8 to go to the next item.")
    slow_print("→ Try a loop with a counter to automate your pointer walk!")

    # Bonus
    slow_print(f"{BOLD}🚀 Bonus Challenge:{RESET}")
    slow_print("→ Sum all values in the array using a loop and a pointer.")
    slow_print("→ Try walking *backward* through the array after reaching the end!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Fantastic! You’ve just mastered memory navigation. Pointers are powerful tools — use them wisely! 🧠🧭{RESET}")
