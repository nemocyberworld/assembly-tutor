# lessons/practice_programs/hook_function.py

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
    print(f"\n{BOLD}🪝 hook_function: Hook and Replace a Function at Runtime!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to intercept a function call and reroute it to another function by modifying the call target.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Define an original function and a replacement function.",
        "2️⃣  Replace the *address* of the original with the replacement (in a jump table or pointer).",
        "3️⃣  Jump to the replacement at runtime instead of the original.",
        "4️⃣  (Optional) Restore the original function to 'unhook' it."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Imagine rerouting a phone call: you dial Alice, but the system secretly forwards the call to Bob instead!\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Function Pointer Hooking Simulation{RESET}")
    slow_print(f"""{DIM}
section .data
    func_ptr dq original      ; pointer to the function to call

section .text
global _start

_start:
    ; Hook: point to replacement instead of original
    mov     qword [func_ptr], replacement

    ; Call the function via pointer
    call    [func_ptr]

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall

original:
    ; Original function
    mov     rdi, 1            ; Let's say it prints 1 (or returns 1)
    jmp     done

replacement:
    ; Replacement function
    mov     rdi, 99           ; Hooked! This returns 99 instead
    jmp     done

done:
    ; Use rdi however you want
    ret
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create a small program that swaps out one function pointer for another, and confirm it's calling the new function!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Use `dq` to store a function address, and `call [func_ptr]` to call via pointer.")
    slow_print("→ You can simulate C-like function pointers using memory.")
    slow_print("→ Try printing a value or setting a register to verify the hook worked.")

    # Bonus
    slow_print(f"\n{BOLD}🎁 Bonus Challenge:{RESET}")
    slow_print("→ Restore the original function after a few calls (like toggling the hook).")
    slow_print("→ Use a jump patch (`jmp replacement`) if you want to hook inline code!")

    # Wrap-up
    print(f"\n{BOLD}{GREEN}🪄 You now know how to hijack a function and reroute control — powerful stuff for systems hackers and debugger ninjas!{RESET}")
