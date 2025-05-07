# lessons/basics/logic_gates.py

# 🎨 Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

import time
import random

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🔌 Welcome to Logic Gates Simulator! 🧠{RESET}")
    slow_print(f"{CYAN}Computers use tiny electronic gates to make decisions. Let’s simulate them with binary!{RESET}")
    print(f"\n{YELLOW}We’ll cover these gates:{RESET}")
    print(f"{GREEN}✔ AND  - Outputs 1 only if both inputs are 1")
    print(f"{GREEN}✔ OR   - Outputs 1 if either input is 1")
    print(f"{GREEN}✔ NOT  - Flips the input: 1 → 0, 0 → 1{RESET}\n")
    input(f"{BLUE}Press Enter to continue...{RESET}")

def simulate_gates():
    print(f"\n{BOLD}{BLUE}🧪 Logic Gate Simulation:{RESET}")

    pairs = [(0,0), (0,1), (1,0), (1,1)]
    
    print(f"\n{CYAN}🔹 AND Gate 🔹{RESET}")
    for a, b in pairs:
        result = a & b
        print(f"{a} AND {b} = {GREEN if result else RED}{result}{RESET}")

    print(f"\n{CYAN}🔹 OR Gate 🔹{RESET}")
    for a, b in pairs:
        result = a | b
        print(f"{a} OR  {b} = {GREEN if result else RED}{result}{RESET}")

    print(f"\n{CYAN}🔹 NOT Gate 🔹{RESET}")
    for a in [0, 1]:
        result = 1 - a
        print(f"NOT {a} = {GREEN if result else RED}{result}{RESET}")

def logic_quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Mini Logic Gate Quiz!{RESET}")
    gates = ['AND', 'OR', 'NOT']
    score = 0

    for i in range(5):
        gate = random.choice(gates)
        if gate == 'NOT':
            a = random.randint(0, 1)
            answer = 1 - a
            user = input(f"{YELLOW}What is NOT {a}? {RESET}")
        else:
            a, b = random.randint(0, 1), random.randint(0, 1)
            if gate == 'AND':
                answer = a & b
            else:
                answer = a | b
            user = input(f"{YELLOW}What is {a} {gate} {b}? {RESET}")

        try:
            if int(user) == answer:
                print(f"{GREEN}✅ Correct!{RESET}")
                score += 1
            else:
                print(f"{RED}❌ Nope. Correct answer is {answer}.{RESET}")
        except:
            print(f"{RED}⚠️ Invalid input. Skipped!{RESET}")

    print(f"\n{BLUE}🎯 Score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🎉 Perfect! Logic Wizard!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Great job! Keep going!{RESET}")
    else:
        print(f"{RED}💡 No worries! Try again to improve!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    print(f"{CYAN}✔ Logic gates are the building blocks of digital systems.")
    print(f"✔ Each gate performs a simple binary operation.")
    print(f"✔ By combining gates, computers can do math, make decisions, and more!{RESET}")
    print(f"\n{GREEN}Now you understand how 1s and 0s build brains of machines! 🤖{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    simulate_gates()
    logic_quiz()
    summary()
