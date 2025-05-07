# lessons/practice_programs/loop_sum.py

import time

# ANSI colors
C = {
    "CYAN": "\033[96m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "MAGENTA": "\033[95m",
    "BLUE": "\033[94m",
    "DIM": "\033[2m",
    "BOLD": "\033[1m",
    "RESET": "\033[0m",
}

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{C['BOLD']}➕ Lesson: Sum Numbers from 1 to N Using a Loop{C['RESET']}\n")
    time.sleep(0.5)

    slow_print(f"{C['CYAN']}🎯 Goal:{C['RESET']} Use a loop in x86-64 assembly to add numbers from 1 to N.\n")

    slow_print(f"{C['BLUE']}📘 Why This Is Awesome:{C['RESET']}")
    slow_print("  • Learn how to use loops to accumulate values.")
    slow_print("  • Understand registers like counters and accumulators.")
    slow_print("  • Practice control flow and arithmetic at the same time.\n")

    slow_print(f"{C['YELLOW']}🔧 Instructions:{C['RESET']}")
    steps = [
        "1️⃣  Set N (the number you're summing to, e.g., 10).",
        "2️⃣  Initialize an accumulator register (like `rax`) to 0.",
        "3️⃣  Use a loop counter register (like `rbx`) starting at 1.",
        "4️⃣  In the loop, add `rbx` to `rax`, then increment `rbx`.",
        "5️⃣  Continue until `rbx` > N.",
    ]
    for step in steps:
        slow_print(f"{C['MAGENTA']}{step}{C['RESET']}")
        time.sleep(0.3)

    slow_print(f"\n{C['BOLD']}🧠 Example Code: Sum from 1 to 10{C['RESET']}")
    print(f"""{C['DIM']}
section .text
global _start

_start:
    mov     rcx, 10         ; N = 10
    xor     rax, rax        ; sum = 0
    mov     rbx, 1          ; counter = 1

sum_loop:
    add     rax, rbx        ; sum += counter
    inc     rbx             ; counter++
    cmp     rbx, rcx
    jle     sum_loop        ; loop while counter <= N

    ; rax now holds the sum of 1 to 10 (55)

    ; exit
    mov     rdi, 0
    mov     rax, 60
    syscall
{C['RESET']}""")

    slow_print(f"\n{C['GREEN']}🎯 Your Task:{C['RESET']} Modify `rcx` to try different values of N. Observe how `rax` holds the final sum!")

    slow_print(f"\n{C['BLUE']}💡 Tips:{C['RESET']}")
    slow_print("  - Use `add` for accumulation.")
    slow_print("  - `rcx` is a good general-purpose counter.")
    slow_print("  - Be careful: if N is too big, registers might overflow!")

    slow_print(f"\n{C['BOLD']}🚀 Bonus Challenges:{C['RESET']}")
    slow_print("  - Try summing even numbers only (hint: increment by 2).")
    slow_print("  - Use the formula `N*(N+1)/2` and compare it with your loop result.")
    slow_print("  - Modify to sum numbers in reverse from N down to 1.\n")

    slow_print(f"{C['CYAN']}🏁 Loops are the heartbeat of programs — make them count (literally)! 💓{C['RESET']}\n")
