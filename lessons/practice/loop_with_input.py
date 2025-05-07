# lessons/practice_programs/loop_with_input.py

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
    print(f"\n{C['BOLD']}🔁 Lesson: Loop a Given Number of Times Based on Input{C['RESET']}\n")
    time.sleep(0.5)

    slow_print(f"{C['CYAN']}🎯 Goal:{C['RESET']} Create a loop that runs a number of times specified by user input (from stdin).\n")

    slow_print(f"{C['BLUE']}🧠 Why This Matters:{C['RESET']}")
    slow_print("  • Loops based on input are dynamic — they adapt to the user's needs.")
    slow_print("  • Great for tasks where the number of iterations isn’t known in advance.\n")

    slow_print(f"{C['YELLOW']}🔧 Instructions:{C['RESET']}")
    steps = [
        "1️⃣  Read a number (N) from the user using `syscall read`.",
        "2️⃣  Convert the string input to an actual number (ASCII ➡ integer).",
        "3️⃣  Use a counter to run a loop N times.",
        "4️⃣  Print something during each loop iteration.",
    ]
    for step in steps:
        slow_print(f"{C['MAGENTA']}{step}{C['RESET']}")
        time.sleep(0.3)

    slow_print(f"\n{C['BOLD']}📜 Example: Loop N Times Based on Input{C['RESET']}")
    print(f"""{C['DIM']}
section .bss
    input   resb 10

section .text
global _start

_start:
    ; --- Read from stdin ---
    mov     rax, 0          ; syscall: read
    mov     rdi, 0          ; stdin
    mov     rsi, input      ; buffer
    mov     rdx, 10         ; max bytes
    syscall

    ; --- Convert input string to integer ---
    mov     rsi, input
    xor     rcx, rcx        ; rcx = 0 (our counter)
    xor     rbx, rbx        ; rbx = 0 (result)

.convert_loop:
    mov     al, [rsi + rcx]
    cmp     al, 10          ; newline?
    je      .done_convert
    sub     al, '0'
    imul    rbx, rbx, 10
    add     rbx, rax
    inc     rcx
    jmp     .convert_loop

.done_convert:
    ; rbx now contains N (loop count)
    xor     rax, rax        ; loop counter

.loop_start:
    cmp     rax, rbx
    je      .loop_end

    ; (You can insert work here, like printing)
    inc     rax
    jmp     .loop_start

.loop_end:
    ; exit
    mov     rdi, 0
    mov     rax, 60
    syscall
{C['RESET']}""")

    slow_print(f"\n{C['GREEN']}🎯 Your Task:{C['RESET']} Try entering different numbers and confirm the loop runs the expected number of times.")

    slow_print(f"\n{C['BLUE']}💡 Tips:{C['RESET']}")
    slow_print("  - Input from `read` is a string — convert it digit by digit.")
    slow_print("  - This is a great chance to practice ASCII manipulation.")
    slow_print("  - Don’t forget to handle newline (ASCII 10) from pressing Enter.\n")

    slow_print(f"{C['BOLD']}🚀 Bonus Challenges:{C['RESET']}")
    slow_print("  - Print the loop index during each iteration.")
    slow_print("  - Skip printing if the index is divisible by 3.")
    slow_print("  - Exit the loop early if the count goes over 5.\n")

    slow_print(f"{C['CYAN']}🎉 Awesome work! Input-driven loops = dynamic control power!{C['RESET']}\n")
