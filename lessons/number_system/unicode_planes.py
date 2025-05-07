# lessons/basics/unicode_planes.py

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
    print(f"{BOLD}{MAGENTA}🌍 Welcome to 'Explore Unicode Planes'!{RESET}")
    slow_print(f"{CYAN}In this lesson, we’ll learn about the different Unicode planes, such as the Basic Multilingual Plane (BMP), Supplementary Multilingual Plane (SMP), and more!")
    slow_print(f"{CYAN}By the end, you'll understand how Unicode characters are distributed across these planes and how to work with them in Python. Let’s get started! 🚀")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def explain_unicode_planes():
    print(f"\n{BOLD}{BLUE}📖 What Are Unicode Planes?{RESET}")
    slow_print(f"{CYAN}✔ Unicode is a standard for encoding characters, and it’s organized into different planes.")
    slow_print(f"{CYAN}✔ Each plane contains a range of code points, with the first plane (BMP) containing the most commonly used characters.")
    slow_print(f"{CYAN}✔ Other planes contain less common characters, including emojis, rare languages, and ancient scripts.")
    slow_print(f"{CYAN}✔ Unicode planes help in organizing characters in a manageable way. Let's take a look at some of the main planes!")

def explore_unicode_planes():
    print(f"\n{BOLD}{CYAN}🔍 Explore the Major Unicode Planes{RESET}")
    
    # Basic Multilingual Plane (BMP)
    slow_print(f"\n{BOLD}{GREEN}🌍 Basic Multilingual Plane (BMP){RESET}")
    slow_print(f"{CYAN}✔ This plane contains the most commonly used characters, including most modern languages' characters and common symbols.")
    slow_print(f"{CYAN}✔ The BMP spans from U+0000 to U+FFFF, covering over 65,000 characters.")
    slow_print(f"{CYAN}✔ Some examples: Latin alphabet, Greek letters, Cyrillic, Arabic, Chinese, and more.")
    print(f"{CYAN}Example BMP Character: {RESET}{chr(0x0041)} (A)")

    # Supplementary Multilingual Plane (SMP)
    slow_print(f"\n{BOLD}{GREEN}📜 Supplementary Multilingual Plane (SMP){RESET}")
    slow_print(f"{CYAN}✔ The SMP contains characters for historic scripts, musical notation, and mathematical symbols.")
    slow_print(f"{CYAN}✔ The SMP spans from U+010000 to U+01FFFF, and it holds characters for things like emojis and additional languages.")
    print(f"{CYAN}Example SMP Character: {RESET}{chr(0x1F600)} (😀)")

    # Supplementary Ideographic Plane (SIP)
    slow_print(f"\n{BOLD}{GREEN}📖 Supplementary Ideographic Plane (SIP){RESET}")
    slow_print(f"{CYAN}✔ The SIP is specifically for East Asian ideographs (such as Chinese characters).")
    slow_print(f"{CYAN}✔ It spans from U+020000 to U+02FFFF and contains characters used for historic and modern Chinese, Japanese, and Korean writing.")
    print(f"{CYAN}Example SIP Character: {RESET}{chr(0x20000)} (𠀀)")

    # Tertiary Ideographic Plane (TIP)
    slow_print(f"\n{BOLD}{GREEN}🖋️ Tertiary Ideographic Plane (TIP){RESET}")
    slow_print(f"{CYAN}✔ The TIP is the plane where even rarer Chinese characters are found. It spans from U+030000 to U+03FFFF.")
    slow_print(f"{CYAN}✔ This plane is home to characters used in historical and classical texts.")
    print(f"{CYAN}Example TIP Character: {RESET}{chr(0x30000)} (𰀀)")

    # Private Use Area (PUA)
    slow_print(f"\n{BOLD}{GREEN}🔒 Private Use Area (PUA){RESET}")
    slow_print(f"{CYAN}✔ The PUA is a special plane used for private use, where users can define custom characters that don't have an official Unicode code point.")
    slow_print(f"{CYAN}✔ The PUA spans from U+E000 to U+F8FF.")
    print(f"{CYAN}Example PUA Character: {RESET}{chr(0xE000)} ()")

def explore_unicode_codepoints():
    print(f"\n{BOLD}{CYAN}🔧 Working with Unicode Codepoints in Python{RESET}")
    slow_print(f"{CYAN}Now let’s see how we can work with Unicode characters and their code points in Python.")
    
    # Displaying characters and their codepoints
    characters = ['A', '😊', '𠜎', '❤️', '🦄']
    for char in characters:
        codepoint = hex(ord(char))
        print(f"\n{BOLD}{YELLOW}Character: {char}{RESET}")
        print(f"{CYAN}Unicode Codepoint: {RESET}{codepoint}")
        print(f"{CYAN}UTF-8 Encoded (Hex): {RESET}{char.encode('utf-8').hex()}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Unicode Planes Quiz!{RESET}")
    score = 0

    questions = [
        ("Which plane contains the most commonly used characters?", "BMP"),
        ("Which plane contains most emojis and symbols?", "SMP"),
        ("Which Unicode plane is used for rare Chinese characters?", "SIP"),
        ("Where can you find Private Use Area characters?", "PUA"),
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
        print(f"{GREEN}🎉 Great job! You're a Unicode plane expert!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}👍 Well done! You’re on the right track!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing, and you’ll get it soon!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Unicode is organized into different planes: BMP, SMP, SIP, TIP, and PUA.")
    slow_print(f"✔ The BMP is the most commonly used and contains characters for modern languages and common symbols.")
    slow_print(f"✔ Other planes like the SMP and SIP contain characters for historical scripts and emojis.")
    slow_print(f"✔ Python makes it easy to work with Unicode codepoints and encode/decode characters.")
    print(f"{GREEN}Keep exploring Unicode, and you'll unlock more amazing characters and symbols! 🌟{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_unicode_planes()
    explore_unicode_planes()
    explore_unicode_codepoints()
    quiz()
    summary()
