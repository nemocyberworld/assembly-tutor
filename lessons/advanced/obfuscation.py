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
    print(f"\n{BOLD}🕵️ Assembly Obfuscation Techniques (x86-64){RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}🔒 Obfuscation hides the intent of code — making it harder to reverse, analyze, or detect.{RESET}")
    slow_print(f"{CYAN}In assembly, this means twisting logic, confusing disassemblers, or even rewriting runtime behavior.{RESET}")
    time.sleep(1)

    # Use Cases
    slow_print(f"\n{BOLD}🎯 Common Use Cases:{RESET}")
    use_cases = [
        "✔ Malware evasion (anti-analysis, anti-disassembly)",
        "✔ Software protection and license checks",
        "✔ Capture-the-flag (CTF) puzzles",
        "✔ Code optimization or novelty (e.g. sizecoding demos)"
    ]
    for case in use_cases:
        slow_print(f"{MAGENTA}{case}{RESET}")
        time.sleep(0.3)

    # Technique: Instruction Substitution
    slow_print(f"\n{BOLD}🔄 Technique 1: Instruction Substitution{RESET}")
    slow_print(f"{CYAN}Replace obvious instructions with equivalent — but harder to read — versions.{RESET}")
    slow_print(f"""{MAGENTA}
Instead of:
    xor rax, rax

Try:
    sub rax, rax
    or  rax, 0
    mov rax, rax
{RESET}""")
    time.sleep(1)

    # Technique: Control Flow Flattening
    slow_print(f"\n{BOLD}🧩 Technique 2: Control Flow Flattening{RESET}")
    slow_print(f"{CYAN}Break linear execution into indirect jumps and fake logic to confuse analysis.{RESET}")
    slow_print(f"""{MAGENTA}
cmp rdi, 1
jne .fake
jmp .real

.fake:
    nop
    nop
    jmp .real

.real:
    ; Real logic here
{RESET}""")
    time.sleep(1)

    # Technique: Junk Insertion
    slow_print(f"\n{BOLD}🗑️ Technique 3: Junk Instruction Insertion{RESET}")
    slow_print(f"{CYAN}Insert meaningless instructions to bloat disassembly or confuse pattern-matching tools.{RESET}")
    slow_print(f"""{MAGENTA}
add rax, 0
nop
xchg rbx, rbx
{RESET}""")
    time.sleep(1)

    # Technique: Encoded Instructions
    slow_print(f"\n{BOLD}🔐 Technique 4: Runtime Decoding (Polymorphic Code){RESET}")
    slow_print(f"{CYAN}Store instructions in an encoded format and decode them just before execution.{RESET}")
    slow_print(f"""{MAGENTA}
; Encrypted shellcode stub
decode:
    xor byte [rip+payload], 0xAA
    jmp payload

payload:
    db 0xCC  ; ← XOR’d byte (will be valid code after decode)
{RESET}""")
    time.sleep(1)

    # Obfuscation in Action
    slow_print(f"\n{BOLD}🧪 Simulated Obfuscation in Python:{RESET}")
    slow_print(f"{GREEN}→ Clear version:{RESET}")
    def clean():
        slow_print("  rax = 0")

    slow_print(f"{RED}→ Obfuscated version:{RESET}")
    def obfuscated():
        slow_print("  rax = rax")
        slow_print("  rax ^= rax")
        slow_print("  add rax, 0")

    time.sleep(0.5)
    slow_print(f"\n{BOLD}Original logic:{RESET}")
    clean()
    time.sleep(0.5)

    slow_print(f"\n{BOLD}Obfuscated logic:{RESET}")
    obfuscated()
    time.sleep(1)

    # Risks
    slow_print(f"\n{BOLD}⚠️ Considerations:{RESET}")
    risks = [
        "✘ Makes debugging and maintenance extremely hard",
        "✘ Can trigger antivirus or heuristic warnings",
        "✘ Obfuscation ≠ Security — it just slows reverse engineering",
        "✔ Great for CTFs, experimentation, or anti-analysis"
    ]
    for line in risks:
        slow_print(f"{RED if '✘' in line else GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Obfuscation hides logic through confusing, non-obvious code",
        "✔ Techniques include junk insertion, substitution, flattening, and encoding",
        "✔ Use responsibly — for protection, not permanent defense"
    ]
    for item in summary:
        slow_print(f"{GREEN}{item}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write a function that always returns 0, but hides that fact using 3+ obfuscation tricks!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to dive into polymorphic engines or anti-disassembler tricks next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")