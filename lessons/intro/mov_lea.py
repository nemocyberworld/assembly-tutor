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
    print(f"\n{BOLD}🚚 Data Movement in Assembly: {CYAN}mov{RESET} and {CYAN}lea{RESET}{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}Assembly is all about moving stuff around — from memory to registers, registers to registers, and more!{RESET}")
    time.sleep(1)
    slow_print(f"{YELLOW}Two of the most important instructions for this are: {BOLD}mov{RESET} and {BOLD}lea{RESET}.{RESET}")
    time.sleep(1.5)

    print(f"\n{CYAN}{BOLD}📦 The mov Instruction{RESET}\n")
    slow_print(f"{GREEN}{BOLD}mov destination, source{RESET}")
    slow_print(f"{CYAN}➡️ This copies data from the source and places it into the destination.{RESET}")
    time.sleep(1)

    slow_print(f"\n{MAGENTA}Example 1: Moving a number into a register{RESET}")
    slow_print(f"{GREEN}mov rax, 5{RESET}       🧮 Now rax holds the value 5")
    time.sleep(0.8)

    slow_print(f"\n{MAGENTA}Example 2: Moving one register into another{RESET}")
    slow_print(f"{GREEN}mov rbx, rax{RESET}     🔁 Copy whatever is in rax into rbx")
    time.sleep(0.8)

    slow_print(f"\n{MAGENTA}Example 3: Moving data from memory to register{RESET}")
    slow_print(f"{GREEN}mov rax, [var]{RESET}   📦 Load the value stored at memory location 'var' into rax")
    time.sleep(1)

    slow_print(f"\n{RED}❗ Important: {RESET}{YELLOW}mov copies data, it doesn't move it in the 'cut-paste' sense — the original stays where it was!{RESET}")
    time.sleep(2)

    print(f"\n{CYAN}{BOLD}🔍 The lea Instruction (Load Effective Address){RESET}\n")
    slow_print(f"{GREEN}{BOLD}lea destination, [expression]{RESET}")
    slow_print(f"{CYAN}➡️ lea is like mov, but instead of copying the value at a memory address, it copies the address itself!{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{MAGENTA}Example 4: Getting an address instead of a value{RESET}")
    slow_print(f"{GREEN}lea rsi, [var]{RESET}   🧭 rsi now holds the address of 'var', not its content")
    time.sleep(1)

    slow_print(f"\n{MAGENTA}Example 5: Using lea for arithmetic tricks{RESET}")
    slow_print(f"{GREEN}lea rax, [rbx + rcx*4]{RESET}   ➕ rax = rbx + rcx*4 (no memory access!)")
    slow_print(f"{YELLOW}💡 This is faster than doing actual math with add/mul because lea doesn't touch memory!{RESET}")
    time.sleep(2)

    print()
    slow_print(f"{BOLD}{CYAN}🧪 Let's simulate how these instructions behave...{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}{GREEN}🧠 Initial State:{RESET}")
    slow_print(f"  rax = 0, rbx = 10, rcx = 2")
    time.sleep(1)

    print(f"\n{BOLD}{GREEN}💡 Step 1: {RESET}{GREEN}mov rax, rbx{RESET}")
    slow_print(f"  ➡️ Copy rbx into rax → rax = 10")
    time.sleep(1)

    print(f"\n{BOLD}{GREEN}💡 Step 2: {RESET}{GREEN}lea rdx, [rbx + rcx*4]{RESET}")
    slow_print(f"  ➡️ Compute address-like math → rdx = 10 + 2*4 = 18")
    time.sleep(1)

    slow_print(f"\n{YELLOW}⚙️ This shows how lea can be used like a math helper without touching memory.{RESET}")
    time.sleep(1.5)

    print()
    slow_print(f"{CYAN}🔐 Summary:{RESET}")
    summary = [
        f"{GREEN}✅ {BOLD}mov{RESET}{GREEN} is used to copy values — from constants, memory, or other registers.{RESET}",
        f"{GREEN}✅ {BOLD}lea{RESET}{GREEN} is used to load an address (or do address math). It’s sneaky-powerful!{RESET}",
        f"{GREEN}🚀 You'll use these constantly — they are the bread and butter of Assembly programming!{RESET}",
    ]
    for line in summary:
        slow_print(line)
        time.sleep(1)

    print()
    slow_print(f"{BOLD}{MAGENTA}🧠 Coming up: Using mov and lea to manipulate variables and work with memory!{RESET}")
    time.sleep(1.5)
    print(f"\n{BOLD}📚 Lesson complete! Ready to experiment with mov and lea in code?{RESET}")

