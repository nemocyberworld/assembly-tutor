# lessons/practice_programs/find_max.py

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
    print(f"\n{BOLD}🏆 Find the Maximum Element in an Array!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to scan through an array of integers and find the largest one using Assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Create an array of integers (e.g., 5, 12, 7, 99, 3).",
        "2️⃣  Initialize a variable to hold the 'current maximum'.",
        "3️⃣  Loop through each number in the array:",
        "    🔸 If the current number is greater than the max, update the max.",
        "4️⃣  When done, the max variable holds the largest number!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine you’re judging a contest 🏅 — each new contestant is compared to the current best. If they beat the champ, they take the crown!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Find the max in [3, 7, 2, 10, 6]{RESET}")
    slow_print(f"""{DIM}
section .data
    numbers     dq 3, 7, 2, 10, 6   ; array of 64-bit integers
    count       equ 5              ; number of elements

section .bss
    max_value   resq 1             ; space to store the result

section .text
global _start

_start:
    lea     rsi, [numbers]         ; pointer to array
    mov     rcx, count             ; loop counter
    mov     rax, [rsi]             ; first element as initial max
    mov     rbx, 1                 ; start at second element

find_loop:
    cmp     rbx, rcx               ; check if we've hit the end
    jge     done

    mov     rdx, [rsi + rbx*8]     ; load next number
    cmp     rdx, rax               ; compare with current max
    jle     skip
    mov     rax, rdx               ; update max if needed

skip:
    inc     rbx
    jmp     find_loop

done:
    mov     [max_value], rax       ; store the result in memory

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create an array of at least 5 numbers and write a loop that finds and stores the largest one!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `mov rdx, [rsi + index*8]` to access the next 64-bit number.")
    slow_print("→ Keep your current max in `rax`, or a memory location.")
    slow_print("→ Use `cmp` and `jle` to skip numbers that aren't bigger.")
    slow_print("→ Remember to multiply the index by 8 (for 64-bit values).\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Print the result to the terminal using a syscall!")
    slow_print("→ Try finding the *smallest* number instead.")
    slow_print("→ Make it work for an array of signed integers!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Boom! You just wrote your first comparison-based algorithm in Assembly! That's how pros do it — one number at a time. 🔍💪{RESET}")
