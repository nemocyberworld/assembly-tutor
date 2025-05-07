# lessons/practice_programs/swap_values.py

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
    print(f"\n{BOLD}🔁 Swap Values Using a Function!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Create a function that swaps the contents of two memory locations.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Allocate space for two integers using `.bss` or on the stack.",
        "2️⃣  Put values in those locations (e.g., 42 and 99).",
        "3️⃣  Write a function that takes *pointers* to those values.",
        "4️⃣  Swap them using a temporary register (like `rax`).",
        "5️⃣  Verify they’ve been swapped by checking the memory values."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Swapping is like trading items. 🧢🧤")
    slow_print("You need a temporary hand (register) to hold one item while you give the other!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Swapping 42 and 99{RESET}")
    slow_print(f"""{DIM}
section .bss
    a   resq 1        ; space for first value
    b   resq 1        ; space for second value

section .text
global _start

_start:
    mov     qword [a], 42
    mov     qword [b], 99

    lea     rdi, [a]       ; pass address of a
    lea     rsi, [b]       ; pass address of b
    call    swap           ; swap([a], [b])

    ; Now [a] = 99, [b] = 42

    mov     rax, 60        ; syscall: exit
    xor     rdi, rdi
    syscall

; ----------------------------
swap:
    mov     rax, [rdi]     ; rax = *a
    mov     rbx, [rsi]     ; rbx = *b

    mov     [rdi], rbx     ; *a = b
    mov     [rsi], rax     ; *b = a

    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Implement the `swap` function and try it on different pairs like (5, 10), (0, 999), etc.")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `lea` to get the address of a variable (like getting a pointer).")
    slow_print("→ Always use a temporary register to hold one value during the swap.")
    slow_print("→ Don't overwrite both values too early!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try swapping values in an array — can you reverse the first two elements?")
    slow_print("→ Print values before and after to verify correctness.")
    slow_print("→ Make your swap function reusable and efficient!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Nice work! You now understand how to swap values using pointers — a key idea in C, assembly, and beyond! ⚙️💡{RESET}")
