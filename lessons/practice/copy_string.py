# lessons/practice_programs/copy_string.py

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
    print(f"\n{BOLD}📋 Copy a Null-Terminated String in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to copy a string, character by character, from one memory location to another using a loop.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define a null-terminated string in the `.data` section.",
        "2️⃣  Reserve space for the destination using `.bss`.",
        "3️⃣  Use two pointers: one for source, one for destination.",
        "4️⃣  Loop through each byte: copy from source to dest.",
        "5️⃣  Stop when you hit the null terminator (byte = 0)."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine you’re a scribe 🧾. You read a letter one character at a time and rewrite it on a new sheet. You stop when you see a period (null terminator)!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Copy \"Hi!\" to Another Location{RESET}")
    slow_print(f"""{DIM}
section .data
    source      db  'Hi!', 0          ; null-terminated source string

section .bss
    destination resb 10               ; reserve space for copy

section .text
global _start

_start:
    lea     rsi, [source]             ; source pointer
    lea     rdi, [destination]        ; destination pointer

copy_loop:
    mov     al, [rsi]                 ; load byte from source
    mov     [rdi], al                 ; store byte into destination
    cmp     al, 0                     ; is it null terminator?
    je      done                      ; if yes, stop
    inc     rsi                       ; move to next source byte
    inc     rdi                       ; move to next destination byte
    jmp     copy_loop

done:
    ; String has been copied successfully!

    ; Exit program
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write your own string and copy it into a new memory area using a loop, one character at a time!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `db 'your string', 0` to define a null-terminated string.")
    slow_print("→ Use `.bss` and `resb` to make space for the destination.")
    slow_print("→ Don’t forget to copy the null terminator — it marks the end of the string!")
    slow_print("→ You can later print the copied string using a syscall if you want.\n")

    # Bonus
    slow_print(f"{BOLD}🚀 Bonus Challenge:{RESET}")
    slow_print("→ Try copying longer strings — does it still work?")
    slow_print("→ Modify the destination after copying — maybe reverse it or convert to uppercase?")
    slow_print("→ Print both original and copied strings to confirm your success!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome! Copying strings builds your understanding of memory, loops, and pointer arithmetic. You’re thinking like a real low-level pro now! 💾🧠{RESET}")
