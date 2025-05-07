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
    slow_print(f"\n🎌 {BOLD}Welcome to: Understanding Flags and the Status Register!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 Flags are special bits in a register that reflect the outcome of instructions.{RESET}", 0.02)
    slow_print(f"{YELLOW}🔎 Think of them like traffic signals for your CPU — they tell it what just happened.{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🏛️ Meet the FLAGS Register:{RESET}\n", 0.02)
    flags = [
        ("ZF (Zero Flag)", "🚫 Set if the result of an operation is ZERO."),
        ("SF (Sign Flag)", "➖ Set if the result is NEGATIVE."),
        ("CF (Carry Flag)", "📦 Set if there's an unsigned overflow (carry out)."),
        ("OF (Overflow Flag)", "💥 Set if there's a signed overflow."),
        ("PF (Parity Flag)", "🔢 Set if the number of set bits in the result is even."),
        ("AF (Adjust Flag)", "🔧 Set on carry/borrow between lower nibbles (used in BCD math)."),
    ]

    for flag, desc in flags:
        slow_print(f"  {GREEN}{flag:<18}{RESET} {MAGENTA}{desc}{RESET}", 0.01)
        time.sleep(0.3)

    print()
    slow_print(f"{YELLOW}📦 Let's break each of these down with examples and explanations:{RESET}\n", 0.02)

    # Zero Flag
    slow_print(f"{BOLD}{CYAN}1. ZF - Zero Flag:{RESET}", 0.02)
    slow_print("✅ Set when an operation results in zero.\n", 0.01)
    zf_example = [
        ("mov al, 5", "Load 5 into AL"),
        ("sub al, 5", "5 - 5 = 0 → ZF is set!"),
    ]
    for line, explain in zf_example:
        slow_print(f"  {CYAN}{line:<15}{RESET} {MAGENTA}{explain}{RESET}", 0.01)
    slow_print(f"  {YELLOW}👉 Because the result is 0, ZF = 1. Useful for 'je' (jump if equal).{RESET}\n")

    # Sign Flag
    slow_print(f"{BOLD}{CYAN}2. SF - Sign Flag:{RESET}", 0.02)
    slow_print("🟥 Set when the result is negative (most significant bit = 1).\n", 0.01)
    sf_example = [
        ("mov al, 5", "Load 5 into AL"),
        ("sub al, 10", "5 - 10 = -5 → SF is set!"),
    ]
    for line, explain in sf_example:
        slow_print(f"  {CYAN}{line:<15}{RESET} {MAGENTA}{explain}{RESET}", 0.01)
    slow_print(f"  {YELLOW}👉 Result is negative (in two's complement: 0xFB). SF = 1.{RESET}\n")

    # Carry Flag
    slow_print(f"{BOLD}{CYAN}3. CF - Carry Flag:{RESET}", 0.02)
    slow_print("📤 Set on *unsigned* overflow (when result doesn’t fit).\n", 0.01)
    cf_example = [
        ("mov al, 255", "Max 8-bit value (0xFF)"),
        ("add al, 1", "255 + 1 = 0 → CF is set!"),
    ]
    for line, explain in cf_example:
        slow_print(f"  {CYAN}{line:<15}{RESET} {MAGENTA}{explain}{RESET}", 0.01)
    slow_print(f"  {YELLOW}👉 The 8-bit register wraps to 0, but overflowed → CF = 1!{RESET}\n")

    # Overflow Flag
    slow_print(f"{BOLD}{CYAN}4. OF - Overflow Flag:{RESET}", 0.02)
    slow_print("🔥 Set on *signed* overflow (e.g., 127 + 1 → -128).\n", 0.01)
    of_example = [
        ("mov al, 127", "Max signed 8-bit: 0111 1111"),
        ("add al, 1", "127 + 1 = -128 → OF is set!"),
    ]
    for line, explain in of_example:
        slow_print(f"  {CYAN}{line:<15}{RESET} {MAGENTA}{explain}{RESET}", 0.01)
    slow_print(f"  {YELLOW}👉 Sign changed incorrectly (positive → negative). OF = 1!{RESET}\n")

    # Parity Flag
    slow_print(f"{BOLD}{CYAN}5. PF - Parity Flag:{RESET}", 0.02)
    slow_print("🎲 Set if result has even number of 1s (used in error detection).\n", 0.01)
    pf_example = [
        ("mov al, 0b00001111", "4 ones → even → PF is set!"),
        ("mov al, 0b00001110", "3 ones → odd → PF is clear!"),
    ]
    for line, explain in pf_example:
        slow_print(f"  {CYAN}{line:<25}{RESET} {MAGENTA}{explain}{RESET}", 0.01)
    slow_print(f"  {YELLOW}👉 PF is useful in string comparisons and loop decisions.{RESET}\n")

    # Adjust Flag
    slow_print(f"{BOLD}{CYAN}6. AF - Adjust Flag:{RESET}", 0.02)
    slow_print("🔩 Set if there's a carry from bit 3 to bit 4 (used in BCD math).\n", 0.01)
    af_example = [
        ("mov al, 0x0F", "Lower nibble = 1111"),
        ("add al, 0x01", "0x0F + 1 = 0x10 → carry from bit 3 → AF is set!"),
    ]
    for line, explain in af_example:
        slow_print(f"  {CYAN}{line:<15}{RESET} {MAGENTA}{explain}{RESET}", 0.01)
    slow_print(f"  {YELLOW}👉 Mostly used in older decimal arithmetic. Rare today, but still exists!{RESET}\n")

    time.sleep(1)
    slow_print(f"{GREEN}🎮 These flags are critical for decision-making in assembly!", 0.02)
    slow_print(f"{YELLOW}You’ll use them with conditional jumps like:{RESET}", 0.02)
    slow_print(f"""
    {CYAN}je{RESET} — Jump if Equal (ZF == 1)
    {CYAN}jl{RESET} — Jump if Less (SF != OF)
    {CYAN}jg{RESET} — Jump if Greater (ZF == 0 and SF == OF)
    {CYAN}jc{RESET} — Jump if Carry (CF == 1)
    {CYAN}jo{RESET} — Jump if Overflow (OF == 1)
    """, 0.01)

    slow_print(f"{BOLD}🎉 Boom! Now you speak CPU emotions! 🧠💬{RESET}", 0.02)
    slow_print(f"{CYAN}Flags drive logic, loops, and conditions — master them, and you master flow control!{RESET}\n", 0.02)

    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
