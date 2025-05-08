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
    print(f"\n{BOLD}🧮 Bitwise Operations in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    intro = [
        f"{YELLOW}👾 Bitwise operations work directly with individual bits — the 1s and 0s that make up all data.{RESET}",
        f"{YELLOW}🧠 These are *low-level superpowers* used for performance, encryption, hardware control, and more.{RESET}",
        f"{YELLOW}⚙️ We'll learn four common ones: {BOLD}AND{RESET}, {BOLD}OR{RESET}, {BOLD}XOR{RESET}, and {BOLD}NOT{RESET}.{RESET}",
    ]
    for line in intro:
        slow_print(line)
        time.sleep(1)

    print()
    slow_print(f"{CYAN}{BOLD}📘 Bitwise AND (and){RESET}")
    slow_print("  Keeps only the bits that are 1 in BOTH values.")
    slow_print(f"{MAGENTA}  Example:{RESET}")
    slow_print("    1101 (13)")
    slow_print("  & 1011 (11)")
    slow_print("  -----------")
    slow_print("    1001 (9)")
    time.sleep(1)

    print()
    slow_print(f"{CYAN}{BOLD}📘 Bitwise OR (or){RESET}")
    slow_print("  Keeps bits that are 1 in EITHER value.")
    slow_print(f"{MAGENTA}  Example:{RESET}")
    slow_print("    1101 (13)")
    slow_print("  | 1011 (11)")
    slow_print("  -----------")
    slow_print("    1111 (15)")
    time.sleep(1)

    print()
    slow_print(f"{CYAN}{BOLD}📘 Bitwise XOR (xor){RESET}")
    slow_print("  Keeps bits that are 1 in ONE value, but not both.")
    slow_print(f"{MAGENTA}  Example:{RESET}")
    slow_print("    1101 (13)")
    slow_print("  ^ 1011 (11)")
    slow_print("  -----------")
    slow_print("    0110 (6)")
    time.sleep(1)

    print()
    slow_print(f"{CYAN}{BOLD}📘 Bitwise NOT (not){RESET}")
    slow_print("  Flips all the bits (0 → 1, 1 → 0).")
    slow_print(f"{MAGENTA}  Example (8-bit view):{RESET}")
    slow_print("    NOT 11001100")
    slow_print("     => 00110011")
    slow_print(f"{RED}⚠️ Be careful! NOT inverts all bits — this affects negative numbers due to two's complement!{RESET}")
    time.sleep(2)

    print()
    slow_print(f"{YELLOW}🧪 Here's how it looks in x86-64 Assembly:{RESET}")
    code = [
        ("mov rax, 13", "🧠 rax = 1101"),
        ("mov rbx, 11", "🧠 rbx = 1011"),
        ("and rax, rbx", "🔗 rax = rax & rbx (result: 1001)"),
        ("or rax, rbx",  "🔗 rax = rax | rbx (result: 1111)"),
        ("xor rax, rbx", "🔗 rax = rax ^ rbx (result: 0110)"),
        ("not rax",      "🌀 Flip all bits in rax"),
    ]
    for line, explanation in code:
        print(f"  {CYAN}{line:<20}{RESET} {MAGENTA}{explanation}{RESET}")
        time.sleep(0.6)

    print()
    slow_print(f"{GREEN}✨ Bitwise operations are foundational for systems programming, cryptography, and fast math tricks!{RESET}")
    slow_print(f"{GREEN}You’ll use them more than you think — especially in performance-critical or security-sensitive code.{RESET}")
    time.sleep(1.5)

    print()
    slow_print(f"{BOLD}{CYAN}🧭 Up next: logical decisions with CMP and conditional jumps! 🪂{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Ready to bit-flip your way to mastery?{RESET}")
    lessons/intro/arithmetic.py
