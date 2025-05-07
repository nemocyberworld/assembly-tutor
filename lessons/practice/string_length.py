# lessons/practice_programs/string_length.py

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
    print(f"\n{BOLD}🔤 Calculate the Length of a String in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to find the length of a null-terminated string (like in C) using a loop in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define a string in the `.data` section, ending with a null byte (0).",
        "2️⃣  Use a register (e.g., `rsi`) to point to the start of the string.",
        "3️⃣  Use a loop to check each byte until you hit the null terminator.",
        "4️⃣  Count the number of bytes — that’s your string length!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine walking down a hallway with tiles 📏. Each tile has a letter on it. You keep stepping forward until you hit an empty tile — that's the end of the string!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Finding the Length of \"Hello\"{RESET}")
    slow_print(f"""{DIM}
section .data
    mystring    db 'Hello', 0     ; null-terminated string

section .text
global _start

_start:
    lea     rsi, [mystring]       ; pointer to start of string
    xor     rcx, rcx              ; counter = 0

count_loop:
    mov     al, [rsi + rcx]       ; get current character
    cmp     al, 0                 ; is it null terminator?
    je      done                  ; if yes, we're done!
    inc     rcx                   ; otherwise, increase count
    jmp     count_loop            ; and repeat

done:
    ; rcx now holds the string length (5 in this case)

    mov     rax, 60               ; syscall: exit
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Define your own null-terminated string and write a loop that counts how many characters it has!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Make sure your string ends with a `0` (null byte) — that’s how the loop knows when to stop.")
    slow_print("→ Use `lea` to get the address of your string, and `mov al, [rsi + rcx]` to grab characters one by one.")
    slow_print("→ Use `rcx` or another register as a counter.")

    # Bonus
    slow_print(f"{BOLD}🚀 Bonus Challenge:{RESET}")
    slow_print("→ Try writing multiple strings and counting each one!")
    slow_print("→ Print the length of the string using a syscall.")
    slow_print("→ What happens if you forget the null byte? 🤯 Try it and find out (carefully).")

    # Wrap-up
    print(f"\n{BOLD}🏁 Nicely done! Understanding how strings work at the byte level gives you serious low-level insight. Keep it up! 💥{RESET}")
