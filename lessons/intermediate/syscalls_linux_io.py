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
    print(f"\n{BOLD}📣 Syscalls & Basic Linux I/O in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧩 In Assembly, we talk to the operating system directly using *system calls* — low-level functions exposed by Linux.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}We do this by placing values in specific registers and triggering the {BOLD}syscall{RESET}{CYAN} instruction.{RESET}")
    time.sleep(1)

    # Syscall overview
    slow_print(f"\n{BOLD}💡 Linux Syscall Convention (x86-64){RESET}")
    convention = [
        ("rax", "Syscall number"),
        ("rdi", "1st argument"),
        ("rsi", "2nd argument"),
        ("rdx", "3rd argument"),
        ("r10", "4th argument"),
        ("r8",  "5th argument"),
        ("r9",  "6th argument"),
    ]
    for reg, use in convention:
        slow_print(f"  {BOLD}{reg:<4}{RESET} - {use}")
        time.sleep(0.6)

    slow_print(f"{MAGENTA}🔢 The syscall number tells Linux what to do — like write to a file or read input.{RESET}")
    time.sleep(1)

    # Example: write to stdout
    slow_print(f"\n{BOLD}📤 Example: Write to stdout (syscall #1){RESET}")
    example = [
        "mov rax, 1          ; syscall: write",
        "mov rdi, 1          ; file descriptor: stdout",
        "mov rsi, message    ; pointer to buffer",
        "mov rdx, 13         ; length of message",
        "syscall"
    ]
    for line in example:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.6)

    slow_print(f"{CYAN}This writes 13 bytes from `message` to the screen!{RESET}")
    time.sleep(1)

    # Simulate behavior
    slow_print(f"\n{MAGENTA}🔧 Simulating the output...{RESET}")
    message = "Hello, world!"
    slow_print(f"  {BOLD}stdout ←{RESET} {message}")
    time.sleep(1)

    # Example: exit syscall
    slow_print(f"\n{BOLD}🛑 Example: Exit cleanly (syscall #60){RESET}")
    exit_code = [
        "mov rax, 60         ; syscall: exit",
        "mov rdi, 0          ; exit code",
        "syscall"
    ]
    for line in exit_code:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.6)

    slow_print(f"{CYAN}Always end your program with an exit syscall — no return = crash! 🧨{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Use syscall numbers to request OS services (e.g., write = 1, exit = 60){RESET}")
    slow_print(f"{GREEN}✔ Arguments go into registers (rdi, rsi, rdx, etc.) based on position{RESET}")
    slow_print(f"{GREEN}✔ Use syscall to perform I/O, file ops, memory allocation, and more{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Up next: We’ll write a full program in assembly that prints a string and exits cleanly using only syscalls!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")