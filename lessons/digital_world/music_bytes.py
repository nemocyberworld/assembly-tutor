# lessons/hex/music_bytes.py

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
    print(f"{BOLD}{MAGENTA}🎧 Music Files in Hex!{RESET}")
    slow_print(f"{CYAN}Ever wondered what your favorite MP3 looks like under the hood?")
    slow_print("Or why WAV files begin with 'RIFF'? 🎵")
    slow_print("Let’s peek into music files at the byte level!")
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
    print(f"\n{BOLD}{BLUE}🔍 First 64 Bytes in Hex + ASCII:{RESET}")
    for i in range(0, len(byte_data), 16):
        chunk = byte_data[i:i+16]
        hex_part = ' '.join(f"{b:02X}" for b in chunk)
        ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        print(f"{BLUE}{0x0000 + i:04X}{RESET}  {YELLOW}{hex_part:<48}{RESET} {GREEN}|{ascii_part}|{RESET}")

def demo_music_header():
    print(f"\n{BOLD}{MAGENTA}🎼 Demo: Reading a WAV or MP3 Header{RESET}")
    sample_wav = "sample.wav"
    sample_mp3 = "sample.mp3"

    for file in [sample_wav, sample_mp3]:
        if not os.path.exists(file):
            print(f"{YELLOW}💡 Tip: Add a '{file}' file in this folder to see real data.{RESET}")
            continue

        print(f"\n{CYAN}📁 {file}:{RESET}")
        data = read_hex_bytes(file)
        if data:
            format_hex_view(data)

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ WAV files start with 'RIFF' and 'WAVE'")
    slow_print("✔ MP3 files often start with 'ID3' (metadata) or 0xFFFB (frame sync)")
    slow_print("✔ Hex views help you identify file types and structure")
    print(f"{GREEN}🎶 You're now listening to bytes with your brain!{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick Byte Challenge!{RESET}")
    test_bytes = b'RIFF$\x00\x00\x00WAVEfmt '
    format_hex_view(test_bytes)
    guess = input(f"{YELLOW}🧠 What type of file does this look like? {RESET}").strip().lower()
    if "wav" in guess or "wave" in guess:
        print(f"{GREEN}✅ Correct! That's a WAV header!{RESET}")
    else:
        print(f"{RED}❌ Not quite. That was a WAV file header!{RESET}")

    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    demo_music_header()
    quiz()
    summary()

if __name__ == "__main__":
    run()
