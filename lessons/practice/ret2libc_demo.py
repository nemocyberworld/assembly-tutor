# lessons/practice_programs/ret2libc_demo.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🎯 ret2libc_demo: Craft a ret2libc Attack (For Education Only!){RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Understand how attackers can exploit buffer overflows to call libc functions (like `system`) by controlling the return address.\n")
    time.sleep(0.5)

    # ⚠️ Ethical Note
    slow_print(f"{RED}⚠️  Ethical Note:{RESET} This lesson is for defensive security education only. Never use these techniques outside of legal lab environments.\n")

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Set up a vulnerable function with a local buffer and no bounds checking.",
        "2️⃣  Overflow the buffer and overwrite the return address with the address of `system`.",
        "3️⃣  Place the address of \"/bin/sh\" in memory and use it as a parameter.",
        "4️⃣  Watch the shell spawn (if successful)!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine a sneaky detour: Instead of returning home (normal flow), you jump into a library and say: \"Hey system(), run this command for me!\"\n")

    # Example (simplified C)
    slow_print(f"{BOLD}💻 Vulnerable C Code for Context:{RESET}")
    slow_print(f"""{DIM}
void vulnerable() {{
    char buffer[64];
    gets(buffer);  // ⚠️ Vulnerable to overflow!
}}

int main() {{
    vulnerable();
    return 0;
}}
{RESET}""")

    slow_print(f"{BOLD}🧠 Exploit Idea (Pseudocode Assembly):{RESET}")
    slow_print(f"""{DIM}
[buffer] ... [padding] ... [RET] -> address of system()
                                -> return address (dummy or exit)
                                -> address of "/bin/sh"
{RESET}""")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `objdump`, `nm`, or `gdb` to find addresses of `system` and `\"/bin/sh\"`.")
    slow_print("→ Disable ASLR temporarily (on test system): `echo 0 > /proc/sys/kernel/randomize_va_space`.")
    slow_print("→ Compile with: `gcc -fno-stack-protector -z execstack -no-pie vuln.c -o vuln`.")

    # Bonus
    slow_print(f"\n{BOLD}🎁 Bonus Exploration:{RESET}")
    slow_print("→ Try using `exit` as a fake return address to prevent crashing.")
    slow_print("→ Turn ASLR back on and observe how it blocks the attack.")

    # Final Words
    print(f"\n{GREEN}{BOLD}🔐 Defensive Lesson:{RESET} Always validate inputs, use stack canaries, enable NX/ASLR, and avoid dangerous functions like `gets()`!")
    print(f"{BOLD}🎓 You've just peeked behind the curtain of low-level software exploitation — great job!{RESET}")
