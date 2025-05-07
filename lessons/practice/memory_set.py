# lessons/practice_programs/memory_set.py

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
    print(f"\n{BOLD}🧼 Fill Memory with a Specific Byte (like memset)!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to fill a block of memory with a single byte value using a loop in Assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Reserve a block of memory using `.bss`.",
        "2️⃣  Choose a byte value to fill (e.g. `0xFF`, `'A'`, `0`).",
        "3️⃣  Use a loop to write that value into each byte of the block.",
        "4️⃣  Stop when you've filled the entire region!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine painting every tile 🎨 in a hallway with the same color. You start at the beginning and move forward one step at a time, painting each tile.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Fill 16 bytes with `0x41` ('A'){RESET}")
    slow_print(f"""{DIM}
section .bss
    buffer  resb 16        ; reserve 16 bytes of memory

section .text
global _start

_start:
    lea     rdi, [buffer]  ; pointer to the buffer
    mov     rcx, 16        ; number of bytes to fill
    mov     al, 0x41       ; value to store ('A')

fill_loop:
    mov     [rdi], al      ; store the value into memory
    inc     rdi            ; move to the next byte
    loop    fill_loop      ; repeat until rcx == 0

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create a buffer, pick a byte (like `0x00`, `'X'`, etc.), and write it into every slot of the buffer!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `.bss` with `resb` to make space.")
    slow_print("→ Use `mov [rdi], al` to store a single byte.")
    slow_print("→ You can use `loop` with `rcx`, or manually count with `dec` and `jnz`.")
    slow_print("→ Try viewing memory with a debugger like `gdb` to confirm your values!\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try filling different values into different regions.")
    slow_print("→ What if you fill with `0` and treat it like a C-string?")
    slow_print("→ Write a version that fills `words` (2 bytes) or `dwords` (4 bytes) instead!")

    # Wrap-up
    print(f"\n{BOLD}🏁 You just made your own tiny memory brush! Mastery of memory is mastery of machines — well done! 🧠💾{RESET}")
