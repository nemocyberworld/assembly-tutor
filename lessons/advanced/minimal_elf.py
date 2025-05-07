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
    print(f"\n{BOLD}📦 Writing Minimal ELF Binaries by Hand (x86-64){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧠 ELF (Executable and Linkable Format) is the standard binary format on Linux.{RESET}")
    slow_print(f"{CYAN}Most compilers generate massive ELF binaries — but we can craft the bare minimum by hand!{RESET}")
    time.sleep(1)

    slow_print(f"\n{BOLD}🔧 Goal: Write a 100–200 byte ELF binary that prints 'Hi' and exits cleanly.{RESET}")
    time.sleep(1)

    # Concept
    slow_print(f"\n{BOLD}📐 Minimal ELF Requirements:{RESET}")
    items = [
        "🔹 ELF Header (64 bytes)",
        "🔹 One Program Header (56 bytes)",
        "🔹 Code section with raw instructions",
    ]
    for item in items:
        slow_print(f"{GREEN}{item}{RESET}")
        time.sleep(0.4)

    slow_print(f"\n{MAGENTA}🔹 No need for .text, .data, or even a symbol table! Just binary headers + instructions.{RESET}")
    time.sleep(1)

    # Architecture
    slow_print(f"\n{BOLD}🏗️ ELF Architecture (Barebones){RESET}")
    layout = [
        "[0x00] ELF Header",
        "[0x40] Program Header (PT_LOAD)",
        "[0x78] Code: syscall instructions (write + exit)"
    ]
    for part in layout:
        slow_print(f"{CYAN}{part}{RESET}")
        time.sleep(0.4)

    # Hex code walk-through
    slow_print(f"\n{BOLD}💡 Example: Hand-Crafted ELF Binary (Hex View){RESET}")
    slow_print(f"{YELLOW}This binary prints 'Hi\\n' using the write syscall, then exits.{RESET}")
    example = [
        "7f 45 4c 46             ; Magic: 0x7F 'E' 'L' 'F'",
        "02 01 01 00             ; 64-bit, little-endian",
        "00...                   ; padding",
        "type: ET_EXEC, machine: EM_X86_64",
        "entry: 0x78             ; entry point → start of code",
        "phoff: 0x40             ; program header offset",
        "1 program header (PT_LOAD), R-X permissions",
        "---",
        "code:                   ; at offset 0x78",
        "mov rax, 1              ; syscall: write",
        "mov rdi, 1              ; fd: stdout",
        "lea rsi, [rip+msg]      ; ptr to 'Hi\\n'",
        "mov rdx, 3              ; length",
        "syscall",
        "mov rax, 60             ; syscall: exit",
        "xor rdi, rdi            ; status = 0",
        "syscall",
        "msg: db 'Hi\\n'"
    ]
    for line in example:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    slow_print(f"\n{BOLD}📦 Final Binary Size: ~150 bytes{RESET}")
    slow_print(f"{CYAN}You can assemble it with `nasm`, set the headers with a hex editor, or generate it with Python.{RESET}")
    time.sleep(1)

    # Tips
    slow_print(f"\n{BOLD}🛠️ Pro Tips for Minimal ELF Crafting:{RESET}")
    tips = [
        "✔ Use PT_LOAD only — no need for section headers",
        "✔ Set e_entry to your code offset",
        "✔ Avoid relocations and dynamic linking",
        "✔ Syscalls are your best friend"
    ]
    for tip in tips:
        slow_print(f"{MAGENTA}{tip}{RESET}")
        time.sleep(0.4)

    # Summary
    slow_print(f"\n{YELLOW}🧾 Summary:{RESET}")
    summary = [
        "✔ You can craft a minimal ELF binary by manually writing the headers and raw code",
        "✔ Use syscalls directly to avoid libc",
        "✔ Resulting binary can be under 200 bytes!"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Write a 128-byte ELF binary that echoes 'Done'! No compiler allowed!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want help with assembling one from scratch in Python or NASM?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")