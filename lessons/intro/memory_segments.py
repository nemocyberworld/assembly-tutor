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
    slow_print(f"\n🧠 {BOLD}Lesson: Memory Segments in x86-64 Assembly{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}🏗️ Every Assembly program is split into memory segments. Each serves a specific purpose.{RESET}", 0.02)
    slow_print(f"{YELLOW}🔍 Let's explore the three main ones: {CYAN}.data{YELLOW}, {CYAN}.bss{YELLOW}, and {CYAN}.text{YELLOW}.{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}📦 1. .data Segment – Initialized Data{RESET}", 0.02)
    slow_print(f"{GREEN}Stores variables that are declared and initialized with a value before the program runs.{RESET}", 0.02)
    slow_print(f"{MAGENTA}Think of this as: 'Hey computer, I already know what this variable should be!'{RESET}\n", 0.02)

    slow_print(f"{CYAN}{BOLD}Example:{RESET}", 0.02)
    slow_print(f"""
  {CYAN}section .data{RESET}
  {CYAN}greeting db "Hello", 0{RESET}    {MAGENTA}; initialized string with null terminator{RESET}
    """, 0.01)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}📦 2. .bss Segment – Uninitialized Data{RESET}", 0.02)
    slow_print(f"{GREEN}Holds variables that are declared but not initialized.{RESET}", 0.02)
    slow_print(f"{MAGENTA}This is for saying: 'I’ll need this variable later, but I don't have a value yet.'{RESET}\n", 0.02)

    slow_print(f"{CYAN}{BOLD}Example:{RESET}", 0.02)
    slow_print(f"""
  {CYAN}section .bss{RESET}
  {CYAN}buffer resb 64{RESET}        {MAGENTA}; reserve 64 bytes for buffer (no initial value){RESET}
    """, 0.01)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🎬 3. .text Segment – Code Lives Here!{RESET}", 0.02)
    slow_print(f"{GREEN}Contains the actual instructions your CPU will execute. This is where your program starts running.{RESET}", 0.02)
    slow_print(f"{MAGENTA}This is the action movie segment: all the code, drama, and syscalls happen here!{RESET}\n", 0.02)

    slow_print(f"{CYAN}{BOLD}Example:{RESET}", 0.02)
    slow_print(f"""
  {CYAN}section .text{RESET}
  {CYAN}global _start{RESET}

  {CYAN}_start:{RESET}
      {CYAN}mov rax, 60{RESET}         {MAGENTA}; syscall: exit{RESET}
      {CYAN}xor rdi, rdi{RESET}        {MAGENTA}; status code 0{RESET}
      {CYAN}syscall{RESET}            {MAGENTA}; execute the syscall{RESET}
    """, 0.01)
    time.sleep(1)

    slow_print(f"{BOLD}{GREEN}✅ Summary:{RESET}", 0.02)
    slow_print(f"""
{CYAN}.data{RESET}  - Initialized variables  
{CYAN}.bss{RESET}   - Uninitialized variables (just space)  
{CYAN}.text{RESET}  - Your program's instructions (code)

{YELLOW}🧪 When assembling, the OS loads each segment into different parts of memory. Understanding them helps avoid bugs and use memory efficiently!{RESET}
""", 0.01)

    time.sleep(1)
    slow_print(f"{BOLD}{CYAN}🚀 Now go write your own `.data`, `.bss`, and `.text` and make the CPU dance! 💃🕺{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
