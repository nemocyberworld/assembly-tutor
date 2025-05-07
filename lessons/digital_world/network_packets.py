# lessons/network/network_packets.py

import time
import socket

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to Network Packets in Binary!{RESET}")
    slow_print(f"{CYAN}Ever wondered how your messages travel across the web?")
    slow_print("They're broken into packets — tiny bundles of binary data! 📦")
    input(f"\n{YELLOW}Press Enter to simulate sending a message... {RESET}")

def string_to_binary(message):
    return ' '.join(f'{ord(c):08b}' for c in message)

def send_packet(message):
    print(f"\n{BOLD}{BLUE}🚀 Simulating Packet Transmission...{RESET}")
    binary = string_to_binary(message)
    print(f"{CYAN}Message: {GREEN}{message}{RESET}")
    print(f"{YELLOW}Binary Packet:{RESET}")
    print(f"{MAGENTA}{binary}{RESET}")

    slow_print(f"\n{CYAN}Sending packet over the network... 📡{RESET}")
    for byte in binary.split():
        print(f"{GREEN}➡ Sending byte: 0b{byte}{RESET}")
        time.sleep(0.1)
    print(f"\n{BLUE}✅ Packet delivered successfully!{RESET}")

def explain_packet_structure():
    print(f"\n{BOLD}{MAGENTA}🧠 Packet Structure (Simplified):{RESET}")
    slow_print(f"{CYAN}✔ Header: Where is it going?")
    slow_print("✔ Payload: The actual message in binary")
    slow_print("✔ Footer: Optional checksum or end marker")
    print(f"{GREEN}It's like mailing a letter — with a TO, message, and stamp! ✉️{RESET}")

def simulate_socket_demo():
    print(f"\n{BOLD}{BLUE}🔌 Try Real Socket Encoding (Offline){RESET}")
    test_msg = "Hello, Net!"
    encoded = test_msg.encode('utf-8')
    print(f"{CYAN}UTF-8 Bytes: {RESET}{' '.join(f'{b:02X}' for b in encoded)}")
    print(f"{YELLOW}Binary: {RESET}{' '.join(f'{b:08b}' for b in encoded)}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Text is converted to bytes before it's sent.")
    slow_print("✔ Network packets carry this data across the world.")
    slow_print("✔ Binary is the universal language for computers 🧠")
    print(f"{GREEN}You just sent your first virtual packet! 🚀{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    user_message = input(f"{YELLOW}Type a short message to send: {RESET}")
    send_packet(user_message)
    explain_packet_structure()
    simulate_socket_demo()
    summary()

if __name__ == "__main__":
    run()
