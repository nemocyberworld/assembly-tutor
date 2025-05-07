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
    print(f"{BOLD}{MAGENTA}💻 Welcome to Hex in Assembly!{RESET}")
    slow_print(f"{CYAN}In assembly language, hex is often used to represent machine code instructions and memory addresses. 🧠")
    slow_print(f"{CYAN}Let's learn how to work with hex values in assembly instructions! 🌟")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def hex_in_assembly():
    slow_print(f"\n{BOLD}{BLUE}🔍 Hex in Assembly Instructions{RESET}")
    slow_print(f"{CYAN}In assembly, hexadecimal is used because it's more compact and easier to read than binary. 🤓")
    slow_print(f"{CYAN}Hexadecimal is a base-16 system, meaning it uses digits from 0 to 9 and letters A to F.")
    slow_print(f"{CYAN}For example, the number 255 in decimal is written as 0xFF in hex. 🧮")
    slow_print(f"\n{YELLOW}Example: MOV AX, 0xFF{RESET}")
    slow_print(f"{CYAN}This assembly instruction moves the hexadecimal value 0xFF into the AX register. 🚀")

def demo_instructions():
    print(f"\n{BOLD}{CYAN}🔁 Let’s look at more examples of assembly instructions using hex!{RESET}")
    instructions = ['MOV AX, 0x1F', 'MOV BX, 0x7E', 'MOV CX, 0xA5', 'MOV DX, 0xFF']
    for instruction in instructions:
        print(f"{YELLOW}{instruction}{RESET}")
        time.sleep(1)
    slow_print(f"\n{BOLD}{BLUE}🔄 Reverse Example: MOV BX, 0xA5{RESET}")
    slow_print(f"{CYAN}This means moving the value 0xA5 into the BX register. A5 in hex is 10100101 in binary. 🧑‍💻")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Hex in Assembly Quiz!{RESET}")
    score = 0

    for i in range(5):
        print(f"\n{YELLOW}Question {i+1}:{RESET}")
        mode = random.choice(['hex_instruction', 'binary_instruction'])

        if mode == 'hex_instruction':
            hex_val = format(random.randint(0, 255), 'X')
            correct = f"0x{hex_val}"
            user = input(f"🧠 What is the hex value for 0b{BOLD}{format(random.randint(0, 255), '08b')}{RESET}? ").strip().upper()
            if user == correct:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! The correct answer is {correct}{RESET}")

        else:  # binary_instruction
            bin_val = format(random.randint(0, 255), '08b')
            correct = f"0x{format(int(bin_val, 2), 'X')}"
            user = input(f"🧠 What is the hex value for 0b{BOLD}{bin_val}{RESET}? ").strip().upper()
            if user == correct:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope! The correct answer is {correct}{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🎉 Excellent! You're a Hex Assembly Pro!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Great job! Keep practicing!{RESET}")
    else:
        print(f"{RED}💡 No worries! Try again—you’ll get it!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hexadecimal is used in assembly for machine code and memory addresses.")
    slow_print(f"{CYAN}✔ Each hex digit represents 4 binary digits.")
    slow_print(f"{CYAN}✔ Common assembly instruction format: MOV Register, 0xHexValue")
    print(f"{GREEN}Keep practicing with hex and assembly—you’ll be a pro in no time! 💪{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    hex_in_assembly()
    demo_instructions()
    quiz()
    summary()
