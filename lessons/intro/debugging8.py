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
    slow_print(f"\n{BOLD}🔍 Welcome to GDB Lesson 8: Tracing Syscalls, Debugging Children, and Memory Inspection!{RESET}\n", 0.02)
    time.sleep(1)

    # Section 1: Syscall Tracing
    slow_print(f"{CYAN}{BOLD}\n🛠️ Section 1: Tracing System Calls with strace and GDB{RESET}\n", 0.02)
    slow_print("Sometimes, a program crashes because of a failed syscall (like open, read, or write).", 0.02)
    slow_print("Tools like `strace` help us trace all syscalls made by a program. Let's see how:", 0.02)

    slow_print(f"\n{BOLD}Example Program (syscall.asm):{RESET}", 0.01)
    slow_print(f"""
{CYAN}section .data{RESET}
    msg db "Hello", 0xA
    len equ $ - msg

{CYAN}section .text{RESET}
    global _start

_start:
    mov rax, 1      ; syscall: write
    mov rdi, 1      ; stdout
    mov rsi, msg    ; buffer
    mov rdx, len    ; length
    syscall

    mov rax, 60     ; syscall: exit
    xor rdi, rdi
    syscall
""", 0.01)

    slow_print(f"\n{GREEN}Compile and run with strace:{RESET}", 0.02)
    slow_print("  nasm -f elf64 syscall.asm -o syscall.o", 0.01)
    slow_print("  ld syscall.o -o syscall", 0.01)
    slow_print("  strace ./syscall", 0.01)

    slow_print(f"\n{YELLOW}🔍 This will list all syscalls made — perfect for debugging interaction with the OS!{RESET}\n", 0.02)

    # Section 2: Child Process Debugging
    slow_print(f"{CYAN}{BOLD}\n👶 Section 2: Debugging Child Processes{RESET}\n", 0.02)
    slow_print("When your program forks, the child may crash or behave oddly. You can use GDB to follow it!", 0.02)
    slow_print("\nUse this in GDB:", 0.01)
    slow_print(f"  {MAGENTA}set follow-fork-mode child{RESET} — Follow the child process after fork", 0.01)
    slow_print(f"  {MAGENTA}set detach-on-fork off{RESET} — Stay attached to both parent and child (multi-process)\n", 0.01)

    slow_print("GDB will now stop in the child after a fork. Handy for debugging processes like shells, servers, etc.", 0.02)

    # Section 3: Valgrind + GDB for Memory Inspection
    slow_print(f"{CYAN}{BOLD}\n🧠 Section 3: Memory Debugging with Valgrind + GDB{RESET}\n", 0.02)
    slow_print("Valgrind detects memory leaks, invalid reads/writes, and more. Combine it with GDB for deep analysis.", 0.02)

    slow_print(f"\n{BOLD}Example C Program (leaky.c):{RESET}", 0.01)
    slow_print(f"""
{CYAN}#include <stdlib.h>

int main() {{
    int *arr = malloc(5 * sizeof(int));
    arr[6] = 42; // Invalid write
    return 0;
}}{RESET}
""", 0.01)

    slow_print(f"{GREEN}Compile and run with Valgrind:{RESET}", 0.01)
    slow_print("  gcc -g leaky.c -o leaky", 0.01)
    slow_print("  valgrind --vgdb=yes --vgdb-error=0 ./leaky", 0.01)

    slow_print(f"\nIn another terminal, attach GDB with:{RESET}", 0.01)
    slow_print("  gdb ./leaky", 0.01)
    slow_print("  target remote | vgdb", 0.01)

    slow_print(f"\nNow you can inspect stack, heap, and variables during Valgrind's analysis!{RESET}\n", 0.02)

    # Extended Valgrind Section
    slow_print(f"{CYAN}{BOLD}\n📦 Section 4: Advanced Valgrind Usage{RESET}\n", 0.02)

    slow_print(f"{YELLOW}\n💧 Memory Leak Example:{RESET}", 0.02)
    slow_print(f"""
#include <stdlib.h>

int main() {{
    int *ptr = malloc(10 * sizeof(int));
    ptr[0] = 123;
    return 0;  // forgot to free
}}""", 0.01)
    slow_print(f"Run: {GREEN}valgrind --leak-check=full ./a.out{RESET}", 0.01)
    slow_print("Valgrind will report 'definitely lost' if memory isn't freed.", 0.02)

    slow_print(f"\n{YELLOW}💥 Use-After-Free Example:{RESET}", 0.02)
    slow_print(f"""
#include <stdlib.h>
#include <stdio.h>

int main() {{
    int *ptr = malloc(sizeof(int));
    free(ptr);
    *ptr = 5;  // boom
    return 0;
}}""", 0.01)
    slow_print("Valgrind will show 'invalid write' warning. Never use freed memory!", 0.02)

    slow_print(f"\n{YELLOW}🧊 Uninitialized Read:{RESET}", 0.02)
    slow_print(f"""
int main() {{
    int x;
    return x;  // uninitialized read
}}""", 0.01)
    slow_print("Valgrind will alert you. Always initialize variables!", 0.02)

    slow_print(f"\n🕵️ Use {GREEN}--track-origins=yes{RESET} to trace where uninitialized values came from.", 0.02)

    slow_print(f"\n{BOLD}{GREEN}🎉 That's it! You're now equipped to trace syscalls, debug children, and inspect memory like a legend! 🧠🔧{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
