# lessons/practice_programs/early_exit_loop.py

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
    print(f"\n{C['BOLD']}🏃‍♂️ Lesson: Exit a Loop Early with a Condition{C['RESET']}\n")
    time.sleep(0.5)

    slow_print(f"{C['CYAN']}🎯 Goal:{C['RESET']} Learn how to break out of a loop before it finishes using a condition.\n")

    slow_print(f"{C['BLUE']}🧠 Why This Is Important:{C['RESET']}")
    slow_print("  • Sometimes, you don’t need to finish every iteration of a loop.")
    slow_print("  • Breaking out early improves efficiency and is used in searches, error detection, etc.\n")

    slow_print(f"{C['YELLOW']}🔧 Instructions:{C['RESET']}")
    steps = [
        "1️⃣  Start a loop to count from 1 upward.",
        "2️⃣  Use a register (like `rax`) as a counter.",
        "3️⃣  Check for a specific condition (e.g., counter == 5).",
        "4️⃣  If condition is true, jump out of the loop early.",
        "5️⃣  Use `jmp` to skip the rest of the loop.",
    ]
    for step in steps:
        slow_print(f"{C['MAGENTA']}{step}{C['RESET']}")
        time.sleep(0.3)

    slow_print(f"\n{C['BOLD']}🧠 Example Code: Exit loop when counter hits 5{C['RESET']}")
    print(f"""{C['DIM']}
section .text
global _start

_start:
    xor     rax, rax        ; counter = 0

loop_start:
    inc     rax             ; counter++
    cmp     rax, 5
    je      loop_exit       ; if rax == 5, jump out

    ; Do something here (e.g., print, work, etc.)
    jmp     loop_start      ; repeat loop

loop_exit:
    ; Done looping early!

    ; exit
    mov     rdi, 0
    mov     rax, 60
    syscall
{C['RESET']}""")

    slow_print(f"\n{C['GREEN']}🎯 Your Task:{C['RESET']} Modify the condition to exit at different values. What happens if you exit at 3? Or 8?")

    slow_print(f"\n{C['BLUE']}💡 Tips:{C['RESET']}")
    slow_print("  - `je` (jump if equal) is perfect for break-style exits.")
    slow_print("  - You can also use `jne`, `jl`, `jg`, etc. to customize when you exit.")
    slow_print("  - Think of `loop_exit:` as your escape hatch!\n")

    slow_print(f"{C['BOLD']}🚀 Bonus Challenges:{C['RESET']}")
    slow_print("  - Exit when a number is divisible by 7 (use `test` or `div`).")
    slow_print("  - Count down instead of up and break early when counter hits 1.")
    slow_print("  - Combine with a sum loop and exit early if the total exceeds a threshold.\n")

    slow_print(f"{C['CYAN']}🔚 Know when to quit — your loops should too!{C['RESET']}\n")
