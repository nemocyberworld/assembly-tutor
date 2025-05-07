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
    print(f"{BOLD}{MAGENTA}🔢 Welcome to Hex Arithmetic and Logic! 🧠{RESET}")
    slow_print(f"{CYAN}In this lesson, we'll explore how to perform arithmetic and logical operations using hexadecimal numbers.")
    slow_print(f"Hex numbers are widely used in programming, especially in areas like memory addressing and graphics.")
    slow_print(f"Let’s start with the basics!")
    input(f"\n{YELLOW}Press Enter to continue and learn some hex math!{RESET}")

def hex_arithmetic():
    print(f"\n{BOLD}{CYAN}➗ Hexadecimal Arithmetic Operations:{RESET}")
    slow_print(f"Hexadecimal arithmetic follows the same rules as decimal arithmetic, but with a base of 16.")
    
    # Example: Adding Hex Numbers
    hex_num1 = 0x1A  # 26 in decimal
    hex_num2 = 0x2F  # 47 in decimal
    addition_result = hex_num1 + hex_num2
    print(f"{GREEN}Addition: {hex(hex_num1)} + {hex(hex_num2)} = {hex(addition_result)}{RESET}")
    
    # Subtraction
    subtraction_result = hex_num2 - hex_num1
    print(f"{BLUE}Subtraction: {hex(hex_num2)} - {hex(hex_num1)} = {hex(subtraction_result)}{RESET}")
    
    # Multiplication
    multiplication_result = hex_num1 * hex_num2
    print(f"{YELLOW}Multiplication: {hex(hex_num1)} * {hex(hex_num2)} = {hex(multiplication_result)}{RESET}")
    
    # Division
    division_result = hex_num2 // hex_num1
    print(f"{MAGENTA}Division: {hex(hex_num2)} // {hex(hex_num1)} = {hex(division_result)}{RESET}")
    
    slow_print(f"These operations are performed just like regular arithmetic, but with hex numbers!")
    input(f"\n{YELLOW}Press Enter to continue and learn about logical operations!{RESET}")

def hex_logical_operations():
    print(f"\n{BOLD}{CYAN}🧠 Hexadecimal Logical Operations:{RESET}")
    slow_print(f"Logical operations like AND, OR, XOR, and NOT are often used in computer science and programming.")
    
    # Example values
    hex_val1 = 0xA5  # 10100101 in binary
    hex_val2 = 0x3C  # 00111100 in binary
    
    # AND Operation
    and_result = hex_val1 & hex_val2
    print(f"{GREEN}AND: {hex(hex_val1)} & {hex(hex_val2)} = {hex(and_result)}{RESET}")
    
    # OR Operation
    or_result = hex_val1 | hex_val2
    print(f"{BLUE}OR: {hex(hex_val1)} | {hex(hex_val2)} = {hex(or_result)}{RESET}")
    
    # XOR Operation
    xor_result = hex_val1 ^ hex_val2
    print(f"{YELLOW}XOR: {hex(hex_val1)} ^ {hex(hex_val2)} = {hex(xor_result)}{RESET}")
    
    # NOT Operation (inverts the bits)
    not_result = ~hex_val1
    print(f"{MAGENTA}NOT: ~{hex(hex_val1)} = {hex(not_result)}{RESET}")
    
    slow_print(f"These operations manipulate the bits of the numbers, and they are used extensively in bitwise programming.")
    input(f"\n{YELLOW}Press Enter to continue and do some practice with hex math!{RESET}")

def hex_math_practice():
    print(f"\n{BOLD}{MAGENTA}🎮 Hex Math Practice Challenge!{RESET}")
    score = 0
    
    # Practice problems
    problems = [
        {"question": "What is 0x1F + 0x24?", "answer": 0x43},
        {"question": "What is 0xA2 - 0x59?", "answer": 0x49},
        {"question": "What is 0x8C * 0x2?", "answer": 0x118},
        {"question": "What is 0x7F // 0x1F?", "answer": 0x3}
    ]
    
    # Ask user for answers
    for i, problem in enumerate(problems, 1):
        print(f"\n{YELLOW}Question {i}:{RESET}")
        slow_print(f"{CYAN}{problem['question']}{RESET}")
        user_answer = input(f"{YELLOW}Your answer (in hex): {RESET}").strip()
        
        # Convert user input to hex
        try:
            user_answer = int(user_answer, 16)
            if user_answer == problem["answer"]:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Incorrect! The correct answer is {hex(problem['answer'])}.{RESET}")
        except ValueError:
            print(f"{RED}⚠️ Invalid hex input! Please enter a valid hex number.{RESET}")
    
    # Score and feedback
    print(f"\n{BOLD}{BLUE}🏁 Practice Complete! Your score: {score}/{len(problems)}{RESET}")
    if score == len(problems):
        print(f"{GREEN}🎉 Excellent! You’re a hex math expert!{RESET}")
    elif score >= len(problems) // 2:
        print(f"{YELLOW}👍 Great job! Keep practicing to master hex math!{RESET}")
    else:
        print(f"{RED}💡 Don’t worry! Keep practicing and you’ll improve!{RESET}")
    
def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hexadecimal arithmetic uses the same rules as decimal, but with a base of 16.")
    slow_print(f"✔ Logical operations like AND, OR, XOR, and NOT manipulate individual bits of numbers.")
    slow_print(f"✔ Hex math and logic are crucial in fields like low-level programming, embedded systems, and cryptography.")
    print(f"{GREEN}Awesome! You now have a strong understanding of hex arithmetic and logic! 🧑‍💻💡{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    hex_arithmetic()
    hex_logical_operations()
    hex_math_practice()
    summary()

if __name__ == "__main__":
    run()
