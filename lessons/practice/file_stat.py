# lessons/practice_programs/file_stat.py

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
    print(f"\n{BOLD}📂 Get File Metadata Using `stat`!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Use the `stat` syscall to read metadata (size, timestamps, permissions) from a file.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Allocate space in `.bss` for a `stat` structure (around 144 bytes).",
        "2️⃣  Set `rdi` to the filename pointer.",
        "3️⃣  Set `rsi` to the pointer to the structure buffer.",
        "4️⃣  Place syscall number 4 (for `stat`) in `rax`, and call `syscall`.",
        "5️⃣  Inspect the buffer: it holds file size, last modified time, and more!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of `stat` like asking the file system, “Hey, tell me all about this file!” 📋✨\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Use `stat` to Get File Size{RESET}")
    slow_print(f"""{DIM}
section .data
    filename db "test.txt", 0

section .bss
    statbuf resb 144             ; buffer for stat result

section .text
    global _start

_start:
    mov     rdi, filename        ; filename
    mov     rsi, statbuf         ; buffer to store stat result
    mov     rax, 4               ; syscall: stat
    syscall

    ; Let's get file size: it's at offset 48 (st_size)
    mov     rax, [statbuf + 48]  ; load file size into rax

    ; Convert and print the size (just a demo — printing is optional)

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Use `stat` to print the size of any file you choose. (Create `test.txt` first if needed!)\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ You can inspect other fields like permissions (offset 24) or modification time (offset 88).")
    slow_print("→ This uses the older `stat` syscall (number 4). You can also try `fstat` (5) or `newfstatat` (262).")
    slow_print("→ If the syscall fails, it returns -1 in `rax` — check for errors!")

    # Bonus
    slow_print(f"{BOLD}🌟 Bonus Challenge:{RESET}")
    slow_print("→ Try printing the modification time too (at offset 88).")
    slow_print("→ What happens if the file doesn’t exist? Detect that gracefully.")

    # Wrap-up
    print(f"\n{BOLD}🏁 Great job! Now you can peek under the hood of the file system like a true systems hacker. 🔍💾{RESET}")
