# lessons/basics/char_width.py

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
    print(f"{BOLD}{MAGENTA}🧑‍🏫 Welcome to 'Fixed-Width vs Variable-Width Encodings' Lesson!{RESET}")
    slow_print(f"{CYAN}In this lesson, we’ll explore two major types of character encodings: Fixed-Width and Variable-Width.")
    slow_print(f"{CYAN}By the end, you’ll understand the differences between them and how they impact how we store and represent text in memory.")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_fixed_width():
    print(f"\n{BOLD}{BLUE}📖 Fixed-Width Encodings{RESET}")
    slow_print(f"{CYAN}✔ In a fixed-width encoding, each character uses the same number of bytes, regardless of the character itself.")
    slow_print(f"{CYAN}✔ For example, in ASCII (a fixed-width encoding), every character is represented using exactly 1 byte.")
    slow_print(f"{CYAN}✔ This means that for any given character, the memory size is always constant. It's simple, predictable, and efficient for basic text.")
    print(f"\n{YELLOW}Example: ASCII Encoding{RESET}")
    slow_print(f"{CYAN}Each character in ASCII is 1 byte wide, meaning whether you have 'A', 'B', or 'Z', each takes up 1 byte of memory.")

def explain_variable_width():
    print(f"\n{BOLD}{BLUE}📖 Variable-Width Encodings{RESET}")
    slow_print(f"{CYAN}✔ In a variable-width encoding, different characters can use different numbers of bytes.")
    slow_print(f"{CYAN}✔ For example, in UTF-8 (a variable-width encoding), common characters (like letters) use 1 byte, but more complex characters (like emojis) can use 2, 3, or even 4 bytes.")
    slow_print(f"{CYAN}✔ This means you can store more characters in less space if you’re only using basic characters, but it can vary for others.")
    print(f"\n{YELLOW}Example: UTF-8 Encoding{RESET}")
    slow_print(f"{CYAN}In UTF-8, the character 'A' takes 1 byte, but '😊' (an emoji) takes 4 bytes!")

def compare_fixed_vs_variable():
    print(f"\n{BOLD}{CYAN}⚖️ Fixed-Width vs Variable-Width: Comparison{RESET}")
    slow_print(f"{CYAN}✔ Fixed-width encodings are faster and simpler to process because each character is the same size.")
    slow_print(f"{CYAN}✔ Variable-width encodings are more space-efficient for text with many common characters but require more complexity when processing.")
    print(f"{RED}Key Difference: In fixed-width encodings, memory usage is predictable; in variable-width encodings, memory usage can vary greatly depending on the characters used.{RESET}")
    
    print(f"\n{CYAN}Let’s look at a simple comparison in Python:")
    
    # Simulating the difference between fixed-width and variable-width
    ascii_text = "Hello"
    utf8_text = "Hello 😊"
    
    print(f"{GREEN}Fixed-width Encoding (ASCII):{RESET} {len(ascii_text.encode('ascii'))} bytes")
    print(f"{GREEN}Variable-width Encoding (UTF-8):{RESET} {len(utf8_text.encode('utf-8'))} bytes")
    
def encoding_examples():
    print(f"\n{BOLD}{MAGENTA}🔍 Example Encoding Process{RESET}")
    slow_print(f"{CYAN}Let’s see how different characters are represented in memory using different encodings.")
    
    characters = ['A', 'B', '😊', '日', 'π']
    
    for char in characters:
        ascii_bytes = char.encode('ascii', errors='replace')  # ASCII (for comparison)
        utf8_bytes = char.encode('utf-8')  # UTF-8 (variable width)
        print(f"\nCharacter: {char}")
        print(f"{CYAN}  ASCII (Fixed-width): {len(ascii_bytes)} byte(s) → {ascii_bytes}{RESET}")
        print(f"{CYAN}  UTF-8 (Variable-width): {len(utf8_bytes)} byte(s) → {utf8_bytes}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Encoding Quiz Time!{RESET}")
    score = 0

    questions = [
        ("In a fixed-width encoding, how many bytes does each character take?", "1 byte"),
        ("Which encoding is an example of variable-width encoding?", "UTF-8"),
        ("Which encoding is simpler and faster to process?", "Fixed-width"),
        ("Which encoding is more space-efficient for text with many common characters?", "Variable-width"),
    ]
    
    for i, (q, a) in enumerate(questions, 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip()
        if user.lower() == a.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is: {GREEN}{a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Your score: {score}/4{RESET}")
    if score == 4:
        print(f"{GREEN}🎉 Excellent! You're a pro at encodings!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👍 Great work! Keep learning to master encoding concepts!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing! You'll get the hang of it!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Fixed-width encodings allocate the same number of bytes for each character, making them simple and predictable.")
    slow_print(f"{CYAN}✔ Variable-width encodings allocate different numbers of bytes for different characters, making them more efficient in terms of memory usage.")
    slow_print(f"{CYAN}✔ UTF-8 is a popular variable-width encoding, while ASCII is a fixed-width encoding.")
    slow_print(f"{CYAN}✔ Each encoding type has its strengths depending on the context, and understanding these will help you work with different text formats effectively.")
    print(f"{GREEN}Keep practicing, and you’ll be a text encoding expert in no time! 🧠{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explain_fixed_width()
    explain_variable_width()
    compare_fixed_vs_variable()
    encoding_examples()
    quiz()
    summary()

if __name__ == "__main__":
    run()
