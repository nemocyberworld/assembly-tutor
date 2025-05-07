# lessons/tcp/tcp_flags_bits.py

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

# TCP Flag Values (in Binary Representation)
SYN = 0b00000010
ACK = 0b00010000
FIN = 0b00000100
RST = 0b00000001
PSH = 0b01000000
URG = 0b00100000

def slow_print(text, delay=0.07):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🌐 Welcome to TCP Flag Visualization!{RESET}")
    slow_print(f"{CYAN}TCP flags are special control bits used to manage the connection states and flow control during data transmission.")
    slow_print(f"In this lesson, we’ll visualize these flags in binary form and see how they work. 🔑")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def tcp_flags_overview():
    print(f"\n{BOLD}{CYAN}🔍 What Are TCP Flags?{RESET}")
    slow_print(f"{CYAN}TCP flags are 1-bit values in the TCP header used to control the connection. The flags manage various states such as connection setup, data flow, and termination.")
    slow_print(f"Here are the key TCP flags (represented in binary):")
    print(f"1. **SYN** (Synchronize) – Initiates a connection.")
    print(f"2. **ACK** (Acknowledge) – Acknowledges the receipt of data.")
    print(f"3. **FIN** (Finish) – Closes the connection.")
    print(f"4. **RST** (Reset) – Resets the connection.")
    print(f"5. **PSH** (Push) – Pushes data immediately to the application layer.")
    print(f"6. **URG** (Urgent) – Marks data as urgent.")
    print(f"\n{YELLOW}Let's visualize these flags in action!{RESET}")

def visualize_tcp_flags():
    print(f"\n{BOLD}{CYAN}🔧 Visualizing TCP Flags in Binary{RESET}")
    slow_print(f"{CYAN}TCP flags are set as individual bits in the TCP header. When multiple flags are set together, they form a binary number.")
    
    # Demonstrate SYN flag
    print(f"\n{MAGENTA}SYN Flag (SYN = 1){RESET}")
    syn_flag = SYN
    print(f"{YELLOW}Binary: {bin(syn_flag)}{RESET}")
    print(f"{CYAN}This packet has the SYN flag set to 1, meaning it is attempting to initiate a connection.")

    # Demonstrate ACK flag
    print(f"\n{MAGENTA}ACK Flag (ACK = 1){RESET}")
    ack_flag = ACK
    print(f"{YELLOW}Binary: {bin(ack_flag)}{RESET}")
    print(f"{CYAN}This packet has the ACK flag set to 1, acknowledging the receipt of data.")

    # Demonstrate SYN + ACK flag (combined)
    print(f"\n{MAGENTA}SYN + ACK Flags Set (SYN = 1, ACK = 1){RESET}")
    syn_ack_flags = SYN | ACK
    print(f"{YELLOW}Binary: {bin(syn_ack_flags)}{RESET}")
    print(f"{CYAN}This packet has both SYN and ACK flags set, indicating that the server is responding to the client's SYN request.")

    # Demonstrate all flags set together
    print(f"\n{MAGENTA}All Flags Set (SYN + ACK + FIN + RST + PSH + URG){RESET}")
    all_flags = SYN | ACK | FIN | RST | PSH | URG
    print(f"{YELLOW}Binary: {bin(all_flags)}{RESET}")
    print(f"{CYAN}This packet has all TCP flags set, which is highly unusual but can be used in special cases like connection reset or urgent data.")

def tcp_flags_analysis():
    print(f"\n{BOLD}{CYAN}🔍 Analyzing TCP Flag Combinations{RESET}")
    slow_print(f"{CYAN}Let's look at some common flag combinations and their meanings:")
    
    # SYN + ACK (Used for Handshake)
    print(f"\n{MAGENTA}SYN + ACK (Binary: {bin(SYN | ACK)}){RESET}")
    slow_print(f"{CYAN}This combination is used during the TCP handshake to establish a connection between a client and server.")
    
    # FIN (Used to Close Connection)
    print(f"\n{MAGENTA}FIN (Binary: {bin(FIN)}){RESET}")
    slow_print(f"{CYAN}The FIN flag is used to signal the end of a TCP connection.")
    
    # PSH (Used to Push Data)
    print(f"\n{MAGENTA}PSH (Binary: {bin(PSH)}){RESET}")
    slow_print(f"{CYAN}When the PSH flag is set, it indicates that the data should be sent immediately to the application layer.")
    
    # URG (Urgent Data)
    print(f"\n{MAGENTA}URG (Binary: {bin(URG)}){RESET}")
    slow_print(f"{CYAN}The URG flag marks data as urgent, requiring immediate attention by the receiver.")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 TCP Flags Quiz Time!{RESET}")
    print(f"\n{CYAN}What does the ACK flag signify in a TCP packet?{RESET}")
    print(f"{YELLOW}A) Acknowledges the receipt of data.{RESET}")
    print(f"{YELLOW}B) Closes the connection.{RESET}")
    print(f"{YELLOW}C) Initiates the connection.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "A":
        print(f"{GREEN}✅ Correct! The ACK flag indicates that data has been acknowledged by the receiver.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is A. ACK acknowledges the receipt of data.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ TCP flags are used to control the state of a TCP connection and manage data transmission.")
    slow_print(f"✔ Flags such as SYN, ACK, FIN, RST, PSH, and URG are each represented as individual bits.")
    slow_print(f"✔ Combinations of these flags are used during different phases of communication, such as establishing or closing a connection.")
    print(f"{GREEN}Now you have a clearer understanding of TCP flags and how they function in binary form! 🌍🔐{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    tcp_flags_overview()
    visualize_tcp_flags()
    tcp_flags_analysis()
    quiz()
    summary()

if __name__ == "__main__":
    run()
