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
    print(f"\n{BOLD}🧬 Self-Modifying Code in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}💥 Self-modifying code (SMC) changes its own instructions at runtime — yes, code that rewrites itself!{RESET}")
    slow_print(f"{CYAN}It’s rare and dangerous, but also powerful in specific use cases like obfuscation or optimizing hot paths.{RESET}")
    time.sleep(1)

    # Common Use Cases
    slow_print(f"\n{BOLD}🎯 Common Use Cases for SMC:{RESET}")
    use_cases = [
        "✔ Obfuscation and anti-debugging in malware",
        "✔ Optimizing tight loops based on runtime data",
        "✔ Implementing polymorphic code or JIT compilers",
        "✔ Crafting retro-style demos or puzzles"
    ]
    for case in use_cases:
        slow_print(f"{MAGENTA}{case}{RESET}")
        time.sleep(0.3)

    # High-level idea
    slow_print(f"\n{BOLD}📦 How It Works:{RESET}")
    slow_print(f"{CYAN}At runtime, you overwrite bytes in your code section (or a copied region) with new instructions, then jump to them.{RESET}")
    time.sleep(1)

    # Python Simulation
    slow_print(f"\n{BOLD}🧪 Simulating Self-Modifying Code in Python:{RESET}")
    code_state = "A"

    def execute():
        if code_state == "A":
            slow_print(f"{GREEN}→ Current logic: Printing 'Phase A'{RESET}")
        elif code_state == "B":
            slow_print(f"{CYAN}→ Code modified! Now printing 'Phase B'{RESET}")

    slow_print(f"\n{BOLD}🚀 Run 1:{RESET}")
    execute()
    time.sleep(0.5)

    slow_print(f"\n{RED}✏️ Modifying 'code'...{RESET}")
    code_state = "B"
    time.sleep(1)

    slow_print(f"\n{BOLD}🚀 Run 2:{RESET}")
    execute()
    time.sleep(1)

    # Assembly Example
    slow_print(f"\n{BOLD}🧠 x86-64 Assembly Example (Concept):{RESET}")
    slow_print(f"""{MAGENTA}
section .text
global _start

_start:
    mov byte [code], 0x90     ; overwrite instruction with NOP
    jmp code

code:
    db 0xCC                   ; originally an INT3 (breakpoint)
{RESET}""")
    time.sleep(1)

    # Caveats
    slow_print(f"\n{BOLD}⚠️ Real-World Challenges:{RESET}")
    warnings = [
        "✘ Modern CPUs use instruction caching — changes might not be seen immediately",
        "✘ Most OSes mark code pages as read-only/executable (W^X)",
        "✔ You may need mprotect() to make memory writable",
        "✘ Debuggers may misinterpret self-modifying flows"
    ]
    for w in warnings:
        slow_print(f"{RED if '✘' in w else GREEN}{w}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Self-modifying code rewrites itself at runtime",
        "✔ It’s mostly used in obfuscation, performance hacks, or demos",
        "✔ Needs writable + executable memory to work",
        "✔ Can cause trouble with caches, debuggers, and AV tools"
    ]
    for item in summary:
        slow_print(f"{GREEN}{item}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write assembly that toggles between two versions of a loop by overwriting its own instructions! Bonus: make it switch every N runs.{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to try this in NASM or simulate SMC in shellcode?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")