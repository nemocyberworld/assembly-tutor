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
    print(f"\n{BOLD}🐚 Writing a `/bin/sh` Shell Spawner in Assembly (x86-64){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🔓 Spawning a shell is a classic shellcode goal — it gives the attacker command execution capabilities!{RESET}")
    slow_print(f"{CYAN}We’ll do it using the `execve` syscall to run `/bin/sh` directly from assembly.{RESET}")
    time.sleep(1)

    # Intro to execve
    slow_print(f"\n{BOLD}📘 Syscall: execve(path, argv, envp){RESET}")
    slow_print(f"{GREEN}In x86-64 Linux, registers for `execve` are:{RESET}")
    execve_regs = [
        "• rax = 59     (syscall number)",
        "• rdi = pointer to \"/bin/sh\"",
        "• rsi = pointer to argv array (NULL-terminated)",
        "• rdx = pointer to envp array (NULL or NULL-terminated)"
    ]
    for reg in execve_regs:
        slow_print(f"{MAGENTA}{reg}{RESET}")
        time.sleep(0.3)

    # Code walk-through
    slow_print(f"\n{BOLD}💡 Example: execve(\"/bin/sh\", NULL, NULL){RESET}")
    code = [
        "global _start",
        "section .text",
        "_start:",
        "  xor rsi, rsi              ; argv = NULL",
        "  xor rdx, rdx              ; envp = NULL",
        "  mov rax, 59               ; syscall number for execve",
        "  lea rdi, [rel binsh]      ; pointer to \"/bin/sh\"",
        "  syscall",
        "",
        "section .data",
        "binsh: db \"/bin/sh\", 0"
    ]
    for line in code:
        slow_print(f"{CYAN}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{GREEN}✅ This will invoke a shell if executed properly — no arguments or environment needed.{RESET}")
    time.sleep(1)

    # Shellcode version
    slow_print(f"\n{BOLD}🔬 Minimal Shellcode (no NULL bytes){RESET}")
    shellcode = [
        "\\x48\\x31\\xf6",            # xor    rsi, rsi
        "\\x48\\x31\\xd2",            # xor    rdx, rdx
        "\\x48\\xbb\\2f\\62\\69\\6e\\2f\\73\\68\\00",  # mov rbx, '/bin/sh\\0'
        "\\x53",                      # push   rbx
        "\\x48\\x89\\e7",             # mov    rdi, rsp
        "\\xb0\\x3b",                 # mov    al, 59
        "\\x0f\\x05"                  # syscall
    ]
    for byte in shellcode:
        slow_print(f"{MAGENTA}{byte}{RESET}")
        time.sleep(0.2)

    slow_print(f"\n{CYAN}🚀 This version builds the `/bin/sh` string on the stack to avoid the `.data` section entirely — more compact and injection-friendly!{RESET}")
    time.sleep(1)

    # Summary
    slow_print(f"\n{YELLOW}📌 Summary:{RESET}")
    summary = [
        "✔ Use syscall 59 (execve) with /bin/sh",
        "✔ Avoid null bytes to make shellcode injection-safe",
        "✔ Push /bin/sh onto the stack, point rdi to it",
        "✔ Leave rsi and rdx as NULL for no args/env"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.4)

    # Safety reminder
    slow_print(f"\n{RED}⚠️ Reminder: Spawning a shell is a powerful operation. Always test in isolated environments like VMs or containers.{RESET}")
    time.sleep(1)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write 32-bit or 64-bit execve shellcode that avoids all null bytes and hardcodes a different shell path (like `/bin/bash`).{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Would you like to trace this shellcode in a debugger or convert it to hex?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
