# lessons/practice_programs/elf_parser.py

import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    print(f"\n{BOLD}📦 elf_parser: Parse ELF Headers Manually{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to read and interpret the header of an ELF binary file by directly inspecting its bytes.\n")
    time.sleep(0.5)

    # Why Learn This
    slow_print(f"{BLUE}💡 Why Is This Cool?{RESET}")
    slow_print("→ ELF (Executable and Linkable Format) is the backbone of Linux executables.")
    slow_print("→ Understanding ELF helps in reverse engineering, binary exploitation, and low-level debugging.\n")

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Open the ELF file in binary mode using syscalls or C file IO.",
        "2️⃣  Read the first 64 bytes (that's the ELF header).",
        "3️⃣  Parse key fields: magic number, architecture, entry point, etc.",
        "4️⃣  Print them out nicely for human eyes!",
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}🗃️ Analogy:{RESET} Think of the ELF header like the table of contents in a book—it tells you what’s inside and where to find it.\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Parse ELF Magic and Entry Point (in C){RESET}")
    slow_print(f"""{DIM}
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdint.h>

int main() {
    int fd = open("some_binary", O_RDONLY);
    if (fd < 0) return 1;

    unsigned char header[64];
    read(fd, header, 64);

    printf("Magic: %02x %02x %02x %02x\\n", header[0], header[1], header[2], header[3]);
    uint64_t entry = *(uint64_t*)(header + 24);
    printf("Entry point: 0x%lx\\n", entry);

    close(fd);
    return 0;
}
{RESET}""")

    # Tips
    slow_print(f"\n{BLUE}📌 Tips:{RESET}")
    slow_print("→ The ELF header starts with 0x7F followed by 'E', 'L', 'F'.")
    slow_print("→ Use the ELF64 spec to understand all 64 bytes of the header.")
    slow_print("→ Use `readelf -h <file>` to compare your parsed output!")

    # Bonus
    slow_print(f"\n{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Parse and print the section header offset and number of sections.")
    slow_print("→ Try loading a 32-bit ELF too. Can your parser adapt? 🤓")

    # Wrap-up
    print(f"\n{GREEN}{BOLD}🏁 Bravo! You just peered into the inner workings of a Linux binary. Welcome to the world of binary ninjas! 🥷📂{RESET}")
