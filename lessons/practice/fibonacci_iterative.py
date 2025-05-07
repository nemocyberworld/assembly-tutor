# lessons/practice_programs/fibonacci_iterative.py

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
    print(f"\n{BOLD}🔂 Fibonacci the Fast Way — Iterative Style!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn to compute Fibonacci numbers using a loop instead of recursion.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Fibonacci(n) = 0, 1, 1, 2, 3, 5, 8, ...",
        "2️⃣  Start with two variables: prev = 0, curr = 1.",
        "3️⃣  Loop from 2 to n, updating the two variables: next = prev + curr.",
        "4️⃣  Store the result in a register like `rax`.",
        "5️⃣  Use simple `add`, `mov`, and loop instructions!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} It's like counting steps 🦶— you only need the last two numbers to take the next one!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Fibonacci(6) = 8{RESET}")
    slow_print(f"""{DIM}
; fibonacci_iterative(n): returns nth Fibonacci number
; input:  rdi = n
; output: rax = Fibonacci(n)

global _start
section .text

_start:
    mov     rdi, 6          ; n = 6
    call    fibonacci

    ; result in rax (should be 8)

    mov     rax, 60         ; syscall: exit
    xor     rdi, rdi
    syscall

; ----------------------------
fibonacci:
    cmp     rdi, 1
    jbe     .base_case      ; if n == 0 or 1, return n

    mov     rax, 0          ; prev = 0
    mov     rbx, 1          ; curr = 1
    mov     rcx, 2          ; counter = 2

.loop:
    cmp     rcx, rdi
    ja      .done

    mov     rdx, rax        ; rdx = prev
    add     rdx, rbx        ; rdx = prev + curr (next)
    mov     rax, rbx        ; prev = curr
    mov     rbx, rdx        ; curr = next
    inc     rcx
    jmp     .loop

.done:
    mov     rax, rbx        ; return curr (final result)
    ret

.base_case:
    mov     rax, rdi        ; return n (0 or 1)
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write your own iterative Fibonacci function! Try different input values (n = 3, 5, 10).")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Track two registers: one for the previous value, one for the current.")
    slow_print("→ Start your loop at 2, since 0 and 1 are base cases.")
    slow_print("→ Use `cmp`, `ja`, and `jmp` for your loop control.")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Print all intermediate Fibonacci numbers during the loop!")
    slow_print("→ Modify it to store all values in an array.")
    slow_print("→ Try calculating really big Fibonacci numbers — how far can you go?")

    # Wrap-up
    print(f"\n{BOLD}🏁 Well done! You now know both recursive and iterative Fibonacci — power and performance in one! 💪🧠{RESET}")
