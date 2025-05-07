# lessons/basics/file_encoding_mismatch.py

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
    print(f"{BOLD}{MAGENTA}📚 Welcome to 'Diagnosing and Fixing Encoding Mismatches' Lesson!{RESET}")
    slow_print(f"{CYAN}In this lesson, we will learn how encoding mismatches happen in files, how to diagnose them, and how to fix these issues effectively.")
    slow_print(f"{CYAN}By the end, you’ll be able to handle common file encoding problems when working with text files in Python.")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_encoding_mismatch():
    print(f"\n{BOLD}{BLUE}📖 What is Encoding Mismatch?{RESET}")
    slow_print(f"{CYAN}✔ An encoding mismatch happens when a file is read with the wrong encoding format, causing unreadable or incorrect characters.")
    slow_print(f"{CYAN}✔ This is a common issue when a file is saved in one encoding (e.g., UTF-8) but read with another (e.g., ISO-8859-1).")
    slow_print(f"{CYAN}✔ Mismatches often appear as strange symbols, question marks, or corrupted characters, making the file’s content unreadable.")
    print(f"{RED}Example of Encoding Mismatch: If a UTF-8 file is read as ISO-8859-1, it can produce strange characters like: {RESET}ï¿½")

def diagnose_encoding_mismatch():
    print(f"\n{BOLD}{CYAN}🔍 How to Diagnose Encoding Mismatches{RESET}")
    slow_print(f"{CYAN}✔ To diagnose an encoding mismatch, you first need to check the encoding of the file and compare it with the encoding used to read it.")
    slow_print(f"{CYAN}✔ In Python, you can use the `chardet` library to detect a file's encoding.")
    
    try:
        import chardet
        print(f"{GREEN}✅ 'chardet' library is available for detecting file encodings!{RESET}")
    except ImportError:
        print(f"{RED}❌ 'chardet' library not found. You can install it with 'pip install chardet'!{RESET}")

    print(f"\n{CYAN}Let’s simulate diagnosing a mismatch. We will create a UTF-8 file and read it incorrectly as ISO-8859-1.")

    # Simulating writing a UTF-8 encoded file
    with open("utf8_file.txt", "w", encoding="utf-8") as f:
        f.write("Hello, this is a UTF-8 file! 👋")

    print(f"\n{CYAN}Now, let's try reading the file as ISO-8859-1 (incorrectly)...")
    try:
        with open("utf8_file.txt", "r", encoding="iso-8859-1") as f:
            content = f.read()
            print(f"{RED}❌ Mismatch detected! Here's the incorrect content: {RESET}{content}")
    except UnicodeDecodeError as e:
        print(f"{RED}❌ Encoding mismatch error: {RESET}{e}")

def fix_encoding_mismatch():
    print(f"\n{BOLD}{GREEN}🛠️ Fixing Encoding Mismatches{RESET}")
    slow_print(f"{CYAN}✔ To fix encoding mismatches, you need to open the file with the correct encoding.")
    slow_print(f"{CYAN}✔ If you know the correct encoding, simply specify it when opening the file with Python’s `open()` function.")
    print(f"{CYAN}Let's fix the issue by reading the file with the correct encoding (UTF-8).")

    with open("utf8_file.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"{GREEN}✅ Fixed! Correct content: {RESET}{content}")

def handle_common_encoding_problems():
    print(f"\n{BOLD}{CYAN}🔧 Handling Common Encoding Problems{RESET}")
    slow_print(f"{CYAN}✔ Sometimes, you may not know the exact encoding of a file. In such cases, you can use the `chardet` library to auto-detect the encoding.")
    slow_print(f"{CYAN}✔ If the file contains non-UTF-8 characters but is mostly UTF-8, you can try to open it with `errors='replace'` to prevent crashes.")
    
    # Simulating an encoding problem where we don’t know the encoding
    slow_print(f"{CYAN}Let’s simulate using 'chardet' to detect an unknown encoding:")
    
    try:
        import chardet
        with open("utf8_file.txt", "rb") as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result["encoding"]
            print(f"{GREEN}✅ Detected encoding: {encoding}{RESET}")
    except ImportError:
        print(f"{RED}❌ 'chardet' is not installed. Please install it with 'pip install chardet'.{RESET}")
    
    # Simulating reading with 'replace' error handling
    slow_print(f"{CYAN}Now, let’s read the file with error handling to avoid crashes:")
    
    with open("utf8_file.txt", "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
        print(f"{GREEN}✅ Successfully read file with replaced characters: {RESET}{content}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Encoding Mismatch Quiz Time!{RESET}")
    score = 0

    questions = [
        ("What causes encoding mismatches?", "Reading a file with the wrong encoding"),
        ("Which library can help detect file encodings in Python?", "chardet"),
        ("How can you fix an encoding mismatch?", "Open the file with the correct encoding"),
        ("What does `errors='replace'` do when opening a file?", "It replaces characters that can’t be decoded with a replacement character"),
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
        print(f"{GREEN}🎉 Excellent! You’ve mastered encoding mismatches!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👍 Great job! Keep practicing to improve!{RESET}")
    else:
        print(f"{RED}💡 Keep experimenting with encoding handling—you'll get it!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Encoding mismatches occur when a file is opened with the wrong encoding, resulting in unreadable characters.")
    slow_print(f"✔ To diagnose this, check the encoding and compare it with the file's actual encoding. You can use the `chardet` library for detection.")
    slow_print(f"✔ To fix mismatches, simply specify the correct encoding when opening the file, or use `errors='replace'` to prevent crashes.")
    slow_print(f"✔ Python makes handling encoding problems easy with simple functions like `open()` and error handling options.")
    print(f"{GREEN}Keep learning and experimenting with encoding handling to avoid common pitfalls! 🧠{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_encoding_mismatch()
    diagnose_encoding_mismatch()
    fix_encoding_mismatch()
    handle_common_encoding_problems()
    quiz()
    summary()
