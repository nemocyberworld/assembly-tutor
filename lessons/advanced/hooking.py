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
    print(f"\n{BOLD}🪝 Function Hooking & Binary Patching (x86-64){RESET}\n")
    time.sleep(1)

    # Intro
    slow_print(f"{YELLOW}🔧 Hooking lets you change a program's behavior — without modifying its source code!{RESET}")
    slow_print(f"{CYAN}It works by redirecting function calls, often through overwriting instructions in memory or the binary itself.{RESET}")
    time.sleep(1)

    # Use cases
    slow_print(f"\n{BOLD}💡 Common Use Cases:{RESET}")
    uses = [
        "✔ Debugging or monitoring function calls (e.g., malloc hooks)",
        "✔ Replacing or bypassing security checks",
        "✔ Injecting new logic into closed-source programs",
        "✔ Malware analysis or instrumentation"
    ]
    for item in uses:
        slow_print(f"{MAGENTA}{item}{RESET}")
        time.sleep(0.3)

    # Example: Overwriting first bytes of a function
    slow_print(f"\n{BOLD}✏️ Basic Method: Overwriting Function Prologue{RESET}")
    slow_print(f"{GREEN}In assembly, you can redirect execution by overwriting the start of a function with a JMP instruction.{RESET}")
    slow_print(f"""{CYAN}
  ; Original function prologue:
  0x401000: 55                push rbp
  0x401001: 48 89 e5          mov rbp, rsp

  ; After patch:
  0x401000: e9 <offset>       jmp my_hook
{RESET}""")
    time.sleep(1)

    # Python simulation
    slow_print(f"\n{BOLD}🧪 Simulated Hook in Python:{RESET}")
    def original_function():
        slow_print(f"{RED}→ Original function logic{RESET}")

    def my_hook():
        slow_print(f"{GREEN}→ Hooked! New behavior injected.{RESET}")

    slow_print(f"\n{BOLD}📦 Before Hooking:{RESET}")
    original_function()
    time.sleep(1)

    slow_print(f"\n{BOLD}🪝 Hook Applied! Redirecting call to new function...{RESET}")
    hook = my_hook  # Simulated patch

    slow_print(f"\n{BOLD}📦 After Hooking:{RESET}")
    hook()
    time.sleep(1)

    # Patching binary files
    slow_print(f"\n{BOLD}🧷 Binary Patching with `pwntools` or `r2`:{RESET}")
    slow_print(f"{YELLOW}You can modify a binary directly using tools like radare2 or hex editors.{RESET}")
    slow_print(f"""{MAGENTA}
  ; In r2:
  oo+ ./target_binary
  s sym.func_to_hook
  wa jmp sym.my_hook
{RESET}""")
    time.sleep(1)

    # Caveats
    slow_print(f"\n{BOLD}⚠️ Things to Watch Out For:{RESET}")
    warnings = [
        "✘ Overwriting too many bytes may corrupt surrounding code",
        "✘ JMP offset must be carefully calculated",
        "✘ Page protections (read-only) may block patching",
        "✔ Use mprotect() to make code pages writable temporarily"
    ]
    for w in warnings:
        slow_print(f"{RED if '✘' in w else GREEN}{w}{RESET}")
        time.sleep(0.3)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Hooking redirects execution flow — great for debugging or customization",
        "✔ Binary patching replaces bytes to modify instructions",
        "✔ Works at runtime or statically",
        "✔ Tools like radare2 and pwntools simplify the process"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Try patching a binary to skip a password check. Can you JMP past the failure logic?{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to walk through building a real hook with `libc` or patching ELF bytes?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
