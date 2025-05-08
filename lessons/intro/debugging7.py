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
    slow_print(f"\n{BOLD}🔎 GDB Lesson 7: Peering into the Abyss — Libraries, Heap, and Pretty-Printing! 🧠{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}Now that you're a breakpoint and watchpoint master... it's time to dive deeper!{RESET}")
    slow_print("Ever wonder how to step into library calls? Or inspect dynamically allocated memory? Or see pretty-printed structs? Let's go!\n")

    print(f"\n{CYAN}{BOLD}📚 1. Stepping Into Library Calls (Or Not){RESET}\n")
    slow_print(f"{GREEN}By default, GDB skips over standard library functions like printf, malloc, etc.{RESET}")
    slow_print("But what if you want to see what's going on under the hood?")

    slow_print(f"\n{BOLD}Option A: Step over (default){RESET}")
    slow_print(f"{CYAN}(gdb) next{RESET} → Skips into the next line of user code")

    slow_print(f"\n{BOLD}Option B: Step into EVERYTHING{RESET}")
    slow_print(f"{CYAN}(gdb) set step-mode on{RESET}")
    slow_print(f"{CYAN}(gdb) step{RESET} → Will now go into libc, printf, malloc... if you dare!")

    slow_print(f"\n{YELLOW}⚠️ Caution: You'll enter the Matrix. Exit with:{RESET} {CYAN}(gdb) finish{RESET} or {CYAN}(gdb) return{RESET}")

    print(f"\n{CYAN}{BOLD}💾 2. Debugging the Heap (malloc, free, etc.){RESET}\n")
    slow_print("Dynamic memory lives in the heap. Want to see it? Here's how.")

    slow_print(f"{MAGENTA}Example:{RESET}")
    print(f"""{CYAN}
#include <stdlib.h>

int main() {{
    int *arr = malloc(5 * sizeof(int));
    arr[0] = 42;
    free(arr);
    return 0;
}}
{RESET}""")

    steps = [
        "(gdb) b main",
        "(gdb) run",
        "(gdb) next",
        "(gdb) print arr",
        "→ Shows the pointer address (e.g., 0x55555576f2a0)",
        "(gdb) x/5dw arr",
        "→ Dumps 5 words at that heap location",
    ]
    for step in steps:
        slow_print(f"{CYAN}{step}{RESET}")
        time.sleep(0.5)

    slow_print(f"{GREEN}🧠 Pro Tip:{RESET} Use `x/20xb` to dump raw bytes, or `x/5i` to disassemble from any memory location.")

    print(f"\n{CYAN}{BOLD}🌈 3. Pretty-Printing Complex Data Structures{RESET}\n")
    slow_print("C structs can be messy to print. But GDB is smart.")

    slow_print(f"{MAGENTA}Example:{RESET}")
    print(f"""{CYAN}
struct Point {{
    int x;
    int y;
}};

int main() {{
    struct Point p = {{10, 20}};
    return 0;
}}
{RESET}""")

    steps = [
        "(gdb) print p",
        "→ $1 = {{x = 10, y = 20}}  ← easy!",
        "(gdb) print p.x",
        "→ $2 = 10",
        "(gdb) set print pretty on",
        "→ Prints arrays and structs in a readable format",
    ]
    for step in steps:
        slow_print(f"{CYAN}{step}{RESET}")
        time.sleep(0.5)

    slow_print(f"{GREEN}📌 Summary:{RESET}")
    summary = [
        f"{BOLD}step-mode on{RESET} — lets you dive into standard libraries",
        f"{BOLD}x/{RESET} — explore memory at any location (heap, stack, globals)",
        f"{BOLD}set print pretty on{RESET} — beautiful struct/array output",
    ]
    for line in summary:
        slow_print(f"{YELLOW}{line}{RESET}")
        time.sleep(0.4)

    slow_print(f"\n{BOLD}🧪 Mini Challenge:{RESET}")
    slow_print("Write a C program with a struct containing a pointer to heap-allocated memory.\nTry printing the struct and the heap data together!")

    slow_print(f"\n{CYAN}{BOLD}🎯 You now see through the runtime illusion. You're one with the debugger.{RESET}")
    slow_print(f"{CYAN}Next time: we’ll trace syscalls and even debug child processes... 🧬{RESET}\n")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
