# lessons/practice_programs/nested_loops.py

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
    print(f"\n{BOLD}🧩 Lesson: Use Nested Loops for Matrix Traversal{RESET}\n")
    time.sleep(0.5)

    slow_print(f"{CYAN}🎯 Goal:{RESET} Learn to simulate a 2D loop (like rows and columns) using nested loops in x86-64 assembly.\n")

    slow_print(f"{BLUE}🤔 Why This Matters:{RESET}")
    slow_print("  • It's essential for handling grids, matrices, and 2D arrays.")
    slow_print("  • Nested loops teach you the structure of structured repetition.")
    slow_print("  • It's how we traverse maps, game boards, pixel data, etc.\n")

    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use `rdi` as your outer loop counter (e.g. row).",
        "2️⃣  Use `rsi` as your inner loop counter (e.g. column).",
        "3️⃣  Use labels for each loop, decrement counters, and use `cmp` + `jne` to loop.",
        "4️⃣  (Optional) Print or modify a value for each [row][col] pair."
    ]
    for line in steps:
        slow_print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{BOLD}🧠 Example Code: Traverse a 3x3 Grid{RESET}")
    print(f"""{DIM}
section .text
global _start

_start:
    mov     rdi, 3              ; rows

outer_loop:
    mov     rsi, 3              ; columns (reset each row)

inner_loop:
    ; Simulate work: like accessing [rdi][rsi]
    nop                         ; replace with real logic
    dec     rsi
    cmp     rsi, 0
    jne     inner_loop          ; continue inner loop

    dec     rdi
    cmp     rdi, 0
    jne     outer_loop          ; continue outer loop

    ; Exit
    mov     rax, 60             ; syscall: exit
    xor     rdi, rdi
    syscall
{RESET}""")

    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Adjust the loop to simulate a 5x4 grid. Try printing the coordinates or updating a value for each cell!")

    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("  - Always reset the inner loop counter inside the outer loop.")
    slow_print("  - Use comments to simulate cell access: like accessing [rdi][rsi].")
    slow_print("  - Add a delay (if using a simulator) to see the loop visually.\n")

    slow_print(f"{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("  - Count the total number of loop iterations (cells).")
    slow_print("  - Create a pattern (like diagonal only) by checking if rdi == rsi.")
    slow_print("  - Store values into memory based on [row][col] position (advanced).\n")

    slow_print(f"{CYAN}🌀 Nested loops are the secret to simulating 2D magic in assembly. Dive deep and get looping!{RESET} 💻✨\n")
