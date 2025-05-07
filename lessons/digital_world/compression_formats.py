# lessons/compression/compression_formats.py

import time
import zlib
import zipfile
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
    print(f"{BOLD}{MAGENTA}📦 Welcome to Compression Magic!{RESET}")
    slow_print(f"{CYAN}Ever wondered how big files shrink into something tiny when zipped or gzipped?")
    slow_print("Today, we’re going to see the magic of compression at the byte level! 💫")
    input(f"\n{YELLOW}Press Enter to explore compression... {RESET}")

def demo_zip_compression():
    data = b"This is a test sentence that we will compress using ZIP format. " * 10
    print(f"{BOLD}{CYAN}🔧 Compressing Data with ZIP...{RESET}")
    
    # Create a zip file and write data to it
    with zipfile.ZipFile("example.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr("file.txt", data)

    # Show original and compressed sizes
    original_size = len(data)
    zip_size = len(open("example.zip", "rb").read())
    
    print(f"{YELLOW}Original Size   : {original_size} bytes{RESET}")
    print(f"{GREEN}Compressed Size : {zip_size} bytes{RESET}")
    print(f"{BOLD}{CYAN}ZIP Compression Ratio:{RESET} {original_size / zip_size:.2f}")

def demo_gzip_compression():
    data = b"This is some data that will be compressed using GZIP format. " * 10
    print(f"\n{BOLD}{CYAN}🔧 Compressing Data with GZIP...{RESET}")

    # Compress data with gzip
    compressed = zlib.compress(data)

    # Show original and compressed sizes
    original_size = len(data)
    gzip_size = len(compressed)

    print(f"{YELLOW}Original Size   : {original_size} bytes{RESET}")
    print(f"{GREEN}Compressed Size : {gzip_size} bytes{RESET}")
    print(f"{BOLD}{CYAN}GZIP Compression Ratio:{RESET} {original_size / gzip_size:.2f}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick Compression Quiz!{RESET}")
    
    print(f"\n{CYAN}Which compression format usually results in smaller files? ZIP or GZIP?{RESET}")
    answer = input(f"{YELLOW}Your Answer: {RESET}").strip().lower()

    if "gzip" in answer:
        print(f"{GREEN}✅ Correct! GZIP is often more efficient for compression than ZIP.{RESET}")
    else:
        print(f"{RED}❌ Nope! GZIP usually provides better compression rates than ZIP.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Compression formats like ZIP and GZIP reduce data size for storage or transmission.")
    slow_print("✔ ZIP is versatile and widely used for archives, while GZIP is great for data transfer.")
    slow_print("✔ Compression algorithms identify patterns and reduce redundancies in data.")
    print(f"{GREEN}Now you can see the magic that happens when files shrink! ✨{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    demo_zip_compression()
    demo_gzip_compression()
    quiz()
    summary()
