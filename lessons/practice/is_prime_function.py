# lessons/practice_programs/is_prime_function.py

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
    print(f"\n{BOLD}🔢 Prime Checker Function in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Write a function in assembly that checks if a given number is a prime number.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Pass the number to test in `rdi`.",
        "2️⃣  Handle special cases (e.g., numbers < 2 are not prime).",
        "3️⃣  Loop from 2 up to sqrt(n), checking for divisibility.",
        "4️⃣  Return 1 in `rax` if it's prime, or 0 if not.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of checking if a number has any 'sneaky factors' that divide it evenly. If it does — not prime! 😲🔍\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: is_prime(7) = 1, is_prime(10) = 0{RESET}")
    slow_print(f"""{DIM}
section .text
    global _start

_start:
    mov     rdi, 7           ; number to test
    call    is_prime

    ; Exit with result in rdi
    mov     rdi, rax
    mov     rax, 60
    syscall

; is_prime(rdi) -> rax = 1 (prime) or 0 (not prime)
is_prime:
    cmp     rdi, 2
    jl      .not_prime       ; if n < 2 → not prime
    mov     rcx, 2           ; rcx = current divisor

.loop:
    mov     rax, rdi
    xor     rdx, rdx
    div     rcx              ; divide rdi by rcx

    cmp     rdx, 0
    je      .not_prime       ; if divisible → not prime

    inc     rcx
    mov     rax, rcx
    imul    rax, rax
    cmp     rax, rdi
    jbe     .loop            ; while (rcx*rcx <= rdi)

    mov     rax, 1           ; it's prime!
    ret

.not_prime:
    xor     rax, rax         ; not prime → return 0
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write a function called `is_prime` that returns 1 if the number is prime, and 0 if not.")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `div` to check if the number is divisible.")
    slow_print("→ Primes only have two divisors: 1 and themselves.")
    slow_print("→ Loop only up to the square root of the number (to save time!).")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Use the result to print 'prime' or 'not prime' using `printf`.")
    slow_print("→ Extend your program to find all primes below 100.")
    slow_print("→ Can you make it more efficient using only odd divisors (after 2)? 🤯")

    # Wrap-up
    print(f"\n{BOLD}🏁 Bravo! You've just written your own prime checker — in assembly! You're thinking like a CPU now! 🧠⚡️{RESET}")
