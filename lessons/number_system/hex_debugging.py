import random
import time
import struct

# 🎨 Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🔍 Welcome to Hex Debugging 101!{RESET}")
    slow_print(f"{CYAN}Hex values are your window into memory and stack when debugging low-level programs.")
    slow_print("You’ll learn how to view memory as hex, understand stack contents, and spot bugs! 🐞")
    input(f"\n{YELLOW}Press Enter to begin your memory journey... {RESET}")

def view_memory_simulated(data):
    print(f"\n{BOLD}{BLUE}📦 Simulated Memory (Bytes to Hex){RESET}")
    print(f"{CYAN}Raw Data: {data}{RESET}")
    hex_view = ' '.join(f"{byte:02X}" for byte in data)
    print(f"{YELLOW}Memory Dump (Hex): {hex_view}{RESET}")

def simulate_stack():
    print(f"\n{BOLD}{MAGENTA}🧠 Simulated Stack Push & Pop (Hex View){RESET}")
    stack = []
    
    # Push values (simulate call)
    for val in [0x1000, 0x2000, 0x3000]:
        stack.append(val)
        print(f"{GREEN}PUSH: 0x{val:08X}{RESET}")

    print(f"\n{CYAN}🧾 Stack Snapshot:{RESET}")
    for i, val in enumerate(reversed(stack), 1):
        print(f"{YELLOW}SP-{i*4:02}: 0x{val:08X}{RESET}")

    # Pop (simulate return)
    popped = stack.pop()
    print(f"\n{RED}POP: 0x{popped:08X} (Return Address){RESET}")

def explain_debugging():
    print(f"\n{BOLD}{CYAN}🧠 Debugging with Hex: Why It Matters{RESET}")
    slow_print("✔ Hex lets you see raw memory — what your CPU actually reads")
    slow_print("✔ You can trace values pushed to the stack (function calls, returns)")
    slow_print("✔ Crashes often show hex addresses — knowing how to read them = power 💪")

def interactive_memory_viewer():
    print(f"\n{BOLD}{BLUE}🛠️ Try Viewing Your Own Bytes{RESET}")
    raw = input(f"{YELLOW}Enter ASCII text (e.g., Hello): {RESET}")
    data = raw.encode()
    hex_view = ' '.join(f"{byte:02X}" for byte in data)
    print(f"{GREEN}Hex View: {hex_view}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Debugging Quiz Time!{RESET}")
    score = 0

    questions = [
        ("What does the hex 0x41414141 represent in ASCII?", "AAAA"),
        ("Which direction does the stack grow?", "Down"),
        ("What's the hex of ASCII 'Hi'?", "4869"),
    ]

    for i, (q, correct) in enumerate(questions, 1):
        user = input(f"\n{YELLOW}Q{i}: {q} {RESET}\nYour Answer: ").strip().upper()
        if correct.upper() in user:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! Answer: {correct}{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Finished! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🧠 Debugging Master! Nice work!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Almost there! Just one bug left!{RESET}")
    else:
        print(f"{RED}🔁 Keep practicing — you'll be a memory ninja soon!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Memory and stack are visualized in hexadecimal in low-level debugging")
    slow_print("✔ ASCII and function return addresses often appear in hex")
    slow_print("✔ You can simulate and explore memory behavior using Python!")
    print(f"{GREEN}You're now a debugger with X-ray vision into the stack! 🕵️‍♂️{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explain_debugging()
    view_memory_simulated(b"Debug")
    simulate_stack()
    interactive_memory_viewer()
    quiz()
    summary()

if __name__ == "__main__":
    run()
