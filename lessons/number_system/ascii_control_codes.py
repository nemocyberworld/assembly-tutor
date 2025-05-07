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
    slow_print(f"{CYAN}In ASCII, control characters are non-printable characters that control the behavior of devices, like printers or terminals.")
    slow_print("Let's explore some of the most common control characters like Line Feed (LF), Carriage Return (CR), and Bell (BEL)! 🎵")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_control_characters():
    print(f"\n{BOLD}{BLUE}📖 What Are ASCII Control Characters?{RESET}")
    slow_print(f"{CYAN}✔ ASCII control characters range from 0 to 31 in decimal (0x00 to 0x1F in hex).")
    slow_print(f"{CYAN}✔ These characters don't produce visible symbols, but instead control devices or the display.")
    slow_print("Some key control characters include:")
    slow_print(f"{YELLOW}- LF (Line Feed): Moves the cursor down to the next line (ASCII 10).{RESET}")
    slow_print(f"{YELLOW}- CR (Carriage Return): Moves the cursor back to the beginning of the line (ASCII 13).{RESET}")
    slow_print(f"{YELLOW}- BEL (Bell): Makes a sound or alert (ASCII 7).{RESET}")
    print(f"\n{CYAN}Let's dive into how these characters work!{RESET}")

def demonstrate_lf_cr_bel():
    print(f"\n{BOLD}{CYAN}🔍 Demonstration of LF, CR, and BEL{RESET}")
    
    print(f"\n{BOLD}{GREEN}Example 1: Line Feed (LF) - Moving to the next line{RESET}")
    slow_print(f"{CYAN}This text is followed by a Line Feed (LF) character...\n")
    
    print(f"{BOLD}{GREEN}Example 2: Carriage Return (CR) - Returning to the start of the line{RESET}")
    slow_print(f"{CYAN}This text will be overwritten by a Carriage Return (CR) character.")
    print(f"{RED}\rThis line has been replaced!{RESET}")
    
    print(f"\n{BOLD}{MAGENTA}Example 3: Bell (BEL) - Sound or alert{RESET}")
    slow_print(f"{CYAN}Now, we'll simulate a Bell (BEL) character. You might not hear it here, but on some systems, it makes a sound.\a")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 ASCII Control Characters Quiz!{RESET}")
    score = 0

    questions = [
        ("What ASCII control character is used to move to the next line?", "LF"),
        ("Which control character moves the cursor back to the start of the line?", "CR"),
        ("What control character makes an alert sound?", "BEL"),
        ("What is the ASCII value of Line Feed (LF)?", "10"),
        ("What is the ASCII value of Carriage Return (CR)?", "13"),
    ]

    for i, (q, a) in enumerate(questions, 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip()
        if user.lower() == a.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is: {GREEN}{a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Your score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🌟 Excellent! You're an ASCII control character expert!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Nice work! You're on your way to mastering control characters!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing, and you’ll get it next time!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ASCII control characters are non-printable characters used for controlling devices or formatting text.")
    slow_print(f"✔ Common control characters include LF (Line Feed), CR (Carriage Return), and BEL (Bell).")
    slow_print(f"✔ These characters may be invisible in the terminal, but they have important functions.")
    print(f"{GREEN}Great job completing the lesson! Keep practicing with control characters for better understanding! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_control_characters()
    demonstrate_lf_cr_bel()
    quiz()
    summary()
