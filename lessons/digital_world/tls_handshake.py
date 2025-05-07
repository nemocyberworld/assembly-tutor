# lessons/tls_handshake/tls_handshake.py

import binascii
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
    """Simulate slow printing for better engagement."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🔒 Welcome to TLS Handshake Messages!{RESET}")
    slow_print(f"{CYAN}The TLS handshake is the process where a client and server agree on how to securely communicate. It involves several messages to establish trust, encryption methods, and more.")
    slow_print("In this lesson, we will inspect those handshake messages in their raw binary form.")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def display_tls_handshake_messages():
    """Display sample TLS handshake messages and their binary forms."""
    print(f"\n{BOLD}{CYAN}🔍 TLS Handshake Messages Analysis{RESET}")
    
    # Sample TLS Handshake Messages
    handshake_messages = [
        "Client Hello",
        "Server Hello",
        "Certificate",
        "Server Hello Done",
        "Client Key Exchange",
        "Finished"
    ]
    
    print(f"\n{BOLD}{CYAN}ASCII Representation of Handshake Messages:{RESET}")
    for message in handshake_messages:
        slow_print(f"{MAGENTA}{message}{RESET}")
    
    print(f"\n{BOLD}{CYAN}Now, let's see how these messages look in binary...{RESET}")

    # Convert each handshake message to bytes and then to hex
    for message in handshake_messages:
        message_bytes = message.encode('utf-8')
        print(f"\n{YELLOW}{message} in Hex: {RESET}")
        hex_rep = binascii.hexlify(message_bytes).decode('utf-8')
        formatted_hex = ' '.join([hex_rep[i:i+2] for i in range(0, len(hex_rep), 2)])
        slow_print(formatted_hex)

def explain_tls_handshake_fields():
    """Explain each part of the TLS handshake."""
    print(f"\n{BOLD}{CYAN}📘 Key TLS Handshake Messages:{RESET}")
    slow_print(f"{CYAN}1. `Client Hello` - The client initiates the handshake, proposing encryption algorithms and random data.")
    slow_print(f"{CYAN}2. `Server Hello` - The server responds, agreeing on encryption algorithms and sending its random data.")
    slow_print(f"{CYAN}3. `Certificate` - The server sends its certificate to authenticate itself.")
    slow_print(f"{CYAN}4. `Server Hello Done` - The server signals it is done with its part of the handshake.")
    slow_print(f"{CYAN}5. `Client Key Exchange` - The client sends a key exchange message, often involving public key cryptography.")
    slow_print(f"{CYAN}6. `Finished` - Both client and server send a 'Finished' message to signal the handshake is complete.")

def demo_random_binary_data():
    """Show random binary data, simulating a handshake message."""
    print(f"\n{BOLD}{CYAN}🔮 Let's simulate a raw handshake message in binary!{RESET}")
    random_binary_data = ''.join(random.choice(['0', '1']) for _ in range(128))  # Random 128-bit binary string
    print(f"{CYAN}Simulated Binary Data (128-bit):\n{RESET}{YELLOW}{random_binary_data}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 TLS Handshake Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: Which message in the TLS handshake contains the server's certificate?{RESET}")
    print(f"{YELLOW}A) Client Hello{RESET}")
    print(f"{YELLOW}B) Server Hello{RESET}")
    print(f"{YELLOW}C) Certificate{RESET}")
    print(f"{YELLOW}D) Finished{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, C, or D): {RESET}").strip().upper()

    if answer == "C":
        print(f"{GREEN}✅ Correct! The `Certificate` message contains the server's certificate.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is C. The server sends its certificate to authenticate itself.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ The TLS handshake involves several key messages, such as `Client Hello`, `Server Hello`, `Certificate`, and others.")
    slow_print(f"✔ Each message can be represented in binary and hex format, which allows us to inspect the raw transmission of data between client and server.")
    slow_print(f"✔ Understanding these messages helps in securing and debugging encrypted communications like HTTPS.")
    print(f"{GREEN}By learning how TLS works at the byte level, you're enhancing your ability to understand web security! 🔐{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    display_tls_handshake_messages()
    explain_tls_handshake_fields()
    demo_random_binary_data()
    quiz()
    summary()

if __name__ == "__main__":
    run()
