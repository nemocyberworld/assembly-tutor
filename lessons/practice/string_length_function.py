# lessons/practice_programs/string_length_function.py

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
    print(f"\n{BOLD}🔡 String Length via Function Call!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Write a function that calculates the length of a null-terminated string — like your own version of `strlen`!\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Pass the address of a null-terminated string in `rdi`.",
        "2️⃣  Inside the function, walk through the string one byte at a time.",
        "3️⃣  Stop when you find the null terminator (`0`).",
        "4️⃣  Return the length (number of bytes before null) in `rax`.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine counting beads on a necklace until you reach a knot that stops you. 🧵📿\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: strlen(\"hello\") = 5{RESET}")
    slow_print(f"""{DIM}
section .data
    message db "hello", 0    ; Null-terminated string

section .text
    global _start

_start:
    mov     rdi, message     ; Pass address of string
    call    strlen           ; rax will contain the length

    ; Exit with length as return code
    mov     rdi, rax         ; exit code = string length
    mov     rax, 60          ; syscall: exit
    syscall

; strlen function: input in rdi, output in rax
strlen:
    xor     rax, rax         ; length = 0

.count_loop:
    cmp     byte [rdi + rax], 0  ; check for null terminator
    je      .done
    inc     rax              ; increment length
    jmp     .count_loop

.done:
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create your own `strlen` function that counts how many characters until the null terminator.")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Null-terminated strings end with `0`, so scan until you hit that.")
    slow_print("→ Use `rax` to count how many characters you’ve moved past.")
    slow_print("→ Don’t forget to return from your function with `ret`!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Modify the function to count only alphabetic characters.")
    slow_print("→ Try printing the result using `printf` or a syscall.")
    slow_print("→ What if the string is empty? Make sure your code handles it!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Boom! You've built a real function that works like `strlen` — and in assembly! 💪🧠{RESET}")
