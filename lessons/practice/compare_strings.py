# lessons/practice_programs/compare_strings.py

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
    print(f"\n{BOLD}🧪 Compare Two Strings for Equality in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to compare two null-terminated strings one character at a time, and check if they’re the same.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define two strings in the `.data` section, ending with a null byte (`0`).",
        "2️⃣  Set up two pointers — one for each string.",
        "3️⃣  Loop through both strings, comparing characters.",
        "4️⃣  If any pair of characters is different, they’re not equal.",
        "5️⃣  If you reach the null terminator on both strings *at the same time*, they are equal!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of checking two secret codes 🔐. You compare them letter by letter. One mismatch — the lock stays shut. Perfect match? Access granted! ✅\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Compare \"hello\" and \"hello\"{RESET}")
    slow_print(f"""{DIM}
section .data
    str1    db  "hello", 0
    str2    db  "hello", 0

section .text
global _start

_start:
    lea     rsi, [str1]         ; pointer to first string
    lea     rdi, [str2]         ; pointer to second string

compare_loop:
    mov     al, [rsi]
    mov     bl, [rdi]
    cmp     al, bl              ; compare characters
    jne     not_equal           ; if different, they're not equal

    cmp     al, 0               ; are we at the end of both strings?
    je      equal               ; if yes, strings are equal

    inc     rsi
    inc     rdi
    jmp     compare_loop

not_equal:
    ; strings are not equal
    mov     rax, 60
    mov     rdi, 1              ; exit code 1 = not equal
    syscall

equal:
    ; strings are equal
    mov     rax, 60
    xor     rdi, rdi            ; exit code 0 = equal
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create two strings and compare them character by character. Exit with code 0 if equal, 1 if not!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Always end your strings with a null terminator (0).")
    slow_print("→ Use `lea` to load the address of the strings.")
    slow_print("→ Use `cmp` and conditional jumps (`jne`, `je`) to control the flow.")
    slow_print("→ Don't forget to check both characters *and* for end-of-string!\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try comparing strings of different lengths.")
    slow_print("→ What happens if one string has an extra space or punctuation?")
    slow_print("→ Can you build a version that returns which string is greater (like `strcmp`)?")

    # Wrap-up
    print(f"\n{BOLD}🏁 Boom! You’ve just built your own string comparison logic. Great job mastering loops, pointers, and character-level thinking! 💡🧠{RESET}")
