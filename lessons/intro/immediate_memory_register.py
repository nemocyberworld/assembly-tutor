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
    print(f"\n{BOLD}🔍 Lesson: Working with Immediate, Memory, and Register Values{RESET}\n")
    time.sleep(1)

    intro = [
        f"{YELLOW}🧠 Assembly deals with values in 3 main forms: {BOLD}immediate, register, and memory{RESET}{YELLOW}.{RESET}",
        f"{YELLOW}Let's break them down with examples, analogies, and code!{RESET}"
    ]
    for line in intro:
        slow_print(line)
        time.sleep(1)

    print()
    slow_print(f"{CYAN}📌 Immediate values are literal constants written right into instructions.{RESET}")
    slow_print(f"{GREEN}Example:{RESET}  {CYAN}mov rax, 42{RESET}   {MAGENTA}# Put the value 42 directly into rax{RESET}")
    slow_print(f"{YELLOW}💡 Analogy: Like writing a number on a sticky note and handing it to someone.{RESET}")
    time.sleep(1.5)

    print()
    slow_print(f"{CYAN}📌 Register values are stored in the CPU's internal fast storage — registers like rax, rbx, etc.{RESET}")
    slow_print(f"{GREEN}Example:{RESET}  {CYAN}mov rbx, rax{RESET}   {MAGENTA}# Copy the value in rax into rbx{RESET}")
    slow_print(f"{YELLOW}💡 Analogy: Like handing a copy of a note you already have to someone else.{RESET}")
    time.sleep(1.5)

    print()
    slow_print(f"{CYAN}📌 Memory values are stored in RAM — your program can read from or write to specific addresses.{RESET}")
    slow_print(f"{GREEN}Example:{RESET}  {CYAN}mov rax, [my_var]{RESET}   {MAGENTA}# Load the value stored at label 'my_var' into rax{RESET}")
    slow_print(f"{YELLOW}💡 Analogy: Like looking up a file by name from a cabinet and reading its contents.{RESET}")
    time.sleep(2)

    print()
    slow_print(f"{BOLD}{MAGENTA}🔄 Let’s compare them side by side:{RESET}")
    comparison = [
        ("mov rax, 5", "Immediate — put 5 directly into rax"),
        ("mov rax, rbx", "Register — copy value from rbx to rax"),
        ("mov rax, [value]", "Memory — read value from memory label 'value' into rax"),
        ("mov [result], rax", "Memory — write rax's value into memory label 'result'"),
    ]
    for code, explanation in comparison:
        slow_print(f"  {CYAN}{code:<25}{RESET} {MAGENTA}{explanation}{RESET}")
        time.sleep(0.8)

    print()
    slow_print(f"{GREEN}🧪 Here’s a simulated snippet using all 3 types:{RESET}")
    time.sleep(1)

    example_code = [
        "section .data",
        "  my_number dq 10",
        "  result dq 0",
        "",
        "section .text",
        "  global _start",
        "_start:",
        "  mov rax, 5          ; immediate",
        "  mov rbx, [my_number] ; memory",
        "  add rax, rbx        ; rax = 5 + 10",
        "  mov [result], rax   ; memory",
        "  mov rax, 60         ; exit syscall",
        "  xor rdi, rdi        ; status code 0",
        "  syscall"
    ]
    for line in example_code:
        color = CYAN if line.strip().startswith(('mov', 'add', 'xor', 'syscall')) else MAGENTA
        slow_print(f"  {color}{line}{RESET}")
        time.sleep(0.2)

    print()
    slow_print(f"{YELLOW}🎯 Now you can spot and use immediate, register, and memory values in real code!{RESET}")
    slow_print(f"{YELLOW}We'll use all of them together when doing arithmetic, function calls, and more.{RESET}")
    time.sleep(1.5)

    print()
    slow_print(f"{BOLD}{CYAN}➡️ Coming up next: {GREEN}Doing math in Assembly — add, sub, mul, div! 🧮{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")

