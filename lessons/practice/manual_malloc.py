# lessons/practice_programs/manual_malloc.py

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
    print(f"\n{BOLD}🧠 manual_malloc: Allocate Memory with mmap!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to dynamically allocate memory at runtime using the `mmap` syscall in x86-64 Linux.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use syscall 9 (mmap) to request a new memory block.",
        "2️⃣  Set size, protection (read/write), flags (anonymous/private), and file descriptor (-1).",
        "3️⃣  The syscall returns a pointer to usable memory — like malloc!",
        "4️⃣  Optionally write values to that memory and later deallocate with `munmap`."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of `mmap` as calling the landlord (kernel) to rent an empty apartment (memory). Once granted, it’s all yours to use!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Allocate 4096 Bytes and Store a Value{RESET}")
    slow_print(f"""{DIM}
section .data
    size    equ 4096
    prot    equ 3            ; PROT_READ | PROT_WRITE
    flags   equ 0x22         ; MAP_PRIVATE | MAP_ANONYMOUS

section .text
    global _start

_start:
    ; Arguments for mmap
    xor     rdi, rdi         ; addr = NULL (let kernel choose)
    mov     rsi, size        ; length = 4096 bytes
    mov     rdx, prot        ; PROT_READ | PROT_WRITE
    mov     r10, flags       ; MAP_PRIVATE | MAP_ANONYMOUS
    mov     r8, -1           ; fd = -1 (no file)
    xor     r9, r9           ; offset = 0
    mov     rax, 9           ; syscall number for mmap
    syscall

    ; rax now holds pointer to memory
    mov     [rax], byte 42   ; store value 42 at start of block

    ; Done – exit cleanly
    mov     rdi, 0
    mov     rax, 60
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Allocate memory with `mmap`, write a few numbers into it, and read them back. Try changing the size!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use syscall 9 for `mmap`, 11 for `munmap` (if you want to free it).")
    slow_print("→ Memory returned is like a giant byte array — pointer in `rax`.")
    slow_print("→ Sizes are often in multiples of 4096 (page size).\n")

    # Bonus
    slow_print(f"{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Store an array of integers in the block.")
    slow_print("→ Loop through the array and calculate the sum.")
    slow_print("→ Free the memory with `munmap`!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Woohoo! You just built your own malloc using `mmap` — low-level memory mastery unlocked! 💾🧠{RESET}")
