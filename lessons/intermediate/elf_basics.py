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
    print(f"\n{BOLD}📦 How Assembly Fits in ELF Binaries (Executable and Linkable Format){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🧱 When you write Assembly and compile it, the result is an ELF binary — the standard format on Linux systems.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}This format structures code and data so the OS knows how to load and run your program.{RESET}")
    time.sleep(1)

    # What is an ELF
    slow_print(f"\n{BOLD}🔍 What's in an ELF binary?{RESET}")
    slow_print(f"{GREEN}An ELF file has a header, sections, and segments — each playing a different role.{RESET}")
    time.sleep(0.7)

    slow_print(f"\n{BOLD}📁 Sections (used during linking):{RESET}")
    sections = [
        (".text", "Contains your actual code (instructions)"),
        (".data", "Holds initialized writable data (e.g., strings)"),
        (".bss", "Uninitialized data (e.g., buffers, variables)"),
        (".rodata", "Read-only constants"),
        (".symtab", "Symbol table for labels and functions"),
        (".strtab", "String table (for symbol names)"),
    ]
    for name, desc in sections:
        slow_print(f"  {GREEN}{name:<8}{RESET} - {desc}")
        time.sleep(0.5)

    slow_print(f"\n{BOLD}🚚 Segments (used during execution):{RESET}")
    slow_print(f"{MAGENTA}The loader reads segments to create a running process. Examples include:{RESET}")
    slow_print(f"  {GREEN}LOAD{RESET} - code/data loaded into memory")
    slow_print(f"  {GREEN}DYNAMIC{RESET} - dynamic linking info (for shared libs)")
    slow_print(f"  {GREEN}INTERP{RESET} - path to dynamic linker (ld-linux)")

    time.sleep(1)

    # Entry point
    slow_print(f"\n{BOLD}🎯 Entry Point and _start:{RESET}")
    slow_print(f"{CYAN}Your assembly program begins at a label like {BOLD}_start{RESET}{CYAN}, which is marked as the entry point in the ELF header.{RESET}")
    slow_print(f"{MAGENTA}This is where execution begins when the program is loaded!{RESET}")
    time.sleep(1)

    # Tools
    slow_print(f"\n{BOLD}🛠 Tools to inspect ELF binaries:{RESET}")
    tools = [
        ("readelf -h", "View the ELF header"),
        ("readelf -S", "List all sections"),
        ("objdump -d", "Disassemble the .text section (shows instructions)"),
        ("objdump -x", "Show symbol and section headers"),
        ("file", "Identify the file type (e.g., ELF 64-bit LSB)"),
    ]
    for cmd, desc in tools:
        slow_print(f"  {GREEN}{cmd:<15}{RESET} - {desc}")
        time.sleep(0.4)

    # Compilation pipeline
    slow_print(f"\n{BOLD}⚙️ Compilation Pipeline Overview:{RESET}")
    steps = [
        "1. Write your assembly (.s or .asm)",
        "2. Use `nasm` or `as` to assemble it into an object file (.o)",
        "3. Use `ld` or `gcc` to link it into an ELF binary",
    ]
    for step in steps:
        slow_print(f"{YELLOW}{step}{RESET}")
        time.sleep(0.5)

    # Visual
    slow_print(f"\n{CYAN}🧩 ELF combines your code, data, and metadata into a single file the OS can run.{RESET}")
    slow_print(f"{GREEN}Assembly is the raw material — ELF is the container!{RESET}")
    time.sleep(1.2)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ ELF is the standard binary format on Linux{RESET}")
    slow_print(f"{GREEN}✔ Your assembly code ends up in sections like .text and .data{RESET}")
    slow_print(f"{GREEN}✔ The entry point tells the OS where to begin execution{RESET}")
    slow_print(f"{GREEN}✔ Tools like objdump and readelf help you explore ELF files{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Up next: We'll explore how to inject and run shellcode from an ELF file!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")