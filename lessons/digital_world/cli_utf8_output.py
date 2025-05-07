# lessons/cli/cli_utf8_output.py

import time
import binascii
import sys

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
    print(f"{BOLD}{MAGENTA}📜 Welcome to Analyzing UTF-8 Terminal Output!{RESET}")
    slow_print(f"{CYAN}In this lesson, we will explore how UTF-8 encoded characters appear in the terminal, and how to analyze the bytes behind the text.")
    slow_print(f"We'll see how characters like emojis and symbols are rendered in the terminal and how to inspect them using Python. 🧑‍💻💡")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def display_utf8_output():
    print(f"\n{BOLD}{CYAN}🔍 Displaying UTF-8 Output{RESET}")
    slow_print(f"{CYAN}Let’s first explore how some common UTF-8 characters are displayed in the terminal.")

    # Example characters: normal text, emoji, and special symbols
    examples = [
        "Hello, World!",
        "😊",  # emoji
        "©",   # copyright symbol
        "你好",  # Chinese characters
    ]
    
    for example in examples:
        print(f"\n{YELLOW}Displaying: {example}{RESET}")
        slow_print(f"{CYAN}Here’s what it looks like in the terminal:{RESET}")
        print(f"{example}")
        
        # Display the UTF-8 byte encoding of the string
        utf8_bytes = example.encode('utf-8')
        print(f"{MAGENTA}UTF-8 Encoded Bytes:{RESET}")
        print(f"{CYAN}{binascii.hexlify(utf8_bytes).upper()}{RESET}")

def analyze_cli_utf8():
    print(f"\n{BOLD}{CYAN}🔎 Analyzing UTF-8 Output from CLI{RESET}")
    slow_print(f"{CYAN}When a terminal program outputs text in UTF-8, it might seem like simple text, but it's actually encoded in bytes behind the scenes.")
    slow_print(f"Let’s break down the process of how UTF-8 encoding works and how we can see it on a byte level.")

    # Example: UTF-8 encoded string with a few characters
    example_text = "Goodbye, World! 🌍"
    print(f"\n{YELLOW}Original Text: {example_text}{RESET}")

    # Encoding the text to UTF-8 bytes
    utf8_bytes = example_text.encode('utf-8')
    print(f"{MAGENTA}UTF-8 Encoded Bytes:{RESET}")
    print(f"{CYAN}{binascii.hexlify(utf8_bytes).upper()}{RESET}")

    slow_print(f"\nNotice how each character has different byte lengths. For instance, the emoji '🌍' requires more bytes than regular ASCII characters.")

def utf8_in_terminal():
    print(f"\n{BOLD}{CYAN}💻 How UTF-8 Is Interpreted by the Terminal{RESET}")
    slow_print(f"{CYAN}When you print text to a terminal, the program sends UTF-8 encoded bytes to the terminal.")
    slow_print(f"The terminal then decodes the bytes back to characters to display them visually on the screen.")
    slow_print(f"Let’s analyze a simple process in Python to simulate this behavior.")

    # Simulate terminal output with UTF-8 encoding
    example_text = "Hello, Terminal! 🚀"
    print(f"\n{YELLOW}Terminal Output: {example_text}{RESET}")
    print(f"\n{CYAN}Below are the UTF-8 bytes sent by the terminal for the above text:{RESET}")

    # Displaying the raw bytes sent to the terminal
    utf8_bytes = example_text.encode('utf-8')
    print(f"{MAGENTA}UTF-8 Encoded Bytes for Terminal Output:{RESET}")
    print(f"{CYAN}{binascii.hexlify(utf8_bytes).upper()}{RESET}")

    slow_print(f"\nSo, when you type something in the terminal, it’s actually a series of byte sequences being sent to the terminal program.")
    slow_print(f"These bytes are interpreted as text and displayed as characters or symbols, depending on the encoding.")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 UTF-8 Terminal Output Quiz Time!{RESET}")
    print(f"\n{CYAN}What happens when you type a non-ASCII character in a terminal program?{RESET}")
    print(f"{YELLOW}A) The character is printed directly as a symbol.{RESET}")
    print(f"{YELLOW}B) The character is converted into multiple bytes and then printed.{RESET}")
    print(f"{YELLOW}C) The terminal throws an error and stops working.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "B":
        print(f"{GREEN}✅ Correct! Non-ASCII characters are converted into multiple bytes and then printed in the terminal.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is B. Non-ASCII characters in UTF-8 are represented by multiple bytes.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 is a variable-length encoding system that uses 1 to 4 bytes to represent characters.")
    slow_print(f"✔ Terminal programs interpret UTF-8 encoded bytes and display them as text, whether it's a symbol, emoji, or regular ASCII character.")
    slow_print(f"✔ Understanding UTF-8 encoding helps us understand how different characters are stored and transmitted over the terminal.")
    print(f"{GREEN}Now you’re equipped to analyze and understand UTF-8 output from terminal programs! 💻🌐{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    display_utf8_output()
    analyze_cli_utf8()
    utf8_in_terminal()
    quiz()
    summary()

