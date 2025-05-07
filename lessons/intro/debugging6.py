import time

# ANSI color codes
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
    slow_print(f"\n{BOLD}👀 GDB Lesson 6: Watching and Catching Like a Debugging Ninja! 🥷{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}You've already mastered breakpoints, stack frames, and stepping through code.{RESET}")
    slow_print(f"{YELLOW}Now it's time to level up your reflexes with two powerful weapons: {BOLD}watch{RESET}{YELLOW} and {BOLD}catch{RESET}.{RESET}")
    time.sleep(1.5)

    print(f"\n{CYAN}{BOLD}🔍 1. watch - Watch a Variable Like a Hawk{RESET}\n")
    slow_print("Imagine you want to know the exact moment a variable changes...")
    slow_print("That's where `watch` comes in!")
    time.sleep(1)

    slow_print(f"{MAGENTA}Let's look at this simple C program:{RESET}")
    print(f"""{CYAN}
int counter = 0;

int main() {{
    counter = 5;
    counter += 10;
    counter *= 2;
    return 0;
}}
{RESET}""")

    slow_print(f"{GREEN}Step-by-step debugging to observe changes in `counter`:{RESET}")
    steps = [
        "(gdb) b main",
        "(gdb) run",
        "(gdb) watch counter",
        "(gdb) c",
        "→ Breaks when counter is set to 5",
        "(gdb) c",
        "→ Breaks again when counter becomes 15",
        "(gdb) c",
        "→ Breaks when counter becomes 30",
    ]
    for step in steps:
        slow_print(f"{CYAN}{step}{RESET}")
        time.sleep(0.5)

    slow_print(f"\n{GREEN}📌 You can also use conditions with watchpoints!{RESET}")
    slow_print(f"{CYAN}(gdb) watch counter if counter > 20{RESET} → Only breaks if counter exceeds 20")

    print(f"\n{CYAN}{BOLD}🔥 2. catch - Trap Runtime Events Like a Ninja!{RESET}\n")
    slow_print("What if you want to break when something *happens*, not when a line is reached?")
    slow_print("Use `catch` to trap events like `throw`, `exec`, `signal`, and more!")
    time.sleep(1)

    slow_print(f"{MAGENTA}For example:{RESET} Let's say your program gets a segmentation fault.")
    print(f"""{CYAN}
int *p = NULL;

int main() {{
    *p = 10;  // segfault!
    return 0;
}}
{RESET}""")

    slow_print(f"{GREEN}Here's how to catch that in GDB:{RESET}")
    steps = [
        "(gdb) catch signal SIGSEGV",
        "(gdb) run",
        "→ GDB breaks as soon as the segfault signal is raised!",
    ]
    for step in steps:
        slow_print(f"{CYAN}{step}{RESET}")
        time.sleep(0.5)

    slow_print(f"\n{YELLOW}More things you can catch:{RESET}")
    catch_list = [
        "🧲 catch throw        — when a C++ exception is thrown",
        "⚠️  catch syscall      — when a syscall is made (Linux only)",
        "⏹️  catch exec         — when the program calls exec",
        "💥 catch signal SIGABRT — when the program aborts",
    ]
    for item in catch_list:
        slow_print(f"{MAGENTA}{item}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{BOLD}✨ Pro Tip:{RESET} Combine {CYAN}catch{RESET} with {CYAN}bt{RESET} to instantly get the stack trace when the event happens!")

    print(f"\n{GREEN}🧠 Summary:{RESET}")
    summary = [
        f"{BOLD}🔎 watch <var>{RESET}  — Breaks when the value of the variable changes",
        f"{BOLD}🪤 catch <event>{RESET} — Breaks when a specific runtime event occurs",
        f"{BOLD}💣 Useful for: debugging segfaults, unexpected mutations, or exceptions",
    ]
    for line in summary:
        slow_print(f"{YELLOW}{line}{RESET}")
        time.sleep(0.4)

    print(f"\n{GREEN}{BOLD}✅ Practice Challenge:{RESET}")
    slow_print("Write a short program where a variable is modified inside a loop.\nSet a `watch` to see when it hits a specific value.")

    slow_print(f"\n{CYAN}{BOLD}🎯 Mission Complete! You’ve mastered dynamic breakpoints!{RESET}")
    slow_print(f"{CYAN}Next up: stepping through libraries and inspecting heap allocations! 🔬{RESET}\n")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
