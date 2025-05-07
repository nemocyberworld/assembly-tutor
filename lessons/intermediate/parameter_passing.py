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
    print(f"\n{BOLD}📨 Passing Arguments via Registers (System V ABI){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}💡 In x86-64 Assembly (Linux), the first six arguments to a function are passed in registers — not on the stack.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}This is defined by the {BOLD}System V AMD64 ABI{RESET}{CYAN} — the standard calling convention on Linux.{RESET}")
    time.sleep(1)

    # Argument register order
    slow_print(f"\n{BOLD}📌 Argument Registers Order:{RESET}")
    args = [
        ("rdi", "1st argument"),
        ("rsi", "2nd argument"),
        ("rdx", "3rd argument"),
        ("rcx", "4th argument"),
        ("r8",  "5th argument"),
        ("r9",  "6th argument"),
    ]
    for reg, desc in args:
        slow_print(f"  {BOLD}{reg:<4}{RESET} - {desc}")
        time.sleep(0.5)

    slow_print(f"{MAGENTA}Any additional arguments go on the stack after that (rare in assembly).{RESET}")
    time.sleep(1)

    # Example
    slow_print(f"\n{BOLD}💡 Example: Calling a function with three arguments{RESET}")
    example = [
        "mov rdi, 5          ; arg1 → rdi",
        "mov rsi, 10         ; arg2 → rsi",
        "mov rdx, 15         ; arg3 → rdx",
        "call my_function"
    ]
    for line in example:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.6)

    # Simulate call
    slow_print(f"\n{CYAN}🔧 Simulating the call...{RESET}")
    args_values = {
        "rdi": 5,
        "rsi": 10,
        "rdx": 15
    }
    for reg, val in args_values.items():
        slow_print(f"  {BOLD}{reg}{RESET} = {val}")
        time.sleep(0.5)

    # Function receives the values
    slow_print(f"{MAGENTA}Inside the function, these values are immediately available in the registers!{RESET}")
    time.sleep(1)

    # Return value
    slow_print(f"\n{BOLD}🔙 Return values go in rax{RESET}")
    slow_print(f"{CYAN}A typical function returns a single value using {BOLD}rax{RESET}{CYAN}.{RESET}")
    time.sleep(1)
    slow_print(f"{GREEN}Example: mov rax, rdi  ; return value in rax{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ First 6 arguments go in: rdi, rsi, rdx, rcx, r8, r9{RESET}")
    slow_print(f"{GREEN}✔ Use mov to assign values before calling the function{RESET}")
    slow_print(f"{GREEN}✔ Return values are placed in rax by the callee{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Up next: We'll define a function that takes two arguments, adds them, and returns the result!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")