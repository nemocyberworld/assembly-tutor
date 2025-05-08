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
    print(f"\n👋 {BOLD}Welcome to: What is Assembly Language?{RESET}\n")
    time.sleep(1)

    intro_lines = [
        f"{YELLOW}🧠 Assembly is a language designed to talk directly to your computer's brain — the CPU.{RESET}",
        f"{YELLOW}💡 Unlike high-level languages (like Python), Assembly gives you full control over the hardware.{RESET}",
        f"{YELLOW}🔍 Every instruction tells the CPU *exactly* what to do — no shortcuts, no magic!{RESET}",
    ]
    for line in intro_lines:
        slow_print(line)
        time.sleep(1.2)

    print()
    slow_print(f"{CYAN}🤔 Still a bit fuzzy? Here's a quick comparison:{RESET}")
    time.sleep(1)

    analogy = [
        f"{MAGENTA}🧱 High-Level Language (Python):{RESET}  print('Hello, world!')",
        f"{MAGENTA}🧰 Mid-Level Language (C):       printf(\"Hello, world!\\n\");",
        f"{MAGENTA}⚙️  Low-Level Language (Assembly):{RESET} mov rax, 1 / syscall / etc.",
    ]
    for line in analogy:
        slow_print("   " + line)
        time.sleep(1)

    print()
    slow_print(f"{GREEN}🔎 So... why should *you* learn Assembly?{RESET}")
    time.sleep(1)
    reasons = [
        f"{GREEN}🧠 It helps you understand what your programs are really doing under the hood.{RESET}",
        f"{GREEN}🚀 It's essential for writing super-fast code and optimizing performance.{RESET}",
        f"{GREEN}🛡️ It's crucial in cybersecurity, ethical hacking, and reverse engineering.{RESET}",
        f"{GREEN}🧰 And it's the foundation for writing OS kernels, drivers, and bootloaders!{RESET}",
    ]
    for line in reasons:
        slow_print("  " + line)
        time.sleep(1.1)

    print()
    slow_print(f"{YELLOW}📦 In this course, we'll focus on {BOLD}x86-64 Assembly{RESET}{YELLOW}, the modern 64-bit architecture used by most PCs today.{RESET}")
    time.sleep(1.2)
    slow_print(f"{YELLOW}We'll write real programs using the {BOLD}NASM assembler{RESET}{YELLOW}, and run them directly on Linux using {BOLD}syscalls{RESET}{YELLOW}.{RESET}")
    time.sleep(2)

    print()
    slow_print(f"{CYAN}{BOLD}🧭 Ready to explore the CPU's inner workings? Up next: {GREEN}Registers — the tiny storage units at the heart of everything!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
