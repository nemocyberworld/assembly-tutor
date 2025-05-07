import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🧩 Linking Object Files Together in Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🛠 In real-world programs, code is split into multiple files for modularity. These are assembled separately into object files, then linked together.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}Each file can define functions, variables, or data. Linking combines them into a single executable binary.{RESET}")
    time.sleep(1)

    # Overview
    slow_print(f"\n{BOLD}🔗 Linking Overview:{RESET}")
    steps = [
        "1. Assemble each .asm/.s file into a .o object file",
        "2. Use a linker (like `ld` or `gcc`) to combine them",
        "3. Resolve all symbols (labels, function names, globals)",
    ]
    for step in steps:
        slow_print(f"{GREEN}{step}{RESET}")
        time.sleep(0.5)

    # Example layout
    slow_print(f"\n{BOLD}📁 Example: Two-File Program{RESET}")
    slow_print(f"{MAGENTA}file1.asm defines a function. file2.asm calls it.{RESET}")
    time.sleep(1)

    slow_print(f"\n{GREEN}file1.asm:{RESET}")
    code1 = [
        "global print_hello",
        "section .text",
        "print_hello:",
        "    mov rax, 1          ; write syscall",
        "    mov rdi, 1          ; stdout",
        "    mov rsi, msg        ; message pointer",
        "    mov rdx, len        ; length",
        "    syscall",
        "    ret",
        "section .data",
        "msg db 'Hello!', 10",
        "len equ $ - msg"
    ]
    for line in code1:
        slow_print(f"  {CYAN}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{GREEN}file2.asm:{RESET}")
    code2 = [
        "extern print_hello",
        "global _start",
        "section .text",
        "_start:",
        "    call print_hello",
        "    mov rax, 60",
        "    xor rdi, rdi",
        "    syscall"
    ]
    for line in code2:
        slow_print(f"  {CYAN}{line}{RESET}")
        time.sleep(0.3)

    # How to assemble/link
    slow_print(f"\n{BOLD}🧰 How to Assemble and Link:{RESET}")
    commands = [
        "nasm -f elf64 file1.asm -o file1.o",
        "nasm -f elf64 file2.asm -o file2.o",
        "ld file1.o file2.o -o hello"
    ]
    for cmd in commands:
        slow_print(f"{GREEN}$ {cmd}{RESET}")
        time.sleep(0.5)

    slow_print(f"\n{MAGENTA}✔ The linker resolves 'print_hello' across files — because one declares it global, and the other declares it extern.{RESET}")
    time.sleep(1)

    # Common errors
    slow_print(f"\n{BOLD}⚠️ Common Linking Issues:{RESET}")
    errors = [
        "❌ Undefined reference – forgot to declare extern or global",
        "❌ Duplicate symbols – same label in multiple files",
        "❌ Wrong calling conventions – mismatched stack/register use"
    ]
    for issue in errors:
        slow_print(f"{RED}{issue}{RESET}")
        time.sleep(0.5)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ You can build large programs from multiple object files{RESET}")
    slow_print(f"{GREEN}✔ Use 'global' to export symbols, 'extern' to import them{RESET}")
    slow_print(f"{GREEN}✔ Use a linker to combine object files into one executable{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Break a program into two files and try linking them!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")