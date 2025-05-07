# lessons/tcp/tcp_three_way.py

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to TCP Handshake Visualization!{RESET}")
    slow_print(f"{CYAN}The TCP three-way handshake establishes a connection between two devices over a network. It ensures both sides are ready to communicate.")
    slow_print(f"Let's dive into how the handshake works, and visualize it in binary.🔑")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def tcp_handshake_overview():
    print(f"\n{BOLD}{CYAN}🔍 What is the TCP Three-Way Handshake?{RESET}")
    slow_print(f"{CYAN}Before data can be exchanged over a TCP connection, the two devices must perform a handshake to ensure they are ready to communicate.")
    slow_print("This handshake involves three steps:")
    print(f"1. **SYN** (Synchronize): The client sends a request to start a connection.")
    print(f"2. **SYN-ACK** (Synchronize-Acknowledge): The server acknowledges the request and responds.")
    print(f"3. **ACK** (Acknowledge): The client acknowledges the server's response, and the connection is established.")
    print(f"\n{YELLOW}Let's visualize this process in binary to see how it looks under the hood!{RESET}")

def visualize_tcp_handshake():
    print(f"\n{BOLD}{CYAN}🔧 Visualizing the TCP Handshake{RESET}")
    slow_print(f"{CYAN}The TCP handshake is represented by control flags in the header of each TCP packet. Let's break it down.")
    
    # Step 1: SYN from client to server
    print(f"\n{MAGENTA}Step 1: SYN (Client → Server){RESET}")
    slow_print(f"{CYAN}The client sends a packet with the SYN flag set to 1 (binary representation). Here's what it looks like in raw binary:")
    syn_packet = b'\x00\x00\x00\x00\x00\x02'  # Simplified representation of SYN packet
    syn_packet_hex = binascii.hexlify(syn_packet).decode('utf-8')
    print(f"{YELLOW}SYN Packet in Hex: {syn_packet_hex}{RESET}")
    print(f"{CYAN}Binary Representation: {bin(int(syn_packet_hex, 16))}{RESET}")

    # Step 2: SYN-ACK from server to client
    print(f"\n{MAGENTA}Step 2: SYN-ACK (Server → Client){RESET}")
    slow_print(f"{CYAN}The server responds with a SYN-ACK packet, acknowledging the client's request. Here's the binary representation:")
    syn_ack_packet = b'\x00\x00\x00\x02\x00\x12'  # Simplified SYN-ACK response
    syn_ack_packet_hex = binascii.hexlify(syn_ack_packet).decode('utf-8')
    print(f"{YELLOW}SYN-ACK Packet in Hex: {syn_ack_packet_hex}{RESET}")
    print(f"{CYAN}Binary Representation: {bin(int(syn_ack_packet_hex, 16))}{RESET}")

    # Step 3: ACK from client to server
    print(f"\n{MAGENTA}Step 3: ACK (Client → Server){RESET}")
    slow_print(f"{CYAN}The client sends the final ACK packet, acknowledging the server's response. Here's the binary representation:")
    ack_packet = b'\x00\x00\x00\x04\x00\x14'  # Simplified ACK packet
    ack_packet_hex = binascii.hexlify(ack_packet).decode('utf-8')
    print(f"{YELLOW}ACK Packet in Hex: {ack_packet_hex}{RESET}")
    print(f"{CYAN}Binary Representation: {bin(int(ack_packet_hex, 16))}{RESET}")

def tcp_handshake_analysis():
    print(f"\n{BOLD}{CYAN}🔍 Analyzing the TCP Handshake Process{RESET}")
    slow_print(f"{CYAN}Let's summarize the three steps of the handshake:")
    print(f"1. **SYN**: The client sends a SYN packet to initiate the connection.")
    print(f"2. **SYN-ACK**: The server responds with a SYN-ACK packet to acknowledge the connection.")
    print(f"3. **ACK**: The client sends the final ACK packet to confirm the connection.")
    slow_print(f"\n{GREEN}The connection is now established, and data can be exchanged!{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 TCP Handshake Quiz Time!{RESET}")
    print(f"\n{CYAN}What does the SYN flag in a TCP packet signify?{RESET}")
    print(f"{YELLOW}A) The packet is requesting a connection.{RESET}")
    print(f"{YELLOW}B) The packet is sending data.{RESET}")
    print(f"{YELLOW}C) The packet is closing the connection.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "A":
        print(f"{GREEN}✅ Correct! The SYN flag indicates that the packet is requesting a connection (start of the handshake).{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is A. SYN is used to initiate a connection in the handshake.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ The TCP handshake is a process used to establish a reliable connection between two devices.")
    slow_print(f"✔ The handshake involves three packets: SYN, SYN-ACK, and ACK.")
    slow_print(f"✔ We can visualize each of these packets as raw hex and binary data to understand the low-level process.")
    print(f"{GREEN}Now you have a deeper understanding of how TCP connections are established! 🌐💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    tcp_handshake_overview()
    visualize_tcp_handshake()
    tcp_handshake_analysis()
    quiz()
    summary()

if __name__ == "__main__":
    run()
