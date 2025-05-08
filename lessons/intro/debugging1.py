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
    slow_print(f"\n🐞 {BOLD}Welcome to the Debugging Basics lesson!{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}In this lesson, you'll learn how to debug x86-64 Assembly programs using tools like {BOLD}gdb{RESET}{YELLOW} and {BOLD}ndisasm{RESET}{YELLOW}.{RESET}")
    slow_print(f"{YELLOW}Debugging helps you step through your code, inspect memory/registers, and understand what's really going on under the hood!{RESET}\n")
    time.sleep(2)

    slow_print(f"{CYAN}{BOLD}🧠 Our Example Program:{RESET}\n")
    example_code = [
        ("section .data", "🗃️ We'll store our message here."),
        ('msg db "Debug me!", 0xA', "💬 The message to print followed by newline"),
        ("len equ $ - msg", "📏 Length of the message"),
        ("", ""),
        ("section .text", "🎬 Code section starts here"),
        ("global _start", "🚀 Entry point of our program"),
        ("", ""),
        ("_start:", "🏁 Start label"),
        ("mov rax, 1", "🧠 syscall number for write"),
        ("mov rdi, 1", "🖥️ stdout"),
        ("mov rsi, msg", "📍 address of message"),
        ("mov rdx, len", "📐 length of message"),
        ("syscall", "📣 perform write"),
        ("", ""),
        ("mov rax, 60", "🧹 syscall number for exit"),
        ("xor rdi, rdi", "🔚 exit code 0"),
        ("syscall", "🏁 exit program"),
    ]

    for code, explanation in example_code:
        if code.strip() == "":
            print()
            continue
        slow_print(f"{CYAN}  {code:<30}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
        time.sleep(0.15)

    slow_print(f"\n{BOLD}{GREEN}🛠️ Let's Compile the Program with Debug Symbols{RESET}\n")
    slow_print(f"{YELLOW}Use the following NASM and LD commands to keep debug symbols:{RESET}")
    slow_print(f"""
{GREEN}nasm -f elf64 -g debug.asm -o debug.o{RESET}
{GREEN}ld debug.o -o debug{RESET}
""", 0.01)

    time.sleep(2)

    slow_print(f"{CYAN}{BOLD}🔍 Using `ndisasm` to Disassemble Your Code:{RESET}")
    slow_print(f"{YELLOW}Want to see raw machine instructions? Try this:{RESET}")
    slow_print(f"""
{GREEN}ndisasm -b 64 debug{RESET}
""")
    slow_print(f"{MAGENTA}This gives you the raw opcodes, addresses, and assembly — great for reverse engineering or deep analysis!{RESET}\n")

    time.sleep(2)

    slow_print(f"{CYAN}{BOLD}🎯 Using `gdb` to Debug Your Assembly Program:{RESET}")
    slow_print(f"{YELLOW}Let’s walk through a live debugging session!{RESET}")
    slow_print(f"""
{GREEN}gdb ./debug{RESET}
""", 0.01)

    slow_print(f"{YELLOW}Inside GDB, try these commands:{RESET}")
    gdb_commands = [
        ("start", "🚀 Start running program and stop at the entry point."),
        ("layout asm", "🧾 View the assembly code layout (ncurses view)."),
        ("info registers", "🔎 View the current register values."),
        ("x/s $rsi", "📜 Inspect the message string stored at RSI."),
        ("break _start", "🛑 Set a breakpoint at the _start label."),
        ("si", "👣 Step one instruction at a time."),
        ("c", "🏃 Continue running the program."),
        ("quit", "🚪 Exit GDB."),
    ]

    for cmd, explanation in gdb_commands:
        slow_print(f"{GREEN}  {cmd:<20}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
        time.sleep(0.1)

    time.sleep(2)

    slow_print(f"\n{BOLD}{RED}❗ Common Pitfalls to Debug:{RESET}")
    pitfalls = [
        "Did you forget to null-terminate a string?",
        "Did you use the wrong syscall number?",
        "Are your registers set up correctly before calling syscall?",
        "Is your label spelled correctly?",
        "Are you trying to read/write to the correct memory address?",
    ]
    for pitfall in pitfalls:
        slow_print(f"{RED}- {pitfall}{RESET}", 0.01)

    time.sleep(1)

    slow_print(f"\n{GREEN}{BOLD}🎉 You've Learned the Basics of Debugging!{RESET}")
    slow_print(f"{YELLOW}From disassembly to stepping through code, you now have tools to fix bugs and deeply understand how your assembly runs.{RESET}")
    slow_print(f"{CYAN}{BOLD}Next time your program crashes, you’ll know where to look! 🧠💥{RESET}\n")
    slow_print(f"\n{BOLD}{CYAN}🧠 Let's understand how breakpoints work in GDB...{RESET}", 0.02)
    slow_print(f"{YELLOW}A breakpoint is a marker that tells GDB to pause the program before a certain instruction is executed.{RESET}", 0.02)
    slow_print(f"{YELLOW}This allows us to examine what's going on at that moment — perfect for debugging!{RESET}", 0.02)
    time.sleep(1)

    slow_print(f"\n{GREEN}✅ Setting a Breakpoint:{RESET}", 0.02)
    slow_print(f"  (gdb) {BOLD}break _start{RESET}", 0.01)
    slow_print(f"  This sets a breakpoint at the '_start' label in your program.", 0.02)
    time.sleep(0.5)

    slow_print(f"\n{GREEN}🎬 Running the program:{RESET}", 0.02)
    slow_print(f"  (gdb) {BOLD}run{RESET}", 0.01)
    slow_print(f"  Your program will begin executing and then pause right at '_start'.", 0.02)
    time.sleep(0.5)

    slow_print(f"\n{GREEN}🔍 Checking Registers:{RESET}", 0.02)
    slow_print(f"  (gdb) {BOLD}info registers{RESET}", 0.01)
    slow_print(f"  This command shows the contents of all the CPU registers — super useful!", 0.02)
    time.sleep(1)

    slow_print(f"\n{GREEN}🔬 Step-by-Step Execution:{RESET}", 0.02)
    slow_print(f"  (gdb) {BOLD}stepi{RESET}", 0.01)
    slow_print(f"  Executes the next instruction and pauses again. This is how we walk through code one line at a time.", 0.02)
    time.sleep(1)

    slow_print(f"\n{GREEN}📍 Examining Memory:{RESET}", 0.02)
    slow_print(f"  (gdb) {BOLD}x/10xb $rsp{RESET}", 0.01)
    slow_print(f"  This shows 10 bytes of memory at the stack pointer ($rsp).", 0.02)
    slow_print(f"  You can change the format too: use 'x/4xw' for 4 words in hex, or 'x/8d' for decimal.", 0.02)
    time.sleep(1)

    slow_print(f"\n{GREEN}🔁 Continue Execution:{RESET}", 0.02)
    slow_print(f"  (gdb) {BOLD}continue{RESET}", 0.01)
    slow_print(f"  Continues running the program until the next breakpoint or the end.", 0.02)
    time.sleep(1)

    slow_print(f"\n{GREEN}🏁 Quitting GDB:{RESET}", 0.02)
    slow_print(f"  (gdb) {BOLD}quit{RESET}", 0.01)
    slow_print(f"  You'll be asked to confirm if the program is still running.", 0.02)
    time.sleep(1)

    slow_print(f"\n{YELLOW}🎯 Summary:{RESET}", 0.02)
    slow_print(f"  🔹 Use breakpoints to pause and inspect.", 0.02)
    slow_print(f"  🔹 Use stepi to walk through one instruction at a time.", 0.02)
    slow_print(f"  🔹 Use info registers and x to view what's happening inside.", 0.02)
    slow_print(f"  🔹 Use continue to let your program run again.", 0.02)
    time.sleep(1)

    slow_print(f"\n{BOLD}🎉 Congrats! You've completed Lesson 1 of GDB debugging!{RESET}", 0.02)
    slow_print(f"{CYAN}In the next lesson, you'll learn how to debug more complex logic — loops, function calls, and more!{RESET}", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
