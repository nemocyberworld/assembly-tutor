# lessons/practice_programs/infinite_loop.py

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
    print(f"\n{BOLD}♾️ Lesson: Create an Infinite Loop{RESET}\n")
    time.sleep(1)

    slow_print(f"{CYAN}🎯 Goal:{RESET} Write a loop in x86-64 assembly that runs forever... or until you press {BOLD}Ctrl+C{RESET}!\n")

    slow_print(f"{BLUE}🤔 Why Learn This?{RESET}")
    slow_print("Infinite loops are useful for:")
    slow_print("  • Keeping a program running (like an OS kernel)")
    slow_print("  • Polling for input")
    slow_print("  • Debugging flow control\n")

    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    instructions = [
        "1️⃣  Define a label (e.g., `start:`).",
        "2️⃣  Do something inside the loop (like `nop`, a no-op).",
        "3️⃣  Jump back to the label with `jmp`.",
        "4️⃣  (Optional) Add a print to see it in action.",
        "5️⃣  Run the code and press Ctrl+C to stop."
    ]
    for line in instructions:
        slow_print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{BOLD}🧠 Example Code:{RESET}")
    print(f"""{DIM}
section .text
global _start

_start:
loop_forever:
    nop             ; do nothing
    jmp loop_forever

    ; You'll need to press Ctrl+C to stop the program!
{RESET}""")

    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create your own infinite loop. Try replacing `nop` with your own logic (maybe a syscall or increment a counter).")

    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("  - `nop` means 'no operation'—useful when you need a placeholder.")
    slow_print("  - Infinite loops are powerful... and dangerous. Use wisely.")
    slow_print("  - Always test them in a safe environment—you'll need {BOLD}Ctrl+C{RESET} to escape!\n")

    slow_print(f"{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("  - Add a counter inside the loop and break after a certain number of iterations.")
    slow_print("  - Make it blink something (if using a simulator that supports output).")
    slow_print("  - Add a syscall inside the loop to print something repeatedly (careful—it’s fast!).\n")

    slow_print(f"{CYAN}🌀 Now you’ve built your first infinite engine. Welcome to the world of low-level control!{RESET} 🚦\n")
