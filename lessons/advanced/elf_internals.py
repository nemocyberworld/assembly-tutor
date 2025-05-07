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
    print(f"\n{BOLD}📦 ELF Internals: Sections, Headers, and Linking{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🔍 ELF (Executable and Linkable Format) is the standard binary format used on Linux systems for executables, shared libs, and object files.{RESET}")
    time.sleep(1)

    # Basic layout
    slow_print(f"\n{BOLD}🗂️ Basic Structure of an ELF Binary:{RESET}")
    layout = [
        "• ELF Header       – Metadata for loaders and tools",
        "• Program Headers  – How the binary should be loaded in memory",
        "• Section Headers  – Describe the layout of sections like .text, .data",
        "• Sections         – Contain actual code, data, symbols, etc."
    ]
    for item in layout:
        slow_print(f"{CYAN}{item}{RESET}")
        time.sleep(0.4)

    # ELF Header
    slow_print(f"\n{BOLD}📘 ELF Header:{RESET}")
    header_info = [
        "Magic bytes:       \\x7F 'E' 'L' 'F'",
        "Class:             32-bit or 64-bit",
        "Endianness:        Little or big",
        "Type:              Executable, relocatable, shared object, core dump",
        "Entry point:       Address where execution starts"
    ]
    for line in header_info:
        slow_print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)

    # Program vs Section headers
    slow_print(f"\n{GREEN}🤔 Program Headers vs Section Headers:{RESET}")
    slow_print(f"{CYAN}• Program headers are for the OS loader → how to map the file into memory")
    slow_print(f"• Section headers are for the linker → how to link and relocate code and data{RESET}")
    time.sleep(1)

    # Common sections
    slow_print(f"\n{BOLD}🧱 Common Sections:{RESET}")
    sections = [
        ".text    – Executable code",
        ".data    – Initialized global variables",
        ".bss     – Uninitialized globals (zeroed by loader)",
        ".rodata  – Read-only data (e.g. const strings)",
        ".symtab  – Symbol table (for linking)",
        ".strtab  – String table (symbol names)",
        ".rel/.rela – Relocation info"
    ]
    for s in sections:
        slow_print(f"{CYAN}{s}{RESET}")
        time.sleep(0.3)

    # Linking
    slow_print(f"\n{BOLD}🔗 Linking Process:{RESET}")
    linking_steps = [
        "1️⃣ Compiler produces .o (object) files with code/data/symbols",
        "2️⃣ Linker combines .o files into a final ELF executable",
        "3️⃣ It resolves symbols, applies relocations, and writes final sections",
        "4️⃣ Loader reads program headers and maps segments into memory"
    ]
    for step in linking_steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.4)

    # Inspecting ELF files
    slow_print(f"\n{YELLOW}🛠️ Tools to Explore ELF Files:{RESET}")
    tools = [
        "📄 `readelf -a <file>`    – full ELF structure",
        "🧠 `objdump -D <file>`     – disassembly of .text",
        "🧪 `xxd` or `hexdump`     – raw binary view",
        "🔍 `file <file>`          – basic ELF metadata",
        "🧵 `nm <file>`            – show symbols"
    ]
    for tool in tools:
        slow_print(f"{GREEN}{tool}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ ELF contains headers, sections, and metadata for loading/linking",
        "✔ Program headers = runtime loader view",
        "✔ Section headers = linker view",
        "✔ Tools like `readelf`, `objdump`, and `nm` are essential for reverse engineering"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Use `readelf` and `objdump` on a binary to locate the entry point and disassemble its `.text` section.{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to go deeper with relocation entries or try building a custom linker?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
