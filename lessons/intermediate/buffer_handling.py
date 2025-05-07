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
    print(f"\n{BOLD}📥 Handling Buffers and Input in x86-64 (Linux){RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}💡 Reading user input in Assembly means interacting directly with the OS — no high-level helpers here!{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}We'll use the {BOLD}read{RESET}{CYAN} syscall (number 0) to fill a buffer from stdin (fd = 0).{RESET}")
    time.sleep(1)

    # Syscall layout
    slow_print(f"\n{BOLD}📌 read syscall (Linux x86-64):{RESET}")
    syscall_args = [
        ("rax", "0      (sys_read)"),
        ("rdi", "0      (file descriptor: stdin)"),
        ("rsi", "buffer (pointer to memory)"),
        ("rdx", "length (max bytes to read)")
    ]
    for reg, val in syscall_args:
        slow_print(f"  {BOLD}{reg:<4}{RESET} → {val}")
        time.sleep(0.4)

    slow_print(f"{MAGENTA}After the syscall, rax will contain the number of bytes actually read.{RESET}")
    time.sleep(1)

    # Example with .bss
    slow_print(f"\n{BOLD}💡 Example: Reading up to 100 bytes into a buffer{RESET}")
    slow_print(f"{CYAN}We’ll declare the buffer in the {BOLD}.bss{RESET}{CYAN} section (uninitialized data).{RESET}")
    time.sleep(1)

    code = [
        "section .bss",
        "    buffer resb 100",  # reserve 100 bytes
        "",
        "section .text",
        "    global _start",
        "",
        "_start:",
        "    mov rax, 0          ; syscall: read",
        "    mov rdi, 0          ; file descriptor: stdin",
        "    mov rsi, buffer     ; pointer to buffer",
        "    mov rdx, 100        ; max bytes to read",
        "    syscall",
        "",
        "    ; rax now holds number of bytes read",
        "",
        "    ; (optional) write buffer to stdout to confirm",
        "    mov rdi, 1          ; stdout",
        "    mov rax, 1          ; syscall: write",
        "    syscall",
        "",
        "    ; exit cleanly",
        "    mov rax, 60         ; syscall: exit",
        "    xor rdi, rdi",
        "    syscall"
    ]
    for line in code:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.4)

    slow_print(f"{MAGENTA}✅ After reading, your buffer in memory now holds what the user typed!{RESET}")
    time.sleep(1)

    # Notes on buffers
    slow_print(f"\n{YELLOW}📎 Notes on Buffer Safety:{RESET}")
    slow_print(f"{RED}⚠️ Be careful not to overflow buffers — always check how many bytes were read!{RESET}")
    slow_print(f"{GREEN}✔ Use rax (return value) to safely work with only the valid data.{RESET}")
    time.sleep(1.2)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ Use syscall 0 (read) with rsi pointing to a buffer, and rdx as max length{RESET}")
    slow_print(f"{GREEN}✔ Declare buffers in the {BOLD}.bss{RESET}{GREEN} section with {BOLD}resb{RESET}{GREEN}{RESET}")
    slow_print(f"{GREEN}✔ The return value (rax) tells you how much was actually read{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 Next up: We’ll learn how to parse and process this input — like turning strings into numbers!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")