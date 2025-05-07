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
    print(f"\n{BOLD}📦 Local Variables & Stack Allocation in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 In high-level languages, local variables live on the stack. Assembly does the same — but manually!{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}We allocate space on the stack using the {BOLD}sub rsp, N{RESET}{CYAN} instruction, and free it with {BOLD}add rsp, N{RESET}.{RESET}")
    time.sleep(1)

    # Basic prologue/epilogue
    slow_print(f"\n{BOLD}📌 Function Prologue & Epilogue (Recap){RESET}")
    steps = [
        "push rbp            ; save caller's base pointer",
        "mov rbp, rsp        ; set up our base pointer",
        "sub rsp, N          ; allocate N bytes for local vars",
        "...                 ; (use local space here)",
        "add rsp, N          ; free space before return",
        "pop rbp             ; restore base pointer",
        "ret                 ; return to caller",
    ]
    for step in steps:
        slow_print(f"  {GREEN}{step}{RESET}")
        time.sleep(0.5)

    # Local variable example
    slow_print(f"\n{BOLD}💡 Example: Reserve 16 bytes for two 8-byte local variables{RESET}")
    slow_print(f"{MAGENTA}After sub rsp, 16 — the space below rsp is now ours to use!{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}We access local variables relative to {BOLD}rbp{RESET}{CYAN}, like so:{RESET}")
    slow_print(f"  [rbp - 8] → first local var")
    slow_print(f"  [rbp - 16] → second local var")
    time.sleep(1)

    # Simulate local variable behavior
    slow_print(f"\n{CYAN}🔧 Simulating local variable storage...{RESET}")
    local_vars = {
        "[rbp - 8]": 42,
        "[rbp - 16]": 99
    }
    for addr, val in local_vars.items():
        slow_print(f"  {BOLD}{addr}{RESET} = {val}")
        time.sleep(0.5)

    # Releasing memory
    slow_print(f"\n{MAGENTA}✅ We must always free the space by restoring rsp (add rsp, N) before returning!{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Local variables live in stack space below {BOLD}rsp{RESET}{GREEN}, accessed via offsets from {BOLD}rbp{RESET}{GREEN}.{RESET}")
    slow_print(f"{GREEN}✔ Use {BOLD}sub rsp, N{RESET}{GREEN} to allocate, and {BOLD}add rsp, N{RESET}{GREEN} to clean up.{RESET}")
    slow_print(f"{GREEN}✔ This is manual memory management — every byte is your responsibility!{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Next up: We'll practice using local variables inside real functions with conditionals and loops!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")