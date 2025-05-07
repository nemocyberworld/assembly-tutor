# lessons/practice_programs/mmap_anon.py

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
    print(f"\n{BOLD}📦 Allocate Memory Dynamically with `mmap`!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to use the `mmap` syscall to allocate anonymous memory at runtime.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Prepare arguments for the `mmap` syscall (number 9).",
        "2️⃣  Set size, protection, flags, and other parameters.",
        "3️⃣  Call `mmap`, and it returns a memory address in `rax`.",
        "4️⃣  Use that memory — for strings, arrays, anything!",
        "5️⃣  Use `munmap` later if you want to free it."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine asking the OS for a block of empty land (memory), and the OS says: 'Sure, here’s your plot at 0x1234!' 🌱\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Allocate 4096 Bytes of RW Memory{RESET}")
    slow_print(f"""{DIM}
section .text
    global _start

_start:
    xor     rdi, rdi              ; addr = 0 (let kernel choose)
    mov     rsi, 4096             ; length = 4096 bytes
    mov     rdx, 3                ; PROT_READ | PROT_WRITE
    mov     r10, 0x22             ; MAP_PRIVATE | MAP_ANONYMOUS
    mov     r8, -1                ; fd = -1 (anonymous)
    xor     r9, r9                ; offset = 0
    mov     rax, 9                ; syscall: mmap
    syscall

    ; rax now has a pointer to 4096 bytes of fresh memory 🎉

    ; Optional: write something into memory
    mov     byte [rax], 'H'
    mov     byte [rax+1], 'i'
    mov     byte [rax+2], 10      ; newline

    ; write(1, rax, 3)
    mov     rdi, 1
    mov     rsi, rax
    mov     rdx, 3
    mov     rax, 1
    syscall

    ; exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Allocate 8192 bytes of memory using `mmap`, store a short string, and print it out using `write`!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use protection flags: 1 = PROT_READ, 2 = PROT_WRITE, 3 = both.")
    slow_print("→ Use flags: 0x20 = MAP_ANONYMOUS, 0x02 = MAP_PRIVATE.")
    slow_print("→ File descriptor must be -1 for anonymous mapping.")

    # Bonus
    slow_print(f"{BOLD}🌟 Bonus Challenge:{RESET}")
    slow_print("→ Try using `munmap` (syscall 11) to free the memory.")
    slow_print("→ Write a small allocator that carves out memory chunks from your mmap’d block!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Fantastic! Now you’re allocating memory on your own, just like malloc — but cooler. 🔧🧠{RESET}")
