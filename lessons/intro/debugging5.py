import time

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    slow_print(f"\n{BOLD}{CYAN}📚 GDB Lesson 4: Stack Frames and Function Call Tracing{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🎯 This lesson dives into how GDB helps you inspect function calls and stack frames.{RESET}")
    slow_print(f"{YELLOW}🧠 Understand how functions push/pull from the stack, and trace backtraces like a pro.{RESET}\n")
    time.sleep(1.5)

    slow_print(f"{CYAN}{BOLD}📄 Sample Assembly Code with Functions:{RESET}\n")
    code = [
        "section .text",
        "global _start",
        "", 
        "_start:",
        "  call my_function",
        "  mov rax, 60",
        "  xor rdi, rdi",
        "  syscall",
        "",
        "my_function:",
        "  push rbp",
        "  mov rbp, rsp",
        "  mov rax, 1",
        "  pop rbp",
        "  ret"
    ]
    for line in code:
        slow_print(f"{GREEN}{line}{RESET}", 0.01)

    slow_print(f"\n{MAGENTA}{BOLD}🔧 Let's debug it with GDB:{RESET}")
    slow_print(f"{CYAN}nasm -f elf64 function.asm -o function.o", 0.01)
    slow_print(f"ld function.o -o function", 0.01)
    slow_print(f"gdb ./function{RESET}\n", 0.01)

    slow_print(f"{YELLOW}Set a breakpoint at `my_function`:{RESET}")
    slow_print(f"{GREEN}(gdb) break my_function{RESET}")
    slow_print(f"{GREEN}(gdb) run{RESET}")
    time.sleep(1)

    slow_print(f"{MAGENTA}🧰 Use these commands to trace calls and inspect the stack frame:{RESET}")
    slow_print(f"{GREEN}(gdb) backtrace{RESET}  # Shows the call stack")
    slow_print(f"{GREEN}(gdb) bt{RESET}         # Shortcut for backtrace")
    slow_print(f"{GREEN}(gdb) info frame{RESET}  # Info about the current frame")
    slow_print(f"{GREEN}(gdb) info registers rbp rsp rip{RESET}  # Track stack/frame pointers")
    slow_print(f"\n{CYAN}Each call creates a new frame with saved RBP and return address.{RESET}")
    slow_print(f"GDB lets you navigate these with:{RESET}")
    slow_print(f"{GREEN}(gdb) frame 0{RESET}  # Current")
    slow_print(f"{GREEN}(gdb) frame 1{RESET}  # Caller")
    slow_print(f"{GREEN}(gdb) up / down{RESET}  # Move through frames\n")
    time.sleep(2)

    slow_print(f"{RED}{BOLD}🔥 Bonus Tip:{RESET} Use `layout asm` to view instructions as you step through!")

    slow_print(f"\n{BOLD}{CYAN}📦 Summary:{RESET}")
    slow_print(f"{GREEN}• Each function call creates a new frame\n",
               0.01)
    slow_print(f"• Use `bt`, `frame`, and `info frame` to inspect stack states\n",
               0.01)
    slow_print(f"• Master this and you're decoding the soul of your program!{RESET}\n",
               0.01)

    slow_print(f"\n{BOLD}🎉 You're now ready to debug nested calls, stack frames, and even segmentation faults like a legend! 🧙‍♂️{RESET}\n")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
