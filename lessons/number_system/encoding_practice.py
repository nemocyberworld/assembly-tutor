# lessons/basics/encoding_practice.py

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
    print(f"{BOLD}{MAGENTA}🎉 Welcome to 'Guess the Character from Bytes' Challenge!{RESET}")
    slow_print(f"{CYAN}In this game, you will be given a byte sequence (in UTF-8) and your task is to guess the character it represents!")
    slow_print("Are you ready to test your encoding knowledge? Let's go! 🔍")
    input(f"\n{YELLOW}Press Enter to start... {RESET}")

def byte_to_char(byte_sequence):
    """Manually decode a UTF-8 byte sequence to a character."""
    decoded_characters = []
    i = 0

    while i < len(byte_sequence):
        byte = byte_sequence[i]
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

def practice_guessing_game():
    print(f"\n{BOLD}{CYAN}🎯 Your Task: Guess the Character from the Bytes!{RESET}")
    characters = [
        {"char": "A", "bytes": [0x41]},
        {"char": "🌍", "bytes": [0xF0, 0x9F, 0x8C, 0x8D]},
        {"char": "€", "bytes": [0xE2, 0x82, 0xAC]},
        {"char": "中", "bytes": [0xE4, 0xB8, 0xAD]},
        {"char": "😊", "bytes": [0xF0, 0x9F, 0x98, 0x8A]},
        {"char": "Z", "bytes": [0x5A]},
        {"char": "👾", "bytes": [0xF0, 0x9F, 0x98, 0xBE]},
    ]

    random.shuffle(characters)

    score = 0
    for i, character in enumerate(characters[:5], 1):  # Limit to 5 rounds
        byte_sequence = character["bytes"]
        correct_answer = character["char"]

        print(f"\n{YELLOW}Round {i}: What character does this byte sequence represent?{RESET}")
        print(f"Byte Sequence: {GREEN}{' '.join([hex(byte) for byte in byte_sequence])}{RESET}")

        user_guess = input(f"{YELLOW}Your Guess: {RESET}").strip()
        
        if user_guess == correct_answer:
            print(f"{GREEN}✅ Correct! {RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is: {GREEN}{correct_answer}{RESET}")

    print(f"\n{BOLD}{CYAN}🏁 Game Over! Your score: {score}/5{RESET}")
    if score == 5:
        print(f"{GREEN}🌟 Perfect Score! You're a character encoding master!{RESET}")
    elif score >= 3:
        print(f"{YELLOW}👍 Great job! Keep practicing to master this!{RESET}")
    else:
        print(f"{RED}💡 Keep going, you’ll get it next time!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ UTF-8 encodes characters using 1 to 4 bytes, depending on the character's complexity.")
    slow_print(f"✔ The task was to decode the byte sequence and guess the character it represents.")
    slow_print(f"✔ With practice, you'll get more comfortable with character encoding and decoding!")
    print(f"{GREEN}Great job completing the challenge! 🎉 Keep practicing, and soon decoding will be second nature!{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")
if __name__ == "__main__":
    intro()
    practice_guessing_game()
    summary()
