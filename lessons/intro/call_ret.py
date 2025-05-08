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
    slow_print(f"\n🧭 {BOLD}Welcome to: Function Calls — `call` and `ret`!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}📚 In Assembly, functions don’t just appear and disappear like in high-level languages.", 0.02)
    slow_print(f"{YELLOW}Instead, we manually use `call` and `ret` to manage function flow with the stack!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🧠 What do they do?{RESET}\n", 0.02)
    slow_print(f"""
  {CYAN}call <label>{RESET} → Pushes the return address on the stack and jumps to the label.
  {CYAN}ret{RESET}         → Pops the return address and jumps back to it.
    """, 0.01)
    time.sleep(1)

    slow_print(f"{GREEN}💡 Think of `call` as saying “Remember where I was, then go to this function.”", 0.02)
    slow_print(f"{GREEN}And `ret` says “I’m done — take me back to where I came from.”{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{BOLD}{CYAN}🧪 Example: A Simple Function Call{RESET}", 0.02)
    slow_print(f"Let's simulate calling a function named `greet` from the `_start` entry point.\n", 0.01)

    code_lines = [
        ("section .text", "Declare code section"),
        ("global _start", "Entry point for the program"),
        ("", ""),
        ("_start:", "Program begins here"),
        ("    call greet", "🔁 Save next address and jump to 'greet'"),
        ("    mov rax, 60", "Exit syscall number"),
        ("    xor rdi, rdi", "Return code 0"),
        ("    syscall", "Exit the program"),
        ("", ""),
        ("greet:", "Function definition starts here"),
        ("    mov rdi, message", "Set up argument to print"),
        ("    call print", "Call another function"),
        ("    ret", "🔚 Return to the instruction after 'call greet'"),
        ("", ""),
        ("print:", "Fake print function"),
        ("    ; Imagine printing message here", "Just a placeholder"),
        ("    ret", "🔚 Return back to 'greet'"),
        ("", ""),
        ("section .data", "Data section"),
        ('message db "Hello from greet!", 0xA', "String to print"),
    ]

    for line, explanation in code_lines:
        if line.strip() == "":
            print()
            continue
        slow_print(f"  {CYAN}{line:<40}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)

    time.sleep(1)

    slow_print(f"\n{YELLOW}🧱 What happens to the stack during `call greet`?{RESET}")
    slow_print(f"""
  - 📍 The address of the next instruction (after `call greet`) is pushed onto the stack.
  - 🏃 The CPU jumps to `greet` and begins executing it.
  - 🧹 When `ret` is executed, the CPU pops the return address and jumps back there.
    """, 0.01)

    slow_print(f"{BOLD}{GREEN}This is how Assembly handles functions!{RESET}\n", 0.02)

    time.sleep(1)

    slow_print(f"{CYAN}🧪 Stack snapshot during call:{RESET}")
    slow_print(f"""
    Before `call greet`:
      [Stack top]   ← address of instruction *after* call

    Inside `greet` → Inside `print`
      More return addresses added with nested calls

    Each `ret` unwinds the stack and returns to the correct place!
    """, 0.01)

    time.sleep(1)

    slow_print(f"{GREEN}🔁 Nested `call`/`ret` sequences form the core of recursion, nested logic, and flow control!{RESET}", 0.02)
    slow_print(f"{YELLOW}That’s why understanding the stack is so important in low-level programming.{RESET}\n", 0.02)

    slow_print(f"{BOLD}🎯 Summary:{RESET}")
    slow_print(f"""
  🔹 {CYAN}call label{RESET} saves the return address and jumps to a function
  🔹 {CYAN}ret{RESET} returns back to the saved address

  🔸 Both rely on the {BOLD}stack{RESET} to track the flow!
    """, 0.01)

    time.sleep(1)

    slow_print(f"{CYAN}🏁 You’ve now mastered the mechanics behind function calls in Assembly!{RESET}", 0.02)
    slow_print(f"{GREEN}Keep practicing, and you’ll soon be calling (and returning) like a CPU pro. 🧠💻{RESET}\n", 0.02)

    input(f"{BOLD}➡️ Press Enter to return to the lesson list...{RESET}")
