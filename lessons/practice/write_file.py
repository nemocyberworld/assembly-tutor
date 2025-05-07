# lessons/practice_programs/write_file.py

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
    print(f"\n{BOLD}📄 Write to a File Using Syscalls (No C Required!){RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to create and write to a file using Linux system calls in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use `sys_open` to create (or open) a file. It returns a file descriptor in `rax`.",
        "2️⃣  Use `sys_write` with that descriptor to write text into the file.",
        "3️⃣  Always close the file with `sys_close` when you're done.",
        "4️⃣  Use flags like `O_CREAT | O_WRONLY` and set correct permissions."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine opening a notebook (open), writing a message (write), and closing it (close). Simple I/O! 📒✍️\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Write 'Hello, File!' to output.txt{RESET}")
    slow_print(f"""{DIM}
section .data
    filename db "output.txt", 0
    message  db "Hello, File!", 0xA
    msg_len  equ $ - message

section .text
    global _start

_start:
    ; sys_open("output.txt", O_CREAT|O_WRONLY|O_TRUNC, 0644)
    mov     rax, 2          ; syscall: sys_open
    mov     rdi, filename   ; filename
    mov     rsi, 577        ; flags = O_CREAT | O_WRONLY | O_TRUNC
    mov     rdx, 0o644      ; permissions
    syscall

    mov     r12, rax        ; save file descriptor

    ; sys_write(fd, message, msg_len)
    mov     rax, 1          ; syscall: sys_write
    mov     rdi, r12        ; file descriptor
    mov     rsi, message    ; pointer to data
    mov     rdx, msg_len    ; number of bytes
    syscall

    ; sys_close(fd)
    mov     rax, 3
    mov     rdi, r12
    syscall

    ; exit(0)
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Write your own name to a file called `myname.txt` using system calls only!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ File descriptor is like a handle; store it carefully!")
    slow_print("→ Common flags: `O_CREAT` = 0x40, `O_WRONLY` = 0x1, `O_TRUNC` = 0x200 → combine them!")
    slow_print("→ File permission `0644` gives read/write to you, read to others.")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try appending instead of truncating with `O_APPEND`.")
    slow_print("→ Write two different messages to the same file!")
    slow_print("→ Print a message to stdout if the file write was successful.")

    # Wrap-up
    print(f"\n{BOLD}🏁 Done! You've just written to a file *directly* with the power of syscalls — like a system-level wizard! 🧙‍♂️💾{RESET}")
