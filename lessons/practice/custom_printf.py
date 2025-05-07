# lessons/practice_programs/custom_printf.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🖨️ custom_printf: Build Your Own Basic Print Function!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how formatted printing works by creating a simple version of `printf` in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Create a function that takes a null-terminated string as input.",
        "2️⃣  Use `syscall` with `write` (syscall number 1) to print the string to stdout.",
        "3️⃣  (Bonus) Parse the string manually to support %c or %s placeholders.",
        "4️⃣  Keep it simple: no need to fully implement C-style formatting!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine a mini typewriter function: it reads characters one-by-one from memory and taps them out to the screen.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: A Minimalist `print_string` Function{RESET}")
    slow_print(f"""{DIM}
section .data
    message db "Hello from custom printf!", 10, 0   ; null-terminated string

section .text
    global _start

_start:
    mov     rdi, message     ; pointer to string
    call    print_string     ; print it

    mov     rax, 60          ; exit
    xor     rdi, rdi
    syscall

print_string:
    push    rdi              ; save argument

.next_char:
    mov     al, byte [rdi]   ; load byte
    cmp     al, 0
    je      .done            ; if null, end
    mov     rsi, rdi
    mov     rdx, 1
    mov     rax, 1
    mov     rdi, 1
    syscall
    inc     rdi
    jmp     .next_char

.done:
    pop     rdi
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write a `print_string` function that takes a pointer to a null-terminated string and prints it to the console!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use syscall #1 (`write`) with `rdi=1`, `rsi=pointer`, `rdx=length`.")
    slow_print("→ Loop character by character until you hit a `0` (null terminator).")
    slow_print("→ Want a challenge? Add support for `%c` to print a character.")

    # Bonus
    slow_print(f"\n{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Add your own `print_char` function and use it inside `print_string`.")
    slow_print("→ Try supporting `%s` manually by detecting it in the format string.")

    # Wrap-up
    print(f"\n{GREEN}{BOLD}📣 You just built your first custom print function. The magic of `printf` is no longer a mystery! 🔧💬{RESET}")
