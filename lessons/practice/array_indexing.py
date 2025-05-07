# lessons/practice_programs/array_indexing.py

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
    print(f"\n{BOLD}📚 Access Array Elements with Indexing & Pointers!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to access specific elements in an array using both indexing and pointer arithmetic.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define an array of numbers in the `.data` section.",
        "2️⃣  Use `rsi` or another register to point to the start of the array.",
        "3️⃣  Access elements using: `[rsi + index * element_size]`.",
        "4️⃣  (Optional) Use a loop to visit each element and perform actions!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine your array is a row of mailboxes 📬. Each one is a little further down the street. The index tells you how many steps forward to take!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Access the 3rd element (index 2) from an array{RESET}")
    slow_print(f"""{DIM}
section .data
    my_array    dq 10, 20, 30, 40, 50   ; 64-bit integers

section .bss
    result      resq 1                 ; to store the element

section .text
global _start

_start:
    lea     rsi, [my_array]           ; rsi points to start of array
    mov     rbx, 2                    ; index of the 3rd element
    mov     rax, [rsi + rbx*8]        ; load element at index 2
    mov     [result], rax             ; store it in result

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Pick any index and load that value from an array into a register. Try it with different numbers!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Multiply the index by 8 if you're using 64-bit integers (each element is 8 bytes).")
    slow_print("→ `lea` helps you get the address of the array — it's like a pointer shortcut.")
    slow_print("→ Try using a loop to walk through the array, printing or storing values.\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Use a loop to print every element in the array.")
    slow_print("→ Try summing up all the elements as you go!")
    slow_print("→ Can you write a small routine that fetches the Nth element when given an index?")

    # Wrap-up
    print(f"\n{BOLD}🏁 Nice! You've just unlocked one of the most important powers in low-level programming: direct memory access! 🧠🛠️{RESET}")
