# lessons/practice_programs/pipe_communication.py

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
    print(f"\n{BOLD}🔄 Pipe Communication Between Parent & Child!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Use a pipe to send a message from a parent process to a child process using syscalls.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Create a pipe with the `pipe` syscall — it gives you two file descriptors.",
        "2️⃣  `fork` the process. You'll now have a parent and a child.",
        "3️⃣  Parent writes to the pipe, child reads from it.",
        "4️⃣  Print the message in the child process!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} A pipe is like a paper tube 🧻 between two rooms — one person whispers in one end, the other listens on the other side!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Send Message from Parent to Child via Pipe{RESET}")
    slow_print(f"""{DIM}
section .data
    msg     db "Hello from parent!", 0xA
    msglen  equ $ - msg

section .bss
    pipefd  resd 2              ; pipefd[0] = read end, pipefd[1] = write end
    buffer  resb 64

section .text
    global _start

_start:
    ; Create pipe
    mov     rax, 22             ; syscall: pipe
    mov     rdi, pipefd         ; pointer to pipefd[2]
    syscall

    ; Fork the process
    mov     rax, 57             ; syscall: fork
    syscall

    test    rax, rax
    jnz     .parent             ; rax > 0 means parent

.child:
    ; Child closes write end
    mov     rax, 3
    mov     rdi, [pipefd + 4]
    syscall

    ; Read from pipe
    mov     rax, 0              ; syscall: read
    mov     rdi, [pipefd]       ; read end
    mov     rsi, buffer
    mov     rdx, 64
    syscall

    ; Write to stdout
    mov     rax, 1
    mov     rdi, 1
    mov     rsi, buffer
    mov     rdx, rax            ; use number of bytes read
    syscall

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall

.parent:
    ; Parent closes read end
    mov     rax, 3
    mov     rdi, [pipefd]
    syscall

    ; Write to pipe
    mov     rax, 1
    mov     rdi, [pipefd + 4]   ; write end
    mov     rsi, msg
    mov     rdx, msglen
    syscall

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Use a pipe to send your own message from a parent to a child and print it out from the child process!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ `pipe` gives you two file descriptors: read and write.")
    slow_print("→ `fork` duplicates the current process — both parent and child run the same code!")
    slow_print("→ Always close unused ends of the pipe to avoid leaks or deadlocks.")

    # Bonus
    slow_print(f"{BOLD}🌟 Bonus Challenge:{RESET}")
    slow_print("→ Try sending a longer message or multiple messages.")
    slow_print("→ What happens if you forget to close the write end in the child?")
    slow_print("→ Can you reverse it — make the child send to the parent instead?")

    # Wrap-up
    print(f"\n{BOLD}🏁 Boom! You just built your first inter-process chat with a pipe! This is the start of real-world OS-level programming. 🚇✨{RESET}")
