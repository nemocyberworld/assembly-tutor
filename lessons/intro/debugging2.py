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
    slow_print(f"\n🐞 {BOLD}GDB Lesson 2: Breakpoints and Stepping Through Code{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}In this lesson, we’ll dive into one of GDB’s most useful features: breakpoints.{RESET}", 0.02)
    slow_print(f"{YELLOW}Breakpoints allow you to pause the program at specific points to inspect what’s going on.{RESET}", 0.02)
    slow_print(f"{YELLOW}Let’s also learn how to step through instructions, one by one! 🪜{RESET}\n", 0.02)
    time.sleep(2)

    slow_print(f"{CYAN}{BOLD}📄 Sample Assembly Code:{RESET}\n", 0.02)
    code_lines = [
        ("section .text", "💾 Code section"),
        ("global _start", "🚀 Entry point"),
        ("_start:", "🔰 Start of program"),
        ("    mov rax, 5", "🔢 rax = 5"),
        ("    add rax, 10", "➕ rax += 10 → rax = 15"),
        ("    sub rax, 3", "➖ rax -= 3 → rax = 12"),
        ("    mov rbx, rax", "📦 Copy rax to rbx"),
        ("    mov rax, 60", "🔚 syscall: exit"),
        ("    xor rdi, rdi", "🧼 exit code 0"),
        ("    syscall", "📞 Exit"),
    ]
    for code, explanation in code_lines:
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
        time.sleep(0.2)

    slow_print(f"\n{GREEN}We'll use GDB to pause at key points and examine register values.{RESET}", 0.02)
    time.sleep(1)

    slow_print(f"{BOLD}🛠️ Compile the code first:{RESET}", 0.02)
    slow_print(f"""
{CYAN}nasm -f elf64 example.asm -o example.o{RESET}
{CYAN}ld example.o -o example{RESET}
    """, 0.01)

    time.sleep(1)

    slow_print(f"{BOLD}🐞 Launching GDB:{RESET}", 0.02)
    slow_print(f"{GREEN}gdb ./example{RESET}\n", 0.02)

    slow_print(f"{YELLOW}Now let’s set a breakpoint at the start of our program using the `_start` label:{RESET}", 0.02)
    slow_print(f"{GREEN}(gdb) break _start{RESET}", 0.02)
    slow_print(f"{MAGENTA}This will pause the execution right before the first instruction of _start.{RESET}\n", 0.02)

    slow_print(f"{YELLOW}To start running the program, use:{RESET}", 0.02)
    slow_print(f"{GREEN}(gdb) run{RESET}", 0.02)
    slow_print(f"{MAGENTA}Now we are paused at the first instruction. Time to step through!{RESET}\n", 0.02)

    slow_print(f"{BOLD}🔎 Use these commands to step through the code:{RESET}", 0.02)
    slow_print(f"""
{GREEN}(gdb) si{RESET}       {CYAN}# Step one instruction (good for assembly){RESET}
{GREEN}(gdb) ni{RESET}       {CYAN}# Next instruction (skip over call-like instructions){RESET}
{GREEN}(gdb) info registers{RESET}  {CYAN}# See all registers and their values{RESET}
    """, 0.01)

    slow_print(f"\n{YELLOW}💡 Example session walkthrough:{RESET}", 0.02)
    slow_print(f"""
{GREEN}(gdb) break _start{RESET}
{GREEN}(gdb) run{RESET}
{GREEN}(gdb) si{RESET}
{MAGENTA}# Now you’re at: mov rax, 5{RESET}
{GREEN}(gdb) info registers{RESET}
{MAGENTA}# See rax is still 0{RESET}
{GREEN}(gdb) si{RESET}
{MAGENTA}# rax is now 5{RESET}
{GREEN}(gdb) si{RESET}
{MAGENTA}# Now at: add rax, 10 → rax will be 15 after next step{RESET}
    """, 0.01)

    slow_print(f"{BOLD}🔥 You can set breakpoints at addresses too!{RESET}", 0.02)
    slow_print(f"""
{GREEN}(gdb) disassemble _start{RESET}
{MAGENTA}# This shows memory addresses for instructions.{RESET}

{GREEN}(gdb) break *0x<address>{RESET}
{MAGENTA}# Stops execution right at that memory location.{RESET}
    """, 0.01)

    slow_print(f"\n{GREEN}🏁 To continue running till next breakpoint or program end:{RESET}", 0.02)
    slow_print(f"{GREEN}(gdb) continue{RESET}\n", 0.02)

    time.sleep(1)
    slow_print(f"{BOLD}{CYAN}🎉 Congrats! You've just learned how to use breakpoints and step through your assembly programs with GDB!{RESET}", 0.02)
    slow_print(f"{BOLD}{YELLOW}This is how real debugging starts: slowly, one instruction at a time! 🐢🧠{RESET}", 0.02)
    time.sleep(0.5)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")


if __name__ == "__main__":
    run()
