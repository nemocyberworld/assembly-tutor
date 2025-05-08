import time

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
    slow_print(f"\n{BOLD}{CYAN}🔍 GDB Lesson 3: Inspecting Registers and Memory{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧬 Registers are the CPU's working memory, and inspecting them is essential for debugging.{RESET}")
    slow_print(f"{YELLOW}📦 We'll also learn to peek into memory to examine strings, buffers, and stack content.{RESET}\n")
    time.sleep(1.5)

    slow_print(f"{CYAN}{BOLD}📄 Sample Assembly Code:{RESET}")
    print()
    code = [
        "section .data",
        '  msg db "Hello", 0',
        "",
        "section .text",
        "  global _start",
        "",
        "_start:",
        "  mov rax, 1",
        "  mov rdi, 1",
        "  mov rsi, msg",
        "  mov rdx, 5",
        "  syscall",
        "",
        "  mov rax, 60",
        "  xor rdi, rdi",
        "  syscall"
    ]
    for line in code:
        slow_print(f"{GREEN}{line}{RESET}", 0.01)

    slow_print(f"\n{BOLD}🛠️ Let's assemble, link, and load this into GDB:{RESET}")
    slow_print(f"{CYAN}nasm -f elf64 program.asm -o program.o", 0.01)
    slow_print(f"ld program.o -o program", 0.01)
    slow_print(f"gdb ./program{RESET}", 0.01)
    time.sleep(1)

    slow_print(f"\n{MAGENTA}{BOLD}🔧 Using GDB to Inspect Registers{RESET}")
    slow_print(f"{YELLOW}Let's break at _start and print the contents of registers step-by-step.{RESET}")
    slow_print(f"{GREEN}(gdb) break _start", 0.01)
    slow_print(f"(gdb) run", 0.01)
    slow_print(f"(gdb) info registers", 0.01)

    slow_print(f"\n{CYAN}This prints all general-purpose registers like RAX, RBX, RSP, RBP, etc.{RESET}")
    slow_print(f"🔍 You'll see RAX as 1 (sys_write), RDI as 1 (stdout), RSI pointing to 'msg', and so on.\n")
    time.sleep(2)

    slow_print(f"{MAGENTA}{BOLD}🧠 Examining Specific Registers:{RESET}")
    slow_print(f"{GREEN}(gdb) print $rax", 0.01)
    slow_print(f"{GREEN}(gdb) print/x $rsi", 0.01)
    slow_print(f"{GREEN}(gdb) x/s $rsi{RESET}  # See the string msg points to")
    slow_print(f"\n{YELLOW}💡 The `x` command is used to examine memory. Use it with flags like:{RESET}")
    slow_print(f"{CYAN}x/s  => string", 0.01)
    slow_print(f"x/x  => hex", 0.01)
    slow_print(f"x/d  => decimal", 0.01)
    slow_print(f"x/t  => binary", 0.01)
    slow_print(f"x/i  => disassemble instructions\n", 0.01)

    slow_print(f"{BOLD}{MAGENTA}📚 Examples:{RESET}")
    slow_print(f"{GREEN}(gdb) x/x $rsi{RESET}   => hex value at msg")
    slow_print(f"{GREEN}(gdb) x/5xb $rsi{RESET} => 5 bytes from msg as hex")
    slow_print(f"{GREEN}(gdb) x/5cb $rsi{RESET} => 5 bytes as ASCII characters")
    slow_print(f"{GREEN}(gdb) x/10x $rsp{RESET} => Check values on the stack\n")
    time.sleep(2)

    slow_print(f"{BOLD}{RED}🔥 Bonus: Tracking Stack Changes!{RESET}")
    slow_print(f"{YELLOW}After each step, check how the stack changes:{RESET}")
    slow_print(f"{GREEN}(gdb) x/16x $rsp{RESET}")
    slow_print(f"{CYAN}Compare before and after a `push`, `call`, or function return.\n", 0.01)
    time.sleep(2)

    slow_print(f"{BOLD}{CYAN}🎯 Summary:{RESET}")
    slow_print(f"""
{GREEN}• Use `info registers` or `i r` to see CPU register state
• Use `print $regname` to inspect individual registers
• Use `x/<format> <addr>` to read memory
• Combine these to debug logic, bugs, and memory issues easily{RESET}
""", 0.01)
    time.sleep(1)

    slow_print(f"{BOLD}🎉 You're getting deeper into the brain of your program! Mastering this makes you a debugging ninja! 🧠🕵️‍♂️{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

