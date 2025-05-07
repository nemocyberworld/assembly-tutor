# lessons/practice_programs/count_loop.py

import time

# ANSI Colors
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
    print(f"\n{BOLD}🔁 Lesson: Count from 1 to 10 Using a Loop{RESET}\n")
    time.sleep(1)

    slow_print(f"{CYAN}🎯 Goal:{RESET} Create a simple loop in x86-64 assembly to count numbers from 1 to 10.\n")
    time.sleep(0.5)

    slow_print(f"{BLUE}🧠 Why This Matters:{RESET}")
    slow_print("Loops are the heartbeat of programming! From counting to repeating actions — they're everywhere.")
    slow_print("In assembly, we build loops using labels, `inc` or `add`, and `cmp` + conditional jumps.\n")

    slow_print(f"{YELLOW}📘 Instructions:{RESET}")
    steps = [
        "1️⃣  Set a counter register (e.g., `rcx`) to 1.",
        "2️⃣  Create a label to mark the start of the loop.",
        "3️⃣  Use `cmp` to compare the counter with 10.",
        "4️⃣  Jump out of the loop if the count is done.",
        "5️⃣  Otherwise, increment the counter and jump back.",
        "6️⃣  (Optional) Print the counter to see the numbers!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{BOLD}🧠 Example Code:{RESET}")
    print(f"""{DIM}
section .text
global _start

_start:
    mov     rcx, 1          ; counter = 1

loop_start:
    cmp     rcx, 11         ; stop at 11 (means we printed 1 to 10)
    jge     end_loop        ; if rcx >= 11, exit

    ; 👇 Here you would normally print rcx (skip for now)
    ; For fun: pretend we're printing rcx here!

    inc     rcx             ; rcx = rcx + 1
    jmp     loop_start      ; repeat the loop

end_loop:
    mov     rax, 60         ; syscall: exit
    xor     rdi, rdi
    syscall
{RESET}""")

    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Implement the loop above and add a syscall-based print if you're feeling adventurous!")

    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("  - `inc rcx` is shorthand for `add rcx, 1`.")
    slow_print("  - Use `cmp rcx, 11` to stop **after** 10.")
    slow_print("  - You can also count *downward* using `dec` instead of `inc`.\n")

    slow_print(f"{BOLD}📦 Bonus Challenge:{RESET}")
    slow_print("  - Try counting backward from 10 to 1!")
    slow_print("  - Print only even numbers by skipping odd ones.")
    slow_print("  - Try using `add rcx, 2` to count 2, 4, 6...")

    slow_print(f"\n{CYAN}🎉 You've just created your first real loop in assembly. You're literally building your own CPU brain one line at a time!{RESET}\n")
