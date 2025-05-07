import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def run():
    slow_print(f"\n🔧 {BOLD}Lesson: Intro to Linux System Calls in x86-64 Assembly{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}💡 System calls let your Assembly program talk directly to the Linux kernel.{RESET}", 0.02)
    slow_print(f"{YELLOW}🎯 Today, we’ll learn two important ones: {CYAN}write{YELLOW} and {CYAN}exit{YELLOW}.{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🔊 1. write (syscall number 1){RESET}", 0.02)
    slow_print(f"{GREEN}Used to output data (like printing text to the screen).{RESET}", 0.02)
    slow_print(f"{MAGENTA}Arguments:{RESET}", 0.02)
    slow_print(f"""
  {CYAN}rax = 1{RESET}      {MAGENTA}# syscall number for write
  {CYAN}rdi = 1{RESET}      {MAGENTA}# file descriptor (1 = stdout)
  {CYAN}rsi = addr{RESET}   {MAGENTA}# pointer to the data (string)
  {CYAN}rdx = len{RESET}    {MAGENTA}# number of bytes to write
    """, 0.01)

    slow_print(f"{CYAN}{BOLD}🧪 Example:{RESET}", 0.02)
    slow_print(f"""
  {CYAN}section .data{RESET}
  {CYAN}msg db "Hello from syscall!", 0xA{RESET}
  {CYAN}len equ $ - msg{RESET}

  {CYAN}section .text{RESET}
  {CYAN}global _start{RESET}

  {CYAN}_start:{RESET}
      {CYAN}mov rax, 1{RESET}        {MAGENTA}; syscall: write
      {CYAN}mov rdi, 1{RESET}        {MAGENTA}; stdout
      {CYAN}mov rsi, msg{RESET}      {MAGENTA}; message address
      {CYAN}mov rdx, len{RESET}      {MAGENTA}; message length
      {CYAN}syscall{RESET}           {MAGENTA}; invoke kernel
    """, 0.01)

    time.sleep(1)

    slow_print(f"{CYAN}{BOLD}🏁 2. exit (syscall number 60){RESET}", 0.02)
    slow_print(f"{GREEN}Ends your program gracefully and returns a status code.{RESET}", 0.02)
    slow_print(f"{MAGENTA}Arguments:{RESET}", 0.02)
    slow_print(f"""
  {CYAN}rax = 60{RESET}     {MAGENTA}# syscall number for exit
  {CYAN}rdi = code{RESET}   {MAGENTA}# exit code (0 = success)
    """, 0.01)

    slow_print(f"{CYAN}{BOLD}🧪 Example (continued):{RESET}", 0.02)
    slow_print(f"""
      {CYAN}mov rax, 60{RESET}       {MAGENTA}; syscall: exit
      {CYAN}xor rdi, rdi{RESET}      {MAGENTA}; status 0 (success)
      {CYAN}syscall{RESET}           {MAGENTA}; goodbye!
    """, 0.01)

    time.sleep(1)

    slow_print(f"{BOLD}{GREEN}✅ Summary:{RESET}", 0.02)
    slow_print(f"""
{CYAN}write (rax = 1){RESET}  - Prints output to a file/terminal (stdout = 1)  
{CYAN}exit  (rax = 60){RESET} - Ends the program with a return code

{YELLOW}📎 These are your first tools to interact with the outside world from Assembly!{RESET}
""", 0.01)

    time.sleep(1)
    slow_print(f"{BOLD}{CYAN}🧠 Next up? More syscalls like open, read, and more! But for now — congrats, you're system-level awesome! 🚀{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
