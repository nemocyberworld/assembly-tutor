# lessons/files/file_signatures.py

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

# 🔎 Known file signatures
SIGNATURES = {
    b'\x89PNG\r\n\x1a\n': "PNG image",
    b'%PDF': "PDF document",
    b'\x7fELF': "ELF executable (Linux binary)",
    b'\xFF\xD8\xFF': "JPEG image",
    b'GIF87a': "GIF image (1987)",
    b'GIF89a': "GIF image (1989)"
}

def intro():
    print(f"{BOLD}{MAGENTA}📂 Welcome to File Signature Scanner!{RESET}")
    slow_print(f"{CYAN}Did you know every file begins with a special ID called a 'magic number'?")
    slow_print("It helps your OS know what kind of file it is—before even looking at the name!")
    input(f"\n{YELLOW}Press Enter to scan a file and check its magic... {RESET}")

def read_file_signature(filename, max_len=8):
    try:
        with open(filename, "rb") as f:
            return f.read(max_len)
    except FileNotFoundError:
        print(f"{RED}⚠️ File '{filename}' not found. Check the path or place it in the same folder.{RESET}")
        return None

def identify_file_type(signature):
    for magic, filetype in SIGNATURES.items():
        if signature.startswith(magic):
            return filetype
    return "Unknown file type"

def scan_sample_file():
    print(f"\n{BOLD}{BLUE}🔬 Scanning File...{RESET}")
    sample_file = "sample.bin"  # Rename to your test file (e.g., test.pdf, image.png)

    sig = read_file_signature(sample_file)
    if sig:
        print(f"{YELLOW}Magic Bytes: {GREEN}{' '.join(f'{b:02X}' for b in sig)}{RESET}")
        filetype = identify_file_type(sig)
        print(f"{CYAN}🧠 Identified Type: {BOLD}{filetype}{RESET}")

def explain_magic():
    print(f"\n{BOLD}{MAGENTA}📘 What are Magic Bytes?{RESET}")
    slow_print(f"{CYAN}✔ They're the first few bytes of a file—unique to its format.")
    slow_print("✔ PNG starts with 89 50 4E 47 ...")
    slow_print("✔ PDF starts with 25 50 44 46 ...")
    slow_print("✔ ELF starts with 7F 45 4C 46 ...")
    slow_print("✔ Your computer reads these bytes to determine file type.")
    print(f"{GREEN}It’s like a secret handshake for files! 🤝{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📦 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Magic bytes tell you what a file *really* is, regardless of its name.")
    slow_print("✔ Python can read and compare these to known signatures.")
    slow_print("✔ Great for debugging or writing your own file type detectors.")
    print(f"{GREEN}Now you're a file detective! 🕵️‍♂️🔍{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    scan_sample_file()
    explain_magic()
    summary()
