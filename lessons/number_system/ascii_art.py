# lessons/basics/ascii_art.py

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
    print(f"{BOLD}{MAGENTA}🎨 Welcome to the ASCII Art Lesson!{RESET}")
    slow_print(f"{CYAN}In this lesson, we’ll learn how to create ASCII art and understand the limits of printable characters.")
    slow_print(f"{CYAN}You’ll get to make fun art using just characters and symbols! Let's get started!")
    input(f"\n{YELLOW}Press Enter to begin... {RESET}")

def ascii_art_intro():
    print(f"\n{BOLD}{BLUE}📖 What is ASCII Art?{RESET}")
    slow_print(f"{CYAN}✔ ASCII art is a graphic design technique that uses printable characters (letters, numbers, and symbols) to represent pictures or shapes.")
    slow_print(f"{CYAN}✔ It’s a way to create images using just text in a fixed-width format.")
    slow_print(f"{CYAN}✔ Some popular examples are simple shapes, faces, or even animals made using just characters like 'X', '/', '\\', '|', etc.")
    print(f"{YELLOW}Example of a simple ASCII art triangle:{RESET}")
    slow_print(f"{CYAN}\n     ^\n    / \\\n   /   \\\n  /_____\\", 0.1)
    slow_print(f"\n{CYAN}Amazing, right? Let’s try creating some more complex designs together!")

def create_ascii_face():
    print(f"\n{BOLD}{MAGENTA}😀 Let's Create an ASCII Face!{RESET}")
    slow_print(f"{CYAN}Let's build a simple face using characters!")

    face1 = """
     _______
    /       \\
   |  O   O  |
   |    ^    |
   |   '-'   |
    \_______/
    """
    slow_print(f"\n{YELLOW}Here’s a fun ASCII face:{RESET}")
    print(f"{CYAN}{face1}{RESET}")

    slow_print(f"\n{CYAN}Now let’s modify it a bit—how about changing the eyes?")
    face2 = """
     _______
    /       \\
   |  X   X  |
   |    ^    |
   |   '-'   |
    \_______/
    """
    print(f"\n{CYAN}{face2}{RESET}")
    slow_print(f"\n{CYAN}See how small tweaks can totally change the expression? Try experimenting with your own ideas!")

def printable_limits():
    print(f"\n{BOLD}{CYAN}⚖️ Printable Character Limits{RESET}")
    slow_print(f"{CYAN}Now, let’s understand the limits of printable characters in ASCII art.")
    slow_print(f"{CYAN}ASCII printable characters range from 32 (space) to 126 (~). These include letters, numbers, punctuation marks, and symbols.")
    slow_print(f"{CYAN}Characters below 32 are control codes like newline and tab—they aren’t visible and can't be used for visual art.")

    print(f"\n{GREEN}Let’s print all printable ASCII characters:{RESET}")
    for i in range(32, 127):
        print(chr(i), end=' ')
    print("\n")

def ascii_art_challenge():
    print(f"\n{BOLD}{YELLOW}🎮 ASCII Art Challenge!{RESET}")
    slow_print(f"{CYAN}It’s your turn! Can you create an ASCII art of a simple object using only printable characters?")
    slow_print(f"{CYAN}Try making a house, tree, or anything else. Here’s a sample house to get inspired:")

    house = """
      /\    
     /  \   
    /    \  
   /______\ 
  |        |
  |  [] [] |
  |________|
    """
    slow_print(f"\n{CYAN}{house}{RESET}")

    input(f"\n{YELLOW}Now try making your own ASCII art below! Press Enter when you're ready... {RESET}")

def ascii_art_quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 ASCII Art Quiz Time!{RESET}")
    score = 0

    questions = [
        ("Which of these is a valid ASCII art character? (A) @ (B) \x07 (C) NULL", "A"),
        ("How many printable characters are there in ASCII?", "95"),
        ("Which character cannot be used in ASCII art? (A) ! (B) # (C) BEL", "C"),
    ]

    for i, (q, correct_answer) in enumerate(questions, 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip().upper()
        if user == correct_answer.upper():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is: {GREEN}{correct_answer}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Perfect! You're an ASCII artist now!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Well done! Keep practicing your ASCII art!{RESET}")
    else:
        print(f"{RED}💡 No worries! Keep experimenting and you'll improve!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ ASCII art uses printable characters (letters, symbols, etc.) to create images.")
    slow_print(f"{CYAN}✔ Printable ASCII characters range from 32 to 126—plenty for creative expression.")
    slow_print(f"{CYAN}✔ You can design anything from faces to objects using just text!")
    print(f"{GREEN}Keep practicing and you'll become a text art wizard in no time! 🎨{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    ascii_art_intro()
    create_ascii_face()
    printable_limits()
    ascii_art_challenge()
    ascii_art_quiz()
    summary()

if __name__ == "__main__":
    run()
