# lessons/practice_programs/string_concat.py

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
    print(f"\n{BOLD}➕ Concatenate Two Strings in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to append one null-terminated string to the end of another manually — like `strcat()` in C!\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define two strings (e.g., \"Hello\" and \" World\") in the `.data` section.",
        "2️⃣  Create a buffer in `.bss` large enough to hold both.",
        "3️⃣  Copy the first string into the buffer.",
        "4️⃣  Then copy the second string right after the first one's null terminator.",
        "5️⃣  The result: a single string containing both, null-terminated!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine cutting out two strips of paper with words and taping them end-to-end — now it's one long sentence! 📜\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Join \"Hi\" and \" there!\" into a single string{RESET}")
    slow_print(f"""{DIM}
section .data
    str1    db "Hi", 0
    str2    db " there!", 0

section .bss
    result  resb 32        ; buffer to hold concatenated string

section .text
global _start

_start:
    ; Copy str1 into result
    lea     rsi, [str1]    ; source
    lea     rdi, [result]  ; destination

copy_str1:
    lodsb                 ; load byte from [rsi] into AL, then increment rsi
    stosb                 ; store AL into [rdi], then increment rdi
    test    al, al
    jnz     copy_str1     ; repeat until null terminator (0)

    ; rdi now points to null terminator after str1
    ; Copy str2 into result (after str1)
    lea     rsi, [str2]

copy_str2:
    lodsb
    stosb
    test    al, al
    jnz     copy_str2

    ; Done — result now contains "Hi there!"
    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Define two strings and write a program that combines them into one result buffer!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Always make sure your result buffer is big enough!")
    slow_print("→ Use `lodsb`/`stosb` for byte-wise copy (or manual `mov` if preferred).")
    slow_print("→ Use `test al, al` to check for the null terminator.")
    slow_print("→ Make sure the final result ends with a null byte too!\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try concatenating three or more strings!")
    slow_print("→ What happens if the second string is empty?")
    slow_print("→ Write a function-style routine you can reuse later!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Well done! You've just built your own string glue in Assembly! Keep going — byte-by-byte mastery awaits! 🔧📦{RESET}")
