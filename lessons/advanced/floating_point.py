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
    print(f"\n{BOLD}📐 Floating Point Instructions & FPU Basics (x86-64){RESET}\n")
    time.sleep(1)

    # Intro
    slow_print(f"{YELLOW}🧠 While integers dominate low-level code, floating point is essential for math, graphics, and scientific apps.{RESET}")
    slow_print(f"{CYAN}x86-64 has dedicated floating point units (FPU) and SIMD extensions for fast number crunching.{RESET}")
    time.sleep(1)

    # Two ways
    slow_print(f"\n{BOLD}🔧 Two Ways to Handle Floating Point in x86-64:{RESET}")
    options = [
        "🔹 x87 FPU: legacy stack-based floating point unit",
        "🔹 SSE/AVX: modern SIMD registers (xmm0–xmm15) — faster and preferred"
    ]
    for opt in options:
        slow_print(f"{GREEN}{opt}{RESET}")
        time.sleep(0.4)

    # FPU Stack
    slow_print(f"\n{BOLD}🧮 x87 FPU Stack (Classic Method){RESET}")
    fpu_ops = [
        "fld   [mem]       ; load float onto FPU stack",
        "fld1              ; push 1.0",
        "fadd              ; ST(0) = ST(0) + ST(1)",
        "fsin              ; compute sine",
        "fstp  [mem]       ; pop and store result"
    ]
    for instr in fpu_ops:
        slow_print(f"{MAGENTA}{instr}{RESET}")
        time.sleep(0.3)

    slow_print(f"{CYAN}⚠️ The x87 FPU is a stack — think LIFO. ST(0) is the top.{RESET}")
    time.sleep(1)

    # SSE/AVX preferred
    slow_print(f"\n{BOLD}🚀 SIMD: SSE Instructions (Preferred for Modern x86-64){RESET}")
    simd_ops = [
        "movss  xmm0, [floatA]      ; load scalar float",
        "movss  xmm1, [floatB]",
        "addss  xmm0, xmm1          ; xmm0 += xmm1",
        "sqrtss xmm0, xmm0          ; square root",
        "movss  [result], xmm0      ; store result"
    ]
    for instr in simd_ops:
        slow_print(f"{GREEN}{instr}{RESET}")
        time.sleep(0.3)

    slow_print(f"{CYAN}💡 'ss' means scalar single-precision float. For double, use 'sd'.{RESET}")
    time.sleep(1)

    # Data types
    slow_print(f"\n{BOLD}📊 Common Floating Point Types:{RESET}")
    types = [
        "float     (32-bit, single precision)",
        "double    (64-bit, double precision)",
        "long double (80-bit, used in x87 FPU)"
    ]
    for t in types:
        slow_print(f"{GREEN}✔ {t}{RESET}")
        time.sleep(0.4)

    # Summary
    slow_print(f"\n{YELLOW}🧾 Summary:{RESET}")
    summary = [
        "✔ Use SSE (`xmm`) for floating point math in modern x86-64.",
        "✔ x87 FPU is still valid but mostly legacy — stack-based.",
        "✔ Know your float types: 32-bit, 64-bit, 80-bit.",
        "✔ SIMD also enables vectorized (parallel) floating point ops!"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.4)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Write an assembly function to compute sqrt(a² + b²) using SSE!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want an example with SIMD loops or vector math?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")