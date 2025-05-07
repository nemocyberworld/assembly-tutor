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
    print(f"\n{BOLD}🎯 Code Golf in Assembly: Minimizing Bytes{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}💾 In some scenarios, every byte counts — shellcode, exploits, demos, or fitting a whole program in a tweet!{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}Let's explore byte-saving tips in x86-64 assembly to write smaller code without breaking functionality.{RESET}")
    time.sleep(1)

    # Principle: Form matters
    slow_print(f"\n{BOLD}📏 Size ≠ Speed: A Smaller Instruction Isn't Always Faster{RESET}")
    slow_print(f"{MAGENTA}But in this lesson, we're optimizing for *bytes*, not performance.{RESET}")
    time.sleep(1)

    # Tip 1: Prefer short encodings
    slow_print(f"\n{BOLD}🧠 Tip 1: Prefer Short Instruction Encodings{RESET}")
    examples = [
        "✔ xor eax, eax     → 2 bytes",
        "✘ mov eax, 0       → 5 bytes",
        "✔ push 0           → 1 byte",
        "✘ mov rax, 0       → 10 bytes"
    ]
    for ex in examples:
        slow_print(f"{CYAN}{ex}{RESET}")
        time.sleep(0.3)

    # Tip 2: Use 32-bit ops to zero 64-bit regs
    slow_print(f"\n{BOLD}🪄 Tip 2: Zero with 32-bit Registers{RESET}")
    slow_print(f"{YELLOW}Setting `eax = 0` implicitly zeroes all of `rax`. Saves bytes vs. `mov rax, 0`.{RESET}")
    slow_print(f"{GREEN}✔ xor eax, eax  → same result, smaller encoding{RESET}")
    time.sleep(1)

    # Tip 3: Leverage implicit operands
    slow_print(f"\n{BOLD}⚙️ Tip 3: Use Implicit Operand Instructions{RESET}")
    tips = [
        "✔ cdq (extends eax → edx:eax) instead of mov edx, 0",
        "✔ syscall uses rax implicitly → don’t need to specify rax as dest",
        "✔ lodsb/stosb/rep → operate on al/di/si implicitly"
    ]
    for tip in tips:
        slow_print(f"{CYAN}{tip}{RESET}")
        time.sleep(0.4)

    # Tip 4: Short jumps
    slow_print(f"\n{BOLD}🏃 Tip 4: Short Jumps Are Just 2 Bytes{RESET}")
    slow_print(f"{YELLOW}Jumping within ±127 bytes? Use `jmp short` or `je short`. Saves 3–4 bytes over full jumps.{RESET}")
    time.sleep(1)

    # Tip 5: Use stack for constants
    slow_print(f"\n{BOLD}📦 Tip 5: Push Constants Instead of Moving{RESET}")
    slow_print(f"{MAGENTA}Instead of: mov rax, 0x1{RESET}")
    slow_print(f"{CYAN}Use: push 1; pop rax  → smaller encoding, same effect!{RESET}")
    time.sleep(1)

    # Advanced tricks
    slow_print(f"\n{BOLD}🎩 Bonus Tricks:{RESET}")
    tricks = [
        "• Use loop instead of dec/jnz (1-byte opcode)",
        "• Use call/pop for RIP-relative addressing",
        "• Overlap code/data when safe (self-modifying or obfuscated shellcode)",
        "• Remove unnecessary function prologues/epilogues"
    ]
    for t in tricks:
        slow_print(f"{GREEN}{t}{RESET}")
        time.sleep(0.4)

    # Tooling
    slow_print(f"\n{BOLD}🛠️ Tooling Tips:{RESET}")
    tools = [
        "🔍 Use `ndisasm` or `objdump -d` to compare byte sizes",
        "📦 Assemble with `nasm -f bin` to see raw output",
        "📐 Measure with `wc -c` or hex dumps"
    ]
    for tool in tools:
        slow_print(f"{CYAN}{tool}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Use 32-bit instructions where possible",
        "✔ Prefer implicit operands and short jumps",
        "✔ Push/pop over mov for small constants",
        "✔ Code golf rewards cleverness and creativity"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write the smallest possible shellcode that exits cleanly (using syscall exit)! Try to stay under 10 bytes!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to see real-world shellcode golf examples next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")