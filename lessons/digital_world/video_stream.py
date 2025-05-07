# lessons/hex/video_stream.py

import time
import os

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
    print(f"{BOLD}{MAGENTA}🎞️ Welcome to Byte-Level Video Streams!{RESET}")
    slow_print(f"{CYAN}Ever wondered what an MP4 or AVI file looks like underneath?")
    slow_print("Video is just a stream of bytes, structured to hold audio, video, metadata, and more!")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def read_hex_bytes(filename, num_bytes=64):
    try:
        with open(filename, 'rb') as f:
            bytes_read = f.read(num_bytes)
        return bytes_read
    except FileNotFoundError:
        print(f"{RED}⚠️ File not found: {filename}{RESET}")
        return None

def format_hex_view(byte_data):
    print(f"\n{BOLD}{BLUE}🔍 Hex + ASCII View:{RESET}")
    for i in range(0, len(byte_data), 16):
        chunk = byte_data[i:i+16]
        hex_part = ' '.join(f"{b:02X}" for b in chunk)
        ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        print(f"{BLUE}{0x0000 + i:04X}{RESET}  {YELLOW}{hex_part:<48}{RESET} {GREEN}|{ascii_part}|{RESET}")

def demo_video_header():
    print(f"\n{BOLD}{MAGENTA}📹 Demo: Reading MP4 or AVI Headers{RESET}")
    sample_files = ["sample.mp4", "sample.avi"]

    for file in sample_files:
        if not os.path.exists(file):
            print(f"{YELLOW}💡 Tip: Add a '{file}' file to this folder to see real data.{RESET}")
            continue

        print(f"\n{CYAN}📁 {file}:{RESET}")
        data = read_hex_bytes(file)
        if data:
            format_hex_view(data)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Byte Guessing Game!{RESET}")
    test_bytes = b'\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom'
    format_hex_view(test_bytes)
    guess = input(f"{YELLOW}🧠 This file starts with 'ftyp' — what format is it likely? {RESET}").strip().lower()
    if "mp4" in guess:
        print(f"{GREEN}✅ Correct! That’s an MP4 file header!{RESET}")
    else:
        print(f"{RED}❌ Nope! That was from an MP4 video file.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ MP4 files often start with 'ftyp' (file type box)")
    slow_print("✔ AVI files start with 'RIFF....AVI '")
    slow_print("✔ All video is just structured binary — metadata + stream chunks")
    print(f"{GREEN}🎥 Now you can decode the opening scenes of a video... in HEX!{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    demo_video_header()
    quiz()
    summary()

if __name__ == "__main__":
    run()
