# lessons/security/password_hashes.py

import hashlib
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
    print(f"{BOLD}{MAGENTA}🔐 Welcome to the World of Password Hashes!{RESET}")
    slow_print(f"{CYAN}Ever seen a long string of hex like '5f4dcc3b5aa765d61d8327deb882cf99'?")
    slow_print("That’s a hashed password — not the actual password itself! 🔍")
    input(f"\n{YELLOW}Press Enter to learn how it works... {RESET}")

def hash_password(password, algo='md5'):
    if algo == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        return None

def demo_hashes():
    print(f"\n{BOLD}{BLUE}🔄 Demo: Hashing Passwords with MD5 and SHA-256{RESET}")
    passwords = ['password', '123456', 'hello123', 'admin', 'letmein']
    for pwd in passwords:
        md5 = hash_password(pwd, 'md5')
        sha256 = hash_password(pwd, 'sha256')
        print(f"{YELLOW}🔑 {pwd}:{RESET}")
        print(f"  {GREEN}MD5    : {md5}{RESET}")
        print(f"  {CYAN}SHA-256: {sha256}{RESET}\n")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick Hash Quiz!{RESET}")
    choices = ['123456', 'password', 'letmein']
    chosen = random.choice(choices)
    hashed = hash_password(chosen)

    print(f"\n{CYAN}Given this MD5 hash, can you guess the original password?{RESET}")
    print(f"{BLUE}{hashed}{RESET}")
    answer = input(f"{YELLOW}Your guess: {RESET}").strip()

    if answer == chosen:
        print(f"{GREEN}✅ Correct!{RESET}")
    else:
        print(f"{RED}❌ Nope. It was '{chosen}'!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Passwords are stored as one-way hashes, not plain text.")
    slow_print("✔ Hashes look like random hex but come from real algorithms.")
    slow_print("✔ MD5 is fast but outdated. SHA-256 is stronger.")
    slow_print("✔ Adding 'salt' makes hashes harder to crack!")
    print(f"{GREEN}Now you know what’s behind the curtain of password security! 🔐✨{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    demo_hashes()
    quiz()
    summary()

if __name__ == "__main__":
    run()
