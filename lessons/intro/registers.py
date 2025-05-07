# import time

# # ANSI color codes
# CYAN = "\033[96m"
# GREEN = "\033[92m"
# YELLOW = "\033[93m"
# MAGENTA = "\033[95m"
# RED = "\033[91m"
# BOLD = "\033[1m"
# RESET = "\033[0m"

# def slow_print(text, delay=0.03):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(delay)
#     print()

# def run():
#     print(f"\n{BOLD}🔧 Intro to Assembly & CPU Registers{RESET}\n")
#     time.sleep(1)

#     slow_print(f"{YELLOW}🧠 Before we write more code, we need to understand the CPU’s tiny toolbox — {BOLD}registers!{RESET}")
#     time.sleep(1)

#     overview = [
#         f"{CYAN}💾 Registers are small storage spaces inside your CPU.{RESET}",
#         f"{CYAN}⚡ They are *blazing fast*, much faster than RAM or hard drives.{RESET}",
#         f"{CYAN}📦 The CPU uses them to hold data it’s actively working on — like variables or counters.{RESET}",
#     ]
#     for line in overview:
#         slow_print(line)
#         time.sleep(1)

#     print()
#     slow_print(f"{MAGENTA}🔍 In x86-64 Assembly, there are several general-purpose registers. Here are some stars of the show:{RESET}")
#     time.sleep(1)

#     registers = [
#         (f"{BOLD}rax{RESET}", "🧮 Used for arithmetic, return values, and system calls"),
#         (f"{BOLD}rbx{RESET}", "📦 A general-purpose register (not preserved across syscalls)"),
#         (f"{BOLD}rcx{RESET}", "🔁 Often used as a loop counter"),
#         (f"{BOLD}rdx{RESET}", "📐 Used for data, lengths, I/O parameters"),
#         (f"{BOLD}rsi{RESET}", "📍 Source pointer (e.g. for memory operations)"),
#         (f"{BOLD}rdi{RESET}", "🎯 Destination pointer"),
#         (f"{BOLD}rsp{RESET}", "🪜 Stack pointer — tracks the top of the stack"),
#         (f"{BOLD}rbp{RESET}", "🔖 Base pointer — helps with stack frames in functions"),
#     ]
#     for reg, desc in registers:
#         slow_print(f"  {GREEN}{reg:<5}{RESET} - {desc}")
#         time.sleep(0.8)

#     print()
#     slow_print(f"{YELLOW}📌 The names all start with {BOLD}r{RESET}{YELLOW} because they’re 64-bit (the 'r' means 'register').{RESET}")
#     slow_print(f"{YELLOW}For example: {BOLD}rax{RESET} is the 64-bit version of the old {BOLD}eax{RESET} (32-bit), which came from {BOLD}ax{RESET} (16-bit). Evolution! 🧬{RESET}")
#     time.sleep(2)

#     print()
#     slow_print(f"{CYAN}🧪 In the next lessons, we’ll use these registers to do math, store values, call functions, and more!{RESET}")
#     slow_print(f"{CYAN}You'll see how each one plays a key role in real assembly code.{RESET}")
#     time.sleep(1.5)

#     print()
#     slow_print(f"{BOLD}{MAGENTA}🛠️ Ready to use these in code? Next up: {GREEN}moving data between registers using 'mov'!{RESET}")
#     time.sleep(1)

#     print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
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
    print(f"\n{BOLD}🔧 Intro to Assembly & CPU Registers{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 Before we write more code, we need to understand the CPU’s tiny toolbox — {BOLD}registers!{RESET}")
    time.sleep(1)

    overview = [
        f"{CYAN}💾 Registers are small storage spaces inside your CPU.{RESET}",
        f"{CYAN}⚡ They are *blazing fast*, much faster than RAM or hard drives.{RESET}",
        f"{CYAN}📦 The CPU uses them to hold data it’s actively working on — like variables or counters.{RESET}",
        f"{CYAN}🏃‍♂️ Registers are the first place the CPU checks when performing any task.{RESET}",
        f"{CYAN}🧠 You can think of them as the CPU's working memory or scratchpad.{RESET}"
    ]
    for line in overview:
        slow_print(line)
        time.sleep(1)

    print()
    slow_print(f"{MAGENTA}🔍 In x86-64 Assembly, there are several general-purpose registers. Here are some stars of the show:{RESET}")
    time.sleep(1)

    registers = [
        (f"{BOLD}rax{RESET}", "🧮 Used for arithmetic, return values, and system calls"),
        (f"{BOLD}rbx{RESET}", "📦 A general-purpose register (not preserved across syscalls)"),
        (f"{BOLD}rcx{RESET}", "🔁 Often used as a loop counter"),
        (f"{BOLD}rdx{RESET}", "📐 Used for data, lengths, I/O parameters"),
        (f"{BOLD}rsi{RESET}", "📍 Source pointer (e.g. for memory operations)"),
        (f"{BOLD}rdi{RESET}", "🎯 Destination pointer"),
        (f"{BOLD}rsp{RESET}", "🪜 Stack pointer — tracks the top of the stack"),
        (f"{BOLD}rbp{RESET}", "🔖 Base pointer — helps with stack frames in functions")
    ]
    for reg, desc in registers:
        slow_print(f"  {GREEN}{reg:<5}{RESET} - {desc}")
        time.sleep(0.8)

    print()
    slow_print(f"{YELLOW}📌 The names all start with {BOLD}r{RESET}{YELLOW} because they’re 64-bit (the 'r' means 'register').{RESET}")
    slow_print(f"{YELLOW}For example: {BOLD}rax{RESET} is the 64-bit version of the old {BOLD}eax{RESET} (32-bit), which came from {BOLD}ax{RESET} (16-bit). Evolution! 🧬{RESET}")
    time.sleep(2)

    print()
    slow_print(f"{CYAN}💡 Let's walk through an example to make this more concrete.{RESET}")
    time.sleep(1)

    example = [
        f"{MAGENTA}We want to add two numbers: 5 + 3, and store the result.{RESET}",
        f"{CYAN}We'll use: rax = 5, rbx = 3, then add rax and rbx and store it in rax.{RESET}",
        f"\n{BOLD}Assembly Code:{RESET}",
        f"  {GREEN}mov rax, 5{RESET}        {MAGENTA}# Store 5 in rax{RESET}",
        f"  {GREEN}mov rbx, 3{RESET}        {MAGENTA}# Store 3 in rbx{RESET}",
        f"  {GREEN}add rax, rbx{RESET}      {MAGENTA}# rax = rax + rbx (5 + 3){RESET}"
    ]
    for line in example:
        slow_print(line)
        time.sleep(0.6)

    print()
    slow_print(f"{BOLD}{GREEN}✅ After execution, rax holds: 8{RESET}")
    time.sleep(1)

    print()
    slow_print(f"{YELLOW}📊 Visualizing this in the CPU:{RESET}")
    slow_print(f"  {BOLD}rax:{RESET} 5  →  8")
    slow_print(f"  {BOLD}rbx:{RESET} 3")
    time.sleep(1.5)

    print()
    slow_print(f"{CYAN}🧮 Let’s try one more! Subtract 2 from rax (which is currently 8).{RESET}")
    sub_example = [
        f"  {GREEN}sub rax, 2{RESET}        {MAGENTA}# rax = rax - 2 → 6{RESET}"
    ]
    for line in sub_example:
        slow_print(line)
        time.sleep(0.8)

    slow_print(f"{BOLD}{GREEN}✅ Now rax holds: 6{RESET}")
    time.sleep(1)

    print()
    slow_print(f"{MAGENTA}🎯 These examples are simple, but they show how registers are used like variables.{RESET}")
    slow_print(f"{MAGENTA}In reality, all the complex tasks your programs do eventually boil down to simple register ops!{RESET}")
    time.sleep(2)

    print()
    slow_print(f"{YELLOW}⛏️ We'll dive deeper into each register and use them in loops, function calls, and more!{RESET}")
    slow_print(f"{YELLOW}Next up: {BOLD}How to move data between memory and registers!{RESET}")
    time.sleep(1.5)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
