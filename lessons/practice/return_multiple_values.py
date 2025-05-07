# lessons/practice_programs/return_multiple_values.py

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
    print(f"\n{BOLD}🔁 Return Multiple Values from a Function!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to return more than one value from a function using registers and memory.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Decide how many values to return.",
        "2️⃣  Use registers (like `rax`, `rdx`, `rcx`) for 2–3 small values.",
        "3️⃣  Or pass a pointer to a memory block where the function will store the results.",
        "4️⃣  Return control to the caller and read back the values!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine a chef 🍳 returning a meal on a tray (registers). If it's too much to carry, they leave it in a lunchbox (memory) and hand you the box!\n")

    # Example 1: Using Registers
    slow_print(f"{BOLD}🧠 Example 1: Return min & max using rax and rdx{RESET}")
    slow_print(f"""{DIM}
section .text
global _start

_start:
    mov     rdi, 10         ; a = 10
    mov     rsi, 42         ; b = 42
    call    min_max

    ; rax = min (10)
    ; rdx = max (42)

    mov     rax, 60         ; exit
    xor     rdi, rdi
    syscall

; ---------------------------
min_max:
    cmp     rdi, rsi
    mov     rax, rdi        ; assume a is min
    mov     rdx, rsi        ; assume b is max
    jle     .done

    ; swap if a > b
    mov     rax, rsi
    mov     rdx, rdi

.done:
    ret
{RESET}""")

    # Example 2: Using Memory
    slow_print(f"\n{BOLD}🧠 Example 2: Return two values via a pointer{RESET}")
    slow_print(f"""{DIM}
section .bss
    result resq 2           ; reserve space for 2 values

section .text
global _start

_start:
    lea     rdi, [result]   ; pointer to result memory
    mov     rsi, 7          ; input a
    mov     rdx, 5          ; input b
    call    product_sum

    ; result[0] = a * b = 35
    ; result[1] = a + b = 12

    mov     rax, 60
    xor     rdi, rdi
    syscall

; ---------------------------
; product_sum(ptr, a, b)
; writes product to [ptr], sum to [ptr+8]
product_sum:
    mov     rax, rsi
    imul    rax, rdx
    mov     [rdi], rax       ; store product

    mov     rax, rsi
    add     rax, rdx
    mov     [rdi+8], rax     ; store sum
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write a function that takes two integers and returns both their difference and average (as integers). Try one version with registers, and one with memory!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `rax`, `rdx`, or even `rcx` if you're staying in registers.")
    slow_print("→ Use `resq` in `.bss` to reserve memory for returned values.")
    slow_print("→ You can return structs this way in real C programs too!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Create a struct-like result block with 3 fields: sum, product, and average.")
    slow_print("→ Return all 3 in memory using a single pointer argument.")
    slow_print("→ Call it from another assembly function that prints the values!")

    # Wrap-up
    print(f"\n{BOLD}🏁 You did it! Now you can write functions that return not just one, but MANY results — just like pros do in low-level programming! 🚀📦{RESET}")
