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
    print(f"\n{BOLD}🕵️ Hunting Syscalls Without libc (x86-64 Linux){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧼 Normally, C programs use libc to abstract away syscalls like `write()`, `read()`, and `exit()`...{RESET}")
    slow_print(f"{CYAN}But in raw assembly — or in shellcode — you don’t get libc. You must make syscalls *manually*.{RESET}")
    time.sleep(1)

    # What is a syscall?
    slow_print(f"\n{BOLD}💡 What's a syscall?{RESET}")
    slow_print(f"{GREEN}It's the lowest-level way to ask the Linux kernel to do something for you: read a file, allocate memory, kill a process...{RESET}")
    slow_print(f"{CYAN}They’re identified by a syscall number and parameters passed in registers.{RESET}")
    time.sleep(1)

    # Syscall structure
    slow_print(f"\n{BOLD}🔢 Syscall Structure (System V ABI, x86-64):{RESET}")
    regs = [
        "• rax = syscall number",
        "• rdi = first arg",
        "• rsi = second arg",
        "• rdx = third arg",
        "• r10 = fourth arg",
        "• r8  = fifth arg",
        "• r9  = sixth arg"
    ]
    for reg in regs:
        slow_print(f"{MAGENTA}{reg}{RESET}")
        time.sleep(0.3)

    # Example
    slow_print(f"\n{BOLD}🧪 Example: write(1, msg, len){RESET}")
    code = [
        "mov rax, 1          ; syscall number for write",
        "mov rdi, 1          ; fd = stdout",
        "mov rsi, msg        ; pointer to string",
        "mov rdx, 13         ; length",
        "syscall"
    ]
    for line in code:
        slow_print(f"{CYAN}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{GREEN}This prints a message directly using the kernel — no libc!{RESET}")
    time.sleep(1)

    # Where to find syscall numbers
    slow_print(f"\n{BOLD}🔍 Where Do You Get Syscall Numbers?{RESET}")
    methods = [
        "📄 Linux kernel source (`unistd_64.h`)",
        "🧪 Trial and error in a debugger (e.g., gdb)",
        "🧬 Disassembling known binaries (strace, objdump)",
        "📚 Online references (e.g., syscall tables)"
    ]
    for m in methods:
        slow_print(f"{GREEN}{m}{RESET}")
        time.sleep(0.4)

    # Tip
    slow_print(f"\n{YELLOW}💡 Tip: Use `strace` to trace a real binary and see what syscalls it invokes!{RESET}")
    slow_print(f"{CYAN}$ strace ./your_program{RESET}")
    time.sleep(1)

    # Hunting unknown syscalls
    slow_print(f"\n{BOLD}🧬 Hunting Unknown Syscalls:{RESET}")
    techniques = [
        "• Use known syscall numbers and bruteforce around them",
        "• Build tiny programs with one syscall, disassemble and read the rax value",
        "• Use `gdb` to break on `syscall` and inspect registers",
        "• Log the syscall with `strace` or audit tools"
    ]
    for t in techniques:
        slow_print(f"{MAGENTA}{t}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{YELLOW}📌 Summary:{RESET}")
    summary = [
        "✔ You can invoke Linux syscalls directly in assembly",
        "✔ Syscalls bypass libc — useful for shellcode, exploits, and minimal binaries",
        "✔ Find syscall numbers in kernel headers or online",
        "✔ Tools: gdb, strace, objdump, syscall tables"
    ]
    for s in summary:
        slow_print(f"{GREEN}{s}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Try writing a syscall-only program that uses `open`, `read`, and `write` to print a file — with no libc or startup code!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to disassemble some real-world binaries to see what syscalls they make?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")