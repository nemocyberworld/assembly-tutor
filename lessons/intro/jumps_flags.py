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
    slow_print(f"\n👋 {BOLD}Welcome to the x86-64 Assembly lesson: Conditional Jumps!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}📚 In this lesson, we explore how programs make decisions using flags and jump instructions like {BOLD}`cmp`, `je`, `jne`, `jg`, `jl`, etc.{RESET}{YELLOW}.{RESET}", 0.02)
    slow_print(f"{YELLOW}🧠 These jumps depend on the results of comparisons, often set by the `cmp` instruction.{RESET}\n", 0.02)
    time.sleep(1.5)

    slow_print(f"{CYAN}{BOLD}🔍 Let's break it down!{RESET}\n", 0.02)

    examples = [
        {
            "title": "Unconditional Jump - jmp",
            "code": [
                "jmp skip",
                "mov rax, 1",
                "skip:",
                "mov rbx, 2"
            ],
            "explanation": "🚀 `jmp` always jumps to the label, skipping over `mov rax, 1`. So rbx gets set, rax does not."
        },
        {
            "title": "Compare and Jump if Equal - cmp + je",
            "code": [
                "mov rax, 5",
                "mov rbx, 5",
                "cmp rax, rbx",
                "je equal_label",
                "mov rcx, 1",
                "equal_label:",
                "mov rcx, 0"
            ],
            "explanation": "✅ `je` jumps if the values are equal. `cmp` sets the Zero Flag (ZF). Since rax == rbx, `je` jumps over `mov rcx, 1` and sets rcx to 0."
        },
        {
            "title": "Compare and Jump if Not Equal - jne",
            "code": [
                "mov rax, 5",
                "mov rbx, 3",
                "cmp rax, rbx",
                "jne not_equal",
                "mov rcx, 0",
                "not_equal:",
                "mov rcx, 1"
            ],
            "explanation": "🔄 `jne` jumps if values are NOT equal. Since 5 != 3, the jump happens and rcx becomes 1."
        },
        {
            "title": "Jump if Greater (signed) - jg",
            "code": [
                "mov rax, 10",
                "mov rbx, 3",
                "cmp rax, rbx",
                "jg greater",
                "mov rcx, 0",
                "greater:",
                "mov rcx, 1"
            ],
            "explanation": "⬆️ `jg` (jump if greater) works on signed integers. 10 > 3 is true, so rcx = 1."
        },
        {
            "title": "Jump if Greater or Equal - jge",
            "code": [
                "mov rax, 5",
                "mov rbx, 5",
                "cmp rax, rbx",
                "jge ge_label",
                "mov rcx, 0",
                "ge_label:",
                "mov rcx, 1"
            ],
            "explanation": "🔢 `jge` jumps if the first value is greater or equal to the second. Here, they are equal, so jump occurs."
        },
        {
            "title": "Jump if Less - jl",
            "code": [
                "mov rax, 2",
                "mov rbx, 8",
                "cmp rax, rbx",
                "jl less_label",
                "mov rcx, 0",
                "less_label:",
                "mov rcx, 1"
            ],
            "explanation": "⬇️ `jl` jumps if the first is less than the second (signed). 2 < 8, so jump to `less_label`."
        },
        {
            "title": "Jump if Less or Equal - jle",
            "code": [
                "mov rax, 7",
                "mov rbx, 7",
                "cmp rax, rbx",
                "jle le_label",
                "mov rcx, 0",
                "le_label:",
                "mov rcx, 1"
            ],
            "explanation": "📉 `jle` jumps when values are equal or first is less. Since they are equal, jump happens."
        }
    ]

    for ex in examples:
        slow_print(f"\n{BOLD}{ex['title']}{RESET}", 0.02)
        for line in ex["code"]:
            slow_print(f"  {CYAN}{line}{RESET}", 0.01)
        slow_print(f"{MAGENTA}{ex['explanation']}{RESET}", 0.02)
        time.sleep(0.8)

    slow_print(f"\n{GREEN}🏁 That's a wrap on conditional jumps! Understanding how the CPU makes decisions is key to mastering low-level programming.{RESET}", 0.02)
    slow_print(f"{BOLD}Keep practicing, and try changing values to see how different flags affect program flow! 🧠💡{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")