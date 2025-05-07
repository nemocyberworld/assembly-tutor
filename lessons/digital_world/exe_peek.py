# lessons/binary/exe_peek.py

import time

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
    print(f"{BOLD}{MAGENTA}🔍 Peek Into Linux Binaries!{RESET}")
    slow_print(f"{CYAN}Did you know Linux executables start with a special magic number?")
    slow_print("That's right — they're called ELF files!")
    slow_print("Let’s open one, decode some bytes, and uncover the binary mystery 🧠💻")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def read_elf_header(file_path):
    try:
        with open(file_path, "rb") as f:
            header = f.read(16)
            return header
    except FileNotFoundError:
        print(f"{RED}❌ File not found: {file_path}{RESET}")
        return None

def show_elf_header():
    print(f"\n{BOLD}{BLUE}📁 Loading ELF Header (simulated)...{RESET}")
    elf_header = b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'  # Fake ELF header

    print(f"{GREEN}Bytes:{RESET} ", ' '.join(f"{b:02X}" for b in elf_header))
    print(f"{CYAN}Meaning:{RESET}")
    slow_print("• \x7fELF → Magic number (identifies the file as ELF)", 0.01)
    slow_print("• 02    → 64-bit format", 0.01)
    slow_print("• 01    → Little Endian", 0.01)
    slow_print("• 01    → ELF version", 0.01)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick Quiz: ELF Magic Bytes{RESET}")
    answer = input(f"{YELLOW}What are the first 4 bytes of any ELF file (in hex)? {RESET}").strip().upper()
    if answer.replace(" ", "") == "7F454C46":
        print(f"{GREEN}✅ Correct! That's \\x7F 'E' 'L' 'F' — the ELF magic!{RESET}")
    else:
        print(f"{RED}❌ Nope! It's: 7F 45 4C 46{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ELF files begin with a magic number: 0x7F followed by 'ELF'", 0.02)
    slow_print("✔ You can inspect any file in hex using Python or tools like `hexdump`", 0.02)
    slow_print("✔ ELF headers tell the system how to load and run a program", 0.02)
    print(f"{GREEN}You're now a binary detective! 🕵️‍♀️🔢{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_elf_header()
    quiz()
    summary()
