# lessons/practice_programs/fibonacci_recursive.py

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
    print(f"\n{BOLD}🌀 Recursive Fibonacci in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn to implement the classic recursive Fibonacci function in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Recall: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2).",
        "2️⃣  Base cases: Fibonacci(0) = 0, Fibonacci(1) = 1.",
        "3️⃣  For other values, call the function recursively twice.",
        "4️⃣  Use `call` to recurse and combine results using `add`.",
        "5️⃣  Store intermediate results in registers or on the stack."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of a Fibonacci call like a tree 🌳.\n")
    slow_print("Each branch splits into two smaller branches until you hit the base cases. 🌿\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Fibonacci(5) = 5{RESET}")
    slow_print(f"""{DIM}
; fibonacci(n): returns nth Fibonacci number
; input:  rdi = n
; output: rax = Fibonacci(n)

global _start
section .text

_start:
    mov     rdi, 5          ; calculate Fibonacci(5)
    call    fibonacci

    ; result in rax (should be 5)

    mov     rax, 60         ; syscall: exit
    xor     rdi, rdi
    syscall

; ----------------------------
fibonacci:
    cmp     rdi, 1
    jbe     .base_case      ; if n <= 1, return n

    push    rdi             ; save n
    dec     rdi
    call    fibonacci       ; fib(n-1)
    mov     rbx, rax        ; save fib(n-1)

    pop     rdi             ; restore original n
    push    rbx             ; save fib(n-1)

    sub     rdi, 2
    call    fibonacci       ; fib(n-2)

    pop     rbx             ; restore fib(n-1)
    add     rax, rbx        ; fib(n) = fib(n-1) + fib(n-2)
    ret

.base_case:
    mov     rax, rdi        ; return n (0 or 1)
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Implement the recursive Fibonacci function. Test different values like 3, 5, 7.")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use the call stack carefully: always `push` before calling and `pop` afterward.")
    slow_print("→ Base cases are important: they stop the recursion!")
    slow_print("→ Test with small inputs first — larger ones grow fast! 🐢")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Count how many total function calls are made for Fibonacci(5).")
    slow_print("→ Try writing an iterative version. Compare speed and memory usage.")
    slow_print("→ Add a print syscall to show the result dynamically!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome work! You've just built a recursive Fibonacci function — like a real computer scientist! 💻✨{RESET}")
