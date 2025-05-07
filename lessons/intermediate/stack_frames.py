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
    print(f"\n{BOLD}📚 Stack Frames & Function Structure in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧱 Every time a function is called in Assembly, the CPU sets up a *stack frame* — a small section of memory for that function’s use.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}This frame helps store return addresses, saved registers, and local variables.{RESET}")
    time.sleep(1)

    slow_print(f"{GREEN}At the heart of this setup are two key operations: the {BOLD}prologue{RESET}{GREEN} and the {BOLD}epilogue{RESET}.{RESET}")
    time.sleep(1)

    # Prologue breakdown
    slow_print(f"\n{BOLD}🪜 Prologue — Sets up the stack frame{RESET}")
    prologue = [
        "push rbp        ; Save old base pointer",
        "mov rbp, rsp    ; Set new base pointer",
        "sub rsp, 16     ; Reserve 16 bytes for local variables"
    ]
    for line in prologue:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.7)

    slow_print(f"{MAGENTA}👆 This saves the previous frame pointer and gives you a stable base to access local variables and parameters.{RESET}")
    time.sleep(1)

    # Simulate stack frame
    slow_print(f"\n{CYAN}🔧 Simulating a stack frame...{RESET}")
    rbp = 1000  # Pretend base pointer
    rsp = rbp   # Initially the same
    slow_print(f"  Initial rbp = {rbp}")
    slow_print(f"  Initial rsp = {rsp}")
    rsp -= 16
    slow_print(f"  After 'sub rsp, 16' → rsp = {rsp} (space for local vars)")
    time.sleep(1)

    # Accessing local variable
    slow_print(f"\n{BOLD}📦 Accessing a local variable{RESET}")
    slow_print(f"{CYAN}Say we store a local int at [rbp - 4]. That means: 4 bytes below the base pointer.{RESET}")
    memory = {}
    memory[rbp - 4] = 123
    slow_print(f"  memory[rbp - 4] = {memory[rbp - 4]}")
    time.sleep(1)

    # Epilogue breakdown
    slow_print(f"\n{BOLD}🧼 Epilogue — Cleans up the stack frame{RESET}")
    epilogue = [
        "mov rsp, rbp    ; Restore stack pointer",
        "pop rbp         ; Restore previous base pointer",
        "ret             ; Return to caller"
    ]
    for line in epilogue:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.7)

    slow_print(f"{MAGENTA}👋 This puts everything back the way it was before the function was called.{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Prologue sets up a stable frame to use local memory safely.{RESET}")
    slow_print(f"{GREEN}✔ Epilogue restores the caller's environment before returning.{RESET}")
    slow_print(f"{GREEN}✔ The base pointer (rbp) makes accessing locals and parameters predictable.{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 In the next lesson, we’ll build a function that uses local variables and practices stack-based memory access step by step!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")