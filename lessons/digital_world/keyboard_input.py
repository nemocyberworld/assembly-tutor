# lessons/keyboard/keyboard_input.py

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
    print(f"{BOLD}{MAGENTA}🔑 Welcome to Keyboard Input Breakdown!{RESET}")
    slow_print(f"{CYAN}Have you ever wondered what happens when you press a key on your keyboard?")
    slow_print("Let's explore how your computer translates key presses into digital signals! 💡")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def explain_key_press():
    print(f"\n{BOLD}{CYAN}🔍 What Happens When You Press a Key?{RESET}")
    slow_print(f"{CYAN}When you press a key, your keyboard sends an electrical signal to the computer.")
    slow_print(f"Each key has a corresponding **scancode**, which is a unique code for that key.")
    slow_print(f"Next, the computer maps that code to an **ASCII** (or another encoding) character.")

def demonstrate_key_to_ascii():
    print(f"\n{BOLD}{YELLOW}🔢 Let's See the ASCII Representation!{RESET}")
    key = input(f"{CYAN}Press a key to see its ASCII code: {RESET}")
    key_ascii = ord(key)
    print(f"{GREEN}You pressed '{key}', and its ASCII value is: {key_ascii}{RESET}")

def key_to_binary():
    print(f"\n{BOLD}{CYAN}🖥️ Convert Your Key to Binary!{RESET}")
    key = input(f"{CYAN}Press another key to see its binary code: {RESET}")
    key_binary = format(ord(key), '08b')
    print(f"{GREEN}Your key '{key}' in binary is: {key_binary}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Keyboard Input Quiz Time!{RESET}")
    print(f"\n{CYAN}What happens when you press a key on your keyboard?{RESET}")
    print(f"{YELLOW}A) The key is mapped to an ASCII code.{RESET}")
    print(f"{YELLOW}B) The key's scancode is converted into a character code.{RESET}")
    print(f"{YELLOW}C) Both A and B happen!{RESET}")
    
    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "C":
        print(f"{GREEN}✅ Correct! Both happen! The scancode is mapped to an ASCII character or equivalent.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is C. Both A and B happen when you press a key.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ A key press generates a scancode, which is then mapped to an ASCII character.")
    slow_print(f"✔ The character can be represented in binary or other encoding systems.")
    print(f"{GREEN}Now you know how typing a key turns into digital signals and characters! 💡{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explain_key_press()
    demonstrate_key_to_ascii()
    key_to_binary()
    quiz()
    summary()

if __name__ == "__main__":
    run()
