import time
import random

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
    print(f"{BOLD}{MAGENTA}🧠 Welcome to Hex Instruction Mapping!{RESET}")
    slow_print(f"{CYAN}Hex values can represent CPU instructions, called opcodes.")
    slow_print("Every CPU architecture has its own opcode set.")
    slow_print("In this lesson, we'll explore how to map hex to instructions (x86-style)! ⚙️")
    input(f"\n{YELLOW}Press Enter to start decoding opcodes... {RESET}")

def opcode_demo():
    print(f"\n{BOLD}{BLUE}📦 Common x86 Opcodes in Hex{RESET}")
    instructions = {
        "B8": "MOV EAX, imm32",
        "B9": "MOV ECX, imm32",
        "BA": "MOV EDX, imm32",
        "BB": "MOV EBX, imm32",
        "CD": "INT imm8",
        "90": "NOP (No Operation)",
        "C3": "RET (Return)",
        "EB": "JMP short",
        "E8": "CALL rel32"
    }

    for hex_code, desc in instructions.items():
        print(f"{YELLOW}{hex_code:<5}{RESET} → {GREEN}{desc}{RESET}")
    
    slow_print(f"\n{CYAN}These are just a few! Each hex code tells the CPU to do something very specific.")

def interactive_decoder():
    print(f"\n{BOLD}{MAGENTA}🔍 Try Decoding a Hex Instruction!{RESET}")
    opcode_map = {
        "B8": "MOV EAX, imm32",
        "B9": "MOV ECX, imm32",
        "BA": "MOV EDX, imm32",
        "BB": "MOV EBX, imm32",
        "CD": "INT imm8",
        "90": "NOP (No Operation)",
        "C3": "RET (Return)",
        "EB": "JMP short",
        "E8": "CALL rel32"
    }

    user_input = input(f"{CYAN}Enter a hex opcode (e.g., B8): {RESET}").strip().upper()

    if user_input in opcode_map:
        print(f"{GREEN}✅ That means: {opcode_map[user_input]}{RESET}")
    else:
        print(f"{RED}❌ Unknown or unsupported opcode. Try one from the list above.{RESET}")

def quiz():
    print(f"\n{BOLD}{BLUE}🎮 Opcode Matching Quiz!{RESET}")
    questions = [
        ("B8", "MOV EAX, imm32"),
        ("CD", "INT imm8"),
        ("90", "NOP (No Operation)"),
        ("C3", "RET (Return)"),
        ("EB", "JMP short")
    ]
    random.shuffle(questions)
    score = 0

    for i, (hex_val, correct) in enumerate(questions[:4], 1):
        user = input(f"\n{YELLOW}Q{i}: What does opcode {hex_val} do? {RESET}").strip()
        if correct.lower() in user.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! It's: {correct}{RESET}")
    
    print(f"\n{BOLD}{CYAN}🏁 Quiz Done! Score: {score}/4{RESET}")
    if score == 4:
        print(f"{GREEN}🎉 Opcode Overlord! You crushed it!{RESET}")
    elif score >= 2:
        print(f"{YELLOW}💪 Nice work! Keep decoding!{RESET}")
    else:
        print(f"{RED}🛠 No worries — practice makes perfect!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hex opcodes are how CPUs understand instructions.")
    slow_print("✔ Each opcode has a fixed meaning, like MOV or INT.")
    slow_print("✔ x86 has a large instruction set; today you learned the most common ones!")
    print(f"{GREEN}Great job! Now you're starting to read the language of CPUs! 🚀{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    opcode_demo()
    interactive_decoder()
    quiz()
    summary()

if __name__ == "__main__":
    run()
