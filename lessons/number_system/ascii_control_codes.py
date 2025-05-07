# lessons/basics/ascii_control_codes.py

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
    print(f"{BOLD}{MAGENTA}🔍 Welcome to Understanding ASCII Control Characters!{RESET}")
    slow_print(f"{CYAN}In ASCII, control characters are non-printable characters that control device behavior,")
    slow_print("like moving the cursor, making a beep, or formatting output.")
    slow_print("Let's explore Line Feed (LF), Carriage Return (CR), and Bell (BEL)! 🎵")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_control_characters():
    print(f"\n{BOLD}{BLUE}📖 What Are ASCII Control Characters?{RESET}")
    slow_print(f"{CYAN}✔ ASCII control characters range from decimal 0 to 31 (hex 0x00 to 0x1F).")
    slow_print("✔ They're used to control formatting or trigger device behaviors.")
    slow_print(f"{YELLOW}- LF (Line Feed): Moves the cursor down (ASCII 10).{RESET}")
    slow_print(f"{YELLOW}- CR (Carriage Return): Moves cursor to line start (ASCII 13).{RESET}")
    slow_print(f"{YELLOW}- BEL (Bell): Triggers a beep or alert (ASCII 7).{RESET}")
    input(f"\n{YELLOW}Press Enter to see how they work... {RESET}")

def demonstrate_lf_cr_bel():
    print(f"\n{BOLD}{CYAN}🔍 Demonstration of LF, CR, and BEL{RESET}")

    print(f"\n{BOLD}{GREEN}Example 1: Line Feed (LF){RESET}")
    slow_print(f"{CYAN}This line will be followed by a Line Feed character...\n(This is the next line!){RESET}")

    print(f"\n{BOLD}{GREEN}Example 2: Carriage Return (CR){RESET}")
    slow_print(f"{CYAN}Watch the next print line overwrite using CR:\r", delay=0.04)
    time.sleep(0.5)
    print(f"{RED}This replaces the line start!{RESET}")

    print(f"\n{BOLD}{MAGENTA}Example 3: Bell (BEL){RESET}")
    slow_print(f"{CYAN}Triggering Bell...\a (If your system supports it, you may hear a sound!){RESET}")
    input(f"\n{YELLOW}Press Enter to try a quiz... {RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 ASCII Control Characters Quiz!{RESET}")
    score = 0

    questions = [
        ("What ASCII control character moves to the next line?", "LF"),
        ("Which control character returns to the line start?", "CR"),
        ("Which character makes a beep or alert?", "BEL"),
        ("What is the ASCII value of Line Feed (LF)?", "10"),
        ("What is the ASCII value of Carriage Return (CR)?", "13"),
    ]

    for i, (question, answer) in enumerate(questions, 1):
        user = input(f"{YELLOW}Q{i}: {question} {RESET}").strip()
        if user.lower() == answer.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is: {GREEN}{answer}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Your score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🌟 Excellent! You're an ASCII control character expert!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Great job! You're getting the hang of it!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing, and you’ll get it next time!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ASCII control characters are invisible codes that influence how text is displayed or devices behave.")
    slow_print("✔ Important ones include Line Feed (LF), Carriage Return (CR), and Bell (BEL).")
    slow_print("✔ They're vital in formatting text and interacting with hardware.")
    print(f"{GREEN}Great job completing the lesson! Keep exploring how your computer interprets characters! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to return to the lesson list...{RESET}")

def run():
    intro()
    explain_control_characters()
    demonstrate_lf_cr_bel()
    quiz()
    summary()

if __name__ == "__main__":
    run()
