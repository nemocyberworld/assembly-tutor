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
    slow_print(f"\n🧩 {BOLD}Lesson: Exit Codes and Program Termination in Assembly{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}🚪 Every program eventually ends — and how it exits matters!{RESET}", 0.02)
    slow_print(f"{YELLOW}💡 In Linux, programs return an {BOLD}exit code{RESET}{YELLOW} to signal success or failure.{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🧠 Why Exit Codes Matter:{RESET}", 0.02)
    slow_print(f"""
{GREEN}✔️ 0{RESET}   = Success  
{RED}❌ non-zero{RESET} = Error (specific meaning depends on your program)

These codes help other programs, scripts, or users know what happened.
""", 0.01)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🔚 Exiting Gracefully with `syscall`:{RESET}", 0.02)
    slow_print(f"{MAGENTA}Use syscall number 60 (exit). Pass the exit code in rdi.{RESET}", 0.02)

    slow_print(f"""
{CYAN}mov rax, 60{RESET}       {MAGENTA}; syscall: exit
{CYAN}mov rdi, 0{RESET}        {MAGENTA}; exit code 0 (success)
{CYAN}syscall{RESET}           {MAGENTA}; tell kernel we're done
""", 0.01)

    slow_print(f"{CYAN}{BOLD}📌 Example with Non-Zero Exit Code:{RESET}", 0.02)
    slow_print(f"""
{CYAN}mov rax, 60{RESET}       {MAGENTA}; syscall: exit
{CYAN}mov rdi, 1{RESET}        {MAGENTA}; exit code 1 (generic error)
{CYAN}syscall{RESET}
""", 0.01)
    time.sleep(1)

    slow_print(f"{YELLOW}🧪 Example: Print message and return error code 42{RESET}", 0.02)
    slow_print(f"""
{CYAN}section .data{RESET}
    {CYAN}msg db "Something went wrong!", 0xA{RESET}
    {CYAN}len equ $ - msg{RESET}

{CYAN}section .text{RESET}
    {CYAN}global _start{RESET}

{CYAN}_start:{RESET}
    {CYAN}mov rax, 1{RESET}        {MAGENTA}; write
    {CYAN}mov rdi, 1{RESET}        {MAGENTA}; stdout
    {CYAN}mov rsi, msg{RESET}      {MAGENTA}; message
    {CYAN}mov rdx, len{RESET}      {MAGENTA}; length
    {CYAN}syscall{RESET}

    {CYAN}mov rax, 60{RESET}       {MAGENTA}; exit
    {CYAN}mov rdi, 42{RESET}       {MAGENTA}; exit code 42
    {CYAN}syscall{RESET}
""", 0.01)

    slow_print(f"{GREEN}📟 To see the exit code:{RESET}", 0.02)
    slow_print(f"""
Run the program, then type:
{CYAN}echo $?{RESET}
This shows the exit code of the last program.
""", 0.01)

    time.sleep(1)

    slow_print(f"{BOLD}{GREEN}🎓 Summary:{RESET}", 0.02)
    slow_print(f"""
{CYAN}exit syscall (60){RESET} tells the OS we're done.
{CYAN}rdi{RESET} holds the exit code (0 = success, other = error).

{YELLOW}Use meaningful exit codes to help with debugging, automation, and scripting!{RESET}
""", 0.01)

    slow_print(f"{CYAN}{BOLD}You're now exiting with style! 🚀{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
