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
    print(f"\n{BOLD}🕵️ Anti-Debugging Tricks in Assembly (x86-64 Linux){RESET}\n")
    time.sleep(1)

    # Intro
    slow_print(f"{YELLOW}🔐 In offensive security, malware analysis, and reverse engineering, it's common to see code that resists being debugged.{RESET}")
    slow_print(f"{CYAN}These tricks aim to detect or break debuggers, making analysis harder — and sometimes causing the debugger to crash!{RESET}")
    time.sleep(1)

    # High-level categories
    slow_print(f"\n{BOLD}🧠 Categories of Anti-Debugging Techniques:{RESET}")
    categories = [
        "• Syscall-based detection",
        "• Timing-based checks",
        "• Trap flag manipulation",
        "• Signal abuse or exception tricks",
        "• Breakpoint detection (int3, 0xCC)"
    ]
    for c in categories:
        slow_print(f"{MAGENTA}{c}{RESET}")
        time.sleep(0.3)

    # Technique 1: ptrace self-detect
    slow_print(f"\n{BOLD}🔍 Technique 1: Detect ptrace{RESET}")
    slow_print(f"{CYAN}Linux uses the `ptrace` syscall for debugging. A process can try to attach to itself — if it fails, something else (a debugger) is already tracing it!{RESET}")
    slow_print(f"{GREEN}Assembly snippet (x86-64):{RESET}")
    slow_print(f"""{MAGENTA}
    mov rax, 101       ; syscall number for ptrace
    mov rdi, 0         ; PTRACE_TRACEME
    xor rsi, rsi
    xor rdx, rdx
    syscall
    test rax, rax
    jne debugger_detected
{RESET}""")
    time.sleep(1)

    # Technique 2: Check for breakpoints
    slow_print(f"\n{BOLD}🧨 Technique 2: Scan for 0xCC Breakpoints{RESET}")
    slow_print(f"{YELLOW}Debuggers insert `int3` (opcode 0xCC) to pause execution. Scan your own code for unexpected 0xCCs!{RESET}")
    slow_print(f"{CYAN}This is a classic self-check method — but can be evaded by smarter debuggers.{RESET}")
    time.sleep(1)

    # Technique 3: Trap Flag / Single Step detection
    slow_print(f"\n{BOLD}⚡ Technique 3: Trap Flag Detection{RESET}")
    slow_print(f"{MAGENTA}Setting the Trap Flag (TF) causes an interrupt after every instruction — debuggers rely on this for single-stepping.{RESET}")
    slow_print(f"{CYAN}You can clear it or detect its effects (e.g., via SIGTRAP or exception handlers).{RESET}")
    time.sleep(1)

    # Technique 4: Time delta checks
    slow_print(f"\n{BOLD}⏱️ Technique 4: Timing Attacks{RESET}")
    slow_print(f"{YELLOW}Compare expected execution time (using `rdtsc`) to actual. Stepping through instructions slows things down significantly.{RESET}")
    slow_print(f"{GREEN}✔ Fast run: likely no debugger{RESET}")
    slow_print(f"{RED}✘ Slow run: probably being traced step-by-step{RESET}")
    time.sleep(1)

    # Technique 5: Signal-based crashes
    slow_print(f"\n{BOLD}💥 Technique 5: Abuse Signals or Faults{RESET}")
    slow_print(f"{CYAN}Cause a segmentation fault or illegal instruction and catch it with a signal handler.{RESET}")
    slow_print(f"{MAGENTA}Some debuggers will intercept the signal before your handler does — or fail to resume execution properly.{RESET}")
    time.sleep(1)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Use `ptrace` to detect debuggers",
        "✔ Scan memory for 0xCC breakpoints",
        "✔ Watch for Trap Flag or SIGTRAP behavior",
        "✔ Measure execution time for delays",
        "✔ Use illegal instructions or signals to cause unexpected behavior in debuggers"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Combine `ptrace` detection with timing checks to create a stealthy anti-debug stub! Bonus: Make it exit silently when debugging is detected.{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to dive into debugger evasion techniques for shellcode or ELF binaries next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
