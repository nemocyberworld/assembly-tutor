# lessons/practice_programs/dup_stdout.py

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
    print(f"\n{BOLD}📢 Duplicate stdout with `dup` and Write with It!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to duplicate the standard output (stdout) file descriptor using `dup` and use it to print text!\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use the `dup` syscall to create a copy of stdout (fd = 1).",
        "2️⃣  Use the new file descriptor to write text to the terminal.",
        "3️⃣  Close the new descriptor when done. Clean code is happy code!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} It's like cloning your megaphone 📣 — you can shout into either one and be heard just the same!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Duplicate stdout and use new fd to write{RESET}")
    slow_print(f"""{DIM}
section .data
    message db "Hello from duplicated stdout!", 0xA
    msg_len equ $ - message

section .text
    global _start

_start:
    ; syscall: dup(stdout)
    mov     rax, 32         ; syscall number for dup
    mov     rdi, 1          ; stdout file descriptor
    syscall
    mov     r12, rax        ; store new file descriptor

    ; syscall: write(new_fd, message, msg_len)
    mov     rax, 1          ; syscall: write
    mov     rdi, r12        ; duplicated stdout
    mov     rsi, message
    mov     rdx, msg_len
    syscall

    ; syscall: close(new_fd)
    mov     rax, 3
    mov     rdi, r12
    syscall

    ; syscall: exit(0)
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Duplicate stdout using `dup`, then write a custom message using the new file descriptor!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ File descriptors are just numbers: 0 = stdin, 1 = stdout, 2 = stderr.")
    slow_print("→ `dup` returns the next available file descriptor number.")
    slow_print("→ Always close file descriptors you no longer need!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try duplicating stdin or stderr instead of stdout.")
    slow_print("→ Duplicate multiple times and print using each fd.")
    slow_print("→ Redirect output of one fd to a file (advanced!).")

    # Wrap-up
    print(f"\n{BOLD}🏁 Boom! You just made a copy of stdout and used it like a low-level pro. 🧠🔁🎉{RESET}")
