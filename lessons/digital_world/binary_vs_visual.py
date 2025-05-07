# lessons/binary/binary_vs_visual.py

import time

# 🎨 Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🧠 Binary vs Visual Output{RESET}")
    slow_print(f"{CYAN}Ever wonder how binary becomes images or text?")
    slow_print("Let’s convert 1s and 0s into something you can actually SEE.")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def generate_binary_grid():
    # Simulated binary "image"
    return [
        "01110",
        "10001",
        "10101",
        "10001",
        "01110"
    ]

def binary_to_visual(binary_grid):
    print(f"\n{BOLD}{BLUE}🟢 Visualizing Binary Grid...{RESET}")
    print(f"{CYAN}Binary     →    Visual Output{RESET}")
    for row in binary_grid:
        visual = ''.join('█' if bit == '1' else ' ' for bit in row)
        print(f"{YELLOW}{row}     {RESET}→ {GREEN}{visual}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Guess the Shape!{RESET}")
    binary_grid = [
        "00100",
        "01110",
        "10101",
        "00100",
        "00100"
    ]
    binary_to_visual(binary_grid)
    guess = input(f"{YELLOW}🧠 What shape is that? (Hint: it's a keyboard symbol!) {RESET}").strip().lower()
    if "arrow" in guess or "up" in guess:
        print(f"{GREEN}✅ Nice! That was an upward arrow!{RESET}")
    else:
        print(f"{RED}❌ It was an upward arrow ↑. Keep practicing visual thinking!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Binary isn't just numbers — it's visual instructions too!")
    slow_print("✔ Each '1' or '0' can map to a pixel, color, or shape")
    slow_print("✔ This idea powers fonts, icons, images and more!")
    print(f"{GREEN}Now you're seeing the matrix! 👁️💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    binary_grid = generate_binary_grid()
    binary_to_visual(binary_grid)
    quiz()
    summary()

