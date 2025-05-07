# lessons/practice_programs/read_file.py

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
    print(f"\n{BOLD}📖 Read a File and Print Its Contents!{RESET}\n")
    time.sleep(1)

    # Goal
    slow_print(f"{CYAN}Goal:{RESET} Learn how to open a file, read its contents, and print them to the screen using syscalls in assembly.\n")
    time.sleep(0.5)

    # Instructions
    slow_print(f"{YELLOW}🔧 Instructions:{RESET}")
    steps = [
        "1️⃣  Use the `open` syscall to open a file in read-only mode.",
        "2️⃣  Use the `read` syscall to load file contents into a buffer.",
        "3️⃣  Use the `write` syscall to send the buffer to stdout.",
        "4️⃣  Close the file when you're done!"
    ]
    for step in steps:
        slow_print(f"{MAGENTA}{step}{RESET}")
        time.sleep(0.3)

    # Analogy
    slow_print(f"\n{BLUE}💡 Analogy:{RESET} It's like picking up a book (open), reading a page into your head (read), and saying it out loud (write)! 📚🧠🗣️\n")

    # Example
    slow_print(f"{BOLD}🧠 Example: Read and Print 'myfile.txt'{RESET}")
    slow_print(f"""{DIM}
section .data
    filename db "myfile.txt", 0       ; file to read
    buffer   times 256 db 0           ; space to read into

section .text
    global _start

_start:
    ; open("myfile.txt", O_RDONLY)
    mov     rax, 2                    ; syscall: open
    mov     rdi, filename             ; pointer to filename
    xor     rsi, rsi                  ; flags: O_RDONLY = 0
    xor     rdx, rdx                  ; mode = 0 (unused for read)
    syscall
    mov     r12, rax                  ; save file descriptor in r12

    ; read(fd, buffer, 256)
    mov     rax, 0                    ; syscall: read
    mov     rdi, r12                  ; file descriptor
    mov     rsi, buffer               ; buffer to store data
    mov     rdx, 256                  ; number of bytes to read
    syscall
    mov     r13, rax                  ; number of bytes actually read

    ; write(1, buffer, r13)
    mov     rax, 1                    ; syscall: write
    mov     rdi, 1                    ; file descriptor: stdout
    mov     rsi, buffer               ; buffer with content
    mov     rdx, r13                  ; number of bytes to write
    syscall

    ; close(fd)
    mov     rax, 3
    mov     rdi, r12
    syscall

    ; exit(0)
    mov     rax, 60
    xor     rdi, rdi
    syscall
{RESET}""")

    # Task
    slow_print(f"\n{GREEN}🎯 Your Task:{RESET} Create a file called `hello.txt`, then write assembly code to read and display its contents!")

    # Tips
    slow_print(f"\n{BLUE}💡 Tips:{RESET}")
    slow_print("→ Make sure the file exists in the same folder as your assembly program.")
    slow_print("→ Use `times` to create a buffer (e.g., 256 bytes).")
    slow_print("→ `read` returns the number of bytes it actually read — use that with `write`!")

    # Bonus
    slow_print(f"{BOLD}🎯 Bonus Challenge:{RESET}")
    slow_print("→ Try looping to read files larger than 256 bytes.")
    slow_print("→ Add a check to make sure `open` or `read` didn't return -1 (error).")
    slow_print("→ Read from one file and write to another to make a simple file copier!")

    # Wrap-up
    print(f"\n{BOLD}🏁 Great job! Now you know how to read and display files like a true systems programmer. 🧠💾✨{RESET}")
