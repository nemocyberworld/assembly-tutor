# lessons/practice_programs/call_printf.py

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
    print(f"\n{BOLD}📣 Calling printf from Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to call the C library function `printf` directly from your assembly code!\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use the C library by linking with `gcc` (not just `nasm`).",
        "2️⃣  Define your format string in `.data` (like `'Hello %d\\n'`).",
        "3️⃣  Set up arguments in registers (`rdi`, `rsi`, etc.).",
        "4️⃣  Call `printf` just like any external function!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} It's like asking your neighbor C to help with printing. Just give them clear instructions (format + data)!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Print an Integer with printf{RESET}")
    slow_print(f"""{DIM}
; Save as: call_printf.asm
; Compile: nasm -f elf64 call_printf.asm && gcc -no-pie -o call_printf call_printf.o

section .data
    fmt db "Value is: %d", 10, 0     ; Format string: "Value is: %d\n"

section .text
    extern printf
    global main

main:
    mov     rdi, fmt        ; 1st argument: format string
    mov     rsi, 1234       ; 2nd argument: value to print
    xor     rax, rax        ; Clear rax for vararg calls (System V ABI rule!)
    call    printf          ; Call the C printf function

    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Print your name, a number, or a combination using different format strings!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `db` to define strings. Null-terminate them with `0`.")
    slow_print("→ `rdi` = format string, `rsi` = 1st value, `rdx` = 2nd, etc.")
    slow_print("→ Always clear `rax` to 0 before calling vararg functions like `printf`.")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Print multiple values: e.g., `%d + %d = %d`.")
    slow_print("→ Pass strings using a pointer to `db`-defined text.")
    slow_print("→ Try combining `printf` with custom functions to print computed results!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome job! You’ve just bridged assembly and C — now you can make your programs talk to the outside world! 🎤🔗{RESET}")
