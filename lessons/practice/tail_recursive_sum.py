# lessons/practice_programs/tail_recursive_sum.py

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
    print(f"\n{BOLD}🔁 Tail-Recursive Sum Function (with Optimization Power!) {RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Implement a tail-recursive function in Assembly to calculate the sum of integers from N to 1 (i.e., sum(N) = N + N-1 + ... + 1).\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Write a function that takes two arguments: the current number `n`, and an accumulator `acc`.",
        "2️⃣  If `n == 0`, return `acc` — it's the final sum!",
        "3️⃣  Otherwise, tail-call the function again with `n-1` and `acc + n`.",
        "4️⃣  Use tail-call optimization: avoid growing the call stack if possible."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine you’re adding numbers backwards from 5 to 1.\n")
    slow_print("Instead of remembering each number (stack), just keep a running total (accumulator)! 🧮\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: sum(5) → 5+4+3+2+1 = 15{RESET}")
    slow_print(f"""{DIM}
; tail_recursive_sum(n, acc) returns sum(n) in rax
; rdi = current n
; rsi = accumulator

global _start
section .text

_start:
    mov     rdi, 5          ; n = 5
    xor     rsi, rsi        ; acc = 0
    call    tail_sum

    ; result in rax: should be 15

    mov     rax, 60         ; syscall: exit
    xor     rdi, rdi
    syscall

; ----------------------------------------
tail_sum:
    cmp     rdi, 0
    je      .done

    add     rsi, rdi        ; acc += n
    dec     rdi             ; n -= 1
    jmp     tail_sum        ; tail call (no new stack frame)

.done:
    mov     rax, rsi        ; return acc
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Implement your own tail-recursive function to sum from N to 1. Try different N values, and experiment with printing the result!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Tail-recursion = recursive call is the *last* thing the function does.")
    slow_print("→ Using `jmp` instead of `call` avoids stack buildup (tail-call optimization).")
    slow_print("→ This is a good trick for avoiding stack overflows on large input.")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try implementing this without using recursion at all — just a loop!")
    slow_print("→ Modify the function to calculate factorial instead of a sum.")
    slow_print("→ Compare this with a regular (non-tail) recursive version — what changes on the stack?")

    # Wrap-up
    print(f"\n{BOLD}🏁 Great work! Tail recursion is a powerful concept — it’s like recursion, but stack-friendly! 🚀🎯{RESET}")
