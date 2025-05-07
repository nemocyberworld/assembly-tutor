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
    slow_print(f"\n🎯 {BOLD}Lesson: Using Labels and Creating Flow Control{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}🔖 Labels are names you give to positions in your code.{RESET}", 0.02)
    slow_print(f"{YELLOW}🔁 They help you jump around in your program using instructions like `jmp`, `je`, `call`, and more!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🧠 Why Labels?{RESET}", 0.02)
    slow_print(f"{GREEN}➡️ Labels help organize code and manage control flow, especially in loops, conditionals, and functions.{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}📄 Example 1: Jumping to a Label{RESET}\n", 0.02)
    code1 = [
        ("section .text", ""),
        ("global _start", ""),
        ("", ""),
        ("_start:", ""),
        ("    jmp skip_message", "👉 Jump directly to 'skip_message', skipping next line"),
        ("", ""),
        ("    mov rax, 1", "This won't execute"),
        ("", ""),
        ("skip_message:", "🏷️ A label! Execution continues from here"),
        ("    mov rax, 60", "System call to exit"),
        ("    xor rdi, rdi", "Exit status 0"),
        ("    syscall", "Exit"),
    ]

    for code, explanation in code1:
        if code.strip() == "":
            print()
            continue
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
        time.sleep(0.2)

    time.sleep(1)
    slow_print(f"\n{CYAN}{BOLD}📄 Example 2: Looping with a Label{RESET}\n", 0.02)
    code2 = [
        ("section .text", ""),
        ("global _start", ""),
        ("", ""),
        ("_start:", ""),
        ("    mov rcx, 5", "🔢 Counter set to 5"),
        ("print_loop:", "🏷️ Start of the loop"),
        ("    ; Print message or do something here", ""),
        ("    dec rcx", "📉 Decrease counter"),
        ("    jnz print_loop", "🔁 If rcx != 0, jump to print_loop"),
        ("    mov rax, 60", "System call to exit"),
        ("    xor rdi, rdi", "Exit status 0"),
        ("    syscall", "Exit"),
    ]

    for code, explanation in code2:
        if code.strip() == "":
            print()
            continue
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
        time.sleep(0.2)

    time.sleep(1)
    slow_print(f"\n{CYAN}{BOLD}📄 Example 3: Using Labels with `cmp` and Conditional Jumps{RESET}\n", 0.02)
    code3 = [
        ("section .text", ""),
        ("global _start", ""),
        ("", ""),
        ("_start:", ""),
        ("    mov rax, 10", ""),
        ("    cmp rax, 10", "🔍 Compare rax with 10"),
        ("    je they_are_equal", "✅ Jump if equal"),
        ("    jmp end", "❌ Otherwise, skip"),
        ("", ""),
        ("they_are_equal:", "🏷️ Executed only if rax == 10"),
        ("    ; Do something here", ""),
        ("", ""),
        ("end:", ""),
        ("    mov rax, 60", "Exit"),
        ("    xor rdi, rdi", ""),
        ("    syscall", ""),
    ]

    for code, explanation in code3:
        if code.strip() == "":
            print()
            continue
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
        time.sleep(0.2)

    time.sleep(1)
    slow_print(f"\n{GREEN}✅ Labels give your assembly code structure, readability, and power!{RESET}", 0.02)
    slow_print(f"{BOLD}🏗️ Use them to build loops, conditionals, and functions like a pro!{RESET}", 0.02)
    slow_print(f"\n{CYAN}🧠 Practice writing your own labeled loops and control structures! You're mastering the flow of the CPU! 💪{RESET}", 0.02)
