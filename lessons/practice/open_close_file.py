# lessons/practice_programs/open_close_file.py

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
    print(f"\n{BOLD}📁 Open and Close a File with Syscalls!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to open a file and close it using Linux system calls in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Place the file name in the `.data` section, null-terminated.",
        "2️⃣  Use the `open` syscall (number 2) to open the file.",
        "3️⃣  The return value will be the file descriptor (like a handle to the file).",
        "4️⃣  Use the `close` syscall (number 3) to safely close the file."
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} Think of opening a file like checking out a book from a library 📖. You get a handle (a file descriptor) — and when you're done, you return it (close it).\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Open and Close 'myfile.txt'{RESET}")
    slow_print(f"""{DIM}
section .data
    filename db "myfile.txt", 0  ; file name (null-terminated)

section .text
    global _start

_start:
    ; open("myfile.txt", O_RDONLY = 0, mode = 0)
    mov     rax, 2            ; syscall: open
    mov     rdi, filename     ; pointer to file name
    xor     rsi, rsi          ; flags = O_RDONLY (0)
    xor     rdx, rdx          ; mode = 0 (not used for read)
    syscall

    ; file descriptor returned in rax
    mov     rdi, rax          ; store file descriptor for closing

    ; close(fd)
    mov     rax, 3            ; syscall: close
    syscall

    ; exit(0)
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Open any file (make sure it exists!) and close it safely. Try with different filenames!\n")

    # Tips
    slow_print(f"{BLUE}💡 Tips:{RESET}")
    slow_print("→ Make sure the file name is null-terminated.")
    slow_print("→ `open` returns -1 if it fails — you can check if `rax` is negative.")
    slow_print("→ You can use flags like `O_WRONLY` (1), `O_RDWR` (2), or `O_CREAT` (64) — combine them with `or`!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try opening the file for writing with `O_WRONLY | O_CREAT`, and create it if it doesn’t exist.")
    slow_print("→ Add logic to print an error message if `open` fails (check if `rax` < 0).")
    slow_print("→ Practice with `read` and `write` next — now that you’ve got file access!\n")

    # Wrap-up
    print(f"\n{BOLD}🏁 Nice work! Now you can work with real files using nothing but syscalls and assembly. Low-level mastery unlocked! 🔓📂{RESET}")
