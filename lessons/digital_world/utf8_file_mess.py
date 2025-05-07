# lessons/encoding/utf8_file_mess.py

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
    print(f"{BOLD}{MAGENTA}💥 Welcome to UTF-8 Encoding Failures!{RESET}")
    slow_print(f"{CYAN}Have you ever opened a file and seen strange characters like '�' or '?',")
    slow_print("instead of the expected text? That's what happens when UTF-8 encoding fails!")
    input(f"\n{YELLOW}Press Enter to learn how encoding failures occur... {RESET}")

def show_broken_utf8():
    print(f"\n{BOLD}{CYAN}🔍 Example of Broken UTF-8 Encoding{RESET}")
    
    # Example of a byte sequence that is not valid UTF-8
    invalid_bytes = b'\x80\x81\x82'
    
    try:
        print(f"{YELLOW}Attempting to decode invalid bytes...{RESET}")
        print(invalid_bytes.decode('utf-8'))
    except UnicodeDecodeError as e:
        print(f"{RED}❌ Error: {e}{RESET}")
    
    slow_print(f"{CYAN}This happens because the byte sequence doesn't follow valid UTF-8 rules.")
    slow_print(f"Bytes like '\\x80', '\\x81', '\\x82' are not valid starting points in UTF-8 encoding.")

def demonstrate_malformed_text():
    print(f"\n{BOLD}{CYAN}💥 What Happens When Editors Misinterpret UTF-8?{RESET}")

    # Example of "garbled" text due to wrong encoding
    wrong_encoding_text = b'\xff\xfeT\x00e\x00x\x00t\x00'.decode('utf-16')
    print(f"\n{YELLOW}Text interpreted as UTF-16 instead of UTF-8:{RESET}")
    print(f"{RED}{wrong_encoding_text}{RESET}")
    slow_print(f"{CYAN}This happens when the file was saved as UTF-8, but the editor tried to read it as UTF-16.")

def explain_bom():
    print(f"\n{BOLD}{MAGENTA}🔑 What is a BOM (Byte Order Mark)?{RESET}")
    slow_print(f"{CYAN}A BOM is a special marker at the beginning of a file that tells an editor what encoding to expect.")
    slow_print(f"When a file is saved as UTF-8 without BOM, editors might misinterpret its encoding!")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick Encoding Quiz!{RESET}")
    print(f"\n{CYAN}What would happen if a UTF-8 file is opened as ASCII?{RESET}")
    answer = input(f"{YELLOW}Your Answer: {RESET}").strip().lower()

    if "error" in answer or "garbled" in answer:
        print(f"{GREEN}✅ Correct! It would either throw an error or show incorrect characters.{RESET}")
    else:
        print(f"{RED}❌ Nope! If UTF-8 is opened as ASCII, you get encoding errors or unreadable text.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Encoding failures occur when byte sequences don't follow the expected encoding rules.")
    slow_print("✔ Editors might misinterpret UTF-8 encoded files if they are not opened correctly.")
    slow_print("✔ A BOM can help identify the correct encoding, but it's not always present.")
    print(f"{GREEN}Now you know how to spot broken UTF-8 and how encoding issues happen! 💡{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_broken_utf8()
    demonstrate_malformed_text()
    explain_bom()
    quiz()
    summary()

if __name__ == "__main__":
    run()
