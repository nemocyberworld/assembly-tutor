# lessons/web_requests/web_request_headers.py

import binascii
import time

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
    print(f"{BOLD}{MAGENTA}🌐 Welcome to HTTP Header Analysis!{RESET}")
    slow_print(f"{CYAN}HTTP headers are key components of web requests and responses. They contain vital information about the request, such as the method, user agent, content type, and more.")
    slow_print("By analyzing these headers in both ASCII and Hex formats, we can better understand how web communication works.")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def display_http_request_headers():
    """Display a sample HTTP request header in ASCII and Hex."""
    print(f"\n{BOLD}{CYAN}🔍 HTTP Request Header Analysis{RESET}")
    
    # Sample HTTP request headers
    sample_headers = """
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
    """
    
    print(f"\n{BOLD}{CYAN}ASCII Representation:{RESET}")
    slow_print(sample_headers)
    
    # Convert the headers to bytes for Hex representation
    header_bytes = sample_headers.encode('utf-8')
    
    print(f"\n{BOLD}{CYAN}Hexadecimal Representation:{RESET}")
    hex_representation = binascii.hexlify(header_bytes).decode('utf-8')
    formatted_hex = ' '.join([hex_representation[i:i+2] for i in range(0, len(hex_representation), 2)])
    slow_print(formatted_hex)

def explain_http_header_fields():
    """Explain key fields in the HTTP request header."""
    print(f"\n{BOLD}{CYAN}📝 Key HTTP Header Fields:{RESET}")
    slow_print(f"{CYAN}1. `GET /index.html HTTP/1.1` - The request method (GET) and the resource being requested (/index.html) in HTTP/1.1 format.")
    slow_print(f"{CYAN}2. `Host: www.example.com` - Specifies the domain of the server being requested.")
    slow_print(f"{CYAN}3. `User-Agent: Mozilla/...` - Describes the browser and system sending the request.")
    slow_print(f"{CYAN}4. `Accept: text/html,...` - Tells the server which content types the client can process.")
    slow_print(f"{CYAN}5. `Connection: keep-alive` - Requests the server to keep the connection open after the request is completed.")

def demonstrate_encoding_issues():
    """Show how encoding can cause issues in HTTP headers."""
    print(f"\n{BOLD}{RED}⚠️ Encoding Issues in HTTP Headers{RESET}")
    slow_print(f"{CYAN}Sometimes, special characters or non-ASCII characters can cause issues in HTTP headers.")
    slow_print(f"\nExample of broken encoding in headers:")
    broken_header = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Â AppleWebKit/537.36"
    print(f"{MAGENTA}{broken_header}{RESET}")
    slow_print(f"{CYAN}Notice the strange character (Â)? This could be caused by a mismatched encoding in the HTTP headers.")
    print(f"\n{RED}To fix this, ensure that the headers are properly encoded using UTF-8 or another suitable character encoding.{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: What does the `User-Agent` header tell the server?{RESET}")
    print(f"{YELLOW}A) The client's operating system and browser{RESET}")
    print(f"{YELLOW}B) The IP address of the client{RESET}")
    print(f"{YELLOW}C) The requested resource's content type{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "A":
        print(f"{GREEN}✅ Correct! The `User-Agent` header contains information about the client's operating system and browser.{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is A. The `User-Agent` header helps the server know about the client’s environment.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ HTTP headers are crucial for making requests and responses in web communication. They contain information such as the requested resource, browser details, and supported content types.")
    slow_print(f"✔ HTTP headers can be inspected both in ASCII and Hex formats, allowing us to understand the underlying binary structure.")
    slow_print(f"✔ Encoding issues in headers can occur and may result in unexpected characters, but they can be fixed by ensuring proper encoding.")
    print(f"{GREEN}By understanding HTTP headers in different formats, you can debug web issues and improve your web development skills! 🌍{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    display_http_request_headers()
    explain_http_header_fields()
    demonstrate_encoding_issues()
    quiz()
    summary()

if __name__ == "__main__":
    run()
