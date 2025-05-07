# lessons/env/env_variables.py

import os
import time
import binascii

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
    """Prints text slowly, simulating a typing effect."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}💻 Welcome to Exploring Environment Variables in Raw Memory!{RESET}")
    slow_print(f"{CYAN}In this lesson, we’ll look at environment variables, which are used to store system settings, paths, and other configuration details.")
    slow_print(f"We will explore how these variables are stored in memory and represented in **hexadecimal format**. Let’s dive into the world of system memory! 🔍")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def display_env_variables():
    print(f"\n{BOLD}{CYAN}🔍 Let's Inspect Some Environment Variables{RESET}")
    slow_print(f"{CYAN}Environment variables are key-value pairs that provide system-wide configurations and paths. Let’s see an example of some common environment variables:")

    # Example: Display some environment variables
    env_vars = {
        "HOME": os.environ.get("HOME", "Not set"),
        "PATH": os.environ.get("PATH", "Not set"),
        "USER": os.environ.get("USER", "Not set"),
        "SHELL": os.environ.get("SHELL", "Not set"),
    }

    for var, value in env_vars.items():
        print(f"{YELLOW}{var}: {RESET}{CYAN}{value}{RESET}")

    slow_print(f"\nNow, let’s explore what these variables look like in raw memory and how they are stored in hexadecimal form. 🔐")

def env_variable_to_hex(env_var):
    """Convert an environment variable value to hexadecimal."""
    try:
        env_value = os.environ.get(env_var, None)
        if env_value:
            hex_value = binascii.hexlify(env_value.encode('utf-8')).decode('utf-8')
            return hex_value
        else:
            return "Not found"
    except Exception as e:
        return f"Error: {e}"

def inspect_env_variable_memory():
    print(f"\n{BOLD}{CYAN}🔍 Inspecting Environment Variables in Raw Memory{RESET}")
    slow_print(f"{CYAN}Let’s see how an environment variable, like **HOME**, is represented in raw memory using hexadecimal format.")

    hex_home = env_variable_to_hex("HOME")
    print(f"\n{YELLOW}HOME Environment Variable in Hex: {RESET}")
    print(f"{MAGENTA}{hex_home}{RESET}")

    slow_print(f"\nEach character in the environment variable is encoded in UTF-8, and when represented in hex, we can see its byte-level structure. 🔒")

def memory_breakdown():
    print(f"\n{BOLD}{CYAN}📚 Memory Breakdown: UTF-8 Encoding of Environment Variables{RESET}")
    slow_print(f"{CYAN}The memory representation of an environment variable is encoded using UTF-8. For instance, the string 'HOME' might look like:")

    breakdown_example = {
        "HOME": "48 4F 4D 45",
        "USER": "55 53 45 52",
        "SHELL": "53 48 45 4C 4C"
    }

    for var, hex_rep in breakdown_example.items():
        print(f"{BOLD}{YELLOW}{var}: {RESET}{MAGENTA}{hex_rep}{RESET}")
        slow_print(f"\nIn UTF-8, each character is encoded as a byte (e.g., 'H' is 0x48, 'O' is 0x4F), which you can see in the hex string above.", delay=0.05)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Environment Variable Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: How is an environment variable stored in memory?{RESET}")
    print(f"{YELLOW}A) As plain text without encoding.{RESET}")
    print(f"{YELLOW}B) As a binary sequence, where each character is converted to its ASCII equivalent.{RESET}")
    print(f"{YELLOW}C) As a sequence of bytes encoded in UTF-8 format.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "C":
        print(f"{GREEN}✅ Correct! Environment variables are stored as bytes, encoded in UTF-8 format.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is C. Environment variables are stored as bytes in UTF-8 encoding.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Environment variables store configuration and system info as key-value pairs.")
    slow_print(f"✔ These variables are encoded in UTF-8 and stored in memory as raw bytes. You can inspect them in hexadecimal form for a deeper understanding.")
    slow_print(f"✔ We can use tools like `binascii.hexlify` in Python to convert environment variables into hexadecimal for inspection.")
    print(f"{GREEN}Well done! You've learned how to inspect environment variables in memory and understand their raw byte representation! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    display_env_variables()
    inspect_env_variable_memory()
    memory_breakdown()
    quiz()
    summary()
