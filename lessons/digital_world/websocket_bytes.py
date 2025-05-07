# lessons/web/websocket_bytes.py

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
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🌐 Welcome to WebSocket Frame Exploration!{RESET}")
    slow_print(f"{CYAN}WebSockets allow real-time communication between clients and servers.")
    slow_print("Let's dive into WebSocket frames and see how data is transmitted in raw Hex and Binary! ⚡")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def explain_websocket_frames():
    print(f"\n{BOLD}{CYAN}🔍 What is a WebSocket Frame?{RESET}")
    slow_print(f"{CYAN}A WebSocket frame is the basic unit of communication in a WebSocket connection.")
    slow_print(f"WebSocket frames consist of a header and a payload. The header contains information like the frame's length and masking key.")

def show_websocket_frame():
    print(f"\n{BOLD}{YELLOW}🔢 Example WebSocket Frame in Hex!{RESET}")
    
    # Let's simulate a small WebSocket frame
    # This is a simplified frame structure (not including masking for simplicity)
    # The frame could represent sending a simple message, like "Hello"
    frame_hex = "81 05 48 65 6C 6C 6F"
    print(f"{CYAN}Example Frame in Hex: {frame_hex}{RESET}")
    
    # Breakdown the frame
    print(f"\n{BOLD}{CYAN}🔧 Frame Breakdown:{RESET}")
    print(f"{GREEN}81: Fin (1 bit), RSV1, RSV2, RSV3 (3 bits), Opcode (4 bits){RESET}")
    print(f"{GREEN}05: Payload length (1 byte){RESET}")
    print(f"{GREEN}48 65 6C 6C 6F: Payload data (Hex for 'Hello'){RESET}")
    print(f"{YELLOW}This frame sends the message 'Hello' over WebSocket!{RESET}")

def binary_representation():
    print(f"\n{BOLD}{CYAN}🖥️ WebSocket Frame in Binary!{RESET}")
    frame_binary = bin(int("81", 16))[2:].zfill(8) + bin(int("05", 16))[2:].zfill(8) + ''.join([bin(int(hex_byte, 16))[2:].zfill(8) for hex_byte in ["48", "65", "6C", "6C", "6F"]])
    print(f"{GREEN}Binary Representation of WebSocket Frame: {frame_binary}{RESET}")
    print(f"\n{YELLOW}In binary, we can see the structure of the frame more clearly!{RESET}")

def decode_frame():
    print(f"\n{BOLD}{CYAN}🔓 Decode the WebSocket Frame!{RESET}")
    frame_hex = input(f"{CYAN}Enter a WebSocket frame in Hex to decode (e.g., 81 05 48 65 6C 6C 6F): {RESET}")
    
    # Clean up the input and decode
    frame_bytes = bytes.fromhex(frame_hex)
    try:
        decoded_message = frame_bytes[1:].decode("utf-8")  # Assuming it's a UTF-8 encoded message
        print(f"{GREEN}Decoded message: {decoded_message}{RESET}")
    except Exception as e:
        print(f"{RED}❌ Error decoding the frame: {e}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 WebSocket Frame Quiz Time!{RESET}")
    print(f"\n{CYAN}What does the first byte '81' in a WebSocket frame represent?{RESET}")
    print(f"{YELLOW}A) It's the length of the payload.{RESET}")
    print(f"{YELLOW}B) It indicates that the frame is the final fragment (FIN).{RESET}")
    print(f"{YELLOW}C) It represents the actual message content.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "B":
        print(f"{GREEN}✅ Correct! The first byte '81' indicates that it's the final frame and contains an opcode of 1 (text frame).{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is B. '81' means it's the final fragment of the message.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ WebSocket frames consist of a header and payload.")
    slow_print(f"✔ The header contains control information like the opcode and whether it's the final frame.")
    slow_print(f"✔ Payload data is sent as binary data and can represent messages like 'Hello'!")
    print(f"{GREEN}You’ve unlocked a peek into WebSocket communication at the byte level! 🔑{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explain_websocket_frames()
    show_websocket_frame()
    binary_representation()
    decode_frame()
    quiz()
    summary()

if __name__ == "__main__":
    run()
