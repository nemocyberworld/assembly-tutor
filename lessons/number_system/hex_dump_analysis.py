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
    print(f"{BOLD}{MAGENTA}🔍 Welcome to Hex Dump Analysis! 🧠{RESET}")
    slow_print(f"{CYAN}In this lesson, we will learn how to read and interpret a Hex Dump.")
    slow_print(f"A hex dump is a representation of data as hexadecimal values. It's often used in debugging and forensic analysis.")
    slow_print(f"Let’s dive into a hex dump and start analyzing some data!")
    input(f"\n{YELLOW}Press Enter to begin!{RESET}")

def show_hex_dump():
    print(f"\n{BOLD}{CYAN}📜 Sample Hex Dump Analysis:{RESET}")
    # A simulated hex dump of a small data block (memory or file data)
    hex_dump = """
    00000000  48 65 6C 6C 6F 20 57 6F  72 6C 64 21 20 48 65 6C  |Hello World! Hel|
    00000010  6C 6F 20 57 6F 72 6C 64  21 20 47 6F 6F 64 79  |lo World! Goody|
    00000020  65 20 66 72 6F 6D 20 70  79 74 68 6F 6E 2E 0A  |e from python. .|
    """
    print(f"{GREEN}{hex_dump}{RESET}")
    slow_print(f"Here, we have a dump of ASCII text encoded in hexadecimal format.")
    slow_print(f"Each group of two characters represents one byte.")
    slow_print(f"The first column shows the memory address, the second column is the hex values, and the third column shows the ASCII equivalent.")
    input(f"\n{YELLOW}Press Enter to start analyzing the hex dump!{RESET}")

def analyze_hex_dump():
    print(f"\n{BOLD}{CYAN}🔎 Analyzing Hex Dump Contents:{RESET}")
    slow_print(f"Let’s break down the first row of the hex dump:")
    slow_print(f"Address: 00000000")
    slow_print(f"Hex values: 48 65 6C 6C 6F 20 57 6F  72 6C 64 21 20 48 65 6C")
    slow_print(f"These values represent the following ASCII characters:")
    slow_print(f"{YELLOW}H  e  l  l  o     W  o  r  l  d  !     H  e  l{RESET}")
    input(f"\n{YELLOW}Press Enter to continue with the next row analysis!{RESET}")

def interpret_data():
    print(f"\n{BOLD}{CYAN}💡 Interpreting Data in the Hex Dump:{RESET}")
    slow_print(f"Now, let's interpret the second row:")
    slow_print(f"Address: 00000010")
    slow_print(f"Hex values: 6C 6F 20 57 6F 72 6C 64  21 20 47 6F 6F 64 79")
    slow_print(f"These represent the following characters:")
    slow_print(f"{YELLOW}l  o     W  o  r  l  d  !     G  o  o  d  y{RESET}")
    slow_print(f"As you can see, the hex dump represents ASCII text, making it human-readable!")
    slow_print(f"However, when analyzing binary data, these dumps can represent more complex structures like images, executables, or raw memory dumps.")
    input(f"\n{YELLOW}Press Enter to continue with a Hex Dump Challenge!{RESET}")

def hex_dump_challenge():
    print(f"\n{BOLD}{CYAN}🎯 Hex Dump Challenge!{RESET}")
    slow_print(f"Now it's time for you to try interpreting some hex dump data yourself.")
    
    # Sample hex dump challenge (hidden part for the user to interpret)
    hex_challenge = "00000000  41 42 43 44 45 46 47 48  49 4A 4B 4C 4D 4E 4F 50"
    slow_print(f"Here’s a hex dump (address + hex values):")
    print(f"{YELLOW}{hex_challenge}{RESET}")
    
    # Expected output for interpretation (ASCII)
    expected_answer = "A B C D E F G H I J K L M N O P"
    slow_print(f"Can you interpret the ASCII values? Type your answer below (e.g., A B C D):")
    
    user_answer = input(f"{YELLOW}Your interpretation: {RESET}").strip()
    
    if user_answer == expected_answer:
        print(f"{GREEN}✅ Correct! You correctly interpreted the hex dump.{RESET}")
    else:
        print(f"{RED}⚠️ Oops! That’s not quite right. The correct interpretation is: {expected_answer}{RESET}")
    
    input(f"\n{YELLOW}Press Enter to continue and review key takeaways!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hex dumps are used to represent binary data in a human-readable format, often for debugging and memory analysis.")
    slow_print(f"✔ Each byte of data is represented by two hexadecimal digits, and the ASCII equivalent is shown on the right.")
    slow_print(f"✔ Interpreting hex dumps requires knowledge of how data is encoded and how to map hex values to characters or binary values.")
    slow_print(f"✔ This skill is especially useful for reverse engineering, data analysis, and low-level debugging tasks.")
    slow_print(f"{GREEN}Well done! You’ve now learned how to read and analyze hex dumps like a pro! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    show_hex_dump()
    analyze_hex_dump()
    interpret_data()
    hex_dump_challenge()
    summary()

if __name__ == "__main__":
    run()
