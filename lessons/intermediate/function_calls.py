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
    print(f"\n{BOLD}📞 Function Calls & the System V Calling Convention (x86-64){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 Functions in Assembly don’t magically handle arguments and returns — the CPU uses registers and the stack to manage this manually.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}The System V ABI is the standard calling convention used on Linux for x86-64.{RESET}")
    time.sleep(1)

    slow_print(f"{GREEN}Here’s how arguments and return values are handled:{RESET}")
    time.sleep(1)

    convention = [
        ("rdi", "1st argument"),
        ("rsi", "2nd argument"),
        ("rdx", "3rd argument"),
        ("rcx", "4th argument"),
        ("r8 ", "5th argument"),
        ("r9 ", "6th argument"),
        ("rax", "Return value"),
    ]
    for reg, role in convention:
        slow_print(f"  {BOLD}{reg:<4}{RESET} - {role}")
        time.sleep(0.7)

    print()
    slow_print(f"{MAGENTA}👉 Any arguments beyond the 6th go on the stack. The caller sets up the registers, calls the function, and expects the result in rax.{RESET}")
    time.sleep(1.5)

    # Example function call
    slow_print(f"\n{BOLD}💡 Example: Calling a function that adds two numbers{RESET}")
    slow_print(f"{CYAN}Let’s say we want to call: {BOLD}add_numbers(5, 7){RESET}{CYAN}. Here's how it looks in Assembly:{RESET}")

    asm_lines = [
        "mov rdi, 5     ; 1st argument",
        "mov rsi, 7     ; 2nd argument",
        "call add_numbers",
        "; result now in rax"
    ]
    for line in asm_lines:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.7)

    # Simulated function
    slow_print(f"\n{MAGENTA}🔧 Simulating the call...{RESET}")
    rdi = 5
    rsi = 7
    slow_print(f"  rdi = {rdi}, rsi = {rsi}")
    rax = rdi + rsi
    slow_print(f"  rax (return value) = {rax}")
    time.sleep(1)

    # Function prologue/epilogue
    slow_print(f"\n{BOLD}🧩 Inside the function: Prologue & Epilogue{RESET}")
    slow_print(f"{CYAN}A typical function saves the base pointer and sets up a new stack frame:{RESET}")
    prologue = [
        "push rbp",
        "mov rbp, rsp",
        "; function body...",
        "pop rbp",
        "ret"
    ]
    for line in prologue:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.6)

    print()
    slow_print(f"{YELLOW}📚 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Arguments go in specific registers (rdi, rsi, ...){RESET}")
    slow_print(f"{GREEN}✔ Return value comes back in rax{RESET}")
    slow_print(f"{GREEN}✔ Prologue/epilogue sets up and tears down stack frames{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{CYAN}{BOLD}🧪 In the next lesson, we’ll dive into the stack in more detail and see how recursion and local variables work!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")