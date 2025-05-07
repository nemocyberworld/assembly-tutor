import random
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
    print(f"{BOLD}{MAGENTA}🎨 Welcome to Hex in Web Colors! 🌈{RESET}")
    slow_print(f"{CYAN}In web development, colors are often defined using hexadecimal (hex) codes.")
    slow_print(f"Each hex code represents a color by specifying the intensity of Red, Green, and Blue (RGB).")
    slow_print(f"Hexadecimal is used because it’s shorter and easier to work with compared to binary or decimal.")
    input(f"\n{YELLOW}Press Enter to continue and explore the world of web colors!{RESET}")

def explain_hex_colors():
    print(f"\n{BOLD}{CYAN}🔢 What is a Hex Color Code?{RESET}")
    slow_print(f"A hex color code is a 6-digit code starting with a hash symbol (#).")
    slow_print(f"It’s made up of three pairs of hex digits, each representing the intensity of Red, Green, and Blue.")
    slow_print(f"For example, the hex code #FF5733 breaks down as:")
    print(f"{GREEN}FF = Red intensity (255 in decimal) \n57 = Green intensity (87 in decimal) \n33 = Blue intensity (51 in decimal){RESET}")
    slow_print(f"\nEach pair can range from 00 (no intensity) to FF (maximum intensity).")

def color_demo():
    print(f"\n{BOLD}{YELLOW}🎨 Visualizing Web Colors:{RESET}")
    
    # List of some common colors in hex
    hex_colors = ['#FF5733', '#33FF57', '#3357FF', '#FFD700', '#8A2BE2', '#FF6347']
    
    for color in hex_colors:
        print(f"\n{CYAN}Hex Color: {color}{RESET}")
        print(f"Visual Representation: {BOLD}{color}{RESET}")
        print(f"{GREEN}This color can be used in web design to style backgrounds, text, buttons, and more!{RESET}")
        
        # Simulate showing the color by printing a "block" (for terminal purposes)
        print(f"{color}███████████████████{RESET}")
        time.sleep(1)

def hex_to_rgb():
    print(f"\n{BOLD}{CYAN}🔄 Hex to RGB Conversion:{RESET}")
    slow_print(f"Let’s take a hex color code and convert it to RGB format.")
    
    hex_code = input(f"{YELLOW}Enter a hex color code (e.g., #FF5733): {RESET}").strip()
    if hex_code.startswith('#'):
        hex_code = hex_code[1:]
    
    try:
        # Convert hex to RGB by splitting the hex code into RGB components
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        print(f"{BOLD}{MAGENTA}RGB Equivalent: ({r}, {g}, {b}){RESET}")
    except ValueError:
        print(f"{RED}⚠️ Invalid hex code! Make sure it's in the format #RRGGBB.{RESET}")

def rgb_to_hex():
    print(f"\n{BOLD}{CYAN}🔄 RGB to Hex Conversion:{RESET}")
    slow_print(f"Now, let's take an RGB value and convert it back to hex.")
    
    try:
        r = int(input(f"{YELLOW}Enter Red value (0-255): {RESET}"))
        g = int(input(f"{YELLOW}Enter Green value (0-255): {RESET}"))
        b = int(input(f"{YELLOW}Enter Blue value (0-255): {RESET}"))
        
        # Ensure valid RGB values
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print(f"{RED}⚠️ RGB values must be between 0 and 255!{RESET}")
            return
        
        # Convert RGB to hex
        hex_code = f"#{r:02X}{g:02X}{b:02X}"
        print(f"{BOLD}{MAGENTA}Hex Equivalent: {hex_code}{RESET}")
    except ValueError:
        print(f"{RED}⚠️ Invalid RGB input! Please enter integer values between 0 and 255.{RESET}")

def color_quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Hex Color Quiz!{RESET}")
    score = 0
    
    for i in range(3):
        print(f"\n{YELLOW}Question {i+1}:{RESET}")
        
        # Randomly select a hex color code and ask the user to identify it
        hex_code = random.choice(['#FF5733', '#33FF57', '#3357FF', '#FFD700', '#8A2BE2', '#FF6347'])
        print(f"Visual Representation: {BOLD}{hex_code}{RESET}")
        user_answer = input(f"🧠 What is the RGB equivalent of {BOLD}{hex_code}{RESET}? ").strip()
        
        # Convert hex to RGB and check if the user's answer matches
        r = int(hex_code[1:3], 16)
        g = int(hex_code[3:5], 16)
        b = int(hex_code[5:7], 16)
        correct_answer = f"({r}, {g}, {b})"
        
        if user_answer == correct_answer:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Incorrect! The correct answer is {correct_answer}.{RESET}")
    
    print(f"\n{BOLD}{BLUE}🏁 Quiz Complete! Your score: {score}/3{RESET}")
    if score == 3:
        print(f"{GREEN}🎉 Excellent! You’re a color coding master!{RESET}")
    elif score == 2:
        print(f"{YELLOW}👍 Great job! Keep practicing and you’ll become a pro!{RESET}")
    else:
        print(f"{RED}💡 No worries! Try again—you’re learning!{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Hexadecimal color codes are a compact and widely used format for representing colors in web development.")
    slow_print(f"✔ The RGB model maps Red, Green, and Blue values to a range of 0 to 255, and each color is represented by a 6-digit hex code.")
    slow_print(f"✔ You can easily convert between hex and RGB to work with colors programmatically.")
    print(f"{GREEN}Awesome! You’re now ready to use hex colors in your web projects! 🎨💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    explain_hex_colors()
    color_demo()
    hex_to_rgb()
    rgb_to_hex()
    color_quiz()
    summary()

if __name__ == "__main__":
    run()
