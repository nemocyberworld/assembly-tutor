# lessons/practice_programs/sum_array.py

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
    print(f"\n{BOLD}➕ Sum All Elements of an Integer Array!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to walk through an array in memory and calculate the total sum of all its elements.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define or reserve an array of integers.",
        "2️⃣  Set up a loop to walk through each element using a pointer.",
        "3️⃣  Keep a `sum` register (e.g., `rax`) and add each element to it.",
        "4️⃣  Use pointer math to move forward (8 bytes at a time).",
        "5️⃣  Stop when you've reached the end of the array."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine going trick-or-treating 👻🍬. You collect candies from each house (array element) and add them to your bag (sum).\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Sum of a 5-Element Array{RESET}")
    slow_print(f"""{DIM}
section .data
    array   dq 3, 6, 9, 12, 15     ; 5 integers
    len     equ 5

section .text
global _start

_start:
    xor     rax, rax        ; sum = 0
    mov     rcx, len        ; loop counter
    lea     rsi, [array]    ; pointer to first element

sum_loop:
    cmp     rcx, 0
    je      done

    add     rax, [rsi]      ; sum += *rsi
    add     rsi, 8          ; move to next element (64-bit)
    dec     rcx
    jmp     sum_loop

done:
    ; rax now contains the total sum

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create your own array of 5 or more numbers and sum them using a loop. Print the result if you're feeling fancy!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `.data` to define arrays with known values.")
    slow_print("→ Use `lea` to get the starting address of the array.")
    slow_print("→ Use a counter register (like `rcx`) and pointer (`rsi`) together.")
    slow_print("→ Always increment the pointer by 8 bytes for 64-bit integers.\n")

    # Bonus
    slow_print(f"{BOLD}🎲 Bonus Challenge:{RESET}")
    slow_print("→ Try summing an array with negative numbers. Does it still work?")
    slow_print("→ Can you compute the average of the array? (Hint: divide sum by count)")
    slow_print("→ Try summing an array with 100 elements!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Well done! You've just mastered array traversal and accumulation — a foundational skill in any language, especially Assembly! 💪🧠{RESET}")
