# lessons/basics/bom_markers.py

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
    """Prints text slowly with a delay between characters."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    """Displays the introduction to the BOM lesson."""
    print(f"{BOLD}{MAGENTA}🔍 Welcome to 'Byte Order Mark (BOM)' Lesson!{RESET}")
    slow_print(f"{CYAN}In this lesson, we’ll explore what a Byte Order Mark (BOM) is, how it’s used in text encoding, and why it matters.")
    slow_print(f"{CYAN}By the end, you’ll know how to work with BOMs in Python and understand how they affect the way files are read and written.")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_bom():
    """Explains what a BOM is and shows examples."""
    print(f"\n{BOLD}{BLUE}📖 What is a Byte Order Mark (BOM)?{RESET}")
    slow_print(f"{CYAN}✔ A BOM is a special marker placed at the beginning of a text file to indicate the encoding format used (such as UTF-8, UTF-16).")
    slow_print(f"{CYAN}✔ It is useful for determining byte order (endianness) and encoding type, especially in UTF-16 and UTF-32.")
    slow_print(f"{CYAN}✔ The BOM is optional but can be helpful in preventing misinterpretation of file encoding.")
    print(f"{CYAN}The BOM for UTF-8 is: {RESET}{repr(b'\xef\xbb\xbf')}")
    print(f"{CYAN}The BOM for UTF-16 (Big Endian) is: {RESET}{repr(b'\xfe\xff')}")
    print(f"{CYAN}The BOM for UTF-16 (Little Endian) is: {RESET}{repr(b'\xff\xfe')}")

def show_bom_usage():
    """Describes how BOM is used in practice."""
    print(f"\n{BOLD}{CYAN}🔧 How BOM is Used in File Encoding{RESET}")
    slow_print(f"{CYAN}✔ When a file is opened, the BOM helps the reader or program understand how to interpret the byte sequence.")
    slow_print(f"{CYAN}✔ In UTF-16 or UTF-32, the BOM helps identify the byte order: Big Endian (BE) or Little Endian (LE).")
    slow_print(f"{CYAN}✔ UTF-8 doesn’t need a BOM to define byte order, but it can still include one as a signature to indicate it's UTF-8 encoded.")

def detect_bom_in_file():
    """Simulates detecting BOMs in different file encodings."""
    print(f"\n{BOLD}{MAGENTA}🔍 Detecting a BOM in a File{RESET}")
    slow_print(f"{CYAN}Let’s simulate detecting a BOM in a text file! In practice, we read the first few bytes of the file to see if it starts with a BOM.")

    bom_utf8 = b'\xef\xbb\xbf' + b'Hello, World!'
    print(f"{CYAN}Simulated UTF-8 BOM file content: {RESET}{bom_utf8}")

    if bom_utf8.startswith(b'\xef\xbb\xbf'):
        print(f"{GREEN}✅ BOM Detected: UTF-8{RESET}")
    else:
        print(f"{RED}❌ No BOM detected!{RESET}")

    print(f"\n{CYAN}Now, let’s simulate a UTF-16 BOM check...")

    bom_utf16_be = b'\xfe\xff' + b'Hello, World!'.encode('utf-16-be')
    print(f"{CYAN}Simulated UTF-16 BOM file content: {RESET}{bom_utf16_be}")

    if bom_utf16_be.startswith(b'\xfe\xff'):
        print(f"{GREEN}✅ BOM Detected: UTF-16 Big Endian{RESET}")
    else:
        print(f"{RED}❌ No BOM detected!{RESET}")

def handle_bom_in_python():
    """Demonstrates how to handle BOMs when writing and reading files in Python."""
    print(f"\n{BOLD}{CYAN}🛠️ Handling BOM in Python{RESET}")
    slow_print(f"{CYAN}In Python, you can easily check for and handle BOMs while reading or writing files.")
    slow_print(f"{CYAN}Here’s how you can write a file with a BOM in UTF-8 encoding:")

    with open("example_with_bom.txt", "wb") as f:
        f.write(b'\xef\xbb\xbf')  # UTF-8 BOM
        f.write(b'Hello, World!')

    slow_print(f"{CYAN}Now, let's read the file and see if the BOM is present:")

    with open("example_with_bom.txt", "rb") as f:
        content = f.read()
        if content.startswith(b'\xef\xbb\xbf'):
            print(f"{GREEN}✅ BOM Detected: UTF-8{RESET}")
            content = content[3:]
            print(f"{CYAN}Content after removing BOM: {RESET}{content.decode('utf-8')}")
        else:
            print(f"{RED}❌ No BOM detected!{RESET}")

def quiz():
    """Interactive quiz to test BOM knowledge."""
    print(f"\n{BOLD}{MAGENTA}🎮 BOM Quiz Time!{RESET}")
    score = 0

    questions = [
        ("What does a BOM indicate?", "Encoding format and byte order"),
        ("Does UTF-8 require a BOM?", "No"),
        ("What is the BOM for UTF-16 Big Endian?", "FE FF"),
        ("How do you remove a BOM in Python?", "By slicing the first three bytes after detecting it"),
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
        print(f"{GREEN}🎉 Excellent! You’re BOM-smart!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👍 Good job! Keep practicing!{RESET}")
    else:
        print(f"{RED}💡 Keep exploring BOMs—you'll master it soon!{RESET}")

def summary():
    """Summarizes key takeaways from the BOM lesson."""
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ A BOM is a special marker at the beginning of a file to indicate encoding type and byte order.")
    slow_print(f"✔ It is especially useful in UTF-16 and UTF-32 encodings for determining byte order (endianness).")
    slow_print(f"✔ In UTF-8, the BOM is optional, but it can still serve as a signature for UTF-8 encoded files.")
    slow_print(f"✔ Python makes it easy to work with BOMs when reading or writing files. Just be aware of the BOM when processing text files!")
    print(f"{GREEN}Keep experimenting with BOMs and encoding, and you'll be a file encoding expert! 🧠{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    """Runs the BOM Markers lesson."""
    intro()
    explain_bom()
    show_bom_usage()
    detect_bom_in_file()
    handle_bom_in_python()
    quiz()
    summary()

# Run the lesson
if __name__ == "__main__":
    run()
