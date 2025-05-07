# lessons/web/html_in_ascii.py

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to HTML in ASCII!{RESET}")
    slow_print(f"{CYAN}Did you know every line of HTML is just text?")
    slow_print("That means it's stored and sent using ASCII codes! 🔤")
    input(f"\n{YELLOW}Press Enter to see how HTML becomes ASCII... {RESET}")

def html_to_ascii(html):
    return [(c, ord(c)) for c in html]

def display_ascii_table(html):
    print(f"\n{BOLD}{BLUE}🔍 HTML as ASCII Codes:{RESET}")
    table = html_to_ascii(html)
    for char, code in table:
        display = repr(char)[1:-1]  # Handles escape characters cleanly
        print(f"{GREEN}{display:<4}{RESET} → ASCII {YELLOW}{code}{RESET} → Binary {MAGENTA}{format(code, '08b')}{RESET}")

def explore_sample():
    print(f"\n{BOLD}{CYAN}📄 Sample HTML Code:{RESET}")
    sample_html = "<h1>Hello, world!</h1>"
    print(f"{BLUE}{sample_html}{RESET}")
    display_ascii_table(sample_html)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick ASCII Quiz!{RESET}")
    question = "<p>"
    answer = [ord(c) for c in question]

    user_input = input(f"{YELLOW}What is the ASCII code for '{question}' (space-separated)? {RESET}")
    try:
        user_values = list(map(int, user_input.strip().split()))
        if user_values == answer:
            print(f"{GREEN}✅ Correct!{RESET}")
        else:
            print(f"{RED}❌ Nope! The correct codes are: {answer}{RESET}")
    except:
        print(f"{RED}⚠️ Invalid input. Use space-separated numbers like: 60 112 62{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ HTML is plain text — stored as ASCII bytes")
    slow_print("✔ Every character in HTML has a unique ASCII number")
    slow_print("✔ Computers send HTML as binary based on those numbers")
    print(f"{GREEN}Now you see the web in a whole new light! 🌐💡{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explore_sample()
    quiz()
    summary()
