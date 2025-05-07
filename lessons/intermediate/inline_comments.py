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
    print(f"\n{BOLD}💬 Improving Code Clarity with Inline Comments in Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}📌 Assembly code is low-level and compact — so comments are essential for making sense of what’s going on.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}Good comments explain the purpose of an instruction or group of instructions — not just what they do.{RESET}")
    time.sleep(1)

    # When to comment
    slow_print(f"\n{BOLD}💡 When to Use Inline Comments:{RESET}")
    tips = [
        "✔ Before or after complex logic (loops, pointer math, syscalls)",
        "✔ For non-obvious register usage",
        "✔ For function entry/exit or stack setup",
        "✔ To label constants, addresses, or flags"
    ]
    for tip in tips:
        slow_print(f"{GREEN}{tip}{RESET}")
        time.sleep(0.5)

    # Bad vs good
    slow_print(f"\n{BOLD}❌ Poor Comment Example:{RESET}")
    slow_print(f"  {RED}mov rax, 1       ; move 1 into rax{RESET}")
    slow_print(f"{MAGENTA}This just repeats the instruction! Not helpful.{RESET}")
    time.sleep(1)

    slow_print(f"\n{BOLD}✅ Better Comment Example:{RESET}")
    slow_print(f"  {GREEN}mov rax, 1       ; syscall number for write(){RESET}")
    slow_print(f"{MAGENTA}This tells the reader *why* this is being done.{RESET}")
    time.sleep(1)

    # Annotated sample
    slow_print(f"\n{BOLD}📝 Annotated Example: Writing 'Hi' to stdout{RESET}")
    code = [
        "section .data",
        "    msg db 'Hi', 10     ; our message with newline",
        "    len equ $ - msg     ; length of message",
        "",
        "section .text",
        "    global _start",
        "",
        "_start:",
        "    mov rax, 1          ; syscall: write",
        "    mov rdi, 1          ; file descriptor: stdout",
        "    mov rsi, msg        ; pointer to message",
        "    mov rdx, len        ; message length",
        "    syscall             ; invoke kernel",
        "",
        "    mov rax, 60         ; syscall: exit",
        "    xor rdi, rdi        ; exit code 0",
        "    syscall"
    ]
    for line in code:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.4)

    # Best practices
    slow_print(f"\n{CYAN}💡 Commenting Tips:{RESET}")
    tips2 = [
        "🧠 Don’t state the obvious — focus on *why*, not just *what*",
        "🧩 Use consistent formatting (indent or align them)",
        "📦 Group related code with a comment heading",
        "🧼 Keep them up to date when changing code!"
    ]
    for tip in tips2:
        slow_print(f"{GREEN}{tip}{RESET}")
        time.sleep(0.5)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Inline comments are vital for understanding Assembly{RESET}")
    slow_print(f"{GREEN}✔ Focus on explaining purpose, not repeating instructions{RESET}")
    slow_print(f"{GREEN}✔ Keep comments meaningful, short, and aligned for clarity{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Try rewriting one of your recent snippets with better comments — your future self will thank you!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")