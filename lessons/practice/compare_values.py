# lessons/practice_programs/compare_values.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🔍 Compare Two Values and Print Result (x86-64, Linux){RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}📢 Want to make decisions in assembly? Meet `cmp` and friends!{RESET}")
    slow_print(f"{CYAN}With `cmp` and conditional jumps like `je`, `jl`, and `jg`, you can control your program’s flow!{RESET}")
    time.sleep(1)

    # Setup
    slow_print(f"\n{BOLD}🧰 You'll Use:{RESET}")
    setup_info = [
        "✔ Registers (e.g., `rax`, `rbx`)",
        "✔ `cmp` to compare values (sets flags)",
        "✔ Conditional jumps like `je`, `jl`, `jg`",
        "✔ Syscalls to print the result"
    ]
    for item in setup_info:
        slow_print(f"{MAGENTA}{item}{RESET}")
        time.sleep(0.4)

    # Code Skeleton
    slow_print(f"\n{BOLD}💡 Code Logic Example:{RESET}")
    slow_print(f"""{DIM}
    mov     rax, 7
    mov     rbx, 5
    cmp     rax, rbx
    je      equal
    jl      less
    jg      greater

equal:
    ; print "Equal"
    jmp     end

less:
    ; print "Less than"
    jmp     end

greater:
    ; print "Greater than"

end:
    ; syscall to exit{RESET}""")
    time.sleep(1)

    # Breakdown
    slow_print(f"\n{BOLD}🔍 Breakdown:{RESET}")
    breakdown = [
        "✔ `cmp a, b` sets flags based on `a - b` (but doesn't store the result)",
        "✔ `je` (jump if equal), `jl` (less than), `jg` (greater than)",
        "✔ Jump to the correct label and print result using `write`"
    ]
    for line in breakdown:
        slow_print(f"{CYAN}{line}{RESET}")
        time.sleep(0.4)

    # Build Steps
    slow_print(f"\n{BOLD}⚙️ Build and Run:{RESET}")
    slow_print(f"{MAGENTA}1. Save as `compare_values.asm`")
    slow_print(f"2. Assemble: nasm -f elf64 compare_values.asm -o compare_values.o")
    slow_print(f"3. Link: ld compare_values.o -o compare_values")
    slow_print(f"4. Run: ./compare_values{RESET}")
    time.sleep(1)

    # Challenge
    slow_print(f"\n{BOLD}{GREEN}🎯 Your Task:{RESET}")
    slow_print("→ Try different value combinations.")
    slow_print("→ Observe which branch is taken depending on the result of `cmp`.")

    # Tips & Bonus
    slow_print(f"\n{BOLD}{BLUE}💡 Tip:{RESET} `cmp a, b` subtracts `b` from `a` but only sets flags — not the result.")
    
    slow_print(f"\n{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print(f"{MAGENTA}→ Try comparing signed vs unsigned integers.")
    slow_print("→ Print which value is greater in a format like: '7 > 5'{RESET}")
    time.sleep(1)

    # Wrap-up
    print(f"\n{BOLD}✅ Lesson complete! You now have decision-making power in Assembly! 🧠{RESET}")
