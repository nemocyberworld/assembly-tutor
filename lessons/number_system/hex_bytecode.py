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
    print(f"{BOLD}{MAGENTA}💾 Welcome to the World of Hex Bytecode!{RESET}")
    slow_print(f"{CYAN}Ever wondered how machine code looks under the hood?")
    slow_print(f"Let's peek into bytecode — the low-level hex instructions your CPU understands! ⚙️")
    input(f"\n{YELLOW}Press Enter to begin the bytecode adventure... {RESET}")

def explain_bytecode():
    print(f"\n{BOLD}{BLUE}🔍 What is Hex Bytecode?{RESET}")
    slow_print(f"{CYAN}Bytecode is a set of low-level instructions in binary or hexadecimal.")
    slow_print("Each instruction tells the CPU what to do — like moving data or adding numbers.")
    slow_print(f"{CYAN}For example, 'B8 04 00 00 00' in x86 means 'Move 4 into EAX register'.")
    slow_print("These hex values are just readable versions of raw binary.")

def show_sample_bytecode():
    print(f"\n{BOLD}{MAGENTA}📦 Sample Bytecode (x86, simplified){RESET}")
    bytecode = [
        ("B8 04 00 00 00", "MOV EAX, 4"),
        ("BB 01 00 00 00", "MOV EBX, 1"),
        ("CD 80", "INT 0x80 (System Call)"),
        ("B9 00 00 00 00", "MOV ECX, 0"),
        ("BA 0D 00 00 00", "MOV EDX, 13")
    ]

    for code, meaning in bytecode:
        print(f"{YELLOW}{code:<20}{RESET} => {GREEN}{meaning}{RESET}")

    slow_print(f"\n{CYAN}Notice how each opcode (like B8 or BB) has a meaning.")
    slow_print("They are instructions, and the numbers that follow are data.")

def interactive_decoder():
    print(f"\n{BOLD}{BLUE}🔧 Hex Bytecode Decoder (Simplified){RESET}")
    instructions = {
        "B8": "MOV EAX, ",
        "BB": "MOV EBX, ",
        "CD": "INT ",
        "B9": "MOV ECX, ",
        "BA": "MOV EDX, "
    }

    user_code = input(f"\n{CYAN}Enter a simplified bytecode (e.g., B8 05 00 00 00): {RESET}").strip().upper()
    parts = user_code.split()

    if not parts or parts[0] not in instructions:
        print(f"{RED}❌ Unknown or unsupported opcode! Try one starting with B8, BB, B9, BA, or CD.{RESET}")
        return

    opcode = parts[0]
    data = parts[1:] if opcode != "CD" else [parts[1]]
    if opcode == "CD":
        print(f"{GREEN}🧠 {instructions[opcode]}{data[0]} (System Interrupt){RESET}")
    else:
        value = int(''.join(reversed(data)), 16)
        print(f"{GREEN}🧠 {instructions[opcode]}{value}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Bytecode Quiz Time!{RESET}")
    score = 0
    questions = [
        ("What does 'B8 02 00 00 00' do?", "MOV EAX, 2"),
        ("What instruction is 'CD 80'?", "INT 0x80"),
        ("What register does 'BB' affect?", "EBX"),
        ("What does 'MOV ECX, 0' look like?", "B9 00 00 00 00"),
    ]
    random.shuffle(questions)

    for i, (q, correct) in enumerate(questions[:3], 1):
        user = input(f"\n{YELLOW}Q{i}: {q}{RESET}\nYour Answer: ").strip().upper()
        if correct.upper() in user:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Nope! The correct answer was: {correct}{RESET}")

    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Bytecode Boss! Amazing work!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Good job! A few more reps and you'll be a pro!{RESET}")
    else:
        print(f"{RED}💡 Don't worry! Bytecode takes practice!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hex bytecode represents machine-level instructions.")
    slow_print("✔ Each opcode (like B8, BB) has a specific function in assembly.")
    slow_print("✔ You can decode hex bytecode into readable instructions.")
    print(f"{GREEN}Now you’ve got a glimpse into the language of machines! ⚙️{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_bytecode()
    show_sample_bytecode()
    interactive_decoder()
    quiz()
    summary()
