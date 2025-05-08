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
    slow_print(f"\n👋 {BOLD}Welcome to the lesson: Writing Simple Loops with `jmp` and `cmp`!{RESET}\n", 0.02)
    time.sleep(1)

    slow_print(f"{YELLOW}📚 In this lesson, you'll learn how to build loops using `jmp` (jump) and `cmp` (compare).{RESET}", 0.02)
    slow_print(f"{YELLOW}🔁 We'll explore counting down, counting up, and different jump behaviors — all in raw Assembly!{RESET}\n", 0.02)
    time.sleep(2)

    # === Countdown Example ===
    slow_print(f"{CYAN}{BOLD}📄 Example 1: Countdown Loop from 5 to 1{RESET}\n", 0.02)
    countdown = [
        ("mov rcx, 5", "🔢 Start counter at 5"),
        ("print_loop:", "🔁 Loop start label"),
        ("; pretend we print RCX here", "🖨️ Output logic would go here"),
        ("dec rcx", "➖ Decrease RCX by 1"),
        ("cmp rcx, 0", "🔍 Is RCX zero yet?"),
        ("jne print_loop", "🔄 Jump if Not Equal (keep looping)"),
    ]
    for code, explanation in countdown:
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
    time.sleep(1)

    # === Count Up Example ===
    slow_print(f"\n{CYAN}{BOLD}📄 Example 2: Count Up from 1 to 5{RESET}\n", 0.02)
    count_up = [
        ("mov rcx, 1", "🔢 Start RCX at 1"),
        ("count_up:", ""),
        ("; pretend we print RCX here", "🖨️ Output logic would go here"),
        ("add rcx, 1", "➕ Increment RCX by 1"),
        ("cmp rcx, 6", "🎯 Stop when RCX reaches 6"),
        ("jne count_up", "🔁 Jump if RCX ≠ 6"),
    ]
    for code, explanation in count_up:
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
    time.sleep(1)

    # === Infinite Loop Example ===
    slow_print(f"\n{CYAN}{BOLD}📄 Example 3: Infinite Loop{RESET}\n", 0.02)
    infinite_loop = [
        ("start:", ""),
        ("jmp start", "♾️ Jumps to itself forever!"),
        ("; use Ctrl+C to exit", "🛑 Manual exit needed"),
    ]
    for code, explanation in infinite_loop:
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
    time.sleep(1)

    # === Loop with `je` ===
    slow_print(f"\n{CYAN}{BOLD}📄 Example 4: Loop Using `je` (Jump if Equal){RESET}\n", 0.02)
    je_example = [
        ("mov rcx, 5", "🔢 RCX starts at 5"),
        ("loop_label:", ""),
        ("; pretend we print RCX here", "🖨️ Output logic would go here"),
        ("dec rcx", "➖ Decrement"),
        ("cmp rcx, 0", "🔍 Compare to 0"),
        ("je done", "✅ If equal, jump to done"),
        ("jmp loop_label", "🔁 Otherwise, loop again"),
        ("done:", "🏁 End of loop"),
    ]
    for code, explanation in je_example:
        slow_print(f"  {CYAN}{code:<35}{RESET} {MAGENTA}{explanation}{RESET}", 0.01)
    time.sleep(1)

    # Wrap up
    slow_print(f"\n{GREEN}🎉 You've seen several ways to loop in Assembly using just `cmp` and `jmp` variants!{RESET}", 0.02)
    slow_print(f"{YELLOW}🛠️ These are the building blocks of control flow — before functions, before high-level logic — loops keep your CPU busy!{RESET}", 0.02)

    slow_print(f"\n{BOLD}{CYAN}🔥 Now go try them yourself — tweak the conditions, use other registers, and make the CPU dance! 🧠💃{RESET}\n", 0.02)
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
