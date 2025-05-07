# lessons/bash/bash_script_ascii.py

import binascii
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
    """Prints text slowly, simulating a typing effect."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🖥️ Welcome to Bash Script Inspection!{RESET}")
    slow_print(f"{CYAN}Bash scripts are written in plain text and executed in the terminal. In this lesson, we’ll inspect a Bash script’s raw content and look at its ASCII encoding.")
    slow_print(f"Understanding how encoding works can help us avoid errors and issues when running scripts in different environments.")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def read_file_in_ascii(file_path):
    """Reads a Bash script file and returns its content in ASCII format."""
    try:
        with open(file_path, 'r') as f:
            file_content = f.read()
            ascii_content = ''.join([format(ord(ch), '02X') for ch in file_content])
            return ascii_content
    except Exception as e:
        return f"{RED}Error reading file: {e}{RESET}"

def inspect_bash_script(file_path):
    """Inspects a Bash script by reading and displaying its ASCII content."""
    print(f"\n{BOLD}{CYAN}🔍 Inspecting Bash Script at: {RESET}{YELLOW}{file_path}{RESET}")
    slow_print(f"{CYAN}Let’s take a look at the raw content of this Bash script and how it’s encoded in ASCII.")
    
    # Read the Bash script in ASCII format
    script_ascii = read_file_in_ascii(file_path)
    
    if "Error" in script_ascii:
        print(script_ascii)
        return
    
    # Show the first 256 characters in ASCII (for demo purposes)
    print(f"\n{YELLOW}First 256 Characters in ASCII (Hex):{RESET}")
    print(f"\n{script_ascii[:512]}")  # Display a portion of the ASCII content

def bash_script_encoding_issues():
    print(f"\n{BOLD}{CYAN}⚠️ Potential Encoding Issues{RESET}")
    slow_print(f"{CYAN}If a Bash script was saved in a non-standard encoding or contains characters not recognized by the terminal, it might not execute correctly.")
    
    # Example of a potential issue: Non-ASCII characters
    slow_print(f"\nLet’s simulate an issue with an encoding mismatch, where characters appear incorrectly.", delay=0.05)
    print(f"\n{RED}Example of broken encoding in the terminal:{RESET}")
    print(f"{MAGENTA}ï¿½ç¤¾" + RESET)  # Simulated broken encoding (usually caused by mismatched encoding)

def demo_bash_script_analysis():
    print(f"\n{BOLD}{CYAN}🔍 Demo: Analyzing a Bash Script's ASCII Encoding{RESET}")
    slow_print(f"{CYAN}Let’s analyze a sample Bash script and see how its encoding can affect its execution.")
    
    # Simulated Bash script path (replace with an actual Bash script on your system)
    script_file_path = "sample_script.sh"
    
    # Inspect the file and show its ASCII content
    inspect_bash_script(script_file_path)
    
    # Encoding issue example
    bash_script_encoding_issues()

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Bash Script Encoding Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: What could cause a Bash script to fail when executed due to encoding issues?{RESET}")
    print(f"{YELLOW}A) Non-ASCII characters in the script{RESET}")
    print(f"{YELLOW}B) Incorrect file permissions{RESET}")
    print(f"{YELLOW}C) Missing shebang line{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "A":
        print(f"{GREEN}✅ Correct! Non-ASCII characters or improper encoding could cause the script to fail or display incorrectly in the terminal.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is A. Encoding issues often occur when non-ASCII characters are included without the proper encoding.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Bash scripts are written in plain text, and understanding how they’re encoded can help prevent errors during execution.")
    slow_print(f"✔ ASCII encoding is commonly used, and we can view a script’s encoding by inspecting the raw hexadecimal bytes of its content.")
    slow_print(f"✔ Encoding issues, like non-ASCII characters, can break the execution of a script and cause it to display incorrectly.")
    print(f"{GREEN}Now you know how to inspect a Bash script’s encoding and handle potential issues with character representation! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    demo_bash_script_analysis()
    quiz()
    summary()

