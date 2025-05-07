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
    print(f"\n{BOLD}🚀 Optimizing Assembly Code for Speed (x86-64){RESET}\n")
    time.sleep(1)

    # Introduction
    slow_print(f"{YELLOW}🎯 Assembly gives you full control of performance-critical code — but with great power comes great responsibility!{RESET}")
    slow_print(f"{CYAN}This lesson explores ways to write faster, leaner, and smarter x86-64 instructions.{RESET}")
    time.sleep(1)

    # Key Concepts
    slow_print(f"\n{BOLD}🧠 Key Concepts in Performance:{RESET}")
    concepts = [
        "• Instruction throughput (how many per cycle)",
        "• Instruction latency (how long it takes)",
        "• Pipelines and stalls",
        "• Cache locality and memory access",
        "• Branch prediction and speculation"
    ]
    for c in concepts:
        slow_print(f"{MAGENTA}{c}{RESET}")
        time.sleep(0.4)

    # Tip 1: Avoid slow instructions
    slow_print(f"\n{BOLD}⚠️ Tip 1: Avoid Slow Instructions{RESET}")
    slow_ops = [
        "• div / idiv    – Division is slow (use shifts if possible)",
        "• mul           – Slower than add/sub",
        "• imul          – Better than mul, but still costly",
        "• jmp + bad branches – Kills pipeline if mispredicted"
    ]
    for s in slow_ops:
        slow_print(f"{RED}{s}{RESET}")
        time.sleep(0.3)

    # Tip 2: Strength Reduction
    slow_print(f"\n{BOLD}💡 Tip 2: Use Strength Reduction (Cheaper Operations){RESET}")
    examples = [
        "✘ imul rax, 10      →  takes multiple cycles",
        "✔ lea rax, [rax*8 + rax*2]   →  much faster!",
        "✘ div rbx           →  slow",
        "✔ shift or mask when dividing by powers of 2"
    ]
    for ex in examples:
        slow_print(f"{CYAN}{ex}{RESET}")
        time.sleep(0.4)

    # Tip 3: Minimize memory access
    slow_print(f"\n{BOLD}🧠 Tip 3: Minimize Memory Accesses{RESET}")
    slow_print(f"{YELLOW}Registers are much faster than RAM. Load data once, use it many times.{RESET}")
    slow_print(f"{GREEN}✔ Cache-friendly access (linear, small steps) beats random access.{RESET}")
    time.sleep(1)

    # Tip 4: Unroll loops
    slow_print(f"\n{BOLD}🔁 Tip 4: Unroll Loops to Reduce Branching Overhead{RESET}")
    slow_print(f"{MAGENTA}Example:{RESET}")
    slow_print(f"{CYAN}Instead of looping 4 times, write the body 4x and eliminate the loop entirely — at the cost of more code.{RESET}")
    time.sleep(1)

    # Tip 5: Use LEA smartly
    slow_print(f"\n{BOLD}🛠️ Tip 5: Master the LEA Instruction{RESET}")
    slow_print(f"{GREEN}LEA (Load Effective Address) can perform addition, multiplication, and more — without affecting flags.{RESET}")
    slow_print(f"{CYAN}Great for computing addresses or quick math (e.g., rax = rbx*5 + rcx){RESET}")
    time.sleep(1)

    # Micro-optimizations
    slow_print(f"\n{BOLD}⚙️ Micro-Optimization Tricks:{RESET}")
    tricks = [
        "• Align code to 16-byte boundaries for better fetch",
        "• Use fewer jumps and conditional branches",
        "• Prefer short, pipelinable instruction sequences",
        "• Keep hot loops small enough to fit in L1 cache"
    ]
    for t in tricks:
        slow_print(f"{MAGENTA}{t}{RESET}")
        time.sleep(0.3)

    # Benchmarking
    slow_print(f"\n{BOLD}📏 Always Measure!{RESET}")
    slow_print(f"{CYAN}Use tools like `perf`, `rdtsc`, or `hyperfine` to benchmark your changes — don’t rely on guesswork!{RESET}")
    time.sleep(1)

    # Summary
    slow_print(f"\n{BOLD}📌 Summary:{RESET}")
    summary = [
        "✔ Avoid slow operations like `div` when possible",
        "✔ Replace expensive ops with cheap ones (LEA, shifts)",
        "✔ Minimize memory accesses and favor registers",
        "✔ Write small, predictable loops with few branches",
        "✔ Profile and benchmark to validate improvements"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.3)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🎯 Challenge: Write two versions of a function that computes a × 5. One using `imul`, one using `lea`. Compare performance using `rdtsc`!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Would you like to explore how to use `perf stat` or CPU pipelines next?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
