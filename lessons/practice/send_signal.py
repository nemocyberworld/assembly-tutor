# lessons/practice_programs/send_signal.py

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
    print(f"\n{BOLD}📡 Send a Signal to a Process using `kill`!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Use the `kill` syscall to send a signal (like `SIGTERM`) to another process.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Get the PID (process ID) of the target process (manually or using `ps`).",
        "2️⃣  Use the `kill` syscall (rax = 62) with the target PID.",
        "3️⃣  Choose your signal (e.g., 15 = SIGTERM, 9 = SIGKILL).",
        "4️⃣  Exit cleanly after sending the signal.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine sending a message to another program — like a tap on the shoulder — saying “Hey! Time to go!” or “Stop right now!” 👋\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Send SIGTERM to a Process with PID 12345{RESET}")
    slow_print(f"""{DIM}
section .text
    global _start

_start:
    mov     rdi, 12345     ; PID of the target process
    mov     rsi, 15        ; SIGTERM (15)
    mov     rax, 62        ; syscall: kill
    syscall

    ; Exit normally
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Replace `12345` with a real process ID and try sending `SIGKILL` (signal 9) instead. Watch it disappear! 💀\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `ps aux | grep your_program` to find a target PID.")
    slow_print("→ Signal 9 (SIGKILL) forcefully ends a process.")
    slow_print("→ Signal 15 (SIGTERM) asks it nicely to exit.")

    # Bonus
    slow_print(f"{BOLD}🌟 Bonus Challenge:{RESET}")
    slow_print("→ Try sending signal 0 — it doesn't kill, but checks if the process exists!")
    slow_print("→ Write a child process that ignores SIGTERM, then try SIGKILL!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Great job! Sending signals is how Unix processes communicate and manage behavior. Now you’re sending orders like a pro! 🧠📨{RESET}")
