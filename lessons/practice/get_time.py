# lessons/practice_programs/get_time.py

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
    print(f"\n{BOLD}⏰ Get the Current Time in Assembly!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to use Linux system calls to get the current time in seconds or nanoseconds.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use the `time` syscall (number 201) to get current time in seconds.",
        "2️⃣  OR use `clock_gettime` (number 228) for more precise time (nanoseconds).",
        "3️⃣  Store the result in memory, then optionally print it!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine calling a clock service that tells you the time right now. That’s what `time` and `clock_gettime` do!\n")

    # Example (Using `clock_gettime`)
    slow_print(f"{BOLD}🧠 Example: Get Time Using `clock_gettime` (Real-Time Clock){RESET}")
    slow_print(f"""{DIM}
section .data
    timespec  times 2 dq 0         ; reserve 16 bytes: [seconds, nanoseconds]

section .text
    global _start

_start:
    mov     rax, 228               ; syscall: clock_gettime
    mov     rdi, 0                 ; CLOCK_REALTIME = 0
    mov     rsi, timespec          ; pointer to timespec struct
    syscall

    ; now [timespec] contains seconds
    ; and [timespec + 8] contains nanoseconds

    ; exit(0)
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Use `clock_gettime` to get the current time and inspect both the seconds and nanoseconds parts in memory.\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `dq 0` to reserve 64-bit space for each part of the time.")
    slow_print("→ CLOCK_REALTIME (0) gives you wall-clock time.")
    slow_print("→ You can print the results using `sys_write` or inspect them in a debugger!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Measure the time it takes to run some code by calling `clock_gettime` before and after.")
    slow_print("→ Try `CLOCK_MONOTONIC` (1) for measuring durations unaffected by system clock changes.")
    slow_print("→ Try using the simpler `time` syscall (rax = 201, rdi = NULL or memory pointer).")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome! Now you can talk to the system clock and measure time like a pro. Stopwatch programs, here you come! ⏱️🚀{RESET}")
