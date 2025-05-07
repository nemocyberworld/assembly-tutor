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
    print(f"\n{BOLD}📦 Memory Addressing & Pointer Arithmetic in x86-64{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 In Assembly, memory is accessed through *addresses*. These are just numbers that tell the CPU where to look in RAM.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}Registers like {BOLD}rax, rbx, rcx...{RESET}{CYAN} can store these addresses, and we use square brackets to dereference them — that means to get the value stored *at* that address.{RESET}")
    time.sleep(1)

    slow_print(f"{GREEN}Let's break this down with some examples...{RESET}")
    time.sleep(1)

    # Example 1: mov rax, [rbx]
    slow_print(f"\n{BOLD}💡 Example 1: mov rax, [rbx]{RESET}")
    slow_print(f"{CYAN}This copies the value from the memory location pointed to by {BOLD}rbx{RESET}{CYAN} into {BOLD}rax{RESET}.{RESET}")
    slow_print(f"{MAGENTA}Think: rax = *(rbx){RESET}")
    time.sleep(1)

    # Simulate pointer access
    memory = {1000: 42}
    rbx = 1000
    slow_print(f"\n{GREEN}🔧 Simulated memory: memory[{rbx}] = {memory[rbx]}{RESET}")
    slow_print(f"  {BOLD}rbx points to:{RESET} {rbx}")
    rax = memory[rbx]
    slow_print(f"  {BOLD}After mov rax, [rbx] → rax:{RESET} {rax}")
    time.sleep(1)

    # Example 2: mov [rbx], rax
    slow_print(f"\n{BOLD}💡 Example 2: mov [rbx], rax{RESET}")
    slow_print(f"{CYAN}This stores the value in {BOLD}rax{RESET}{CYAN} into the memory address pointed to by {BOLD}rbx{RESET}.{RESET}")
    slow_print(f"{MAGENTA}Think: *(rbx) = rax{RESET}")
    rax = 99
    memory[rbx] = rax
    slow_print(f"  {BOLD}rax is now:{RESET} {rax}")
    slow_print(f"  {BOLD}After mov [rbx], rax → memory[{rbx}]:{RESET} {memory[rbx]}")
    time.sleep(1)

    # Example 3: Pointer Arithmetic
    slow_print(f"\n{BOLD}💡 Example 3: add rbx, 8{RESET}")
    slow_print(f"{CYAN}This moves the pointer {BOLD}rbx{RESET} 8 bytes forward — like moving to the next element in an array.{RESET}")
    rbx += 8
    slow_print(f"  {BOLD}After add rbx, 8 → rbx:{RESET} {rbx}")
    time.sleep(1)

    slow_print(f"\n{MAGENTA}📏 In x86-64, most data types are aligned in 8-byte increments. So adding 8 to a pointer moves to the next 64-bit value.{RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🔍 So far we've seen how to read from and write to memory using registers as pointers, and how to move those pointers around.{RESET}")
    time.sleep(1)

    slow_print(f"{GREEN}📌 Mastering memory addressing is key to understanding arrays, structs, and dynamic data!{RESET}")
    time.sleep(1.5)

    print()
    slow_print(f"{BOLD}{CYAN}🧪 In the next lesson, we’ll look at addressing modes like [rbx + 4], [rbp - 8], and how the stack works!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")