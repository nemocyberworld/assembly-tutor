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
    print(f"\n{BOLD}🎯 Jump Tables: Fast Branching in Assembly (x86-64){RESET}\n")
    time.sleep(1)

    # Intro
    slow_print(f"{YELLOW}💡 When you have multiple cases (like a switch statement), a jump table can branch quickly by indexing into addresses.{RESET}")
    slow_print(f"{CYAN}Instead of a series of comparisons, the CPU jumps straight to the right code by calculating an offset!{RESET}")
    time.sleep(1)

    # Why use jump tables
    slow_print(f"\n{BOLD}⚡ Why Use Jump Tables?{RESET}")
    reasons = [
        "✔ Faster than if-else or cmp/jmp chains",
        "✔ Constant-time branching: O(1)",
        "✔ Common in compilers for switch/case statements"
    ]
    for r in reasons:
        slow_print(f"{MAGENTA}{r}{RESET}")
        time.sleep(0.3)

    # Layout
    slow_print(f"\n{BOLD}📦 How It Works:{RESET}")
    slow_print(f"{CYAN}A jump table is an array of code addresses. An index is used to look up and jump to the right one.{RESET}")
    slow_print(f"""{GREEN}
  ; Example pseudo layout:
  mov rax, [table + rdi*8]  ; rdi is the case index
  jmp rax
{RESET}""")
    time.sleep(1)

    # Simulate an example
    slow_print(f"\n{BOLD}🔢 Simulating a Jump Table in Python{RESET}")
    def case_0(): slow_print(f"{GREEN}→ Case 0: Print 'Hello'{RESET}")
    def case_1(): slow_print(f"{CYAN}→ Case 1: Add two numbers{RESET}")
    def case_2(): slow_print(f"{YELLOW}→ Case 2: Exit cleanly{RESET}")
    def default(): slow_print(f"{RED}→ Default case: Unknown input{RESET}")

    jump_table = [case_0, case_1, case_2]

    for idx in range(-1, 4):
        slow_print(f"\n{BOLD}📌 Index: {idx}{RESET}")
        if 0 <= idx < len(jump_table):
            jump_table[idx]()
        else:
            default()
        time.sleep(0.7)

    # Assembly snippet
    slow_print(f"\n{BOLD}🧠 Assembly Snippet (x86-64):{RESET}")
    slow_print(f"""{MAGENTA}
  ; rdi holds the case index
  lea rbx, [rel table]
  cmp rdi, 2
  ja  default_case
  mov rax, [rbx + rdi*8]
  jmp rax

table:
  dq case_0
  dq case_1
  dq case_2
{RESET}""")
    time.sleep(1)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Jump tables are efficient for handling many cases",
        "✔ Indexing into code pointers avoids conditionals",
        "✔ Common in compiled switch-case logic",
        "✔ Requires careful bounds checking to avoid crashes"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write a jump table that handles 5 math ops (add, sub, mul, div, mod) by index! Bonus: Add a default fallback handler.{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to simulate this in actual NASM next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")