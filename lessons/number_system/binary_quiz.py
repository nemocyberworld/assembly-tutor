# lessons/basics/binary_quiz.py

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
    print(f"{BOLD}{MAGENTA}🧠 Welcome to the Binary Logic Puzzle & Quiz!{RESET}")
    slow_print(f"{CYAN}Get ready to flex your brain with fun binary challenges!")
    slow_print("We’ll quiz you on conversions, logic operations, and patterns.\n")
    input(f"{YELLOW}Press Enter when you're ready to begin! {RESET}")

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    return format(decimal_num, '08b')

def generate_question():
    q_type = random.choice(['bin2dec', 'dec2bin', 'bitwise_and', 'bitwise_or', 'missing_bit'])

    if q_type == 'bin2dec':
        binary = format(random.randint(1, 255), '08b')
        correct = str(int(binary, 2))
        question = f"🔢 What is the decimal value of 0b{BOLD}{binary}{RESET}?"
        return question, correct

    elif q_type == 'dec2bin':
        decimal = random.randint(1, 255)
        correct = format(decimal, '08b')
        question = f"💡 What is the 8-bit binary for {BOLD}{decimal}{RESET}?"
        return question, correct

    elif q_type == 'bitwise_and':
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        correct = str(a & b)
        question = f"🔗 What is {BOLD}0b{format(a, '08b')}{RESET} AND {BOLD}0b{format(b, '08b')}{RESET} (decimal)?"
        return question, correct

    elif q_type == 'bitwise_or':
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        correct = str(a | b)
        question = f"⚡ What is {BOLD}0b{format(a, '08b')}{RESET} OR {BOLD}0b{format(b, '08b')}{RESET} (decimal)?"
        return question, correct

    elif q_type == 'missing_bit':
        # Insert a ? in a binary number and ask for the missing digit
        full_bin = format(random.randint(1, 255), '08b')
        idx = random.randint(0, 7)
        missing = full_bin[idx]
        puzzle = full_bin[:idx] + '?' + full_bin[idx+1:]
        question = f"🧩 What bit completes this binary number: {BOLD}{puzzle}{RESET}?"
        return question, missing

def run_quiz():
    score = 0
    print(f"\n{BOLD}{CYAN}🎮 BINARY CHALLENGE TIME! 🎮{RESET}")

    for i in range(5):
        print(f"\n{YELLOW}Question {i+1}/{5}:{RESET}")
        question, correct = generate_question()
        user_input = input(f"{question} {BLUE}Your answer: {RESET}")

        if user_input.strip() == correct:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! The correct answer was {correct}.{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🎉 Perfect score! You’re a binary genius!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👏 Nice work! You’re getting the hang of it!{RESET}")
    else:
        print(f"{RED}💡 Keep practicing! You’re on your way!{RESET}")

def review():
    print(f"\n{BOLD}{MAGENTA}📘 Quick Review:{RESET}")
    print(f"{CYAN}✔ Binary is base-2 (0s and 1s)")
    print("✔ Use format(n, '08b') to get 8-bit binary")
    print("✔ Bitwise AND: 1 only if both bits are 1")
    print("✔ Bitwise OR: 1 if at least one bit is 1")
    print("✔ Practice makes perfect! 🧠🖥️{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    run_quiz()
    review()

if __name__ == "__main__":
    run()
