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
    print(f"\n{BOLD}➕ Basic Arithmetic in x86-64: add, sub, inc, dec{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}📐 In Assembly, math is done using instructions that directly affect registers — no variables, just raw values and operations.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}Let's explore the four main arithmetic instructions:{RESET}")
    time.sleep(1)

    instructions = [
        ("add", "Adds one value to another"),
        ("sub", "Subtracts one value from another"),
        ("inc", "Increments (adds 1 to) a value"),
        ("dec", "Decrements (subtracts 1 from) a value"),
    ]
    for name, desc in instructions:
        slow_print(f"  {GREEN}{name:<4}{RESET} - {desc}")
        time.sleep(0.7)

    print()
    slow_print(f"{MAGENTA}🧠 These operations usually modify registers. Let's go step-by-step with some examples!{RESET}")
    time.sleep(1)

    # Example 1: add
    slow_print(f"\n{BOLD}💡 Example 1: add rax, rbx{RESET}")
    time.sleep(0.5)
    slow_print(f"{CYAN}This adds the value in {BOLD}rbx{RESET}{CYAN} to {BOLD}rax{RESET} and stores the result in {BOLD}rax{RESET}.{RESET}")
    slow_print(f"{MAGENTA}It's like: rax = rax + rbx{RESET}")
    time.sleep(1)

    # Simulated register values
    slow_print(f"\n{GREEN}🔧 Let's simulate it...{RESET}")
    rax = 5
    rbx = 3
    slow_print(f"  {BOLD}Initial rax:{RESET} {rax}")
    slow_print(f"  {BOLD}Initial rbx:{RESET} {rbx}")
    rax += rbx
    time.sleep(1)
    slow_print(f"  {BOLD}After add rax, rbx → rax:{RESET} {rax}")
    time.sleep(1)

    # Example 2: sub
    slow_print(f"\n{BOLD}💡 Example 2: sub rax, 2{RESET}")
    slow_print(f"{CYAN}This subtracts 2 from {BOLD}rax{RESET}.{RESET}")
    slow_print(f"{MAGENTA}It's like: rax = rax - 2{RESET}")
    rax -= 2
    time.sleep(1)
    slow_print(f"  {BOLD}After sub rax, 2 → rax:{RESET} {rax}")
    time.sleep(1)

    # Example 3: inc
    slow_print(f"\n{BOLD}💡 Example 3: inc rax{RESET}")
    slow_print(f"{CYAN}This adds 1 to {BOLD}rax{RESET}.{RESET}")
    rax += 1
    time.sleep(1)
    slow_print(f"  {BOLD}After inc rax → rax:{RESET} {rax}")
    time.sleep(1)

    # Example 4: dec
    slow_print(f"\n{BOLD}💡 Example 4: dec rbx{RESET}")
    slow_print(f"{CYAN}This subtracts 1 from {BOLD}rbx{RESET}.{RESET}")
    rbx -= 1
    time.sleep(1)
    slow_print(f"  {BOLD}After dec rbx → rbx:{RESET} {rbx}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🎯 These simple instructions are the foundation for all math in Assembly — loops, counters, calculations... everything!{RESET}")
    time.sleep(1)

    slow_print(f"{GREEN}👀 And remember: these instructions affect the {BOLD}flags register{RESET}{GREEN}, which we’ll explore later for decision-making!{RESET}")
    time.sleep(1.5)

    print()
    slow_print(f"{BOLD}{CYAN}🧪 In the next lesson, we'll start building actual expressions using these and more instructions like 'imul' and 'idiv'!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

