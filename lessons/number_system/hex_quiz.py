import time
import random

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
    print(f"{BOLD}{MAGENTA}🕵️ Welcome to the Hex Decoder Challenge!{RESET}")
    slow_print(f"{CYAN}Can you crack the code and reveal the secret messages hidden in hex?")
    slow_print("Each message is encoded using simple hexadecimal values. Let’s decode like pros! 🔓")
    input(f"\n{YELLOW}Press Enter to begin your decoding adventure... {RESET}")

def hex_to_ascii(hex_str):
    try:
        bytes_data = bytes.fromhex(hex_str)
        return bytes_data.decode('ascii')
    except:
        return None

def show_example():
    print(f"\n{BOLD}{BLUE}🔍 Example: Decoding Hex to ASCII{RESET}")
    hex_input = "48656C6C6F20576F726C64"
    result = hex_to_ascii(hex_input)
    print(f"{YELLOW}Hex: {hex_input}{RESET}")
    print(f"{GREEN}Decoded: {result}{RESET}")

def interactive_challenge():
    print(f"\n{BOLD}{MAGENTA}🧪 Try Decoding Yourself!{RESET}")
    user_input = input(f"{YELLOW}Enter a hex string (e.g., 48656C6C6F): {RESET}").strip()
    decoded = hex_to_ascii(user_input)
    if decoded:
        print(f"{GREEN}✅ Decoded Message: {decoded}{RESET}")
    else:
        print(f"{RED}❌ Invalid hex input! Make sure it's even-length and valid ASCII.{RESET}")

def quiz():
    print(f"\n{BOLD}{CYAN}🎮 Decode These Secret Messages!{RESET}")
    score = 0

    questions = [
        ("48657921", "Hey!"),
        ("57656C636F6D6521", "Welcome!"),
        ("4865782069732066756E", "Hex is fun"),
        ("596F7520676F74207468697321", "You got this!"),
        ("507974686F6E203D20E29885", "Python = ☕"),  # Includes a UTF-8 symbol
    ]
    random.shuffle(questions)

    for i, (hex_code, correct_answer) in enumerate(questions[:3], 1):
        print(f"\n{YELLOW}Q{i}: Decode this hex string:{RESET}\n{CYAN}{hex_code}{RESET}")
        user = input(f"{BOLD}Your Answer: {RESET}").strip()
        if user == correct_answer:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! It was: {correct_answer}{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Hex Hero! You cracked every code!{RESET}")
    elif score == 2:
        print(f"{YELLOW}🕶️ Great job! Just one slipped through!{RESET}")
    else:
        print(f"{RED}🧩 Keep trying — decoding takes practice!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hex can represent any text using ASCII codes")
    slow_print("✔ You can decode messages with `bytes.fromhex()` and `.decode('ascii')`")
    slow_print("✔ Hex decoding is a handy skill for debugging, security, and fun puzzles!")
    print(f"{GREEN}Keep decoding — the world is full of secret messages! 🔐{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_example()
    interactive_challenge()
    quiz()
    summary()

if __name__ == "__main__":
    run()
