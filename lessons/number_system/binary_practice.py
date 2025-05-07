# lessons/basics/binary_practice.py

import random
import time

# 🎨 Terminal color codes
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

def binary_quiz():
    print(f"{BOLD}{CYAN}\n🎮 BINARY PRACTICE MODE 🎮{RESET}")
    print(f"{YELLOW}You’ll be asked to convert between binary and decimal, and solve binary logic puzzles!{RESET}")

    score = 0
    for i in range(5):
        print(f"\n{MAGENTA}🔢 Question {i+1}:{RESET}")

        q_type = random.choice(['bin2dec', 'dec2bin', 'bitwise_and'])
        
        if q_type == 'bin2dec':
            binary = format(random.randint(1, 255), '08b')
            answer = int(binary, 2)
            user = input(f"🧠 What is the decimal value of 0b{BOLD}{binary}{RESET}? ")

        elif q_type == 'dec2bin':
            decimal = random.randint(1, 255)
            answer = format(decimal, '08b')
            user = input(f"💡 What is the binary (8-bit) of {BOLD}{decimal}{RESET}? ")

        elif q_type == 'bitwise_and':
            a = random.randint(1, 255)
            b = random.randint(1, 255)
            answer = a & b
            user = input(f"🔗 What is {BOLD}0b{format(a, '08b')}{RESET} & {BOLD}0b{format(b, '08b')}{RESET} (decimal)? ")

        # Validate
        try:
            if q_type in ['bin2dec', 'bitwise_and']:
                user_val = int(user)
                if user_val == answer:
                    print(f"{GREEN}✅ Correct!{RESET}")
                    score += 1
                else:
                    print(f"{RED}❌ Nope! The correct answer is {answer}.{RESET}")
            elif q_type == 'dec2bin':
                if user.strip() == answer:
                    print(f"{GREEN}✅ Correct!{RESET}")
                    score += 1
                else:
                    print(f"{RED}❌ Nope! The correct answer is {answer}.{RESET}")
        except:
            print(f"{RED}❌ Invalid input. Skipping!{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Practice complete! Your score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🎉 You're a Binary Master! 🧠{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Great job! Keep practicing to master it!{RESET}")
    else:
        print(f"{RED}💡 No worries! Try again—you’re getting there!{RESET}")

def intro_message():
    print(f"{BOLD}{MAGENTA}✨ Welcome to Binary Logic Practice ✨{RESET}")
    slow_print(f"{CYAN}Here you’ll reinforce your understanding of:")
    slow_print(f"🔢 Binary <-> Decimal conversion")
    slow_print(f"🧮 Bitwise operations like AND (&)")
    slow_print(f"🎯 And how binary logic works under the hood!{RESET}\n")
    input(f"{YELLOW}Press Enter to begin the challenge! {RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro_message()
    binary_quiz()
