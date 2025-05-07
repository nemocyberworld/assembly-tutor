import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    slow_print(f"\n✍️ {BOLD}Lesson: Code Formatting and Comments in x86-64 Assembly{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}📚 Writing code that works is great... but writing code that's {BOLD}readable{RESET}{YELLOW} is even better!{RESET}", 0.02)
    slow_print(f"{YELLOW}📝 In this lesson, you'll learn how to make your Assembly code clean, readable, and well-documented.{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🧠 Why Comments Matter:{RESET}", 0.02)
    slow_print(f"""
{MAGENTA}; Good comments explain the {BOLD}why{RESET}{MAGENTA}, not just the what.
; They help future-you (and others) understand the purpose of each line.
; In Assembly, comments start with a semicolon: {CYAN};{RESET}
""", 0.01)

    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🔍 Example: With and Without Comments{RESET}\n", 0.02)

    slow_print(f"{RED}Without comments:{RESET}", 0.02)
    slow_print(f"""
{CYAN}mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, len
syscall
""", 0.01)

    slow_print(f"{GREEN}With comments:{RESET}", 0.02)
    slow_print(f"""
{CYAN}mov rax, 1{RESET}      {MAGENTA}; syscall number for write
{CYAN}mov rdi, 1{RESET}      {MAGENTA}; file descriptor: stdout
{CYAN}mov rsi, msg{RESET}    {MAGENTA}; address of the message
{CYAN}mov rdx, len{RESET}    {MAGENTA}; length of the message
{CYAN}syscall{RESET}         {MAGENTA}; call the kernel
""", 0.01)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}📏 Formatting Tips:{RESET}", 0.02)
    slow_print(f"""
{GREEN}🟢 1. Align your code vertically{RESET}
    Makes it easier to scan and compare lines.

{GREEN}🟢 2. Use spacing consistently{RESET}
    Between opcodes, operands, and comments.

{GREEN}🟢 3. Group related instructions{RESET}
    Add blank lines between code sections (e.g., data, printing, exiting).
""", 0.01)

    slow_print(f"{CYAN}{BOLD}✅ Example: Cleanly Formatted Code{RESET}", 0.02)
    slow_print(f"""
{CYAN}section .data{RESET}
    {CYAN}msg db "Hello!", 0xA{RESET}
    {CYAN}len equ $ - msg{RESET}

{CYAN}section .text{RESET}
    {CYAN}global _start{RESET}

{CYAN}_start:{RESET}
    {CYAN}mov rax, 1{RESET}        {MAGENTA}; syscall: write
    {CYAN}mov rdi, 1{RESET}        {MAGENTA}; file descriptor: stdout
    {CYAN}mov rsi, msg{RESET}      {MAGENTA}; pointer to message
    {CYAN}mov rdx, len{RESET}      {MAGENTA}; length of message
    {CYAN}syscall{RESET}

    {CYAN}mov rax, 60{RESET}       {MAGENTA}; syscall: exit
    {CYAN}xor rdi, rdi{RESET}      {MAGENTA}; return code 0
    {CYAN}syscall{RESET}
""", 0.01)

    time.sleep(1)
    slow_print(f"{CYAN}{BOLD}📚 Summary:{RESET}", 0.02)
    slow_print(f"""
{GREEN}💬 Comments:{RESET} Start with {CYAN};{RESET}, explain intent and purpose.
{GREEN}🧼 Formatting:{RESET} Align code, use whitespace, group logically.

{YELLOW}Clean code = easier debugging, easier learning, and happier humans! 😄{RESET}
""", 0.01)

    slow_print(f"\n{BOLD}{CYAN}💡 Keep your code beautiful — it's not just what it does, it's how it looks too!{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
