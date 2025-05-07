# lessons/practice_programs/reverse_array.py

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
    print(f"\n{BOLD}🔄 Reverse an Array In-Place Using Pointers!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to reverse an array by swapping elements from both ends using pointers in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Reserve or define an array of values (e.g., 5 numbers).",
        "2️⃣  Use two pointers: one at the start, one at the end.",
        "3️⃣  Swap values at those pointers.",
        "4️⃣  Move the start pointer forward and the end pointer backward.",
        "5️⃣  Repeat until they meet or cross — that's a full reverse!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of flipping a pancake stack 🍽️. You take the top and bottom ones and switch them. Keep working inward until they’re all reversed!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Reversing a 5-Element Array{RESET}")
    slow_print(f"""{DIM}
section .bss
    arr     resq 5                 ; reserve space for 5 elements

section .text
global _start

_start:
    ; Store values: [10, 20, 30, 40, 50]
    mov     rax, 10
    mov     [arr], rax

    mov     rax, 20
    mov     [arr + 8], rax

    mov     rax, 30
    mov     [arr + 16], rax

    mov     rax, 40
    mov     [arr + 24], rax

    mov     rax, 50
    mov     [arr + 32], rax

    ; rsi = start pointer
    lea     rsi, [arr]

    ; rdi = end pointer
    lea     rdi, [arr + 32]

reverse_loop:
    cmp     rsi, rdi
    jge     done                  ; done if start >= end

    ; swap values at [rsi] and [rdi]
    mov     rax, [rsi]
    mov     rbx, [rdi]
    mov     [rsi], rbx
    mov     [rdi], rax

    ; move pointers
    add     rsi, 8
    sub     rdi, 8
    jmp     reverse_loop

done:
    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Store at least 5 values in an array and reverse them in-place using two pointers and a loop!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `lea` to set your pointer registers (e.g., `rsi`, `rdi`).")
    slow_print("→ Step by 8 bytes (1 quadword) to move across 64-bit values.")
    slow_print("→ Remember to `cmp` pointers and stop when they meet or cross.")

    # Bonus
    slow_print(f"{BOLD}🚀 Bonus Challenge:{RESET}")
    slow_print("→ Try reversing an array with an *odd* number of elements.")
    slow_print("→ Can you write a loop to print the reversed array using syscalls?")
    slow_print("→ Reverse the array again — does it go back to the original order?")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome work! Reversing with pointers builds confidence in memory and algorithmic thinking. Keep flipping that brain power! 🔁🧠{RESET}")
