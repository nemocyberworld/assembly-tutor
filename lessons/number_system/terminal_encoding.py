# lessons/encoding/terminal_encoding.py

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
    print(f"{BOLD}{MAGENTA}🖥️ Welcome to 'Terminal Encoding: UTF-8 in Action'!{RESET}")
    slow_print(f"{CYAN}Have you ever seen strange symbols in your terminal? Like � or boxes?")
    slow_print("That happens when the terminal misinterprets byte sequences!")
    slow_print(f"Today, we’ll learn how terminals handle UTF-8 and how to keep your output looking sharp! 🌟")
    input(f"\n{YELLOW}Press Enter to begin the adventure... {RESET}")

def terminal_encoding_explained():
    print(f"\n{BOLD}{BLUE}🔍 What’s Happening Behind the Scenes?{RESET}")
    slow_print(f"{CYAN}Terminals receive bytes → decode them using a specific encoding (usually UTF-8).")
    slow_print("If a byte sequence is invalid or incomplete, the terminal shows replacement characters like:")
    print(f"{RED}� (U+FFFD: Replacement Character){RESET}")
    slow_print("So making sure your output is valid UTF-8 is super important!")

def utf8_demo():
    print(f"\n{BOLD}{GREEN}🧪 UTF-8 Output Demo!{RESET}")
    emojis = ["😀", "🐍", "🚀", "💡", "🍕"]
    words = ["Hello", "世界", "नमस्ते", "Привет", "مرحبا"]
    
    slow_print(f"{CYAN}Let's print some international text and emojis:")
    for word in words:
        print(f"{GREEN}→ {word}{RESET}")
    for emoji in emojis:
        print(f"{MAGENTA}→ {emoji}{RESET}")

    slow_print(f"\n{CYAN}Notice how all these characters show correctly?")
    slow_print("That’s because your terminal understands UTF-8!")

def show_byte_sequence():
    print(f"\n{BOLD}{YELLOW}🧬 Let’s Peek Under the Hood!{RESET}")
    text = "€"
    utf8_bytes = text.encode('utf-8')
    hex_view = ' '.join(f"{byte:02X}" for byte in utf8_bytes)

    print(f"{CYAN}Character: {BOLD}{text}{RESET}")
    print(f"{CYAN}UTF-8 Bytes: {GREEN}{hex_view}{RESET}")
    slow_print(f"{CYAN}The euro sign (€) uses 3 bytes in UTF-8: {hex_view}")
    slow_print("This shows how multi-byte characters are transmitted and interpreted.")

def corruption_simulation():
    print(f"\n{BOLD}{RED}⚠️ Simulating Byte Corruption!{RESET}")
    slow_print(f"{CYAN}Let’s break a UTF-8 sequence and see what happens...")

    # Valid UTF-8: 😀 = F0 9F 98 80
    valid_bytes = bytes([0xF0, 0x9F, 0x98, 0x80])
    broken_bytes = bytes([0xF0, 0x9F])  # Incomplete

    print(f"\n{GREEN}Valid Bytes: {valid_bytes} → {valid_bytes.decode('utf-8')}{RESET}")
    try:
        print(f"{RED}Broken Bytes: {broken_bytes} → {broken_bytes.decode('utf-8')}{RESET}")
    except UnicodeDecodeError as e:
        print(f"{RED}❌ UnicodeDecodeError: {e}{RESET}")
    slow_print(f"{CYAN}This error happens when the terminal can't decode the sequence fully!")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick Quiz Time!{RESET}")
    score = 0

    questions = [
        ("Which encoding do most terminals use by default?", "utf-8"),
        ("What symbol appears when a UTF-8 character can't be decoded?", "�"),
        ("True or False: UTF-8 characters can be more than 1 byte long.", "true"),
    ]

    for i, (q, a) in enumerate(questions, 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip().lower()
        if user == a:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! The correct answer was: {a}{RESET}")

    print(f"\n{BLUE}{BOLD}🎯 Final Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 You're a UTF-8 Terminal Master!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👏 Good job! Keep learning!{RESET}")
    else:
        print(f"{RED}📚 No worries, review and try again!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Terminals decode bytes using encodings like UTF-8.")
    slow_print(f"✔ UTF-8 supports emojis and characters from all languages using 1–4 bytes.")
    slow_print("✔ Invalid byte sequences cause decoding errors or show �.")
    print(f"{GREEN}You’re now ready to debug terminal output like a pro! 🧠{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    terminal_encoding_explained()
    utf8_demo()
    show_byte_sequence()
    corruption_simulation()
    quiz()
    summary()
