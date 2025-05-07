# lessons/pdf/pdf_file_bytes.py

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

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}📑 Welcome to PDF File Structure Exploration!{RESET}")
    slow_print(f"{CYAN}Ever wonder what’s inside a PDF file? It's not just a fancy layout.")
    slow_print("Today, we'll inspect its raw structure and encoding. Let’s break down a PDF at the byte level! 🎉")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def pdf_magic_bytes():
    print(f"\n{BOLD}{CYAN}🔍 PDF Magic Bytes and Header{RESET}")
    slow_print(f"{CYAN}Every PDF starts with a specific sequence of bytes called the 'magic bytes'. This identifies the file as a PDF.")
    slow_print(f"The magic bytes for PDF are: %PDF-1.x, where x is the version number of the PDF standard.")
    print(f"\n{YELLOW}Example PDF Magic Bytes: %PDF-1.7{RESET}")
    
def read_pdf_bytes():
    print(f"\n{BOLD}{YELLOW}🔢 Inspecting PDF Header (Magic Bytes and Version){RESET}")
    
    # Simulating reading the first few bytes of a PDF file (typically the header)
    # Let's create a simple example with the header `%PDF-1.7`
    pdf_header = "%PDF-1.7\n"
    pdf_bytes = pdf_header.encode("ascii")  # Convert to bytes
    
    # Show the raw hex representation of the header
    hex_representation = binascii.hexlify(pdf_bytes).decode('utf-8')
    print(f"{CYAN}PDF Header in Hex: {hex_representation}{RESET}")
    
    print(f"\n{GREEN}The first few bytes of a PDF file contain important information, like the PDF version number and the magic bytes.%PDF-1.7 is a PDF file format version.{RESET}")
    
def show_pdf_structure():
    print(f"\n{BOLD}{CYAN}🔧 Breaking Down the PDF Structure{RESET}")
    slow_print(f"{CYAN}A PDF file is made up of multiple sections, including headers, body, cross-reference table, and trailer.")
    slow_print(f"Each part of the file has a specific encoding and structure.")
    print(f"\n{YELLOW}1. Header: Contains magic bytes and version.")
    print(f"2. Body: Stores the actual content (text, images, etc.) in a series of objects.")
    print(f"3. Cross-reference Table: Maps the object numbers to byte offsets in the file.")
    print(f"4. Trailer: Marks the end of the file and references important objects in the body.")
    
def extract_pdf_text():
    print(f"\n{BOLD}{CYAN}🔍 Extracting Text from PDF (Raw Hex and ASCII){RESET}")
    
    # Simulating a simple PDF body with an object
    # This is an example of an object storing text in the body
    pdf_object = "4 0 obj\n<</Type /Page\n/Contents 5 0 R>>\nendobj"
    
    # Convert the object to bytes and hex
    pdf_object_bytes = pdf_object.encode("ascii")
    pdf_object_hex = binascii.hexlify(pdf_object_bytes).decode('utf-8')
    
    print(f"{CYAN}PDF Object in Hex: {pdf_object_hex}{RESET}")
    print(f"{GREEN}This is part of the body, which contains objects like text, images, and links!{RESET}")

def simulate_pdf_file():
    print(f"\n{BOLD}{MAGENTA}📂 Let's Simulate a Simple PDF File!{RESET}")
    pdf_content = """
    %PDF-1.7
    1 0 obj
    <</Type /Catalog /Pages 2 0 R>>
    endobj
    2 0 obj
    <</Type /Pages /Kids [3 0 R] /Count 1>>
    endobj
    3 0 obj
    <</Type /Page /Parent 2 0 R /MediaBox [0 0 300 400] /Contents 4 0 R>>
    endobj
    4 0 obj
    <</Length 44>>
    stream
    BT
    /F1 24 Tf
    100 100 Td
    (Hello, PDF!) Tj
    ET
    endstream
    endobj
    xref
    0 5
    0000000000 65535 f
    0000000009 00000 n
    0000000055 00000 n
    0000000101 00000 n
    0000000180 00000 n
    trailer
    <</Root 1 0 R /Size 5>>
    startxref
    244
    %%EOF
    """
    
    # Show a simulated PDF content's hex representation
    pdf_bytes = pdf_content.encode("ascii")
    pdf_hex = binascii.hexlify(pdf_bytes).decode('utf-8')
    print(f"{CYAN}Simulated PDF in Hex: {pdf_hex[:200]}...{RESET}")
    
    print(f"\n{GREEN}This is a very basic structure of a PDF file, with a catalog, page objects, and content streams!{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 PDF Structure Quiz Time!{RESET}")
    print(f"\n{CYAN}Which part of a PDF file contains the magic bytes and version number?{RESET}")
    print(f"{YELLOW}A) Body{RESET}")
    print(f"{YELLOW}B) Header{RESET}")
    print(f"{YELLOW}C) Trailer{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "B":
        print(f"{GREEN}✅ Correct! The header contains the magic bytes and version number.%PDF-1.7 indicates the PDF version.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is B. The header stores the magic bytes and version number.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ PDFs begin with a special sequence called 'magic bytes' (%PDF-1.x).")
    slow_print(f"✔ The file is structured with headers, body, cross-reference table, and trailer.")
    slow_print(f"✔ Content like text and images are stored as objects within the body.")
    print(f"{GREEN}Now you know how a PDF file is structured under the hood! 🔧💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    pdf_magic_bytes()
    read_pdf_bytes()
    show_pdf_structure()
    extract_pdf_text()
    simulate_pdf_file()
    quiz()
    summary()

if __name__ == "__main__":
    run()
