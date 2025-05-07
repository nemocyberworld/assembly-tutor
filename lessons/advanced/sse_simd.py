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
    print(f"\n{BOLD}🧮 SSE & SIMD: Vectorized Math in x86-64 Assembly{RESET}\n")
    time.sleep(1)

    slow_print(f"{YELLOW}SIMD = Single Instruction, Multiple Data.{RESET}")
    slow_print(f"{CYAN}With SSE (Streaming SIMD Extensions), you can process multiple values at once using vector registers!{RESET}")
    time.sleep(1)

    # What are XMM registers?
    slow_print(f"\n{BOLD}📦 XMM Registers (128-bit){RESET}")
    xmm_info = [
        "🔹 xmm0 to xmm15 are 128-bit registers",
        "🔹 Can hold:",
        "   • Four 32-bit floats (packed single-precision)",
        "   • Two 64-bit doubles (packed double-precision)",
        "   • Packed integers, too (for integer SIMD)",
    ]
    for line in xmm_info:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.4)

    # Why use it?
    slow_print(f"\n{BOLD}🚀 Why SIMD?{RESET}")
    reasons = [
        "✔️ Parallel math — great for graphics, DSP, physics, encryption",
        "✔️ Way faster than looping over scalars",
        "✔️ Often used by compilers under the hood (auto-vectorization)"
    ]
    for r in reasons:
        slow_print(f"{CYAN}{r}{RESET}")
        time.sleep(0.4)

    # Example: Add 4 floats
    slow_print(f"\n{BOLD}💡 Example: Adding 4 floats in parallel{RESET}")
    example = [
        "section .data",
        "  vecA: dd 1.0, 2.0, 3.0, 4.0",
        "  vecB: dd 4.0, 3.0, 2.0, 1.0",
        "  result: times 4 dd 0.0",

        "section .text",
        "  movaps xmm0, [vecA]      ; load 4 floats into xmm0",
        "  movaps xmm1, [vecB]      ; load 4 floats into xmm1",
        "  addps  xmm0, xmm1        ; add packed single-precision",
        "  movaps [result], xmm0    ; store result"
    ]
    for line in example:
        slow_print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)

    # Explanation
    slow_print(f"\n{CYAN}🧠 Each instruction operates on multiple data lanes inside the XMM register.{RESET}")
    slow_print(f"{CYAN}In this example, it’s like doing:{RESET}")
    slow_print(f"{GREEN}[1.0+4.0, 2.0+3.0, 3.0+2.0, 4.0+1.0] = [5.0, 5.0, 5.0, 5.0]{RESET}")
    time.sleep(1)

    # Summary
    slow_print(f"\n{YELLOW}🧾 Summary:{RESET}")
    summary = [
        "✔ SSE enables parallel math using XMM registers.",
        "✔ addps / subps / mulps / divps = packed float operations",
        "✔ SSE is great for optimizing performance-critical loops",
        "✔ Always align your data to 16 bytes for movaps!"
    ]
    for line in summary:
        slow_print(f"{GREEN}{line}{RESET}")
        time.sleep(0.4)

    # Challenge
    slow_print(f"\n{BOLD}{CYAN}🧪 Challenge: Write a function that multiplies two float vectors of 4 elements using SIMD!{RESET}")
    time.sleep(1)

    print(f"\n{BOLD}📚 Lesson complete! Want to move on to AVX (256-bit SIMD)?{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")