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
    print(f"\n{BOLD}🧵 Strings, Arrays, and the .data Section in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}🗃️ The `.data` section is where we define global variables — including strings and arrays — that live in memory when the program starts.{RESET}")
    time.sleep(1)

    slow_print(f"{CYAN}These values don’t change unless we write to them — think of them as persistent constants or global state.{RESET}")
    time.sleep(1)

    # Declaring data
    slow_print(f"\n{BOLD}💡 Declaring strings and arrays in `.data`{RESET}")
    slow_print(f"{CYAN}In NASM (Intel syntax), you'd write something like:{RESET}")

    data_section = [
        "section .data",
        "  message db 'Hello, world!', 0",
        "  numbers dd 1, 2, 3, 4",
    ]
    for line in data_section:
        slow_print(f"  {GREEN}{line}{RESET}")
        time.sleep(0.7)

    slow_print(f"{MAGENTA}🔤 'db' = define byte (used for characters), 'dd' = define doubleword (4 bytes each){RESET}")
    time.sleep(1)

    # Simulate string access
    slow_print(f"\n{CYAN}🔧 Simulating string access in memory...{RESET}")
    message = [ord(c) for c in "Hello, world!"] + [0]
    slow_print(f"  {BOLD}message:{RESET} {message}")
    slow_print(f"  {BOLD}First char (message[0]):{RESET} {chr(message[0])}")
    slow_print(f"  {BOLD}Null terminator:{RESET} {message[-1]}")
    time.sleep(1)

    # Simulate array access
    slow_print(f"\n{BOLD}🧮 Accessing array elements{RESET}")
    numbers = [1, 2, 3, 4]
    slow_print(f"{CYAN}Arrays are just sequential memory. Access using an offset:{RESET}")
    for i, n in enumerate(numbers):
        slow_print(f"  numbers[{i}] = {n}")
        time.sleep(0.5)

    slow_print(f"{MAGENTA}To access numbers[2] in assembly: {BOLD}mov eax, [numbers + 8]{RESET}{MAGENTA} (because 2 × 4 bytes = 8){RESET}")
    time.sleep(1)

    # Summary
    print()
    slow_print(f"{YELLOW}🧾 Summary:{RESET}")
    slow_print(f"{GREEN}✔ The `.data` section holds predefined memory for strings, arrays, and globals{RESET}")
    slow_print(f"{GREEN}✔ Strings are byte arrays ending with 0 (null-terminated){RESET}")
    slow_print(f"{GREEN}✔ Arrays are accessed by calculating the offset: index × size{RESET}")
    time.sleep(1.5)

    slow_print(f"\n{BOLD}{CYAN}🧪 In the next lesson, we’ll build a loop that walks through a string or array and does something useful — like printing characters!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! What would you like to do next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")