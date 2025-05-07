# lessons/practice_programs/wait_child.py

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
    print(f"\n{BOLD}👶👨‍👦 Fork a Child Process and Wait for It!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to use `fork` to create a child process and `waitpid` to wait until it completes.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use `fork` syscall to create a new child process.",
        "2️⃣  In the child (pid = 0), do something simple (like exit).",
        "3️⃣  In the parent, use `waitpid` to wait for the child to finish.",
        "4️⃣  Exit cleanly after the wait completes!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of a parent sending their child off to do a chore. The parent waits until the child returns before moving on.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Fork & Wait{RESET}")
    slow_print(f"""{DIM}
section .bss
    status  resq 1     ; storage for child's exit status

section .text
    global _start

_start:
    mov     rax, 57    ; syscall: fork
    syscall

    cmp     rax, 0
    je      child_code     ; if rax == 0, we're in child
    jg      parent_code    ; if rax > 0, we're in parent

    ; if rax < 0, fork failed
    mov     rax, 60
    mov     rdi, 1      ; error code
    syscall

child_code:
    ; Child just exits
    mov     rax, 60     ; syscall: exit
    xor     rdi, rdi    ; status = 0
    syscall

parent_code:
    ; Parent waits for child
    mov     rdi, -1     ; wait for any child
    lea     rsi, [rel status] ; pointer to status
    xor     rdx, rdx    ; options = 0
    mov     rax, 61     ; syscall: waitpid
    syscall

    ; Done waiting! Exit.
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Fork a child, have it print a message using `write`, then wait for it in the parent!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ `fork` returns 0 in the child, and child's PID in the parent.")
    slow_print("→ Use `.bss` to store the child's status result from `waitpid`.")
    slow_print("→ Always clean up with `exit` after you're done!")

    # Bonus
    slow_print(f"{BOLD}🌟 Bonus Challenge:{RESET}")
    slow_print("→ Try forking *multiple* children and wait for all of them.")
    slow_print("→ Print which process is running: parent or child!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Amazing! You've just built the basic logic behind how shells manage programs. Fork + wait = process parenting mastery! 👑{RESET}")
