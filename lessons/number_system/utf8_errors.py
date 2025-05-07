# lessons/basics/utf8_errors.py

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
    print(f"{BOLD}{MAGENTA}🔥 Welcome to 'How Invalid UTF-8 Sequences Cause Errors'!{RESET}")
    slow_print(f"{CYAN}In this lesson, we’ll explore how invalid UTF-8 byte sequences can cause encoding and decoding errors.")
    slow_print("You'll also get to see how Python handles such errors and how to fix them. Let's dive in! 🧑‍💻")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_utf8_encoding():
    print(f"\n{BOLD}{BLUE}📖 UTF-8 Encoding Overview{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 is a variable-length encoding system that represents characters using 1 to 4 bytes.")
    slow_print(f"{CYAN}✔ It’s widely used because it can handle all Unicode characters and is backward compatible with ASCII.")
    slow_print(f"{CYAN}✔ However, if the byte sequence is not valid, errors occur when decoding the bytes back to characters.")

def demonstrate_invalid_utf8():
    print(f"\n{BOLD}{CYAN}🔍 Demonstrating Invalid UTF-8 Sequences{RESET}")
    
    invalid_sequences = [
        [0x80],  # Invalid single byte (ASCII range is 0x00 to 0x7F)
        [0xC0, 0x80],  # Overlong encoding (shouldn't happen in UTF-8)
        [0xF0, 0x28, 0x8C, 0x28],  # Invalid 4-byte sequence
        [0xFF, 0xFF, 0xFF],  # Completely invalid byte sequence
    ]
    
    for i, seq in enumerate(invalid_sequences, 1):
        byte_sequence = bytes(seq)
        try:
            print(f"\n{BOLD}{RED}Example {i}: Trying to decode an invalid UTF-8 sequence...{RESET}")
            decoded_string = byte_sequence.decode('utf-8')
            print(f"{GREEN}✅ Decoded: {decoded_string}{RESET}")
        except UnicodeDecodeError as e:
            print(f"{RED}❌ Error: {e}{RESET}")

def handle_utf8_errors():
    print(f"\n{BOLD}{CYAN}🔧 Handling UTF-8 Errors: The 'errors' Parameter{RESET}")
    slow_print(f"{CYAN}In Python, when decoding invalid UTF-8 sequences, we can use the 'errors' parameter to control how errors are handled.")
    
    slow_print(f"{YELLOW}Let's see some options for the 'errors' parameter:")
    print(f"{GREEN}- 'strict': Raises a UnicodeDecodeError (default behavior).")
    print(f"{GREEN}- 'ignore': Ignores the invalid bytes.")
    print(f"{GREEN}- 'replace': Replaces invalid bytes with a placeholder (�).")
    
    print(f"\n{BOLD}{MAGENTA}Let's try these out with invalid UTF-8 sequences!{RESET}")

    # Using 'ignore'
    try:
        invalid_bytes = b'\xF0\x28\x8C\x28'
        print(f"{YELLOW}With 'ignore' option: {RESET}{invalid_bytes.decode('utf-8', 'ignore')}")
    except UnicodeDecodeError:
        print(f"{RED}❌ 'ignore' failed... but the invalid bytes were simply skipped!{RESET}")
        
    # Using 'replace'
    print(f"{YELLOW}With 'replace' option: {RESET}{invalid_bytes.decode('utf-8', 'replace')}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 UTF-8 Error Handling Quiz!{RESET}")
    score = 0

    questions = [
        ("What happens if you try to decode an invalid UTF-8 sequence in Python?", "UnicodeDecodeError"),
        ("Which error-handling strategy replaces invalid bytes with a placeholder?", "replace"),
        ("Which error-handling strategy simply skips invalid bytes?", "ignore"),
        ("What is the default error-handling strategy in Python?", "strict"),
    ]

    for i, (q, a) in enumerate(questions, 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip()
        if user.lower() == a.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is: {GREEN}{a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Your score: {score}/4{RESET}")
    if score == 4:
        print(f"{GREEN}🌟 Great job! You're a UTF-8 error-handling pro!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👍 Nice work! You're on your way to mastering UTF-8!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing, and you’ll nail it next time!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 is a flexible encoding, but invalid byte sequences can cause decoding errors.")
    slow_print(f"✔ Python’s 'errors' parameter helps handle these errors, allowing you to either skip or replace invalid bytes.")
    slow_print(f"✔ Understanding these concepts ensures you can effectively manage encoding issues in your applications.")
    print(f"{GREEN}Keep practicing, and you’ll become a UTF-8 expert! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
def run():
    intro()
    explain_utf8_encoding()
    demonstrate_invalid_utf8()
    handle_utf8_errors()
    quiz()
    summary()
if __name__ == "__main__":
    run()
