# lessons/practice_programs/reverse_loop.py

import time

# ANSI color codes
C = {
    "BOLD": "\033[1m",
    "CYAN": "\033[96m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "DIM": "\033[2m",
    "RESET": "\033[0m",
}

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{C['BOLD']}⏬ Lesson: Count Down in Reverse Using a Loop{C['RESET']}\n")
    time.sleep(0.5)

    slow_print(f"{C['CYAN']}🎯 Goal:{C['RESET']} Learn how to use a loop to count down from a number to zero in x86-64 Assembly.\n")

    slow_print(f"{C['BLUE']}🧠 Why It’s Cool:{C['RESET']}")
    slow_print("  • Reverse loops are great for timers, countdowns, and logic that needs a limit.")
    slow_print("  • You'll reinforce loop logic and learn how to decrement and break at the right time!\n")

    slow_print(f"{C['YELLOW']}🔧 Instructions:{C['RESET']}")
    steps = [
        "1️⃣  Set a starting number (like 10) in a register.",
        "2️⃣  Create a loop label.",
        "3️⃣  Print or track the value.",
        "4️⃣  Decrement the value with `dec`.",
        "5️⃣  Jump back to the loop label if the value isn’t zero yet.",
    ]
    for step in steps:
        slow_print(f"{C['MAGENTA']}{step}{C['RESET']}")
        time.sleep(0.3)

    slow_print(f"\n{C['BOLD']}📜 Example: Countdown from 10 to 1{C['RESET']}")
    print(f"""{C['DIM']}
section .text
global _start

_start:
    mov     rcx, 10        ; Start counting from 10

.loop_start:
    ; Optional: print the value here
    ; (You'll need a print syscall or custom routine)

    dec     rcx            ; Decrease by 1
    cmp     rcx, 0
    jne     .loop_start    ; Keep looping until rcx == 0

    ; Done!
    mov     rax, 60
    xor     rdi, rdi
    syscall
{C['RESET']}""")

    slow_print(f"\n{C['GREEN']}🎯 Your Task:{C['RESET']} Make the loop count down from 15 instead. Try printing the value at each step!")

    slow_print(f"\n{C['BLUE']}💡 Tips:{C['RESET']}")
    slow_print("  - `dec` is just like `sub rcx, 1` but shorter.")
    slow_print("  - Use `cmp` to compare your loop counter to zero.")
    slow_print("  - Use `jne` (Jump if Not Equal) to loop back.\n")

    slow_print(f"{C['BOLD']}🚀 Bonus Challenges:{C['RESET']}")
    slow_print("  - Count down by 2s (use `sub rcx, 2`).")
    slow_print("  - Stop the loop early if the number hits 5.")
    slow_print("  - Use a register like `rsi` to store and update the countdown value.\n")

    slow_print(f"{C['CYAN']}💥 Reverse looping is powerful! You just built your own countdown logic in Assembly. Nice!{C['RESET']}\n")
