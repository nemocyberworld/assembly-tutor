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
    slow_print(f"\n👋 {BOLD}Welcome to your first x86-64 Assembly lesson: Hello World!{RESET}\n", 0.07)
    time.sleep(1)

    slow_print(f"{YELLOW}📚 In this lesson, you'll see how to write the classic 'Hello, World!' program in Assembly.{RESET}", 0.02)
    slow_print(f"{YELLOW}🔍 We'll go line by line, explaining what's going on — no prior experience required!{RESET}", 0.07)
    slow_print(f"{YELLOW}🧪 By the end, you'll even know how to run this code on a real Linux system!{RESET}\n", 0.07)
    time.sleep(2)

    slow_print(f"{CYAN}{BOLD}📄 Assembly Code:{RESET}\n", 0.07)
    code_lines = [
        ("section .data", "🗃️ Declares a section to hold data (like strings)"),
        ('msg db "Hello, world!", 0xa', "💬 Defines the message we want to print, ending with newline (0xA = '\\n')"),
        ("len equ $ - msg", "📏 Calculates the length of the message (current address - start)"),
        ("", ""),
        ("section .text", "🎬 Declares the section containing code"),
        ("global _start", "🚀 Tells the linker where our program starts"),
        ("", ""),
        ("_start:", "🟢 Label marking the entry point"),
        ("mov rax, 1", "🧠 System call number 1 = write"),
        ("mov rdi, 1", "🖥️ File descriptor 1 = stdout"),
        ("mov rsi, msg", "📍 rsi points to our message"),
        ("mov rdx, len", "📐 rdx is the length of the message"),
        ("syscall", "📣 Triggers the write syscall"),
        ("", ""),
        ("mov rax, 60", "🧹 System call number 60 = exit"),
        ("xor rdi, rdi", "🔚 Exit code 0 (clean exit)"),
        ("syscall", "🏁 Exit the program"),
    ]

    for code, explanation in code_lines:
        if code.strip() == "":
            print()
            continue
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.07)
        time.sleep(0.25)

    input(f"\n{BOLD}➡️ Press Enter to simulate the program's execution...{RESET}\n")
    slow_print(f"{GREEN}🌀 Running...{RESET}\n", 0.07)
    time.sleep(1.2)

    slow_print(f"{BOLD}{GREEN}💻 Output:{RESET}\n", 0.07)
    slow_print("   Hello, world!", delay=0.08)

    time.sleep(0.5)
    slow_print(f"\n{GREEN}✅ Program exited with status code 0 (success).{RESET}\n", 0.07)
    time.sleep(1)

    slow_print(f"{YELLOW}📦 Want to run this on your own? Here's how!{RESET}", 0.07)
    slow_print(f"""
{BOLD}🛠️ 1. Save the code to a file:{RESET}
    {CYAN}hello.asm{RESET}

{BOLD}🏗️ 2. Assemble and link it (on Linux):{RESET}
    {GREEN}nasm -f elf64 hello.asm -o hello.o{RESET}
    {GREEN}ld hello.o -o hello{RESET}

{BOLD}🚀 3. Run it:{RESET}
    {GREEN}./hello{RESET}

{BOLD}🔍 4. You should see:{RESET}
    {MAGENTA}Hello, world!{RESET}
""", 0.07)

    time.sleep(1)
    slow_print(f"{BOLD}🎉 Great job! You've written and understood your very first Assembly program!{RESET}", 0.07)
    slow_print(f"{BOLD}{CYAN}Keep going — the CPU is your playground! 🧠💻{RESET}\n", 0.07)
    time.sleep(0.5)
    input(f"{BOLD}➡️ Press Enter to return to the lesson list...{RESET}")