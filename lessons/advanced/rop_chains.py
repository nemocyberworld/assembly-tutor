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
    print(f"\n{BOLD}🧩 Return-Oriented Programming (ROP): A Primer{RESET}\n")
    time.sleep(1)

    # Intro
    slow_print(f"{YELLOW}📦 When code injection is blocked (e.g., by DEP/NX), attackers turn to Return-Oriented Programming (ROP).{RESET}")
    slow_print(f"{CYAN}ROP chains together existing snippets of code — called 'gadgets' — ending in 'ret' instructions to perform logic without injecting new code.{RESET}")
    time.sleep(1)

    # Why it works
    slow_print(f"\n{BOLD}💡 Why ROP Works:{RESET}")
    reasons = [
        "• DEP/NX marks memory as non-executable, blocking shellcode",
        "• But code already in the binary (and shared libs) is executable",
        "• ROP hijacks control flow to reuse existing code — no need to inject new code"
    ]
    for r in reasons:
        slow_print(f"{MAGENTA}{r}{RESET}")
        time.sleep(0.3)

    # Anatomy of a gadget
    slow_print(f"\n{BOLD}🧱 What Is a Gadget?{RESET}")
    slow_print(f"{GREEN}A gadget is a short instruction sequence ending in `ret`. Example:{RESET}")
    slow_print(f"""{CYAN}
  pop rdi
  ret
{RESET}""")
    slow_print(f"{YELLOW}We can use this to control the value of {BOLD}rdi{RESET}{YELLOW} by placing a value after the return address on the stack!{RESET}")
    time.sleep(1)

    # ROP stack layout
    slow_print(f"\n{BOLD}📐 Stack Layout in a ROP Chain:{RESET}")
    slow_print(f"{CYAN}Think of the stack as a script. Each `ret` jumps to the next gadget. Example chain:{RESET}")
    slow_print(f"""{MAGENTA}
  [ Address of pop rdi; ret     ]
  [ Value to place in rdi       ]
  [ Address of pop rsi; ret     ]
  [ Value to place in rsi       ]
  [ Address of syscall; ret     ]
{RESET}""")
    time.sleep(1)

    # Using it for syscalls
    slow_print(f"\n{BOLD}🔧 ROP to Invoke a Syscall (like execve){RESET}")
    slow_print(f"{YELLOW}By setting registers (rdi, rsi, rdx) and calling `syscall`, we can spawn a shell — without any injected code!{RESET}")
    slow_print(f"{CYAN}All from chaining gadgets that already exist in libc or the binary itself.{RESET}")
    time.sleep(1)

    # ROPgadget tool
    slow_print(f"\n{BOLD}🛠️ Finding Gadgets: ROPgadget Tool{RESET}")
    slow_print(f"{MAGENTA}Use tools like `ROPgadget` or `radare2` to find usable gadget addresses:{RESET}")
    slow_print(f"""{GREEN}
  ROPgadget --binary ./vuln
{RESET}""")
    slow_print(f"{CYAN}This lists all short instruction sequences ending in `ret` (or `jmp`, `call`, etc.).{RESET}")
    time.sleep(1)

    # Security context
    slow_print(f"\n{BOLD}🔐 Defenders Use ASLR and PIE to Break ROP Chains{RESET}")
    slow_print(f"{YELLOW}Randomizing addresses makes hardcoded gadgets fail — but info leaks can defeat this!{RESET}")
    slow_print(f"{RED}ASLR isn't perfect. ROP still works with the right leaks.{RESET}")
    time.sleep(1)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ ROP allows logic reuse without injecting code",
        "✔ Gadgets are tiny instruction sequences ending in ret",
        "✔ Stack becomes the instruction flow — one ret at a time",
        "✔ Tools like ROPgadget help automate chain creation",
        "✔ Defenses like ASLR, PIE, and stack canaries complicate ROP"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Use ROP to spawn `/bin/sh` by chaining gadgets from libc. Can you build the right chain with `pop rdi`, `pop rsi`, and `syscall`?{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to generate a live ROP chain using an actual ELF binary next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")