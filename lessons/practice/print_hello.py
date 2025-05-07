import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🖨️ 'Hello, World!' in x86-64 Assembly (Linux){RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}📢 The 'Hello, World!' program is a rite of passage in every language — even Assembly!{RESET}")
    slow_print(f"{CYAN}On Linux, we’ll use the `write` syscall to print to standard output (stdout).{RESET}")
    time.sleep(1)

    # Setup
    slow_print(f"\n{BOLD}🧰 System Call Info:{RESET}")
    syscall_info = [
        "✔ Syscall number for write: 1",
        "✔ File descriptor for stdout: 1",
        "✔ Arguments (in order):",
        "   → rdi: file descriptor",
        "   → rsi: pointer to buffer",
        "   → rdx: number of bytes to write"
    ]
    for item in syscall_info:
        slow_print(f"{MAGENTA}{item}{RESET}")
        time.sleep(0.4)

    # Code
    slow_print(f"\n{BOLD}💡 Program (NASM syntax):{RESET}")
    slow_print(f"""{GREEN}section .data{RESET}
    msg db "Hello, World!", 0xA
    len equ $ - msg

{GREEN}section .text{RESET}
    global _start

_start:
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; file descriptor: stdout
    mov rsi, msg        ; pointer to message
    mov rdx, len        ; message length
    syscall

    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; exit code 0
    syscall
""")
    time.sleep(1)

    # Breakdown
    slow_print(f"\n{BOLD}🔍 Breakdown:{RESET}")
    points = [
        "✔ `msg db ...` defines a string with a newline",
        "✔ `len` calculates the size of the string",
        "✔ Registers set up syscall arguments in order: rdi, rsi, rdx",
        "✔ `syscall` triggers the Linux kernel",
        "✔ Program ends with syscall 60 (exit)"
    ]
    for p in points:
        slow_print(f"{CYAN}{p}{RESET}")
        time.sleep(0.4)

    # Build
    slow_print(f"\n{BOLD}⚙️ Build and Run:{RESET}")
    slow_print(f"{MAGENTA}1. Save as `hello.asm`")
    slow_print(f"2. Assemble: nasm -f elf64 hello.asm -o hello.o")
    slow_print(f"3. Link: ld hello.o -o hello")
    slow_print(f"4. Run: ./hello{RESET}")
    time.sleep(1)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Modify the message to print your own name!{RESET}")
    slow_print(f"{MAGENTA}Bonus: Try writing to stderr (fd = 2) instead of stdout!{RESET}")
    time.sleep(1)

    # Wrap-up
    print(f"\n{BOLD}📚 Lesson complete! Next, want to try reading input with `read` or using `.bss` for dynamic space?{RESET}")
