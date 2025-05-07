# lessons/basics/utf8_glyphs.py

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
    print(f"{BOLD}{MAGENTA}🌍 Welcome to 'Visualizing Multibyte Characters and Emojis in UTF-8'!{RESET}")
    slow_print(f"{CYAN}In this lesson, we'll explore how UTF-8 encodes characters that require more than one byte, such as emojis and special symbols.")
    slow_print(f"{CYAN}Let’s see how these multibyte characters work in Python. Ready to dive into some fun glyphs? 🤩")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_utf8_multibyte():
    print(f"\n{BOLD}{BLUE}📖 What is UTF-8 and How Does It Handle Multibyte Characters?{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 is a variable-length encoding scheme, where characters can take anywhere from 1 to 4 bytes.")
    slow_print(f"{CYAN}✔ Most of the common characters (like ASCII ones) use only 1 byte, but emojis and other symbols require multiple bytes.")
    slow_print(f"{CYAN}✔ This allows UTF-8 to represent every character in the Unicode standard, including emojis! 🌟")

def show_multibyte_characters():
    print(f"\n{BOLD}{CYAN}🔍 Visualizing Multibyte Characters and Emojis{RESET}")

    # Let's visualize some UTF-8 encoded characters
    characters = ['❤️', '🌍', '🚀', '🔥', '💻']
    for char in characters:
        byte_representation = char.encode('utf-8')
        print(f"\n{BOLD}{GREEN}Character: {char}{RESET}")
        print(f"{CYAN}UTF-8 Encoded (Hex): {RESET}{byte_representation.hex()}")
        print(f"{CYAN}UTF-8 Encoded (Bytes): {RESET}{list(byte_representation)}")
        print(f"{CYAN}Character Codepoint: {RESET}{hex(ord(char))}")

def demonstrate_encoding_decoding():
    print(f"\n{BOLD}{CYAN}🔧 Encoding and Decoding Multibyte Characters{RESET}")
    slow_print(f"{CYAN}Let's encode and decode an emoji using UTF-8 in Python. We’ll take a heart emoji (❤️), encode it to bytes, then decode it back to a character.")
    
    char = '❤️'
    encoded = char.encode('utf-8')
    decoded = encoded.decode('utf-8')
    
    print(f"\n{BOLD}{YELLOW}Original Character: {char}{RESET}")
    print(f"{CYAN}Encoded in UTF-8: {RESET}{encoded}")
    print(f"{CYAN}Decoded back: {RESET}{decoded}")

    slow_print(f"\nAs you can see, the UTF-8 encoding of this emoji requires 4 bytes. This is because emojis often use more than one byte to represent them in UTF-8.")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 UTF-8 Emoji and Multibyte Character Quiz!{RESET}")
    score = 0

    questions = [
        ("How many bytes does the heart emoji ❤️ use in UTF-8?", "4"),
        ("Which encoding is used to represent multibyte characters like emojis?", "UTF-8"),
        ("Which of these is a multibyte character? (Choose one: ❤️, A, 1, 😊)", "❤️"),
        ("What is the codepoint for the emoji 🌍?", "0x1F30D"),
    ]

    for i, (q, a) in enumerate(questions, 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip()
        if user == a:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is: {GREEN}{a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Your score: {score}/4{RESET}")
    if score == 4:
        print(f"{GREEN}🌟 Awesome! You're a UTF-8 emoji expert!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👍 Nice work! You’re getting the hang of UTF-8!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing, and you’ll master it soon!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 is a variable-length encoding that uses 1 to 4 bytes to represent characters.")
    slow_print(f"✔ Emojis and special characters require multiple bytes to be properly encoded in UTF-8.")
    slow_print(f"✔ We learned how to visualize and work with multibyte characters and how to encode and decode them.")
    print(f"{GREEN}You’re on your way to becoming a UTF-8 pro! Keep exploring and experimenting with multibyte characters! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
def run():
    intro()
    explain_utf8_multibyte()
    show_multibyte_characters()
    demonstrate_encoding_decoding()
    quiz()
    summary()
if __name__ == "__main__":
    run()

