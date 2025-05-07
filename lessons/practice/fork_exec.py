# lessons/practice_programs/fork_exec.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🔀 Fork and Exec in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to use `fork` to create a new process, and `execve` to run another program from that child.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use the `fork` syscall to split your process into parent and child.",
        "2️⃣  In the child (where `fork` returns 0), call `execve` to run a new program.",
        "3️⃣  In the parent, wait for the child to finish using `waitpid`.",
        "4️⃣  Enjoy multitasking — just like the Linux shell does!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine you're a chef 🍳. You split into two chefs (fork), and one of them goes off to cook a new recipe (execve), while the other waits for them to finish (wait).\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Fork and exec `/bin/ls`{RESET}")
    slow_print(f"""{DIM}
section .data
    path    db "/bin/ls", 0
    arg0    db "ls", 0
    argv    dq arg0, 0
    envp    dq 0

section .text
    global _start

_start:
    ; fork the process
    mov     rax, 57         ; syscall: fork
    syscall

    cmp     rax, 0
    je      child_process   ; rax == 0 → we're in the child
    jg      parent_process  ; rax > 0 → we're in the parent

    ; if rax < 0 → fork failed (not handled here)

child_process:
    ; execve("/bin/ls", ["ls"], NULL)
    mov     rax, 59         ; syscall: execve
    mov     rdi, path       ; filename
    mov     rsi, argv       ; argv pointer
    mov     rdx, envp       ; envp pointer (NULL)
    syscall

parent_process:
    ; waitpid(-1, NULL, 0) — wait for any child
    mov     rax, 61         ; syscall: waitpid
    mov     rdi, -1         ; wait for any child
    xor     rsi, rsi        ; no status storage
    xor     rdx, rdx        ; no options
    syscall

    ; exit(0)
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Fork the process and have the child run `/bin/echo Hello from child!`.")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ `fork` returns 0 in the child, >0 in the parent (the child’s PID).")
    slow_print("→ `execve` replaces the current process image — if it succeeds, nothing after it runs.")
    slow_print("→ You'll need to set up `argv` as an array of pointers (null-terminated!).")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try forking **twice** and running two different programs (e.g., `/bin/date` and `/bin/uname`).")
    slow_print("→ Add error checking: What happens if `fork` or `execve` fails?")
    slow_print("→ Add a delay in the parent (`nanosleep` syscall) to observe timing.")

    # Wrap-up
    print(f"\n{BOLD}🏁 Amazing! You just created a multi-process program in pure assembly. This is the heart of how shells, servers, and systems work! 🧠⚙️🚀{RESET}")
