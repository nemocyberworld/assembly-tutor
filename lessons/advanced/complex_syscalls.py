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
    print(f"\n{BOLD}🚀 Advanced Syscalls: mmap, execve, fork (Linux x86-64){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 We've seen simple syscalls like `write` and `exit`. Now let's explore powerful ones that manage memory, processes, and execution!{RESET}")
    time.sleep(1)

    # mmap
    slow_print(f"\n{BOLD}🔧 mmap - Memory Mapping{RESET}")
    slow_print(f"{CYAN}mmap maps memory pages into your address space. It's used for dynamic memory, file I/O, even executable code.{RESET}")
    time.sleep(0.5)

    slow_print(f"{GREEN}Signature:{RESET} void* mmap(void* addr, size_t length, int prot, int flags, int fd, off_t offset)")
    slow_print(f"{MAGENTA}Syscall number: 9{RESET}")

    slow_print(f"{CYAN}In assembly, set args in: rdi, rsi, rdx, r10, r8, r9 → then syscall.{RESET}")
    time.sleep(1)

    # Example
    slow_print(f"\n{BOLD}💡 Example: Allocate 4096 bytes RW memory with mmap{RESET}")
    slow_print(f"{CYAN}Assembly snippet:{RESET}")
    example = [
        "mov rax, 9              ; syscall: mmap",
        "xor rdi, rdi            ; NULL addr (let kernel choose)",
        "mov rsi, 4096           ; size = 4096 bytes",
        "mov rdx, 3              ; PROT_READ | PROT_WRITE",
        "mov r10, 0x22           ; MAP_ANONYMOUS | MAP_PRIVATE",
        "mov r8, -1              ; fd = -1",
        "xor r9, r9              ; offset = 0",
        "syscall"
    ]
    for line in example:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # execve
    slow_print(f"\n{BOLD}🚀 execve - Execute a Program{RESET}")
    slow_print(f"{CYAN}Replaces current process image with a new program. Used in shells, loaders, etc.{RESET}")
    slow_print(f"{MAGENTA}Syscall number: 59{RESET}")

    slow_print(f"{GREEN}Arguments (in registers):{RESET}")
    slow_print(f"  rdi = filename (pointer)")
    slow_print(f"  rsi = argv (pointer to array of pointers)")
    slow_print(f"  rdx = envp (pointer to env vars array)")

    # Example
    slow_print(f"\n{BOLD}💡 Example: execve('/bin/sh', ['/bin/sh'], NULL){RESET}")
    example = [
        "mov rax, 59             ; syscall: execve",
        "lea rdi, [rel filename] ; filename = '/bin/sh'",
        "lea rsi, [rel argv]     ; argv = ['/bin/sh', 0]",
        "xor rdx, rdx            ; envp = NULL",
        "syscall",
        "filename: db '/bin/sh',0",
        "argv: dq filename, 0"
    ]
    for line in example:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # fork
    slow_print(f"\n{BOLD}🌱 fork - Create a Child Process{RESET}")
    slow_print(f"{CYAN}Creates a copy of the current process. Returns 0 in child, child's PID in parent.{RESET}")
    slow_print(f"{MAGENTA}Syscall number: 57{RESET}")

    slow_print(f"\n{BOLD}💡 Example: Forking and checking return value{RESET}")
    example = [
        "mov rax, 57             ; syscall: fork",
        "syscall",
        "cmp rax, 0",
        "je in_child             ; jump if in child",
        "in_parent:",
        "  ; code for parent",
        "  jmp done",
        "in_child:",
        "  ; code for child",
        "done:"
    ]
    for line in example:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ `mmap` lets you request memory from the kernel (heap, buffers, code){RESET}")
    slow_print(f"{GREEN}✔ `execve` loads and runs a new program — no return!{RESET}")
    slow_print(f"{GREEN}✔ `fork` creates a new process, perfect for multitasking setups{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Write a program that forks and uses `execve` in the child!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to explore next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")