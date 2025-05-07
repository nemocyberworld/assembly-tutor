# lessons/data/json_encoding.py

import json
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
    print(f"{BOLD}{MAGENTA}🧾 Welcome to JSON Encoding!{RESET}")
    slow_print(f"{CYAN}JSON (JavaScript Object Notation) is everywhere!")
    slow_print("APIs, configs, databases — all use this human-readable format.")
    slow_print("But how is it stored behind the scenes? Let's find out! 🔍")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def show_json_bytes():
    data = {
        "name": "Ada",
        "age": 42,
        "language": "Python 🐍"
    }

    print(f"\n{BOLD}{BLUE}📦 Sample JSON Data:{RESET}")
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    print(f"{GREEN}{json_str}{RESET}")

    encoded = json_str.encode("utf-8")
    print(f"\n{BOLD}{CYAN}💾 UTF-8 Encoded Bytes:{RESET}")
    print(f"{YELLOW}{encoded}{RESET}")

    print(f"\n{BOLD}{MAGENTA}🔍 Byte Breakdown (char → hex → binary):{RESET}")
    for char in json_str:
        utf8 = char.encode("utf-8")
        hex_val = ' '.join(f"{b:02X}" for b in utf8)
        bin_val = ' '.join(f"{b:08b}" for b in utf8)
        display = repr(char)[1:-1]
        print(f"{GREEN}{display:<3}{RESET} → {CYAN}{hex_val:<12}{RESET} → {MAGENTA}{bin_val}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Encoding Quiz Time!{RESET}")
    question = "true"
    correct_bytes = list(question.encode("utf-8"))
    user_input = input(f"{YELLOW}What are the UTF-8 byte values (in decimal) for \"{question}\"? (space-separated): {RESET}")

    try:
        user_answer = list(map(int, user_input.strip().split()))
        if user_answer == correct_bytes:
            print(f"{GREEN}✅ Correct! Those are the UTF-8 bytes for \"{question}\".{RESET}")
        else:
            print(f"{RED}❌ Not quite. Correct bytes: {correct_bytes}{RESET}")
    except:
        print(f"{RED}⚠️ Invalid input. Please enter numbers like: 116 114 117 101{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ JSON is text-based — saved as UTF-8 by default")
    slow_print("✔ Every character becomes 1 or more bytes (thanks, Unicode!)")
    slow_print("✔ Python’s `json` module makes it easy to encode/decode")
    print(f"{GREEN}Now you can peek into the byte-level world of APIs and files! 🔍{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_json_bytes()
    quiz()
    summary()

if __name__ == "__main__":
    run()
