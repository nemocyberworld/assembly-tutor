# lessons/practice_programs/read_input.py

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
    print(f"\n{BOLD}🎤 Read User Input with Syscalls in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Use `sys_read` to read input from the keyboard (stdin) and store it in memory.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Reserve memory space in the `.bss` section to hold the input.",
        "2️⃣  Use `sys_read` (syscall number 0) to read from `stdin` (file descriptor 0).",
        "3️⃣  Store the result in a buffer and (optionally) print it back using `sys_write`.",
        "4️⃣  Exit cleanly using `sys_exit`."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine a mailbox 📬. You open it (`read`), grab the letter (your input), and put it in a safe place (buffer).\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Read input and echo it back{RESET}")
    slow_print(f"""{DIM}
section .bss
    buffer  resb 100      ; reserve 100 bytes for user input

section .text
    global _start

_start:
    ; sys_read(stdin, buffer, 100)
    mov     rax, 0        ; syscall: sys_read
    mov     rdi, 0        ; file descriptor 0 = stdin
    mov     rsi, buffer   ; where to store input
    mov     rdx, 100      ; max number of bytes to read
    syscall

    ; rax now contains the number of bytes read
    mov     rdx, rax      ; save length for writing

    ; sys_write(stdout, buffer, rdx)
    mov     rax, 1        ; syscall: sys_write
    mov     rdi, 1        ; file descriptor 1 = stdout
    mov     rsi, buffer   ; pointer to the data
    syscall

    ; exit(0)
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Prompt the user to type something, store it in memory, and echo it back to the screen!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Standard file descriptors: 0 = stdin, 1 = stdout, 2 = stderr.")
    slow_print("→ You can write a prompt first using `sys_write` before reading.")
    slow_print("→ Be careful with buffer size — never read more than you allocate!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Count how many characters the user typed (it's in `rax` after `sys_read`).")
    slow_print("→ Add newline handling (optional): strip or check for 0xA.")
    slow_print("→ Use `sys_write` multiple times to build your own simple CLI!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome! You've just created interactive assembly code — your program *talks* to people now! 🧑‍💻🎉{RESET}")
