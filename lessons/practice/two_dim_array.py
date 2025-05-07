# lessons/practice_programs/two_dim_array.py

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
    print(f"\n{BOLD}🧮 Access Elements in a 2D Array (Matrix)!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to access individual elements in a 2D array (matrix) using pointer math in Assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define a 2D array in the `.data` section (flattened into 1D).",
        "2️⃣  Know the number of columns — this is key!",
        "3️⃣  Use: `[base + (row * columns + col) * element_size]` to get the address.",
        "4️⃣  Access or modify the value at that computed address."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of a big egg carton 🥚 — each row has a fixed number of columns. To reach a specific egg, you count rows and columns to find its position in the 1D layout.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Access element at row 1, column 2 of a 3x3 matrix{RESET}")
    slow_print(f"""{DIM}
section .data
    matrix  dq 1, 2, 3,    ; row 0
            dq 4, 5, 6,    ; row 1
            dq 7, 8, 9     ; row 2

    cols    equ 3          ; number of columns in each row

section .bss
    result  resq 1         ; space to store accessed element

section .text
global _start

_start:
    lea     rsi, [matrix]          ; base address of matrix
    mov     rbx, 1                 ; row index (1)
    mov     rcx, 2                 ; column index (2)
    mov     rdx, cols              ; number of columns

    ; Calculate index = row * cols + col
    imul    rbx, rdx               ; rbx = rbx * cols
    add     rbx, rcx               ; rbx = rbx + col

    ; Load the element at that index (each element is 8 bytes)
    mov     rax, [rsi + rbx*8]     ; get matrix[row][col]
    mov     [result], rax          ; store it

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Access an element at a specific row and column in a 2D array. Try different positions!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Remember: row-major layout means rows are stored one after another.")
    slow_print("→ Element index = (row * num_cols + col). Multiply by 8 for 64-bit values.")
    slow_print("→ `lea` gets the base address, then pointer math does the rest.")
    slow_print("→ Start simple: 2x2 or 3x3 matrices are great for practice.\n")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try modifying a specific matrix element (e.g., set matrix[2][1] = 42).")
    slow_print("→ Loop through all elements and sum them.")
    slow_print("→ Try writing a tiny print routine to show each row one-by-one!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Awesome! You now understand how matrices live in memory and how to slice right into them with math. This is real Assembly power! 💥📐{RESET}")
