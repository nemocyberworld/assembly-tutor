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
    print(f"\n{BOLD}🔁 Advanced Control Flow: Loops & Conditionals in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧭 Assembly doesn’t have `if`, `for`, or `while` — just jumps based on condition flags.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}We use labels to mark code positions, and instructions like {BOLD}jmp, je, jne, jl, jg, jz, jnz{RESET}{CYAN} to control flow.{RESET}")
    time.sleep(1)

    # Condition flags
    slow_print(f"\n{BOLD}📌 Condition Flags (Status Register){RESET}")
    flags = [
        ("ZF", "Zero Flag — set if result is zero"),
        ("SF", "Sign Flag — set if result is negative"),
        ("CF", "Carry Flag — set if unsigned overflow occurs"),
        ("OF", "Overflow Flag — set if signed overflow occurs"),
    ]
    for flag, desc in flags:
        slow_print(f"  {BOLD}{flag:<3}{RESET} - {desc}")
        time.sleep(0.7)

    slow_print(f"{MAGENTA}These flags are set by operations like cmp, sub, or test — and used by conditional jumps.{RESET}")
    time.sleep(1)

    # Conditional jump example
    slow_print(f"\n{BOLD}💡 Example: Conditional Jump (if x == 5){RESET}")
    asm = [
        "mov rax, 5",
        "cmp rax, 5",
        "je equal_label",  # Jump if equal (ZF=1)
        "; not equal path",
        "jmp end_label",
        "equal_label:",
        "; code when equal",
        "end_label:"
    ]
    for line in asm:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.6)

    # Looping
    slow_print(f"\n{BOLD}🔄 Example: Loop from 0 to 4 (like a for-loop){RESET}")
    loop_code = [
        "mov rcx, 0",             # Counter
        "loop_start:",
        "cmp rcx, 5",
        "jge loop_end",           # Exit if rcx >= 5
        "; do something here",
        "inc rcx",
        "jmp loop_start",
        "loop_end:"
    ]
    for line in loop_code:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.6)

    # Simulate the loop
    slow_print(f"\n{MAGENTA}🧮 Simulating the loop...{RESET}")
    rcx = 0
    while rcx < 5:
        slow_print(f"  rcx = {rcx} → doing something...")
        rcx += 1
        time.sleep(0.5)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Use {BOLD}cmp{RESET}{GREEN} or {BOLD}test{RESET}{GREEN} to set flags for comparisons{RESET}")
    slow_print(f"{GREEN}✔ Conditional jumps like {BOLD}je, jne, jl, jg, jz, jnz{RESET}{GREEN} react to the flags{RESET}")
    slow_print(f"{GREEN}✔ Loops are just labels + jumps — no `for` or `while`, only structure via control flow{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Next up: We’ll combine conditionals and loops to scan arrays and make decisions!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")