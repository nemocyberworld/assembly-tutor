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
    slow_print(f"\n{BOLD}🛠️ NASM Basics: Write, Assemble, and Run Assembly Code{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}✍️ First, let’s write some basic x86-64 Assembly code using NASM syntax.{RESET}", 0.02)
    time.sleep(1)

    slow_print(f"\n{CYAN}{BOLD}📄 hello.asm:{RESET}\n", 0.02)
    code = [
        ("section .data", "🗃️ Data section for constants"),
        ('msg db "Hello, NASM!", 0xa', "💬 Our string ends with newline"),
        ("len equ $ - msg", "📏 Compute length of the message"),
        ("", ""),
        ("section .text", "🎬 Code section"),
        ("global _start", "🚀 Entry point for the program"),
        ("", ""),
        ("_start:", "🟢 Program starts here"),
        ("mov rax, 1", "🧠 syscall number for write"),
        ("mov rdi, 1", "🖥️ stdout"),
        ("mov rsi, msg", "📍 pointer to message"),
        ("mov rdx, len", "📐 message length"),
        ("syscall", "📣 call kernel"),
        ("", ""),
        ("mov rax, 60", "🔚 syscall number for exit"),
        ("xor rdi, rdi", "🧼 exit code 0"),
        ("syscall", "🏁 end program"),
    ]

    for line, comment in code:
        if line.strip() == "":
            print()
            continue
        slow_print(f"  {CYAN}{line:<35}{RESET} {MAGENTA}{comment}{RESET}", 0.01)
        time.sleep(0.25)

    slow_print(f"\n{BOLD}🧰 Now let’s assemble and run it!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{BOLD}📌 Step 1: Save the file as:{RESET} {CYAN}hello.asm{RESET}")
    slow_print(f"{BOLD}📌 Step 2: Assemble it with NASM:{RESET} {GREEN}nasm -f elf64 hello.asm -o hello.o{RESET}")
    slow_print(f"{BOLD}📌 Step 3: Link it with ld:{RESET} {GREEN}ld hello.o -o hello{RESET}")
    slow_print(f"{BOLD}📌 Step 4: Run it:{RESET} {GREEN}./hello{RESET}")
    time.sleep(1)

    slow_print(f"\n{GREEN}💡 You should see:{RESET} {MAGENTA}Hello, NASM!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}🔍 What’s happening?{RESET}")
    slow_print("You're using NASM (Netwide Assembler) to convert human-readable Assembly into machine code.")
    slow_print("Then `ld` (the linker) creates the executable program.")
    time.sleep(1)

    slow_print(f"\n{BOLD}🎉 Great job! You’ve completed your first full Assembly lifecycle: write → assemble → link → run!{RESET}", 0.03)
    slow_print(f"{BOLD}{CYAN}Next stop: more complex programs and fun with syscalls! 🧠💻{RESET}\n", 0.03)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

