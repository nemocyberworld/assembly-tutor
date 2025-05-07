# lessons/jpeg/jpeg_headers.py

import time
import binascii

# 🎨 Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# JPEG Magic Bytes (Header)
JPEG_MAGIC = b'\xFF\xD8\xFF'

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}📸 Welcome to JPEG Header Exploration!{RESET}")
    slow_print(f"{CYAN}JPEG images have a unique structure, and we can decode them by examining the **magic bytes** at the beginning of the file.")
    slow_print(f"Today, we’ll focus on how to spot these special bytes that help identify JPEG images. 🔍")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def jpeg_header_overview():
    print(f"\n{BOLD}{CYAN}🔍 What is a JPEG Magic Byte?{RESET}")
    slow_print(f"{CYAN}The **magic bytes** are specific sequences of bytes at the start of a file that help identify the type of file. For JPEG images, the magic byte sequence is usually `FF D8 FF`.")
    slow_print(f"These bytes signal the beginning of a JPEG image file. Let's break down what each part means:")

    print(f"\n{YELLOW}JPEG Magic Byte Sequence (Hex): {JPEG_MAGIC.hex().upper()}{RESET}")
    slow_print(f"\n- **FF D8**: Indicates the start of the JPEG file. It’s the **start-of-image (SOI)** marker.")
    slow_print(f"- **FF**: Marks the start of each segment in the JPEG file.")
    slow_print(f"- **D8**: Signals the beginning of the actual image data.")
    slow_print(f"\nThese magic bytes help software identify the JPEG file, even if it's misnamed or corrupted.")

def visualize_jpeg_magic_bytes():
    print(f"\n{BOLD}{CYAN}🔧 Visualizing the JPEG Magic Bytes{RESET}")
    slow_print(f"{CYAN}Now, let’s take a closer look at how we can spot the magic bytes in a JPEG file. We’ll open the file, read its header, and look for `FF D8 FF`.")
    
    # Let's simulate reading a JPEG file header (this is just an example!)
    jpeg_example = b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00'
    print(f"\n{MAGENTA}Reading a Sample JPEG File (First 20 Bytes):{RESET}")
    print(f"{YELLOW}{binascii.hexlify(jpeg_example).upper()}{RESET}")
    
    # Check if the magic bytes are correct
    if jpeg_example[:3] == JPEG_MAGIC:
        print(f"{GREEN}✅ Magic Bytes Found: This is a valid JPEG file!{RESET}")
    else:
        print(f"{RED}❌ No valid JPEG Magic Bytes found! This is not a valid JPEG.{RESET}")

def jpeg_header_structure():
    print(f"\n{BOLD}{CYAN}🔍 Decoding the JPEG Header Structure{RESET}")
    slow_print(f"{CYAN}Beyond the magic bytes, a JPEG file contains several markers and segments, each with specific functions.")
    slow_print(f"Here’s a simplified breakdown of how a JPEG file is structured:")

    print(f"\n{YELLOW}1. **Start of Image (SOI) - `FF D8`**: Marks the beginning of the image file.{RESET}")
    print(f"{YELLOW}2. **APP0 Segment - `FF E0`**: Contains metadata about the image (e.g., JFIF format).{RESET}")
    print(f"{YELLOW}3. **Start of Scan - `FF DA`**: Marks the start of the image data (compressed image pixels).{RESET}")
    print(f"{YELLOW}4. **End of Image (EOI) - `FF D9`**: Marks the end of the image file.{RESET}")
    
    slow_print(f"\nThese segments and markers help decode the image, understand its format, and properly display it.")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 JPEG Header Quiz Time!{RESET}")
    print(f"\n{CYAN}What do the bytes `FF D8 FF` represent in a JPEG file?{RESET}")
    print(f"{YELLOW}A) End of Image Marker{RESET}")
    print(f"{YELLOW}B) Start of Image Marker{RESET}")
    print(f"{YELLOW}C) Data for Image Compression{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "B":
        print(f"{GREEN}✅ Correct! The bytes `FF D8 FF` mark the **Start of Image** in a JPEG file.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is B. `FF D8 FF` marks the **Start of Image** in a JPEG.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ JPEG files are identified by their **magic bytes**: `FF D8 FF` at the start of the file.")
    slow_print(f"✔ The JPEG file contains various segments, each with specific markers such as `FF E0` for metadata and `FF DA` for the image data.")
    slow_print(f"✔ Recognizing the magic bytes helps you determine whether a file is indeed a JPEG image or not.")
    print(f"{GREEN}Now you have a better understanding of how JPEG files are structured and how to identify them! 🌐{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    jpeg_header_overview()
    visualize_jpeg_magic_bytes()
    jpeg_header_structure()
    quiz()
    summary()

if __name__ == "__main__":
    run()
