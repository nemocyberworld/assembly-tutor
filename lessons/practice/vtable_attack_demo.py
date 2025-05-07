# lessons/practice_programs/vtable_attack_demo.py

import time

# ANSI colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RED = "\033[91m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🔓 vtable_attack_demo: Simulate a Virtual Table Hijack in Assembly!{RESET}\n")
    time.sleep(1)

    # ⚠️ Educational Warning
    slow_print(f"{RED}{BOLD}⚠️  WARNING:{RESET} This demo is for educational use only.")
    slow_print(f"{RED}It shows how attackers might hijack function pointers to change program behavior.")
    slow_print("NEVER use this knowledge unethically or outside of secure environments.\n")

    # 🎯 Goal
    slow_print(f"{CYAN}🎯 Goal:{RESET} Simulate how a C++-like virtual table (vtable) might be hijacked at runtime.")
    slow_print("→ Learn how memory layouts and function pointers can be manipulated.\n")

    # 📦 Concept Overview
    slow_print(f"{YELLOW}📦 What’s a vtable?{RESET}")
    slow_print("→ In C++, virtual functions use a vtable — a table of function pointers.")
    slow_print("→ Each object stores a pointer to its vtable.")
    slow_print("→ If an attacker can overwrite that pointer… they control which code gets called!\n")

    # 🛠️ Instructions
    slow_print(f"{YELLOW}🛠️ Instructions:{RESET}")
    steps = [
        "1️⃣  Simulate a class instance in memory: an object with a pointer to a vtable.",
        "2️⃣  Create a 'safe' vtable with normal behavior.",
        "3️⃣  Create a 'malicious' vtable pointing to fake or attacker-controlled code.",
        "4️⃣  Overwrite the object’s vtable pointer to simulate the attack.",
        "5️⃣  Call the virtual method and observe the hijack in action.",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # 🧠 Assembly Concept (Pseudo)
    slow_print(f"\n{BLUE}🧠 Simulation in Assembly (Pseudo-code):{RESET}")
    slow_print(f"""{DIM}
; Set up fake vtables
safe_vtable:
    dq  safe_function

malicious_vtable:
    dq  attacker_code

object:
    dq  safe_vtable     ; pointer to vtable

; Later in code...
    mov rax, [object]    ; load vtable ptr
    call qword [rax]     ; call first method (virtual)

; Attack:
    mov [object], malicious_vtable
    mov rax, [object]
    call qword [rax]     ; BOOM! Now calling attacker's code
{RESET}""")

    # 🔐 Takeaway
    slow_print(f"\n{BLUE}🔐 Takeaway:{RESET}")
    slow_print("→ Low-level manipulation of memory shows how powerful — and dangerous — raw pointers are.")
    slow_print("→ Always validate memory boundaries and never trust user input with raw access!")

    # 🧪 Bonus Challenge
    slow_print(f"\n{BOLD}🧪 Bonus Challenge:{RESET}")
    slow_print("→ Try making a vtable with multiple function pointers.")
    slow_print("→ Simulate switching between different 'classes' at runtime.")
    slow_print("→ Add print statements (via syscall) to trace function flow.\n")

    # ✅ Wrap-up
    slow_print(f"{GREEN}{BOLD}✅ You just simulated a powerful exploit vector in a controlled way. Use this knowledge to protect, not break! 🛡️✨{RESET}")
