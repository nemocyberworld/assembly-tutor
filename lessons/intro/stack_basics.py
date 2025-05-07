import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    slow_print(f"\n🎒 {BOLD}Welcome to: Stack Basics — `push` and `pop`!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 The Stack is a special area of memory used for storing data temporarily.", 0.02)
    slow_print(f"{YELLOW}🎂 Think of it like a stack of plates — you add (push) to the top, and remove (pop) from the top.{RESET}\n", 0.02)

    slow_print(f"{CYAN}{BOLD}🏗️ It’s a Last-In, First-Out (LIFO) structure.{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{GREEN}🧱 Let’s explore the two key instructions:{RESET}")
    slow_print(f"""
  {CYAN}push <reg/val>{RESET}   → Put something onto the stack
  {CYAN}pop <reg>{RESET}        → Take the top item off the stack and put it in a register
    """, 0.01)

    time.sleep(1)

    slow_print(f"{BOLD}{CYAN}🧪 Example 1: Pushing Registers onto the Stack{RESET}", 0.02)
    slow_print("Let's push 2 values onto the stack and observe what happens.\n", 0.01)
    example1 = [
        ("mov rax, 42", "Set rax = 42"),
        ("push rax", "Put 42 on the stack"),
        ("mov rbx, 99", "Set rbx = 99"),
        ("push rbx", "Put 99 on the stack (above 42)"),
    ]
    for instr, desc in example1:
        slow_print(f"  {CYAN}{instr:<15}{RESET} {MAGENTA}{desc}{RESET}", 0.01)

    slow_print(f"\n{YELLOW}🧱 Stack now looks like this (top to bottom):{RESET}")
    slow_print(f"  🧺 99 (top)\n  🧺 42\n")

    time.sleep(1)

    slow_print(f"{BOLD}{CYAN}🔁 Example 2: Popping from the Stack{RESET}", 0.02)
    slow_print("Let’s pop the values back out into different registers.\n", 0.01)
    example2 = [
        ("pop rcx", "Takes 99 off the top and stores it in rcx"),
        ("pop rdx", "Takes 42 and stores it in rdx"),
    ]
    for instr, desc in example2:
        slow_print(f"  {CYAN}{instr:<15}{RESET} {MAGENTA}{desc}{RESET}", 0.01)

    slow_print(f"\n{YELLOW}🧪 Final register values:{RESET}")
    slow_print(f"  {GREEN}rcx = 99{RESET}")
    slow_print(f"  {GREEN}rdx = 42{RESET}\n")

    time.sleep(1)

    slow_print(f"{BOLD}{CYAN}🛑 WARNING: Stack grows downward in memory!{RESET}", 0.02)
    slow_print(f"{YELLOW}So each `push` decreases the stack pointer (`rsp`), and each `pop` increases it.{RESET}\n")

    slow_print(f"{MAGENTA}You don’t usually manipulate `rsp` directly — let `push` and `pop` handle it safely!{RESET}\n")

    time.sleep(1)

    slow_print(f"{CYAN}📌 The Stack is used for many things:", 0.02)
    slow_print(f"""
  ✅ Saving registers
  ✅ Passing arguments
  ✅ Storing return addresses
  ✅ Local variables
    """, 0.01)

    time.sleep(1)

    slow_print(f"{GREEN}🎯 Mastering the stack is key to mastering functions, calls, and memory flow in assembly!{RESET}\n", 0.02)

    slow_print(f"{BOLD}🚀 Practice makes perfect! Try writing your own push/pop sequences to understand stack order.{RESET}\n")

    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
