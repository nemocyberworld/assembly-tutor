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
    print(f"\n{BOLD}📍 Position-Independent Code (PIC) in Assembly (x86-64){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 PIC is code that can run correctly regardless of where it’s loaded in memory.{RESET}")
    slow_print(f"{CYAN}It’s crucial for shared libraries, shellcode, and secure systems (ASLR, PIE).{RESET}")
    time.sleep(1)

    # Why it's useful
    slow_print(f"\n{BOLD}💡 Why Use PIC?{RESET}")
    reasons = [
        "🔸 Required for .so (shared objects)",
        "🔸 Enables memory randomization (ASLR)",
        "🔸 Makes code more reusable and portable",
        "🔸 Essential for shellcode that injects into unknown locations"
    ]
    for r in reasons:
        slow_print(f"{GREEN}{r}{RESET}")
        time.sleep(0.4)

    # Core challenge
    slow_print(f"\n{MAGENTA}🔍 Challenge: Referencing memory without fixed addresses!{RESET}")
    slow_print(f"{CYAN}You can’t do this: `mov rsi, message` if `message` has no absolute address.{RESET}")
    time.sleep(1)

    # Technique
    slow_print(f"\n{BOLD}🔧 Solution: RIP-Relative Addressing{RESET}")
    slow_print(f"{CYAN}Modern x86-64 lets you reference data relative to the instruction pointer (RIP).{RESET}")
    slow_print(f"{MAGENTA}✅ This keeps your code relocatable and position-independent.{RESET}")
    time.sleep(1)

    slow_print(f"\n{GREEN}✅ Example:{RESET}")
    example = [
        "lea rsi, [rip + message]     ; get address of 'message' into rsi",
        "mov rdx, 6                   ; length of message",
        "mov rdi, 1                   ; stdout",
        "mov rax, 1                   ; syscall: write",
        "syscall",
        "mov rax, 60                  ; syscall: exit",
        "xor rdi, rdi                 ; status = 0",
        "syscall",
        "message: db 'Hello!', 10"
    ]
    for line in example:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Explanation
    slow_print(f"\n{BOLD}🧠 Why This Works:{RESET}")
    points = [
        "✔ RIP is the current instruction pointer.",
        "✔ `lea rsi, [rip+offset]` calculates the address relative to where the code is running.",
        "✔ This avoids hardcoding addresses — making the code position-independent."
    ]
    for p in points:
        slow_print(f"{CYAN}{p}{RESET}")
        time.sleep(0.4)

    # Summary
    slow_print(f"\n{YELLOW}🧾 Summary:{RESET}")
    summary = [
        "✔ PIC is essential for secure and flexible binaries.",
        "✔ Use RIP-relative addressing to access local data.",
        "✔ Avoid absolute addresses and fixed pointers."
    ]
    for s in summary:
        slow_print(f"{GREEN}{s}{RESET}")
        time.sleep(0.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Create a minimal shellcode that prints a message using RIP-relative data!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to try converting a fixed-address example into PIC?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")