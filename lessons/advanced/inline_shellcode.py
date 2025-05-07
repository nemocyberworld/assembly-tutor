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
    print(f"\n{BOLD}💣 Inline Shellcode in Assembly (x86-64){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧬 Shellcode is raw binary machine code that gets injected into memory and executed directly.{RESET}")
    slow_print(f"{CYAN}It’s used in exploits, reverse engineering, and very low-level programming.{RESET}")
    time.sleep(1)

    # Inline?
    slow_print(f"\n{BOLD}🔧 What does 'inline' mean here?{RESET}")
    slow_print(f"{GREEN}It means embedding machine instructions directly in memory as byte values — not relying on the OS loader or ELF headers.{RESET}")
    time.sleep(1)

    # Structure
    slow_print(f"\n{BOLD}🏗️ Shellcode Structure:{RESET}")
    structure = [
        "✔ Position-independent (no absolute addresses)",
        "✔ No null bytes (\\x00) — often bad for injection",
        "✔ Tiny — every byte counts",
        "✔ Self-contained — no external dependencies"
    ]
    for line in structure:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.4)

    # Minimal shellcode
    slow_print(f"\n{BOLD}💡 Example: Minimal Exit Shellcode (Linux, x86-64){RESET}")
    code = [
        "global _start",
        "section .text",
        "_start:",
        "  mov rax, 60         ; syscall: exit",
        "  xor rdi, rdi        ; exit code 0",
        "  syscall"
    ]
    for line in code:
        slow_print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"{CYAN}Assembled, this becomes a short string of bytes. Example:{RESET}")
    slow_print(f"{GREEN}\\xb8\\x3c\\x00\\x00\\x00\\x48\\x31\\xff\\x0f\\x05{RESET}")
    time.sleep(1)

    # Usage
    slow_print(f"\n{BOLD}🧪 How to use inline shellcode?{RESET}")
    steps = [
        "1️⃣ Write the machine code as a byte array in C or Python",
        "2️⃣ Mark the memory as executable (e.g., using `mmap` or `VirtualAlloc`)",
        "3️⃣ Cast to a function pointer and call it"
    ]
    for step in steps:
        slow_print(f"{CYAN}{step}{RESET}")
        time.sleep(0.5)

    # C example
    slow_print(f"\n{BOLD}🛠️ Example in C (x86-64 Linux){RESET}")
    c_example = [
        "unsigned char code[] = \"\\xb8\\x3c\\x00\\x00\\x00\\x48\\x31\\xff\\x0f\\x05\";",
        "int (*func)() = (int(*)())code;",
        "func();"
    ]
    for line in c_example:
        slow_print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)

    # Safety
    slow_print(f"\n{RED}⚠️ WARNING: Executing raw shellcode is dangerous and can crash or compromise systems. Only do this in isolated environments (VMs, sandboxes).{RESET}")
    time.sleep(1)

    # Summary
    slow_print(f"\n{YELLOW}📌 Summary:{RESET}")
    summary = [
        "✔ Shellcode = raw executable bytecode",
        "✔ Inline = embedded directly in code or memory",
        "✔ Must be position-independent and compact",
        "✔ Often used in security research, exploit dev, CTFs"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.4)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write shellcode that calls write(1, msg, len) to print 'Hello' to stdout!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to disassemble shellcode or write it from hex?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")