# lessons/dns/dns_query.py

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to DNS Query Exploration!{RESET}")
    slow_print(f"{CYAN}Ever wondered how your computer translates a website like www.example.com into an IP address?")
    slow_print("That's DNS at work! Let's dive into a DNS request and see how it looks in raw bytes.")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def dns_query_overview():
    print(f"\n{BOLD}{CYAN}🔍 Understanding DNS Requests{RESET}")
    slow_print(f"{CYAN}When you type a domain name into your browser, your computer sends a DNS request to a DNS server.")
    slow_print("The server responds with the corresponding IP address.")
    slow_print(f"\n{GREEN}Example DNS request for www.example.com:{RESET}")
    print(f"\n{YELLOW}Query: www.example.com → IP address?{RESET}")

def dns_request_structure():
    print(f"\n{BOLD}{CYAN}🔧 Structure of a DNS Query{RESET}")
    slow_print(f"{CYAN}A DNS query typically consists of the following parts:")
    print(f"1. **Transaction ID**: Identifies the request-response pair (2 bytes).")
    print(f"2. **Flags**: Specifies properties of the request (2 bytes).")
    print(f"3. **Questions**: The number of queries (2 bytes).")
    print(f"4. **Query Name**: The domain name you’re looking for (variable length).")
    print(f"5. **Query Type**: Specifies the type of query (e.g., A record for an IP address) (2 bytes).")
    print(f"6. **Query Class**: Specifies the protocol (e.g., IN for Internet) (2 bytes).")
    
def view_raw_dns_request():
    print(f"\n{BOLD}{YELLOW}🔢 Simulating a DNS Query in Raw Hex{RESET}")
    
    # Simulated DNS query for www.example.com (in a very simplified format)
    dns_query = (
        b'\x12\x34'  # Transaction ID (2 bytes)
        b'\x01\x00'  # Flags (standard query)
        b'\x00\x01'  # Number of questions (1 question)
        b'\x00\x00'  # Number of answers (0 answers)
        b'\x00\x00'  # Number of authority records (0)
        b'\x00\x00'  # Number of additional records (0)
        b'www'        # Query Name: "www"
        b'\x03'       # Length of "example" (3 bytes)
        b'example'    # Query Name: "example"
        b'\x03'       # Length of "com" (3 bytes)
        b'com'        # Query Name: "com"
        b'\x00'       # Null byte to terminate the domain name
        b'\x00\x01'   # Query Type (A record for IPv4 address)
        b'\x00\x01'   # Query Class (IN - Internet)
    )
    
    # Show the raw hex representation of the DNS query
    hex_representation = binascii.hexlify(dns_query).decode('utf-8')
    print(f"{CYAN}DNS Query in Hex: {hex_representation}{RESET}")
    
def simulate_dns_response():
    print(f"\n{BOLD}{CYAN}🔄 Simulating a DNS Response (IP Address){RESET}")
    slow_print(f"{CYAN}In response, the DNS server would send the IP address back to your computer.")
    slow_print(f"Let's simulate a response that returns the IP address for www.example.com.")
    
    # Simulated DNS response (again, highly simplified for learning purposes)
    dns_response = (
        b'\x12\x34'  # Transaction ID (same as query)
        b'\x81\x80'  # Flags (response, no error)
        b'\x00\x01'  # Number of questions (1 question)
        b'\x00\x01'  # Number of answers (1 answer)
        b'\x00\x00'  # Number of authority records (0)
        b'\x00\x00'  # Number of additional records (0)
        b'www'        # Query Name: "www"
        b'\x03'       # Length of "example"
        b'example'    # Query Name: "example"
        b'\x03'       # Length of "com"
        b'com'        # Query Name: "com"
        b'\x00'       # Null byte to terminate the domain name
        b'\x00\x01'   # Query Type (A record)
        b'\x00\x01'   # Query Class (IN - Internet)
        b'\x00\x04'   # Answer length (4 bytes for IPv4 address)
        b'\xc0\xa8\x00\x68'  # IP Address (192.168.0.104 in hex)
    )
    
    # Show the raw hex representation of the DNS response
    hex_response = binascii.hexlify(dns_response).decode('utf-8')
    print(f"{CYAN}DNS Response in Hex: {hex_response}{RESET}")
    print(f"\n{GREEN}The server responds with the IP address 192.168.0.104 for www.example.com!{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 DNS Query Quiz Time!{RESET}")
    print(f"\n{CYAN}What does the Query Type field in a DNS request specify?{RESET}")
    print(f"{YELLOW}A) Domain Name{RESET}")
    print(f"{YELLOW}B) IP Address{RESET}")
    print(f"{YELLOW}C) Record Type (A, MX, etc.){RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "C":
        print(f"{GREEN}✅ Correct! The Query Type specifies what type of DNS record is being requested (e.g., A for IPv4 address).{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is C. The Query Type indicates the DNS record type, such as A for IPv4.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ DNS queries are structured with transaction IDs, flags, and domain names.")
    slow_print(f"✔ The query specifies what type of information is requested, like an IP address (A record).")
    slow_print(f"✔ The DNS response provides the requested data, often in raw hex format.")
    print(f"{GREEN}Now you understand how DNS works under the hood and how raw data looks! 🌐💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    dns_query_overview()
    dns_request_structure()
    view_raw_dns_request()
    simulate_dns_response()
    quiz()
    summary()
