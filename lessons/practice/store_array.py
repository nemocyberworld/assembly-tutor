# lessons/practice_programs/store_array.py

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
    print(f"\n{BOLD}🧮 Store and Access an Array in Memory{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to store multiple values in memory as an array and access them using assembly instructions.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Reserve space for an array using `.bss` or define values in `.data`.",
        "2️⃣  Store values using `mov` with offsets like `[array+0]`, `[array+8]`, etc.",
        "3️⃣  Load the values back using the same offsets or even a loop.",
        "4️⃣  (Optional) Print each value to verify correctness."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine memory as a row of mailboxes 📬. Each box holds a number. You drop numbers into them (store), and later walk by to collect them (load).\n")

    # Example
    slow_print(f"{BOLD}🧠 Example Using `.bss` for an Array:{RESET}")
    slow_print(f"""{DIM}
section .bss
    array   resq 3         ; reserve space for 3 quadwords (3 × 8 bytes)

section .text
global _start

_start:
    mov     rax, 10
    mov     [array], rax          ; store 10 at array[0]

    mov     rax, 20
    mov     [array + 8], rax      ; store 20 at array[1]

    mov     rax, 30
    mov     [array + 16], rax     ; store 30 at array[2]

    ; Retrieve values
    mov     rbx, [array]          ; rbx = 10
    mov     rcx, [array + 8]      ; rcx = 20
    mov     rdx, [array + 16]     ; rdx = 30

    ; Done
    mov     rax, 60               ; syscall: exit
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Store at least 3 numbers in an array, retrieve them, and (optionally) print them one by one!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Remember: each element takes up 8 bytes if you're using 64-bit integers.")
    slow_print("→ Use `[label + offset]` to access array elements manually.")
    slow_print("→ Want a challenge? Loop through the array using a counter and a base pointer!")

    # Bonus
    slow_print(f"{BOLD}🚀 Bonus Challenge:{RESET}")
    slow_print("→ Can you reverse the array in memory?")
    slow_print("→ Try summing all the array values and storing the result in another memory location!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Nice work! Arrays are the building blocks of data structures. Master them, and you're on your way to serious low-level skills! 💪{RESET}")
