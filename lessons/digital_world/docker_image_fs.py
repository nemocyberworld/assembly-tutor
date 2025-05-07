# lessons/docker/docker_image_fs.py

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
    print(f"{BOLD}{MAGENTA}🐳 Welcome to Docker Layer Analysis in Hex!{RESET}")
    slow_print(f"{CYAN}In this lesson, we will explore what a **Docker image layer** looks like in **hexadecimal format**.")
    slow_print(f"We will look at the Docker image layer’s filesystem and learn about how the layers are built.")
    slow_print(f"Let’s see what’s inside the **Docker layers** and how they are represented in raw byte form! 🔍")
    input(f"\n{YELLOW}Press Enter to begin the lesson... {RESET}")

def inspect_docker_layer():
    print(f"\n{BOLD}{CYAN}🔍 Inspecting a Docker Image Layer{RESET}")
    slow_print(f"{CYAN}Docker images are made of layers, each containing filesystem changes. These layers are stored as compressed tarballs in the Docker filesystem.")
    slow_print(f"We’ll take a peek at what one of these layers looks like in hexadecimal format.")

    # Simulated Hex Data of a Docker image layer (this is just an example for educational purposes)
    docker_layer_hex = "78 9c 63 f8 ff ff 3f 03 07 60 40 80 80 f0 60 68 38"
    print(f"\n{YELLOW}Docker Layer Hex Data (Simulated): {RESET}")
    print(f"{MAGENTA}{docker_layer_hex}{RESET}")

    slow_print(f"\nNow, let's break down the structure of this hex data and explain how Docker layers are organized.")

    # Example field breakdown for a Docker layer (fictional example)
    layer_fields = {
        "Compression Type": docker_layer_hex[:2],
        "Layer Data (first 4 bytes)": docker_layer_hex[3:11],
        "Filesystem Changes": docker_layer_hex[11:19],
        "Layer Metadata": docker_layer_hex[19:27]
    }

    for field, value in layer_fields.items():
        print(f"{BOLD}{YELLOW}{field}: {RESET}{CYAN}{value}{RESET}")
        slow_print(f"Field {field} in binary: {bin(int(value.replace(' ', ''), 16))[2:].zfill(8)}", delay=0.05)

def explain_layer_structure():
    print(f"\n{BOLD}{CYAN}📚 Explaining the Docker Layer Structure{RESET}")
    slow_print(f"{CYAN}A Docker image layer typically includes the following elements:")
    
    explanation = {
        "Compression Type": "Docker layers are compressed (usually with gzip). The first part of the hex data often represents the compression method used.",
        "Layer Data": "This is the core data of the layer, which could represent files and changes made to the filesystem.",
        "Filesystem Changes": "This section represents file additions, deletions, and modifications within the layer.",
        "Layer Metadata": "Contains metadata such as layer ID, parent layer ID, and other info about the layer's creation."
    }

    for field, desc in explanation.items():
        print(f"{BOLD}{YELLOW}{field}: {RESET}{CYAN}{desc}{RESET}")
        slow_print(f"Explanation: {desc}", delay=0.05)

def quiz():
    print(f"\n{BOLD}{MAGENTA}🎮 Docker Layer Quiz Time!{RESET}")
    print(f"\n{CYAN}Question: What does the 'Layer Data' section of a Docker image layer contain?{RESET}")
    print(f"{YELLOW}A) The compression type used for the layer.{RESET}")
    print(f"{YELLOW}B) The raw data and filesystem changes, such as files added or modified.{RESET}")
    print(f"{YELLOW}C) Metadata like the layer ID and parent ID.{RESET}")

    answer = input(f"{CYAN}Your Answer (A, B, or C): {RESET}").strip().upper()

    if answer == "B":
        print(f"{GREEN}✅ Correct! The 'Layer Data' section contains raw data and filesystem changes (e.g., files added, modified).{RESET}")
    else:
        print(f"{RED}❌ Nope! The correct answer is B. The 'Layer Data' section holds filesystem changes made in that layer.{RESET}")

def summary():
    print(f"\n{BOLD}{BLUE}📘 Summary:{RESET}")
    slow_print(f"{CYAN}✔ Docker images are made up of multiple layers, each representing filesystem changes.")
    slow_print(f"✔ These layers are stored as compressed tarballs, and when we inspect them in hex, we see the underlying data.")
    slow_print(f"✔ Understanding how Docker layers work helps in troubleshooting image builds, optimizing layer usage, and securing containers.")
    print(f"{GREEN}Congratulations! You've learned how to inspect Docker image layers in hex! 🐳💻{RESET}")
    input(f"\n{BOLD}➡️ Press Enter to go back to the lesson list...{RESET}")

def run():
    intro()
    inspect_docker_layer()
    explain_layer_structure()
    quiz()
    summary()
