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
    print(f"\n{BOLD}🧵 Writing a Simple Bootloader (Real Mode x86){RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}💻 A bootloader is the first piece of code the CPU runs after BIOS/UEFI initialization.{RESET}")
    slow_print(f"{CYAN}It's loaded from the very first 512 bytes of the boot device — known as the {BOLD}Master Boot Record (MBR){RESET}{CYAN}.{RESET}")
    time.sleep(1)

    # Requirements
    slow_print(f"\n{BOLD}📐 Constraints of Bootloader Code:{RESET}")
    constraints = [
        "✔ Must be ≤ 512 bytes",
        "✔ Ends with a magic number: 0xAA55 (at offset 510)",
        "✔ Runs in 16-bit real mode (segment:offset addressing)",
        "✔ No standard library, no OS — you talk to BIOS directly"
    ]
    for c in constraints:
        slow_print(f"{MAGENTA}{c}{RESET}")
        time.sleep(0.4)

    # First Code Example
    slow_print(f"\n{BOLD}💡 Minimal Bootloader Example:{RESET}")
    slow_print(f"""{GREEN}NASM syntax:{RESET}{MAGENTA}
org 0x7c00          ; BIOS loads MBR to this address

mov ah, 0x0e        ; BIOS teletype output
mov al, 'H'
int 0x10            ; print 'H'
jmp $

times 510-($-$$) db 0
dw 0xAA55           ; magic number at byte 511
{RESET}""")
    time.sleep(1)

    # Breakdown
    slow_print(f"\n{BOLD}🔍 Breakdown:{RESET}")
    breakdown = [
        "✔ `org 0x7c00`: the origin where BIOS loads the bootloader",
        "✔ `int 0x10`: BIOS interrupt to print characters to screen",
        "✔ `times ...`: fills out remaining bytes to reach 512 total",
        "✔ `0xAA55`: BIOS checks this signature before booting"
    ]
    for line in breakdown:
        slow_print(f"{CYAN}{line}{RESET}")
        time.sleep(0.4)

    # How to Run
    slow_print(f"\n{BOLD}⚙️ How to Run This Bootloader:{RESET}")
    slow_print(f"{MAGENTA}1. Assemble with NASM:{RESET}")
    slow_print(f"   nasm -f bin boot.asm -o boot.img")

    slow_print(f"{MAGENTA}2. Run in QEMU or Bochs:{RESET}")
    slow_print(f"   qemu-system-x86_64 -drive format=raw,file=boot.img")
    time.sleep(1)

    # Limitations
    slow_print(f"\n{BOLD}⚠️ Limitations of Real Mode:{RESET}")
    limits = [
        "✘ No protected memory or paging",
        "✘ Segment:offset addressing (max 1MB)",
        "✘ No multitasking, no syscalls",
        "✔ Can call BIOS to access disk, keyboard, display"
    ]
    for l in limits:
        slow_print(f"{RED if '✘' in l else GREEN}{l}{RESET}")
        time.sleep(0.3)

    # Expanding the Bootloader
    slow_print(f"\n{BOLD}🚀 What Comes Next:{RESET}")
    roadmap = [
        "✔ Load a second-stage bootloader or kernel from disk",
        "✔ Switch to 32-bit or 64-bit mode (protected/long mode)",
        "✔ Set up GDT, stack, and jump to kernel entry point"
    ]
    for r in roadmap:
        slow_print(f"{GREEN}{r}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Modify the bootloader to print 'HELLO' one letter at a time!{RESET}")
    slow_print(f"{MAGENTA}Bonus: Load and jump to a second sector!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Ready to try BIOS disk reads or switch to protected mode next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")