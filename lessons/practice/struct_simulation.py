# lessons/practice_programs/struct_simulation.py

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
    print(f"\n{BOLD}📦 Simulate a C-style Struct Using Memory Offsets!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to simulate a struct in Assembly by grouping related fields and accessing them using offsets.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define a memory block big enough for all the struct's fields.",
        "2️⃣  Define offsets for each field (e.g., name at +0, age at +8).",
        "3️⃣  Use `[base + offset]` to read or write each field.",
        "4️⃣  (Optional) Pack multiple 'structs' in a larger array!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of a struct like a labeled drawer cabinet 🗄️. Each drawer (offset) holds one piece of data: name, age, score, etc.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Simulate a `Person` struct with fields: age, height{RESET}")
    slow_print(f"""{DIM}
; Struct layout:
; Person:
;   age    -> 0 bytes (offset 0)
;   height -> 8 bytes (offset 8)

section .bss
    person      resb 16        ; 2 fields, 8 bytes each

section .text
global _start

_start:
    lea     rsi, [person]      ; pointer to our "struct"

    ; Set fields
    mov     qword [rsi + 0], 25     ; age = 25
    mov     qword [rsi + 8], 180    ; height = 180 cm

    ; Read fields back
    mov     rax, [rsi + 0]     ; rax = age
    mov     rbx, [rsi + 8]     ; rbx = height

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create a struct with 3 fields (e.g., ID, score, level), store values into it, and read them back!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `.bss` to reserve space for your struct (e.g., `resb 24` for 3 x 8-byte fields).")
    slow_print("→ Define readable labels for offsets: `ID = 0`, `SCORE = 8`, etc.")
    slow_print("→ Use pointer math: `[rsi + offset]` to access the fields.\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Create an array of 3 `Person` structs and fill them in a loop!")
    slow_print("→ Make a function that prints a struct’s data (e.g., name & score).")
    slow_print("→ Simulate nested structs by combining offsets cleverly 🤯")

    # Wrap-up
    print(f"\n{BOLD}🏁 Well done! You’ve just simulated structs — one of the most powerful C features — using only raw memory and math. This is serious systems-level wizardry! 🧙‍♂️🧠{RESET}")
