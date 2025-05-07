# lessons/basics/decode_utf8.py

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
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print(f"{BOLD}{MAGENTA}🔍 Welcome to Manually Decoding UTF-8 Byte Sequences!{RESET}")
    slow_print(f"{CYAN}In UTF-8, characters are encoded using one to four bytes. Let's learn how to decode them manually!")
    slow_print("Understanding the encoding process helps you gain better control over how text is represented. 💡")
    input(f"\n{YELLOW}Press Enter to start the lesson... {RESET}")

def explain_utf8_encoding():
    print(f"\n{BOLD}{BLUE}📖 Understanding UTF-8 Encoding{RESET}")
    slow_print("✔ UTF-8 uses 1 to 4 bytes for encoding characters.")
    slow_print("✔ The first byte starts with a special bit pattern that tells how many bytes the character needs.")
    slow_print(f"{CYAN}Example: The character 'A' is encoded as {GREEN}0x41{RESET}, which is 1 byte.")
    slow_print(f"Meanwhile, '🌍' is encoded as {GREEN}0xF0 0x9F 0x8C 0x8D{RESET}, which is 4 bytes.")
    slow_print("Let's decode UTF-8 byte sequences by following these patterns.")

def decode_utf8_bytes(byte_sequence):
    """Manually decode a UTF-8 byte sequence."""
    decoded_characters = []
    i = 0

    while i < len(byte_sequence):
        byte = byte_sequence[i]
        # Check if the byte is a 1-byte, 2-byte, 3-byte, or 4-byte sequence
        if byte & 0b10000000 == 0:  # 1-byte character (ASCII)
            decoded_characters.append(chr(byte))
            i += 1
        elif byte & 0b11100000 == 0b11000000:  # 2-byte character
            byte2 = byte_sequence[i + 1]
            decoded_characters.append(chr(((byte & 0b00011111) << 6) | (byte2 & 0b00111111)))
            i += 2
        elif byte & 0b11110000 == 0b11100000:  # 3-byte character
            byte2 = byte_sequence[i + 1]
            byte3 = byte_sequence[i + 2]
            decoded_characters.append(chr(((byte & 0b00001111) << 12) | ((byte2 & 0b00111111) << 6) | (byte3 & 0b00111111)))
            i += 3
        elif byte & 0b11111000 == 0b11110000:  # 4-byte character
            byte2 = byte_sequence[i + 1]
            byte3 = byte_sequence[i + 2]
            byte4 = byte_sequence[i + 3]
            decoded_characters.append(chr(((byte & 0b00000111) << 18) | ((byte2 & 0b00111111) << 12) | ((byte3 & 0b00111111) << 6) | (byte4 & 0b00111111)))
            i += 4
        else:
            raise ValueError(f"Invalid UTF-8 byte sequence at byte {i}.")
    return ''.join(decoded_characters)

def interactive_decoding():
    print(f"\n{BOLD}{CYAN}🎯 Let's Decode Some UTF-8 Byte Sequences!{RESET}")
    byte_input = input(f"{YELLOW}Enter a UTF-8 byte sequence (in hexadecimal, space-separated): {RESET}")
    try:
        byte_sequence = [int(b, 16) for b in byte_input.split()]
        decoded_string = decode_utf8_bytes(byte_sequence)
        print(f"{CYAN}Decoded UTF-8 string: {GREEN}{decoded_string}{RESET}")
    except ValueError as e:
        print(f"{RED}❌ Error: {e}{RESET}")

def byte_sequence_examples():
    print(f"\n{BOLD}{BLUE}🔍 UTF-8 Byte Sequence Examples{RESET}")
    examples = [
        {"char": "A", "bytes": "41", "decoded": "A"},
        {"char": "🌍", "bytes": "F0 9F 8C 8D", "decoded": "🌍"},
        {"char": "€", "bytes": "E2 82 AC", "decoded": "€"},
        {"char": "中", "bytes": "E4 B8 AD", "decoded": "中"}
    ]
    for example in examples:
        byte_sequence = example["bytes"]
        decoded_char = example["decoded"]
        print(f"{YELLOW}{byte_sequence}{RESET} → Decoded as: {GREEN}{decoded_char}{RESET}")

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 UTF-8 Byte Sequence Quiz!{RESET}")
    score = 0
    questions = [
        ("What is the UTF-8 byte sequence for 'A'?", "41"),
        ("How many bytes does '🌍' use in UTF-8?", "4"),
        ("What is the UTF-8 byte sequence for '€'?", "E2 82 AC"),
        ("How many bytes does '中' use in UTF-8?", "3"),
        ("Can a single UTF-8 byte represent characters from other languages? (yes/no)", "no"),
    ]
    random.shuffle(questions)

    for i, (q, a) in enumerate(questions[:3], 1):
        user = input(f"{YELLOW}Q{i}: {q} {RESET}").strip()
        if user.lower() == a.lower():
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ The correct answer is: {a}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Quiz Complete! Score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🌟 UTF-8 Decoding Expert! Well done!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👏 Great work! Keep practicing!{RESET}")
    else:
        print(f"{RED}📚 Keep going! You’ll master it soon!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 uses different byte sequences for different characters.")
    slow_print(f"✔ 1 byte is used for ASCII characters, 2-4 bytes for more complex characters.")
    slow_print(f"✔ We manually decode the byte sequence by interpreting the bit patterns.")
    print(f"{GREEN}You’re now ready to decode UTF-8 byte sequences like a pro! 🎉{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    explain_utf8_encoding()
    byte_sequence_examples()
    interactive_decoding()
    quiz()
    summary()
