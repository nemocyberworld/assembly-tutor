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
    print(f"\n{BOLD}🧠 Manual Function Resolution (Shellcode Style){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🔐 In minimalistic assembly (e.g. shellcode), you often can’t rely on linked symbols or standard libraries like libc.{RESET}")
    slow_print(f"{CYAN}You must manually resolve function addresses from memory or system structures!{RESET}")
    time.sleep(1)

    slow_print(f"\n{BOLD}💡 Why Manual Resolution?{RESET}")
    reasons = [
        "🔸 No symbol tables or relocations in shellcode",
        "🔸 Need for dynamic, position-independent code",
        "🔸 Avoiding detection by static scanners"
    ]
    for reason in reasons:
        slow_print(f"{GREEN}{reason}{RESET}")
        time.sleep(0.5)

    slow_print(f"\n{BOLD}🔎 Example Approach on Linux (x86-64):{RESET}")
    steps = [
        "1. Locate the base address of loaded libraries (like libc) via `/proc/self/maps`",
        "2. Parse ELF headers manually to find symbol offsets",
        "3. Compute function addresses using offsets from base",
        "4. Call the resolved function by address"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.5)

    # Simulated strategy
    slow_print(f"\n{BOLD}🔧 Simulated Strategy (Conceptual){RESET}")
    slow_print(f"{CYAN}Imagine we’ve found that `write` is located at offset +0x1110 in libc.{RESET}")
    slow_print(f"{CYAN}If libc is loaded at 0x7ffff7dce000, then `write` = 0x7ffff7dce000 + 0x1110{RESET}")
    time.sleep(1)

    slow_print(f"{GREEN}Assembly-style pseudo-code:{RESET}")
    pseudo = [
        "mov rax, 0x7ffff7dce000        ; base of libc",
        "add rax, 0x1110               ; offset of write",
        "call rax                      ; jump to write()"
    ]
    for line in pseudo:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{BOLD}⚙️ Advanced: Using syscalls without libc{RESET}")
    slow_print(f"{CYAN}Instead of resolving function addresses, shellcode often uses direct syscall numbers to avoid all dependencies.{RESET}")
    slow_print(f"{MAGENTA}For example: syscall 1 is `write`, syscall 60 is `exit`.{RESET}")

    slow_print(f"\n{GREEN}Minimal `write` syscall shellcode example:{RESET}")
    code = [
        "mov rax, 1              ; syscall: write",
        "mov rdi, 1              ; fd: stdout",
        "lea rsi, [rel msg]      ; pointer to message",
        "mov rdx, 12             ; length",
        "syscall",
        "mov rax, 60             ; syscall: exit",
        "xor rdi, rdi            ; exit code 0",
        "syscall",
        "msg: db 'Hi from asm', 10"
    ]
    for line in code:
        slow_print(f"{CYAN}{line}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{YELLOW}🧾 Summary:{RESET}")
    summary = [
        "✔ Manual resolution is key when no symbol tables exist",
        "✔ Use ELF headers and offsets to locate functions",
        "✔ Alternatively, rely on raw syscall numbers directly"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Write shellcode that uses syscall 1 (write) to print a string — no libc allowed!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to try a shellcode crafting challenge next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")