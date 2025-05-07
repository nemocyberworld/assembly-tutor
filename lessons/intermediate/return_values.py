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
    print(f"\n{BOLD}🔙 Returning Values from Functions (System V ABI){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}💡 When a function finishes in x86-64 Assembly, it can return a value to the caller using the {BOLD}rax{RESET}{YELLOW} register.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}Just place the return value in {BOLD}rax{RESET}{CYAN} before you use {BOLD}ret{RESET}{CYAN}, and the caller will receive it.{RESET}")
    time.sleep(1)

    # Show return convention
    slow_print(f"\n{BOLD}📌 Return Value Convention:{RESET}")
    slow_print(f"  {BOLD}rax{RESET} – Holds the return value (up to 64 bits)")
    time.sleep(1)

    slow_print(f"{MAGENTA}Functions returning integers, pointers, or even simple structs use this approach.{RESET}")
    time.sleep(1)

    # Example
    slow_print(f"\n{BOLD}💡 Example: A function that returns the constant 42{RESET}")
    code = [
        "my_func:",
        "    mov rax, 42     ; put return value in rax",
        "    ret             ; return to caller"
    ]
    for line in code:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.6)

    slow_print(f"{CYAN}The caller can now access the result via {BOLD}rax{RESET}.{RESET}")
    time.sleep(1)

    # Simulate a call and return
    slow_print(f"\n{CYAN}🔧 Simulating call to my_func...{RESET}")
    rax = 42
    slow_print(f"  {BOLD}Returned value in rax:{RESET} {rax}")
    time.sleep(1)

    # Return expression
    slow_print(f"\n{BOLD}💡 Example: Return the result of a computation{RESET}")
    example2 = [
        "    mov rdi, 7      ; argument",
        "    call square     ; call function",
        "    ; rax now holds result",
        "",
        "square:",
        "    imul rdi, rdi   ; rdi = rdi * rdi",
        "    mov rax, rdi    ; return rdi in rax",
        "    ret"
    ]
    for line in example2:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.5)

    slow_print(f"{MAGENTA}Here, the result of squaring rdi is returned to the caller in rax!{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Return values go in {BOLD}rax{RESET}{GREEN} by the callee before using {BOLD}ret{RESET}{GREEN}.{RESET}")
    slow_print(f"{GREEN}✔ The caller reads the result from {BOLD}rax{RESET}{GREEN} after the call returns.{RESET}")
    slow_print(f"{GREEN}✔ This is part of the System V AMD64 calling convention on Linux.{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Next up: We'll chain multiple function calls and pass both arguments and return values!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")