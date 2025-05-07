# lessons/logs/log_file_encoding.py

import chardet
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
    """Simulate slow printing for better engagement."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}📂 Welcome to Log File Encoding Insights!{RESET}")
    slow_print(f"{CYAN}Log files contain vital information about system events and behavior. However, encoding differences can cause problems when reading them.")
    slow_print(f"Let's dive into how encoding affects log file interpretation and how to handle encoding issues.")
    input(f"\n{YELLOW}Press Enter to start exploring... {RESET}")

def read_log_file(file_path):
    """Reads a log file and tries to determine its encoding."""
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            encoding = chardet.detect(raw_data)
            return raw_data, encoding['encoding']
    except Exception as e:
        return None, f"{RED}Error reading file: {e}{RESET}"

def display_log_file(file_path):
    """Displays log file content and its encoding."""
    print(f"\n{BOLD}{CYAN}🔍 Inspecting Log File: {RESET}{YELLOW}{file_path}{RESET}")
    raw_data, encoding = read_log_file(file_path)
    
    if encoding == "None":
        print(f"{RED}Error: Could not detect encoding.{RESET}")
        return

    print(f"\n{CYAN}Detected Encoding: {RESET}{YELLOW}{encoding}{RESET}")
    
    try:
        decoded_content = raw_data.decode(encoding)
        slow_print(f"\n{CYAN}Decoded Log File Content:{RESET}")
        print(f"{decoded_content[:300]}")  # Show first 300 characters for brevity
    except UnicodeDecodeError:
        print(f"{RED}Error: Unable to decode file with detected encoding.{RESET}")
        print(f"{CYAN}This might indicate that the file has encoding issues or contains mixed encodings.{RESET}")

def handle_encoding_issues():
    """Simulates handling encoding issues with a log file."""
    print(f"\n{BOLD}{CYAN}⚠️ Encoding Issues in Log Files{RESET}")
    slow_print(f"{CYAN}Sometimes, log files might not display correctly because of mismatched encoding. For example, non-ASCII characters can break the decoding process.")
    
    print(f"\n{RED}Example of broken encoding:{RESET}")
    print(f"{MAGENTA}ï¿½ç¤¾" + RESET)  # Simulated broken encoding for demo

    slow_print(f"\nTo fix these issues, we can try opening the file with different encoding formats or use tools like `iconv` to convert the encoding.")
    print(f"\n{CYAN}Try using the `utf-8` or `latin-1` encoding to resolve issues with unexpected characters.{RESET}")

def demo_log_file_analysis():
    print(f"\n{BOLD}{CYAN}🔍 Demo: Analyzing a Log File's Encoding{RESET}")
    slow_print(f"{CYAN}Let's analyze a sample log file to see how encoding plays a role in reading and interpreting the content.")
    
    # Simulated log file path (replace with an actual log file path on your system)
    log_file_path = "system_log.txt"
    
    display_log_file(log_file_path)
    
    # Simulate encoding handling
    handle_encoding_issues()

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Log File Encoding Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: What might cause a log file to display strange characters when opened?{RESET}")
    print(f"{YELLOW}A) The log file was written in a different encoding{RESET}")
    print(f"{YELLOW}B) The file is corrupted and unreadable{RESET}")
    print(f"{YELLOW}C) The log file is too large to read{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "A":
        print(f"{GREEN}✅ Correct! A log file might display strange characters if it was saved with a different encoding than expected.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is A. Encoding mismatches are the most common cause of display issues in log files.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Log files can be encoded in different formats, and it's important to detect and handle encoding differences when reading them.")
    slow_print(f"✔ Tools like `chardet` can help detect encoding and assist with decoding the content correctly.")
    slow_print(f"✔ Encoding issues can occur when log files contain unexpected characters or mismatched encoding formats.")
    print(f"{GREEN}By understanding encoding differences, you can troubleshoot and fix issues when working with log files. 🔧{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    demo_log_file_analysis()
    quiz()
    summary()

if __name__ == "__main__":
    run()
