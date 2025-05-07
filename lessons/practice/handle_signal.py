# lessons/practice_programs/handle_signal.py

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
    print(f"\n{BOLD}⚠️ Handle a Signal Gracefully with a Custom Handler!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to catch and handle `SIGINT` (like from Ctrl+C) in your assembly program.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Set up a `sigaction` struct with a pointer to your custom handler.",
        "2️⃣  Use the `rt_sigaction` syscall (rax = 13) to install it for SIGINT (2).",
        "3️⃣  In the handler, print a message or clean up resources.",
        "4️⃣  Sit in an infinite loop and try pressing Ctrl+C!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of a signal handler like setting a trap — when someone hits Ctrl+C, your code catches it and says “Not so fast!” 🛑🐭\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Catch Ctrl+C (SIGINT) and Respond{RESET}")
    slow_print(f"""{DIM}
section .data
    sa_handler dq handler    ; address of the handler function
    sa_flags   dq 0
    sa_restorer dq 0
    sa_mask    dq 0, 0       ; 2 x 64-bit words = 128-bit sigset_t

section .text
    global _start

_start:
    ; Setup struct and install handler
    lea     rdi, [rel sigaction_struct]  ; &act
    xor     rsi, rsi                     ; SIGINT = 2
    mov     rdx, 0                       ; oldact = NULL
    mov     r10, 8                       ; size of sigset_t
    mov     rax, 13                      ; syscall: rt_sigaction
    syscall

.loop:
    jmp .loop    ; infinite loop — press Ctrl+C to trigger

handler:
    ; print message and exit
    mov     rax, 1          ; syscall: write
    mov     rdi, 1          ; stdout
    lea     rsi, [rel msg]
    mov     rdx, msg_len
    syscall

    mov     rax, 60         ; syscall: exit
    xor     rdi, rdi
    syscall

section .data
sigaction_struct:
    dq handler              ; sa_handler
    dq 0                   ; sa_flags
    dq 0                   ; sa_restorer (deprecated)
    dq 0, 0                ; sa_mask (128 bits)

msg db "Caught SIGINT! Goodbye! 👋", 10
msg_len equ $ - msg
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Try writing your own SIGINT handler that says something funny or saves data before exiting.\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ `SIGINT` is signal 2 — you handle it with syscall 13 (rt_sigaction).")
    slow_print("→ You must use a proper `sigaction` struct with the right layout.")
    slow_print("→ After setting it up, your loop just waits for the interrupt.")

    # Bonus
    slow_print(f"{BOLD}🌟 Bonus Challenge:{RESET}")
    slow_print("→ Try handling `SIGTERM` or other signals too!")
    slow_print("→ Log how many times Ctrl+C was pressed before exiting!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome! Now your programs can defend themselves from Ctrl+C! You’re mastering low-level system interaction! 💪📲{RESET}")
