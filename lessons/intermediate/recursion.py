import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}🔁 Recursion in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 Recursion means a function calls itself to solve smaller pieces of a problem — just like in C or Python!{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}In Assembly, recursion is possible by using the {BOLD}call{RESET}{CYAN} instruction — even from inside the same function!{RESET}")
    time.sleep(1)

    slow_print(f"{MAGENTA}But you must manually manage arguments, return values, and stack space for each call!{RESET}")
    time.sleep(1)

    # Setup: factorial example
    slow_print(f"\n{BOLD}💡 Let's implement a recursive factorial function:{RESET}")
    slow_print(f"{GREEN}factorial(n) = 1               if n <= 1")
    slow_print(f"factorial(n) = n * factorial(n-1)  otherwise{RESET}")
    time.sleep(1)

    # Registers
    slow_print(f"\n{CYAN}🔧 We'll pass n in {BOLD}rdi{RESET}, return result in {BOLD}rax{RESET}, and use {BOLD}rbx{RESET} as temp storage.{RESET}")
    time.sleep(1)

    # Code walkthrough
    slow_print(f"\n{BOLD}📜 Code Walkthrough:{RESET}")
    factorial_code = [
        "factorial:",
        "    push rbp             ; setup stack frame",
        "    mov rbp, rsp",
        "    push rbx             ; save rbx (caller-saved)",

        "    cmp rdi, 1           ; if n <= 1",
        "    jbe .base_case",

        "    mov rbx, rdi         ; save current n",
        "    dec rdi              ; n - 1",
        "    call factorial       ; recursive call",
        "    imul rax, rbx        ; rax *= saved n",
        "    jmp .done",

        ".base_case:",
        "    mov rax, 1           ; return 1",

        ".done:",
        "    pop rbx              ; restore rbx",
        "    pop rbp              ; restore base pointer",
        "    ret"
    ]
    for line in factorial_code:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.5)

    # Simulate behavior
    slow_print(f"\n{CYAN}📦 Let's simulate factorial(3)...{RESET}")
    time.sleep(1)
    slow_print(f"{BOLD}Call stack:{RESET}")
    slow_print("  factorial(3)")
    slow_print("    → factorial(2)")
    slow_print("        → factorial(1) → returns 1")
    slow_print("      → returns 2 * 1 = 2")
    slow_print("  → returns 3 * 2 = 6")
    time.sleep(1)

    slow_print(f"{MAGENTA}Each call pushes its own return address and arguments on the stack!{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Recursion works via repeated {BOLD}call{RESET}{GREEN} instructions and stack management{RESET}")
    slow_print(f"{GREEN}✔ Carefully save/restore registers like {BOLD}rbx{RESET}{GREEN} (callee-saved){RESET}")
    slow_print(f"{GREEN}✔ Use the stack to isolate each call's variables and return paths{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Try modifying this to compute Fibonacci recursively!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")