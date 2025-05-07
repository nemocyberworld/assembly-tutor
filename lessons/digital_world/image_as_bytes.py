# lessons/digital_world/image_as_bytes.py

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
    print(f"{BOLD}{MAGENTA}🖼 Welcome to 'Image as Bytes: Hex & Binary View!'{RESET}")
    slow_print(f"{CYAN}Did you know your favorite image is just a bunch of bytes?")
    slow_print("And we can actually view them in hexadecimal and binary!")
    input(f"\n{YELLOW}Ready to peek inside an image? Press Enter... {RESET}")

def read_image_bytes(filename, num_bytes=16):
    try:
        with open(filename, "rb") as f:
            return f.read(num_bytes)
    except FileNotFoundError:
        print(f"{RED}⚠️ File not found! Make sure '{filename}' exists in your directory.{RESET}")
        return None

def display_bytes_as_hex_and_binary(data):
    print(f"\n{BOLD}{BLUE}📦 Raw Byte View (Hex + Binary){RESET}")
    for i, byte in enumerate(data):
        hex_val = f"{byte:02X}"
        bin_val = f"{byte:08b}"
        print(f"{YELLOW}Byte {i:02}: {GREEN}0x{hex_val} {CYAN}0b{bin_val}{RESET}")
        time.sleep(0.05)

def explain_file_headers():
    print(f"\n{BOLD}{MAGENTA}🔍 What's in Those First Few Bytes?{RESET}")
    slow_print(f"{CYAN}File headers tell your computer what kind of file it is.")
    slow_print("For example, JPEG files usually start with:")
    print(f"{GREEN}0xFF 0xD8 → That's the JPEG header! 📸{RESET}")
    slow_print("Each file type has a 'magic number' at the beginning.")

def try_sample():
    print(f"\n{BOLD}{BLUE}🧪 Try with a Sample Image!{RESET}")
    sample_file = "sample.jpg"  # You can change this to any image file
    data = read_image_bytes(sample_file)
    if data:
        display_bytes_as_hex_and_binary(data)
        explain_file_headers()

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Images are just files filled with binary data (bytes).")
    slow_print("✔ Each byte can be viewed in hex (0x) and binary (0b) formats.")
    slow_print("✔ File headers help software recognize file types.")
    print(f"{GREEN}Now you're not just seeing images—you’re seeing the *code* behind them! 🧠{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    try_sample()
    summary()
