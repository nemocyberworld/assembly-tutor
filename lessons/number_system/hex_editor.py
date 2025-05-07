import random
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
    print(f"{BOLD}{MAGENTA}🔧 Welcome to the Hex Editor Lesson!{RESET}")
    slow_print(f"{CYAN}In this lesson, we’ll simulate modifying bytes using a Hex Editor. 🖥️")
    slow_print(f"{CYAN}A hex editor allows us to view and edit the raw byte data of a file, represented in hexadecimal format. ✨")
    slow_print(f"{CYAN}Let’s explore how bytes are stored and how you can modify them manually! 🧑‍💻")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def hex_editor_explanation():
    slow_print(f"\n{BOLD}{BLUE}🔍 What is a Hex Editor?{RESET}")
    slow_print(f"{CYAN}A hex editor shows the raw bytes of a file in hexadecimal format. 🧑‍💻")
    slow_print(f"{CYAN}For example, the byte sequence '0x4A 0x65 0x6C 0x6C 0x6F' represents the string 'Hello' in memory. 📝")
    slow_print(f"{CYAN}In a hex editor, we can directly edit the bytes, which is useful for debugging, reversing, or modifying files. 🛠️")
    slow_print(f"\nLet’s start with a small file content, and we’ll simulate modifying it byte by byte!")

def simulate_hex_file():
    slow_print(f"\n{BOLD}{CYAN}💻 Simulated Hex File: {RESET}")
    # Simulate a "file" with hex values representing the string "Hello World!"
    hex_file = ['0x48', '0x65', '0x6C', '0x6C', '0x6F', '0x20', '0x57', '0x6F', '0x72', '0x6C', '0x64', '0x21']
    print(f"{YELLOW}Initial Hex File: {RESET} {' '.join(hex_file)}")

    slow_print(f"\n{CYAN}In a real hex editor, each byte is represented as a two-digit hexadecimal value. Each byte can represent a character or part of a data structure.")
    time.sleep(1)

    # Interactive modification
    slow_print(f"\n{BOLD}{MAGENTA}💡 Let’s Modify the Hex File!{RESET}")
    index = random.randint(0, len(hex_file) - 1)
    original_byte = hex_file[index]

    slow_print(f"\n{CYAN}We are going to change byte {YELLOW}{original_byte}{RESET} at index {YELLOW}{index}{RESET}.")
    new_byte = input(f"{CYAN}Enter a new hex value to replace {original_byte} (e.g., 0x61 for 'a'): ").strip()

    if new_byte.startswith("0x") and len(new_byte) == 4:
        hex_file[index] = new_byte
        slow_print(f"{GREEN}✅ Byte modified successfully!{RESET}")
    else:
        slow_print(f"{RED}❌ Invalid input! Please enter a valid hexadecimal byte (e.g., 0x61).{RESET}")

    slow_print(f"\n{CYAN}Updated Hex File: {RESET} {' '.join(hex_file)}")
    time.sleep(1)

def hex_to_string(hex_list):
    # Convert hex list to a readable string
    return ''.join(chr(int(byte, 16)) for byte in hex_list)

def string_to_hex(input_string):
    # Convert string to hex representation
    return [f'0x{ord(char):02X}' for char in input_string]

def interactive_string_modification():
    slow_print(f"\n{BOLD}{CYAN}🛠️ Modify a String Using a Hex Editor (Simulated){RESET}")
    input_string = input(f"\n{CYAN}Enter a string to modify (e.g., 'Goodbye'): ").strip()

    # Convert string to hex
    hex_representation = string_to_hex(input_string)
    print(f"\n{YELLOW}Initial String in Hex: {RESET} {' '.join(hex_representation)}")

    # Modify one byte
    index = random.randint(0, len(hex_representation) - 1)
    original_byte = hex_representation[index]

    slow_print(f"\n{CYAN}We are going to change byte {YELLOW}{original_byte}{RESET} at index {YELLOW}{index}{RESET}.")
    new_byte = input(f"{CYAN}Enter a new hex value to replace {original_byte} (e.g., 0x61 for 'a'): ").strip()

    if new_byte.startswith("0x") and len(new_byte) == 4:
        hex_representation[index] = new_byte
        slow_print(f"{GREEN}✅ Byte modified successfully!{RESET}")
    else:
        slow_print(f"{RED}❌ Invalid input! Please enter a valid hexadecimal byte (e.g., 0x61).{RESET}")

    # Convert hex back to string
    modified_string = hex_to_string(hex_representation)
    slow_print(f"\n{CYAN}Modified String: {RESET} {modified_string}")
    print(f"\n{YELLOW}Modified Hex: {RESET} {' '.join(hex_representation)}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Hex Editor Quiz Time!{RESET}")
    score = 0

    for i in range(3):
        print(f"\n{YELLOW}Question {i+1}:{RESET}")
        mode = random.choice(['modify', 'interpret'])

        if mode == 'modify':
            hex_value = random.choice(['0x61', '0x62', '0x43', '0x44'])
            correct_char = chr(int(hex_value, 16))
            user_input = input(f"🧠 What character does the hex value {hex_value} represent? ").strip()

            if user_input == correct_char:
                print(f"{GREEN}✅ Correct! {hex_value} represents '{correct_char}'.{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! {hex_value} represents '{correct_char}'.{RESET}")
        else:  # interpret
            string = "Hello"
            hex_rep = string_to_hex(string)
            user_input = input(f"🧠 What hex value represents the character 'H' in the string '{string}'? ").strip()

            if user_input.lower() == hex_rep[0].lower():
                print(f"{GREEN}✅ Correct! The hex value for 'H' is {hex_rep[0]}.{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! The hex value for 'H' is {hex_rep[0]}.{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Great job! You're mastering hex editing!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Nice! Keep practicing to improve your skills!{RESET}")
    else:
        print(f"{RED}💡 Keep trying! You'll get the hang of it soon!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ A hex editor allows us to view and modify the raw bytes of a file in hexadecimal format.")
    slow_print(f"{CYAN}✔ Each byte in memory is represented by two hexadecimal digits (0x00 to 0xFF).")
    slow_print(f"{CYAN}✔ We can modify these bytes to change the data in a file, which is useful for debugging and other tasks.")
    print(f"{GREEN}Keep practicing with hex editors to gain deeper control over byte-level data! 🧑‍💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    hex_editor_explanation()
    simulate_hex_file()
    interactive_string_modification()
    quiz()
    summary()
