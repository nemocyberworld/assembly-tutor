# lessons/memory/memory_layout_view.py

import time
import random
import string

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
    print(f"{BOLD}{MAGENTA}🧠 Peek Into Process Memory!{RESET}")
    slow_print(f"{CYAN}Ever wonder how your program's memory looks?")
    slow_print("Let’s simulate reading memory using hex and ASCII side-by-side.")
    slow_print("You’ll see data like a debugger — real hacker vibes! 😎")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def generate_fake_memory():
    # Simulated memory: mix of text and random bytes
    memory = b''.join(random.choice(string.ascii_letters + string.digits).encode() for _ in range(64))
    return memory

def hex_ascii_line(address, data):
    hex_part = ' '.join(f"{b:02X}" for b in data)
    ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in data)
    return f"{BLUE}{address:08X}{RESET}  {YELLOW}{hex_part:<47}{RESET} {GREEN}|{ascii_part}|{RESET}"

def view_memory():
    memory = generate_fake_memory()
    print(f"\n{BOLD}{BLUE}🔍 Simulated Memory Dump:{RESET}")
    for i in range(0, len(memory), 16):
        line = hex_ascii_line(0x1000 + i, memory[i:i+16])
        print(line)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Memory Reading Quiz!{RESET}")
    sample = b'HelloWorld123456'
    print(f"{BLUE}Memory Line:{RESET} {hex_ascii_line(0x2000, sample)}")
    guess = input(f"{YELLOW}🧠 What ASCII string do you see on the right? {RESET}").strip()
    if guess == "HelloWorld123456":
        print(f"{GREEN}✅ Spot on! You're seeing memory like a pro!{RESET}")
    else:
        print(f"{RED}❌ Not quite. It was 'HelloWorld123456'{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Memory can be viewed as Hex + ASCII side-by-side")
    slow_print("✔ Non-printable bytes are shown as '.' in ASCII view")
    slow_print("✔ This technique is used in debuggers and hex editors")
    print(f"{GREEN}Keep peeking—you’re becoming a memory master! 🧠💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    view_memory()
    quiz()
    summary()

if __name__ == "__main__":
    run()
