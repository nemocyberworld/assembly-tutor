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
    print(f"\n{BOLD}🧩 Inline Assembly in C (GCC Style){RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}🛠️ Inline assembly lets you mix C and raw assembly instructions for performance or low-level control.{RESET}")
    slow_print(f"{CYAN}GCC provides the `asm` or `__asm__` keyword to embed assembly code directly into C programs.{RESET}")
    time.sleep(1)

    # Syntax
    slow_print(f"\n{BOLD}📚 Basic Syntax:{RESET}")
    slow_print(f"""{MAGENTA}
__asm__ ("assembly code");

Or with constraints:
__asm__ (
    "movl %1, %%eax;\\n"
    "addl %%eax, %0;"
    : "=r" (result)
    : "r" (input)
    : "%eax"
);
{RESET}""")
    time.sleep(1)

    # Simple Example
    slow_print(f"\n{BOLD}💡 Example: Add two integers in assembly (C + asm){RESET}")
    slow_print(f"{GREEN}C Code:{RESET}")
    slow_print(f"""{MAGENTA}
int a = 5, b = 3, result;
__asm__ (
    "movl %[x], %%eax;"
    "addl %[y], %%eax;"
    "movl %%eax, %[out];"
    : [out] "=r" (result)
    : [x] "r" (a), [y] "r" (b)
    : "%eax"
);
{RESET}""")
    time.sleep(1)

    # Breakdown
    slow_print(f"\n{BOLD}🔍 What's going on here?{RESET}")
    breakdown = [
        "✔ Inline asm uses AT&T syntax by default on GCC",
        "✔ %[x] and %[y] are named input operands",
        "✔ %%eax is the EAX register — double % due to C escaping",
        "✔ '=r' is an output constraint: any general-purpose register",
        "✔ The third section is a clobber list (registers you modify)"
    ]
    for item in breakdown:
        slow_print(f"{CYAN}{item}{RESET}")
        time.sleep(0.4)

    # Warnings
    slow_print(f"\n{BOLD}⚠️ Gotchas and Tips:{RESET}")
    warnings = [
        "✘ GCC's inline asm is tricky and error-prone — be precise!",
        "✘ Don't forget clobber lists or GCC may optimize around your code",
        "✔ Use extended syntax for anything non-trivial (inputs/outputs)",
        "✔ Prefer using `volatile` for instructions that have side effects"
    ]
    for w in warnings:
        slow_print(f"{RED if '✘' in w else GREEN}{w}{RESET}")
        time.sleep(0.3)

    # Advanced Tip
    slow_print(f"\n{BOLD}💡 Advanced Tip: Volatile Inline ASM{RESET}")
    slow_print(f"{CYAN}Use `asm volatile` to prevent the compiler from optimizing your inline instructions away.{RESET}")
    slow_print(f"{MAGENTA}asm volatile (\"nop\");{RESET}")
    time.sleep(1)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Inline asm lets you insert custom assembly into C functions",
        "✔ GCC syntax uses constraints and clobber lists to manage registers",
        "✔ Use it sparingly — small performance wins, big complexity risks"
    ]
    for s in summary:
        slow_print(f"{GREEN}{s}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write a C function that multiplies two integers using inline assembly and returns the result!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want an example using `syscall` or floating-point inline asm next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")