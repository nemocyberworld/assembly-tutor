# lessons/web/url_encoding.py

import urllib.parse
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
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🌐 Welcome to URL Encoding!{RESET}")
    slow_print(f"{CYAN}Have you ever seen a URL with strange symbols like '%20' or '%3F'?")
    slow_print("That's **percent encoding**! Let's explore how URLs are encoded for the web. 🔐")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def explain_url_encoding():
    print(f"\n{BOLD}{CYAN}🔍 What is URL Encoding?{RESET}")
    slow_print(f"{CYAN}URL encoding, also known as **percent encoding**, converts special characters into a format that can be safely transmitted over the web.")
    slow_print(f"Characters that are not safe to use in URLs (like spaces, slashes, or symbols) are replaced with a '%' followed by two hexadecimal digits.")

def demo_percent_encoding():
    print(f"\n{BOLD}{YELLOW}🔢 Demo: Encoding Special Characters!{RESET}")
    url_component = input(f"{CYAN}Enter a string to see how it's encoded in a URL: {RESET}")
    encoded_url = urllib.parse.quote(url_component)
    print(f"{GREEN}Encoded URL component: {encoded_url}{RESET}")

def decode_url():
    print(f"\n{BOLD}{CYAN}🔓 Decode an Encoded URL!{RESET}")
    encoded_url = input(f"{CYAN}Enter an encoded URL to decode: {RESET}")
    decoded_url = urllib.parse.unquote(encoded_url)
    print(f"{GREEN}Decoded URL: {decoded_url}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 URL Encoding Quiz Time!{RESET}")
    print(f"\n{CYAN}What does '%20' represent in a URL?{RESET}")
    print(f"{YELLOW}A) Space{RESET}")
    print(f"{YELLOW}B) Exclamation mark{RESET}")
    print(f"{YELLOW}C) Question mark{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "A":
        print(f"{GREEN}✅ Correct! '%20' is the percent-encoded representation of a space!{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is A. '%20' represents a space in URLs.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ URL encoding is used to safely represent special characters in a URL.")
    slow_print(f"✔ Characters like spaces are encoded as '%20', and other characters like '?' or '&' have their own codes.")
    print(f"{GREEN}Now you're ready to work with URLs in a safe, web-friendly way! 🌐{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explain_url_encoding()
    demo_percent_encoding()
    decode_url()
    quiz()
    summary()

if __name__ == "__main__":
    run()
