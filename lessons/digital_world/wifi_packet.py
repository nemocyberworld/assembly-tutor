# lessons/network/wifi_packet.py

import time
import binascii
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
    print(f"{BOLD}{MAGENTA}📶 Welcome to Wi-Fi Packet Peek!{RESET}")
    slow_print(f"{CYAN}Ever wonder what a Wi-Fi packet looks like under the hood?")
    slow_print("Today we’ll look at a simplified raw packet in HEX and break it down! 🔍")
    input(f"\n{YELLOW}Press Enter to peek inside a packet... {RESET}")

def create_sample_wifi_packet():
    # Simulated raw Wi-Fi packet (simplified for learning)
    frame_control = b'\x80\x00'   # Beacon frame
    duration = b'\x00\x00'
    dest_mac = b'\xff\xff\xff\xff\xff\xff'  # Broadcast
    src_mac = b'\x00\x11\x22\x33\x44\x55'   # Example device
    bssid = b'\x00\x11\x22\x33\x44\x55'     # Same as source
    seq_ctrl = b'\x10\x00'
    payload = b'WiFi Lesson Packet'
    
    packet = frame_control + duration + dest_mac + src_mac + bssid + seq_ctrl + payload
    return packet

def show_packet(packet):
    hex_data = binascii.hexlify(packet).decode()
    print(f"\n{BOLD}{BLUE}📦 Raw Wi-Fi Packet (Hex):{RESET}")
    grouped = ' '.join([hex_data[i:i+2] for i in range(0, len(hex_data), 2)])
    print(f"{YELLOW}{grouped}{RESET}")

    print(f"\n{BOLD}{CYAN}🧩 Packet Breakdown:{RESET}")
    print(f"{GREEN}Frame Control :{RESET} {packet[0:2].hex()}")
    print(f"{GREEN}Duration      :{RESET} {packet[2:4].hex()}")
    print(f"{GREEN}Dest MAC      :{RESET} {'-'.join(f'{b:02X}' for b in packet[4:10])}")
    print(f"{GREEN}Source MAC    :{RESET} {'-'.join(f'{b:02X}' for b in packet[10:16])}")
    print(f"{GREEN}BSSID         :{RESET} {'-'.join(f'{b:02X}' for b in packet[16:22])}")
    print(f"{GREEN}Seq Control   :{RESET} {packet[22:24].hex()}")
    print(f"{GREEN}Payload       :{RESET} {packet[24:].decode(errors='ignore')}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quick Quiz!{RESET}")
    print(f"{CYAN}What field holds the MAC address of the device sending the packet?{RESET}")
    answer = input(f"{YELLOW}Your Answer: {RESET}").strip().lower()

    if "source" in answer or "src" in answer:
        print(f"{GREEN}✅ Correct! Source MAC is the sender's address.{RESET}")
    else:
        print(f"{RED}❌ Nope! It’s the Source MAC field.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Wi-Fi packets are just structured bytes sent over the air.")
    slow_print("✔ Fields like MAC addresses and control bits are key for networking.")
    slow_print("✔ Tools like Wireshark show these bytes in hex too!")
    print(f"{GREEN}Next time you join Wi-Fi, remember—it’s all just packets flying around! 🚀{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    packet = create_sample_wifi_packet()
    show_packet(packet)
    quiz()
    summary()

if __name__ == "__main__":
    run()
