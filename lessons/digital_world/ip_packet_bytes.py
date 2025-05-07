# lessons/network/ip_packet_bytes.py

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to Dissecting IPv4 Packets in Hex!{RESET}")
    slow_print(f"{CYAN}In this lesson, we will take a closer look at how an IPv4 packet is structured.")
    slow_print(f"We will decode the **IPv4 header** and analyze the hexadecimal representation of the fields.")
    slow_print(f"By the end, you will have a better understanding of how packets travel through networks. 🚀")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def dissect_ip_packet():
    print(f"\n{BOLD}{CYAN}🔍 Dissecting an IPv4 Packet Header{RESET}")
    slow_print(f"{CYAN}Let's start by examining a simple IPv4 packet's header, broken down into its hexadecimal format.")

    # Example of an IPv4 packet header (this is just an example for educational purposes)
    # Fields of the IPv4 header:
    # Version (4 bits) + IHL (4 bits) + Type of Service (8 bits) + Total Length (16 bits)
    # Identification (16 bits) + Flags (3 bits) + Fragment Offset (13 bits) + TTL (8 bits)
    # Protocol (8 bits) + Header Checksum (16 bits) + Source Address (32 bits) + Destination Address (32 bits)

    packet_header_hex = "45 00 00 3c 1c 46 40 00 40 06 b1 e6 c0 a8 00 68 c0 a8 00 01"
    print(f"\n{YELLOW}IPv4 Packet Header (Hex): {RESET}")
    print(f"{MAGENTA}{packet_header_hex}{RESET}")

    # Now, let’s break down this hex string into its fields
    fields = {
        "Version + IHL": packet_header_hex[:2],
        "Type of Service": packet_header_hex[3:5],
        "Total Length": packet_header_hex[5:9],
        "Identification": packet_header_hex[9:13],
        "Flags + Fragment Offset": packet_header_hex[13:17],
        "TTL": packet_header_hex[17:19],
        "Protocol": packet_header_hex[19:21],
        "Header Checksum": packet_header_hex[21:25],
        "Source IP": packet_header_hex[25:33],
        "Destination IP": packet_header_hex[33:]
    }

    # Displaying the dissection of the IPv4 header
    slow_print(f"\nNow, let's break it down field by field, and convert each part into binary and hex for better understanding.\n")

    for field, value in fields.items():
        print(f"{BOLD}{YELLOW}{field}: {RESET}{CYAN}{value}{RESET}")
        slow_print(f"Field {field} in binary: {bin(int(value.replace(' ', ''), 16))[2:].zfill(8)}", delay=0.05)

def explain_ip_fields():
    print(f"\n{BOLD}{CYAN}📚 Explaining IPv4 Header Fields{RESET}")
    slow_print(f"{CYAN}Let’s now explain what each field represents in the IPv4 header.")
    
    explanation = {
        "Version + IHL": "The first 4 bits are the version (IPv4 = 4), and the next 4 bits are the IHL (Internet Header Length).",
        "Type of Service": "8 bits representing the type of service, used for traffic prioritization.",
        "Total Length": "16 bits specifying the total length of the packet (header + data).",
        "Identification": "A 16-bit value used to uniquely identify fragments of a packet.",
        "Flags + Fragment Offset": "3 bits for flags (indicating fragmentation), and 13 bits for the fragment offset.",
        "TTL": "8 bits for the Time-To-Live, indicating how long the packet can stay in the network.",
        "Protocol": "8 bits indicating the protocol used in the data section (e.g., TCP, UDP).",
        "Header Checksum": "16-bit checksum used for error checking of the header.",
        "Source IP": "32 bits representing the source IP address of the sender.",
        "Destination IP": "32 bits representing the destination IP address of the receiver."
    }

    for field, desc in explanation.items():
        print(f"{BOLD}{YELLOW}{field}: {RESET}{CYAN}{desc}{RESET}")
        slow_print(f"Explanation: {desc}", delay=0.05)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 IPv4 Packet Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: What is the total length field in an IPv4 header used for?{RESET}")
    print(f"{YELLOW}A) It specifies the size of the data payload only.{RESET}")
    print(f"{YELLOW}B) It specifies the entire size of the packet (header + data).{RESET}")
    print(f"{YELLOW}C) It indicates the protocol type of the packet.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "B":
        print(f"{GREEN}✅ Correct! The total length field specifies the entire size of the packet, including both the header and the data payload.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is B. The total length field specifies the entire size of the packet.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ IPv4 packets are divided into headers and data. The header contains important information about the packet.")
    slow_print(f"✔ The fields within the header are encoded in hexadecimal, but each can be converted to binary and analyzed.")
    slow_print(f"✔ By understanding the IPv4 header structure, you can gain insights into how data is routed across networks.")
    print(f"{GREEN}Congratulations! You've learned how to dissect an IPv4 packet header in hex. 🖥️🌐{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    dissect_ip_packet()
    explain_ip_fields()
    quiz()
    summary()

if __name__ == "__main__":
    run()
