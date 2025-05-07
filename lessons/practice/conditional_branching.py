# lessons/practice_programs/conditional_branching.py

import time

# ANSI Colors
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
    print(f"\n{BOLD}🔀 Lesson: Branch Based on Multiple Conditions{RESET}\n")
    time.sleep(0.5)

    slow_print(f"{CYAN}🎯 Goal:{RESET} Learn to compare values and branch to different code paths depending on multiple conditions.\n")

    slow_print(f"{BLUE}📚 Why This Is Cool:{RESET}")
    slow_print("  • Let's you build logic like IF/ELSE or SWITCH statements.")
    slow_print("  • Critical for writing meaningful programs — decisions, actions, outcomes!")
    slow_print("  • Makes your assembly code intelligent and dynamic.\n")

    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Load a value into `rax`.",
        "2️⃣  Compare it against multiple constants using `cmp`.",
        "3️⃣  Use jump instructions like `je`, `jl`, `jg`, `jne` to pick the right path.",
        "4️⃣  Print or simulate behavior for each branch."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{BOLD}🧠 Example: Decide Based on Age Value{RESET}")
    print(f"""{DIM}
section .text
global _start

_start:
    mov     rax, 25         ; your age

    cmp     rax, 18
    jl      too_young       ; if age < 18

    cmp     rax, 65
    jg      retire_time     ; if age > 65

    jmp     adult_zone      ; else (between 18–65)

too_young:
    ; simulate print: "You're too young!"
    jmp     done

retire_time:
    ; simulate print: "Time to retire!"
    jmp     done

adult_zone:
    ; simulate print: "Welcome to adulthood!"
    
done:
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    slow_print(f"\n{GREEN}🎯 Your Mission:{RESET} Try changing the `rax` value to test each condition. Then add more branches for fun scenarios like 'teen', 'middle-aged', etc!")

    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("  - Use `cmp` followed by `jl`, `jle`, `je`, `jne`, `jg`, or `jge` for conditionals.")
    slow_print("  - You can stack multiple comparisons in a row before jumping.")
    slow_print("  - Use comments to simulate output or learn how to print with syscalls.\n")

    slow_print(f"{BOLD}🚀 Bonus Challenges:{RESET}")
    slow_print("  - Implement a simple grade system (A/B/C/Fail) based on a test score.")
    slow_print("  - Write a branching tree with 4+ outcomes based on input.")
    slow_print("  - Try combining multiple conditions using logical flags.\n")

    slow_print(f"{CYAN}🧠 Branching is your power to control flow — make your program think! 🌲🔁{RESET}\n")
