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
    print(f"\n{BOLD}💻 Binary Math and Number Representation in x86-64{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🔢 All numbers in Assembly are represented in binary — patterns of 0s and 1s stored in memory and registers.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}Understanding how integers are stored helps you perform arithmetic and interpret results correctly.{RESET}")
    time.sleep(1)

    # Signed vs unsigned
    slow_print(f"\n{BOLD}📌 Signed vs Unsigned Integers:{RESET}")
    slow_print(f"{GREEN}Unsigned integers{RESET} represent only non-negative values: 0 to 2ⁿ - 1")
    slow_print(f"{GREEN}Signed integers{RESET} (two's complement) represent both negative and positive numbers.")
    time.sleep(1)

    slow_print(f"\n{BOLD}🧮 Example: 8-bit Values{RESET}")
    slow_print(f"  {BOLD}Unsigned:{RESET}  00000000 → 0   to   11111111 → 255")
    slow_print(f"  {BOLD}Signed:{RESET}    10000000 → -128 to 01111111 → 127")
    time.sleep(1.2)

    # Two's complement explanation
    slow_print(f"\n{CYAN}🌀 Two's Complement Representation:{RESET}")
    slow_print(f"  - To get the negative of a number: invert all bits and add 1.")
    slow_print(f"  - Makes subtraction and negative values easy to handle in hardware.")
    time.sleep(1.2)

    # Binary math examples
    slow_print(f"\n{BOLD}➕ Binary Addition Example:{RESET}")
    slow_print("  00000101   (5)")
    slow_print("+ 00000011   (3)")
    slow_print("= 00001000   (8)")
    time.sleep(1)

    slow_print(f"\n{BOLD}➖ Binary Subtraction (5 - 3):{RESET}")
    slow_print("  00000101   (5)")
    slow_print("- 00000011   (3)")
    slow_print("= 00000010   (2)")
    time.sleep(1)

    # Overflow note
    slow_print(f"\n{RED}⚠️ Overflow can occur if a result exceeds the number of bits available!{RESET}")
    slow_print(f"{MAGENTA}e.g., 8-bit: 255 + 1 wraps around to 0 (like a speedometer){RESET}")
    time.sleep(1.2)

    # Instructions
    slow_print(f"\n{BOLD}📦 Arithmetic Instructions:{RESET}")
    slow_print(f"{GREEN}add, sub{RESET} — perform signed or unsigned arithmetic")
    slow_print(f"{GREEN}imul, idiv{RESET} — signed multiplication/division")
    slow_print(f"{GREEN}mul, div{RESET} — unsigned multiplication/division")
    time.sleep(1)

    # Flags
    slow_print(f"\n{CYAN}💡 These operations affect CPU flags like:{RESET}")
    slow_print(f"{BOLD}CF{RESET} (Carry), {BOLD}OF{RESET} (Overflow), {BOLD}ZF{RESET} (Zero), {BOLD}SF{RESET} (Sign)")
    slow_print(f"{MAGENTA}We'll use these in conditionals and loops later!{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ All numbers are stored as binary in registers{RESET}")
    slow_print(f"{GREEN}✔ Two's complement handles signed values cleanly{RESET}")
    slow_print(f"{GREEN}✔ Know the size of your operands: 8, 16, 32, or 64 bits{RESET}")
    slow_print(f"{GREEN}✔ Overflow and sign flags help detect issues in math{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Next up: We'll use signed and unsigned division in actual code with 'idiv' and 'div'!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
