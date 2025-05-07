# lessons/practice_programs/find_char.py

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
    print(f"\n{BOLD}🔍 Find the First Occurrence of a Character in a String!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to search for a character inside a null-terminated string using Assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define a string and the target character to search for.",
        "2️⃣  Set up a loop to walk through the string byte by byte.",
        "3️⃣  Use `cmp` to compare each byte with the target.",
        "4️⃣  If it matches, you found it!",
        "5️⃣  If you reach the null terminator (`0`) first, the character wasn’t found."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of scanning a sentence for a hidden letter 🔍 — you go left to right until you spot it or reach the end.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Find 'o' in \"hello world\"{RESET}")
    slow_print(f"""{DIM}
section .data
    mystring    db "hello world", 0
    target      db 'o'

section .text
global _start

_start:
    lea     rsi, [mystring]      ; pointer to string
    movzx   al, byte [target]    ; target character

search_loop:
    mov     bl, [rsi]            ; get current character
    cmp     bl, 0                ; check for end of string
    je      not_found

    cmp     bl, al               ; compare with target
    je      found

    inc     rsi                  ; move to next character
    jmp     search_loop

not_found:
    ; character not found
    mov     rax, 60
    mov     rdi, 1               ; exit code 1 = not found
    syscall

found:
    ; character found
    mov     rax, 60
    xor     rdi, rdi             ; exit code 0 = found
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Define a string and a character, then write a loop to find the first time that character appears!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `movzx` to load the target character safely.")
    slow_print("→ Stop when you hit a match *or* the null terminator.")
    slow_print("→ Use `rsi` as a pointer that walks the string.")
    slow_print("→ You can return the index or just exit with 0/1 for found/not found.\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Print the index (offset) where the character was found!")
    slow_print("→ What if the character appears more than once?")
    slow_print("→ Try writing a version that counts how many times it appears!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome work! You've just learned how to search through memory like a pro! Keep exploring, byte by byte! 🔎🧠{RESET}")
