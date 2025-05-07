# lessons/fonts/font_file_hex.py

import binascii
import os
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
    print(f"{BOLD}{MAGENTA}🔠 Welcome to Font File Exploration!{RESET}")
    slow_print(f"{CYAN}Fonts are more than just letters—they’re files with complex structures that are used to display characters on your screen. In this lesson, we’ll explore TrueType (TTF) and OpenType (OTF) font files.")
    slow_print(f"We’ll look at how these files are represented in hexadecimal and discover some interesting components like font metadata and tables.")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def read_file_in_hex(file_path):
    """Reads a font file and returns its content in hexadecimal format."""
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
            hex_content = binascii.hexlify(file_content).decode('utf-8')
            return hex_content
    except Exception as e:
        return f"{RED}Error reading file: {e}{RESET}"

def inspect_font_file(file_path):
    """Inspects a font file by reading and displaying its hex content."""
    print(f"\n{BOLD}{CYAN}🔍 Inspecting Font File at: {RESET}{YELLOW}{file_path}{RESET}")
    slow_print(f"{CYAN}Let’s take a look at the raw hex content of this font file. Font files contain tables, headers, and metadata, all encoded in bytes.")
    
    # Read the font file in hex format
    font_hex = read_file_in_hex(file_path)
    
    if "Error" in font_hex:
        print(font_hex)
        return
    
    # Show a portion of the hex content (first 256 bytes)
    print(f"\n{YELLOW}First 256 Bytes of Font File (Hex):{RESET}")
    print(f"\n{font_hex[:512]}")  # Display a small portion for demonstration

def font_file_structure():
    print(f"\n{BOLD}{CYAN}📚 Font File Structure Breakdown{RESET}")
    slow_print(f"{CYAN}Font files are typically structured with multiple tables that store various data like the font name, character shapes, and metadata.")
    
    # Common font file tables
    font_tables = [
        "head - Font Header",
        "hhea - Horizontal Header",
        "maxp - Maximum Profile",
        "name - Font Name",
        "cmap - Character to Glyph Mapping",
        "post - PostScript Information",
        "glyf - Glyph Data"
    ]
    
    print(f"\n{YELLOW}Common Font Tables:{RESET}")
    for table in font_tables:
        print(f"{MAGENTA}{table}{RESET}")
        slow_print(f"\nEach of these tables is encoded as part of the font file, and they help define how the font behaves and is displayed on your screen.", delay=0.05)

def demo_font_file_analysis():
    print(f"\n{BOLD}{CYAN}🔍 Demo: Analyzing TTF/OTF Font File Hex{RESET}")
    slow_print(f"{CYAN}Let’s analyze a sample font file and see how different sections of the file correspond to specific components of the font.")
    
    # Simulated font file path (replace with an actual font file on your system)
    font_file_path = "sample_font.ttf"
    
    # Inspect the file and show its hex content
    inspect_font_file(font_file_path)
    
    # Simulate a font file header structure
    slow_print(f"\nThe first few bytes of a font file often contain a **font signature** that tells us what kind of font it is.")
    print(f"\n{YELLOW}Font Signature (for TTF files): {RESET}{MAGENTA}00010000{RESET} (example)")
    slow_print(f"\nThis unique signature helps us recognize the type of font file.")
    
def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Font File Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: What is one of the primary functions of a font file's 'cmap' table?{RESET}")
    print(f"{YELLOW}A) It defines the character-to-glyph mapping.{RESET}")
    print(f"{YELLOW}B) It stores the font's name.{RESET}")
    print(f"{YELLOW}C) It handles font rendering settings.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "A":
        print(f"{GREEN}✅ Correct! The 'cmap' table maps characters to their corresponding glyphs (visual representations).{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is A. The 'cmap' table handles character-to-glyph mapping.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Font files (like TTF and OTF) contain multiple tables encoded in bytes that define various font properties.")
    slow_print(f"✔ The hex representation of a font file reveals raw bytes, table structures, and metadata, which help define how the font behaves.")
    slow_print(f"✔ Important tables include 'head' (header), 'name' (font name), 'cmap' (character mapping), and 'glyf' (glyph data).")
    print(f"{GREEN}Now you know how to peek inside font files and understand their structure at the byte level! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    demo_font_file_analysis()
    font_file_structure()
    quiz()
    summary()
