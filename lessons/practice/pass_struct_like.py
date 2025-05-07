# lessons/practice_programs/pass_struct_like.py

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
    print(f"\n{BOLD}📦 Pass a Struct-Like Memory Block to a Function!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Simulate passing a C-style `struct` to a function by giving a pointer to a memory block.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Create a struct-like memory block (e.g., 3 integers: x, y, z).",
        "2️⃣  Fill it with values in `.data` or `.bss`.",
        "3️⃣  Pass its address to a function using `rdi`.",
        "4️⃣  Inside the function, use offsets to access fields (e.g., `[rdi]`, `[rdi+8]`, etc).",
        "5️⃣  Do something useful with the data, then return."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine mailing a form 📨 — the envelope is the pointer, and the paper inside holds fields like name, age, score... Accessing the right offset means reading the right line!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Sum x, y, and z fields in a struct{RESET}")
    slow_print(f"""{DIM}
section .data
    my_struct: dq 5, 10, 15     ; struct: x=5, y=10, z=15

section .text
global _start

_start:
    lea     rdi, [my_struct]    ; rdi = pointer to struct
    call    sum_fields

    ; rax now holds 30
    mov     rax, 60             ; syscall: exit
    xor     rdi, rdi
    syscall

; ----------------------------------------
; sum_fields(struct_ptr)
; returns x + y + z in rax
sum_fields:
    mov     rax, [rdi]          ; x
    add     rax, [rdi+8]        ; + y
    add     rax, [rdi+16]       ; + z
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create your own struct with 4 fields (like id, age, score, level), pass it to a function, and compute something with it!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Each field is 8 bytes (`dq`), so access them with `[rdi]`, `[rdi+8]`, `[rdi+16]`, etc.")
    slow_print("→ Use `lea` to pass the address of your struct.")
    slow_print("→ Use labels to make your code clearer!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Write two functions: one to read the struct, one to modify a field (e.g., increase score).")
    slow_print("→ Chain function calls to pass the struct around like a real program.")
    slow_print("→ Try integrating with C: pass a struct from C to Assembly!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Nice job! You've just simulated structs in Assembly using pointers and memory offsets — a core skill for systems-level coding! 🧠⚙️{RESET}")
