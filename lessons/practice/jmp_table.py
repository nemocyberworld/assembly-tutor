
# lessons/practice_programs/jmp_table.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🚦 jmp_table: Use a Jump Table for Function Dispatch!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to use a jump table to select and run code based on an index or input.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define multiple labels (functions) to jump to.",
        "2️⃣  Create a table of label *addresses* using `dq label`.",
        "3️⃣  Load the index into a register (like `rax`) and use it to access the correct label.",
        "4️⃣  Use `jmp [table + rax * 8]` to jump based on the index!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine a menu of mini-programs: press button 1 to launch A, button 2 to launch B. A jump table is your menu selector!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: A Jump Table with 3 Handlers{RESET}")
    slow_print(f"""{DIM}
section .data
    table dq handler_0, handler_1, handler_2   ; jump table with 3 entries

section .text
global _start

_start:
    mov     rax, 1              ; choose function 1 (handler_1)
    jmp     [table + rax*8]     ; jump to the function

handler_0:
    ; Code for option 0
    mov     rdi, 0
    jmp     exit

handler_1:
    ; Code for option 1
    mov     rdi, 1
    jmp     exit

handler_2:
    ; Code for option 2
    mov     rdi, 2
    jmp     exit

exit:
    mov     rax, 60             ; syscall: exit
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create a jump table that can select between 4 different 'mini functions' and execute one based on an index!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Make sure your jump table is aligned and the index is in bounds.")
    slow_print("→ Multiply index by 8 (because 64-bit addresses are 8 bytes each).")
    slow_print("→ You can use `mov rax, <index>` to simulate a user choice.")

    # Bonus
    slow_print(f"\n{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Read the index from memory or input instead of hardcoding it.")
    slow_print("→ Try nesting a jump table inside a function for advanced dispatching!")

    # Wrap-up
    print(f"\n{BOLD}{GREEN}✅ You just built a mini dispatcher! Jump tables make your assembly code fast and organized — like magic menus! ✨{RESET}")
