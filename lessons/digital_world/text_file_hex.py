# lessons/encoding/text_file_hex.py

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
    print(f"{BOLD}{MAGENTA}📄 Welcome to: View Text Files in Hex!{RESET}")
    slow_print(f"{CYAN}Ever wondered what a text file looks like underneath?")
    slow_print("In this lesson, we’ll view a file as raw bytes — in ASCII and UTF-8!")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def read_text_file(filename, encoding="utf-8"):
    try:
        with open(filename, "r", encoding=encoding) as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"{RED}⚠️ File '{filename}' not found. Place it in the same folder.{RESET}")
        return None
    except UnicodeDecodeError:
        print(f"{RED}⚠️ Cannot decode using {encoding}. Try a different encoding.{RESET}")
        return None

def show_bytes(content, encoding="utf-8"):
    print(f"\n{BOLD}{BLUE}🔍 Viewing Bytes in {encoding.upper()} Encoding:{RESET}")
    byte_data = content.encode(encoding)
    for i, byte in enumerate(byte_data[:32]):  # show only first 32 bytes
        char = chr(byte) if 32 <= byte <= 126 else '.'
        print(f"{YELLOW}Byte {i:02}: {GREEN}0x{byte:02X} {CYAN}0b{byte:08b} {MAGENTA}{char}{RESET}")

def explain_encodings():
    print(f"\n{BOLD}{MAGENTA}🧠 Encoding Facts:{RESET}")
    slow_print(f"{CYAN}✔ ASCII uses 1 byte per character, for basic English only.")
    slow_print("✔ UTF-8 is more flexible — it supports all characters in Unicode.")
    slow_print("✔ Multi-byte characters in UTF-8 often begin with 0b110xxxxx or 0b1110xxxx.")
    print(f"{GREEN}You’re reading the matrix of your own text files! 🧠{RESET}")

def try_sample():
    print(f"\n{BOLD}{BLUE}🧪 Try with a Sample File!{RESET}")
    sample_file = "sample.txt"

    content = read_text_file(sample_file)
    if content:
        print(f"\n{CYAN}📄 First 100 characters of file:{RESET}")
        print(f"{BOLD}{content[:100]}{RESET}")
        show_bytes(content, "utf-8")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ All text is stored as bytes — ASCII or UTF-8 are just encodings.")
    slow_print("✔ Use Python's `.encode()` to convert text to raw bytes.")
    slow_print("✔ With hex and binary, you can see exactly what’s in your file.")
    print(f"{GREEN}Keep decoding! You're now fluent in byte-speak! 🚀{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    try_sample()
    explain_encodings()
    summary()

if __name__ == "__main__":
    run()
