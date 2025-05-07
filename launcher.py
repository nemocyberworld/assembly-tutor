import importlib
import time
import sys

# ANSI color codes
class C:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    DIM = "\033[2m"

# Lesson structure with display names
LESSON_STRUCTURE = {
    "intro": [
        ("hello_world", "Hello World"),
        ("what_is_asm", "What is Assembly Language?"),
        ("registers", "Intro to Assembly & CPU Registers"),
        ("mov_lea", "Data Movement: `mov`, `lea`"),
        ("immediate_memory_register", "Working with Immediate, Memory, and Register Values"),
        ("arithmetic", "Basic Arithmetic: `add`, `sub`, `inc`, `dec`"),
        ("bitwise_ops", "Bitwise Operations: `and`, `or`, `xor`, `not`"),
        ("flags", "Understanding Flags and Status Register"),
        ("stack_basics", "Stack Basics: `push`, `pop`"),
        ("call_ret", "Function Calls: `call`, `ret`"),
        ("jumps_flags", "Conditional Jumps: `cmp`, `jmp`, `je`, `jne`, etc."),
        ("loops", "Writing Simple Loops with `jmp` and `cmp`"),
        ("labels", "Using Labels and Creating Flow Control"),
        ("memory_segments", "Memory Segments: `.data`, `.bss`, `.text`"),
        ("system_calls", "Intro to Linux Syscalls (`write`, `exit`)"),
        ("exit_codes", "Exit Codes and Program Termination"),
        ("comments_format", "Code Formatting and Comments"),
        ("nasm_basics", "How to Write, Assemble, and Run with NASM"),
        ("debugging1", "Debugging 01: Basics with `gdb` and `ndisasm`"),
        ("debugging2", "Debugging 02: 🛑 Breakpoints and Stepping Through Code"),
        ("debugging3", "Debugging 03: Inspecting Registers and Memory"),
        ("debugging4", "Debugging 04: Stack frames and function call tracing"),
        ("debugging5", "Debugging 05: Nested Calls, Stack Frames, and Segfaults"),
        ("debugging6", "Debugging 06: Watching and Catching Like a Debugging Ninja"),
        ("debugging7", "Debugging 07: Libraries, Heap, and Pretty-Printing"),
        ("debugging8", "Debugging 08: syscall tracing, child process debugging, and memory inspection using Valgrind + GDB.")        

    ],
    "intermediate": [
        ("memory_addressing", "Memory Addressing & Pointer Arithmetic"),
        ("function_calls", "Function Calls & Calling Conventions (System V ABI)"),
        ("stack_frames", "Prologue/Epilogue and Stack Frames"),
        ("strings_arrays", "Strings, Arrays, and the `.data` Section"),
        ("control_flow_advanced", "Advanced Control Flow (Loops & Conditionals)"),
        ("syscalls_linux_io", "Syscalls & Basic Linux I/O"),
        ("local_variables", "Local Variables and Stack Allocation"),
        ("parameter_passing", "Passing Arguments via Registers"),
        ("return_values", "Returning Values from Functions"),
        ("recursion", "Recursion in Assembly"),
        ("buffer_handling", "Handling Buffers and Input"),
        ("binary_math", "Binary Math and Number Representation"),
        ("inline_comments", "Improving Code Clarity with Inline Comments"),
        ("elf_basics", "How Assembly Fits in ELF Binaries"),
        ("linking_object_files", "Linking Object Files Together")
    ],
    "advanced": [
        ("complex_syscalls", "Advanced Syscalls: `mmap`, `execve`, `fork`"),
        ("manual_resolution", "Manual Function Resolution (Shellcode Style)"),
        ("minimal_elf", "Writing Minimal ELF Binaries by Hand"),
        ("position_independent", "Position-Independent Code (PIC)"),
        ("floating_point", "Floating Point Instructions & FPU Basics"),
        ("sse_simd", "SSE and SIMD Registers: Vectorized Math"),
        ("inline_shellcode", "Writing Inline Shellcode in Assembly"),
        ("execve_shell", "Writing a `/bin/sh` Shell Spawner"),
        ("syscall_hunting", "Hunting Syscalls Without libc"),
        ("elf_internals", "ELF Internals: Sections, Headers, and Linking"),
        ("assembly_optimizations", "Optimizing Assembly Code for Speed"),
        ("size_optimizations", "Code Golf: Minimizing Bytes"),
        ("anti_debugging", "Anti-Debugging Tricks in Assembly"),
        ("rop_chains", "Intro to Return-Oriented Programming (ROP)"),
        ("jmp_tables", "Using Jump Tables for Fast Branching"),
        ("hooking", "Function Hooking and Binary Patching"),
        ("self_modifying", "Self-Modifying Code Techniques"),
        ("obfuscation", "Assembly Obfuscation Techniques"),
        ("inline_asm_c", "Inline Assembly in C (GCC Style)"),
        ("bootloader_intro", "Writing a Simple Bootloader")
        
    ],
    
    "practice": [
        #Basics
        ("print_hello", "Print 'Hello, World!' to the Console"),
        ("exit_code", "Return a Specific Exit Code"),
        ("add_numbers", "Add Two Numbers and Print the Result"),
        ("register_swap", "Swap Values Between Registers"),
        ("subtract_numbers", "Subtract One Number from Another"),
        ("multiply_loop", "Multiply Two Numbers Using a Loop"),
        ("compare_values", "Compare Two Values and Print Result"),
        ("store_memory", "Store a Value in Memory and Retrieve It"),
        ("increment_loop", "Increment a Register in a Loop"),
        ("countdown", "Countdown from a Number to Zero"),
        ("jump_test", "Use Conditional Jump Based on Comparison"),
        ("stack_push_pop", "Push and Pop Values on the Stack"),
        ("function_call", "Use call and ret to Simulate a Function"),
        # control_flow
        ("compare_values", "Compare Two Values and Jump"),
        ("count_loop", "Count from 1 to 10 Using a Loop"),
        ("fibonacci_loop", "Print Fibonacci Numbers Using a Loop"),
        ("infinite_loop", "Create an Infinite Loop"),
        ("nested_loops", "Use Nested Loops for Matrix Traversal"),
        ("conditional_branching", "Branch Based on Multiple Conditions"),
        ("loop_sum", "Sum Numbers from 1 to N Using a Loop"),
        ("early_exit_loop", "Exit a Loop Early with a Condition"),
        ("loop_with_input", "Loop a Given Number of Times Based on Input"),
        ("reverse_loop", "Count Down in Reverse Using a Loop"),
        # memory
        ("store_array", "Store and Access an Array in Memory"),
        ("pointer_math", "Manipulate Pointers to Walk Through Memory"),
        ("string_length", "Calculate the Length of a Null-Terminated String"),
        ("reverse_array", "Reverse an Array In-Place Using Pointers"),
        ("sum_array", "Sum All Elements of an Integer Array"),
        ("copy_string", "Copy One Null-Terminated String to Another Location"),
        ("compare_strings", "Compare Two Null-Terminated Strings for Equality"),
        ("find_char", "Find the First Occurrence of a Character in a String"),
        ("memory_set", "Fill a Block of Memory with a Given Byte Value (like memset)"),
        ("string_concat", "Concatenate Two Null-Terminated Strings"),
        ("find_max", "Find the Maximum Element in an Array"),
        ("array_indexing", "Access Array Elements Using Indexing and Pointers"),
        ("two_dim_array", "Access Elements in a 2D Array (Matrix Access)"),
        ("struct_simulation", "Simulate a C-style Struct Using Offsets in Memory"),
        #functions
        ("call_simple", "Call a Simple Function"),
        ("recursive_factorial", "Recursive Factorial Function"),
        ("call_with_multiple_args", "Call Function with Multiple Integer Arguments"),
        ("pass_struct_like", "Pass a Struct-Like Memory Block to a Function"),
        ("return_multiple_values", "Return Multiple Values via Registers or Memory"),
        ("tail_recursive_sum", "Tail-Recursive Sum Function Optimization"),
        ("fibonacci_recursive", "Recursive Fibonacci Function"),
        ("fibonacci_iterative", "Iterative Fibonacci Function"),
        ("swap_values", "Swap Two Values Using a Function"),
        ("nested_calls", "Call a Function from Inside Another Function"),
        ("call_printf", "Call the C Library `printf` Function from Assembly"),
        ("string_length_function", "Calculate String Length via Function Call"),
        ("is_prime_function", "Check if a Number is Prime in a Function"),
        #system
        ("write_file", "Write to a File Using Syscalls"),
        ("read_input", "Read User Input with Syscalls"),
        ("fork_exec", "Fork a Process and Execute Another Program"),
        ("open_close_file", "Open and Close a File Using Syscalls"),
        ("read_file", "Read Contents of a File and Print to stdout"),
        ("get_time", "Get the Current Time Using `time` or `clock_gettime`"),
        ("dup_stdout", "Duplicate stdout and Write Using New File Descriptor"),
        ("pipe_communication", "Use a Pipe for Parent-Child Communication"),
        ("exec_ls", "Execute `/bin/ls` Using `execve`"),
        ("wait_child", "Fork and Wait for Child Process to Finish"),
        ("send_signal", "Send a Signal to a Process Using `kill`"),
        ("handle_signal", "Set Up a Signal Handler for `SIGINT`"),
        ("mmap_anon", "Allocate Anonymous Memory with `mmap`"),
        ("file_stat", "Get File Metadata Using `stat` Syscall"),
        # advance
        ("call_stack_walk", "Walk the Call Stack"),
        ("manual_malloc", "Manually Allocate Memory with mmap"),
        ("segfault_demo", "Cause and Debug a Segmentation Fault"),
        ("custom_printf", "Implement a Very Basic `printf` Function"),
        ("jmp_table", "Use a Jump Table for Function Dispatch"),
        ("hook_function", "Hook and Replace a Function at Runtime"),
        ("stack_canary_demo", "Demonstrate Stack Canary Protection"),
        ("ret2libc_demo", "Craft a ret2libc Attack Demo (Educational Use)"),
        ("tls_access", "Access Thread-Local Storage Manually"),
        ("inline_syscall", "Perform a Syscall Using Inline Assembly in C"),
        ("elf_parser", "Parse ELF Headers Manually"),
        ("manual_stack_frame", "Build and Destroy Your Own Stack Frame"),
        ("syscall_bruteforce", "Brute Force Syscall Numbers (for Education Only)"),
        ("shellcode_runner", "Load and Run Custom Shellcode Safely"),
        ("vtable_attack_demo", "Simulate a vtable Hijack in Assembly")        
        
    ],
    "number_system": [
        ("binary_intro", "Intro to Binary Numbers"),
        ("binary_math", "Binary Math Basics"),
        ("binary_to_decimal", "Convert Binary to Decimal and Vice Versa"),
        ("binary_and_bits", "Understanding Bits and Bit Positions"),
        ("binary_shift", "Left and Right Bit Shifting"),
        ("binary_masking", "Binary Masking and Bitwise Isolation"),
        ("binary_practice", "Practice Binary Conversion and Logic"),
        ("binary_overflow", "Binary Overflow and Two's Complement Basics"),
        ("bit_flags", "Using Bits as Flags and Configuration Switches"),
        ("parity_bits", "Understanding Parity Bits and Basic Error Checking"),
        ("bit_packing", "Pack and Unpack Multiple Values in a Single Byte"),
        ("signed_vs_unsigned", "Signed vs Unsigned Binary Representation"),
        ("twos_complement", "Two's Complement and Negative Numbers"),
        ("binary_timers", "Binary Counting and Timers in Hardware"),
        ("binary_visual", "Visualizing Binary with LEDs and Switches (Simulated)"),
        ("logic_gates", "Simulate Logic Gates with Binary (AND, OR, NOT)"),
        ("binary_quiz", "Challenge: Binary Logic Puzzle & Quiz"),
        # Hexadecimal
        ("hex_intro", "Intro to Hexadecimal"),
        ("hex_ascii", "Hex and ASCII"),
        ("hex_to_binary", "Convert Hex to Binary and Vice Versa"),
        ("hex_addressing", "How Hex is Used in Memory Addressing"),
        ("hex_colors", "Hex in Web Colors and Visual Representation"),
        ("hex_math", "Hex Arithmetic and Logic"),
        ("hex_practice", "Practice Hex Conversion and Debug Reading"),
        ("hex_dump_analysis", "Read and Interpret a Hex Dump"),
        ("hex_in_assembly", "How Hex is Used in Assembly Instructions"),
        ("endianness", "Big-Endian vs Little-Endian Representation"),
        ("hex_editor", "Modify Bytes Using a Hex Editor (Simulated)"),
        ("hex_bytecode", "View and Understand Machine Code in Hex"),
        ("hex_instruction_map", "Map Hex Values to CPU Instructions (Opcodes)"),
        ("hex_float", "Interpret Floating-Point Numbers in Hex (IEEE 754)"),
        ("hex_checksum", "Simple Checksum Calculation with Hex"),
        ("hex_debugging", "Use Hex to Debug Memory and Stack"),
        ("hex_quiz", "Challenge: Decode the Message in Hex!"),
        # ascii_utf
        ("ascii_basics", "ASCII Encoding"),
        ("utf8_intro", "Intro to UTF-8"),
        ("ascii_table", "Explore the ASCII Table (Control + Printable)"),
        ("unicode_basics", "Basics of Unicode Encoding"),
        ("utf8_encoding", "How UTF-8 Encodes Multi-byte Characters"),
        ("char_encoding_diff", "Differences: ASCII vs UTF-8 vs Unicode"),
        ("decode_utf8", "Manually Decode UTF-8 Byte Sequences"),
        ("encoding_practice", "Practice: Guess the Character from Bytes!"),
        ("ascii_control_codes", "Understand ASCII Control Characters (e.g., LF, CR, BEL)"),
        ("utf8_errors", "How Invalid UTF-8 Sequences Cause Errors"),
        ("utf8_glyphs", "Visualize Multibyte Characters and Emojis in UTF-8"),
        ("unicode_planes", "Explore Unicode Planes (BMP, SMP, SIP, etc.)"),
        ("bom_markers", "What is a Byte Order Mark (BOM) and Why It Matters"),
        ("file_encoding_mismatch", "Diagnose and Fix Encoding Mismatches in Files"),
        ("char_width", "Fixed-Width vs Variable-Width Encodings"),
        ("ascii_art", "Make ASCII Art and Understand Printable Limits"),
        ("terminal_encoding", "How Terminals Interpret UTF-8 Output"),
        ("encoding_quiz", "Challenge: Name the Encoded Character!")
        
    ],
    "digital_world": [
        ("image_as_bytes", "What Does an Image Look Like in Hex and Binary?"),
        ("text_file_hex", "Explore a Text File in ASCII and UTF-8"),
        ("file_signatures", "Identify File Types by Magic Bytes (PNG, PDF, ELF)"),
        ("network_packets", "See How Data is Sent in Binary over the Network"),
        ("html_in_ascii", "What HTML Code Looks Like in ASCII Encoding"),
        ("json_encoding", "How JSON Data is Stored and Encoded"),
        ("emoji_bytes", "See the Bytes Behind Emojis in UTF-8"),
        ("exe_peek", "Explore a Linux Binary (ELF) in Hex"),
        ("memory_layout_view", "Peek into Process Memory in Hex and ASCII"),
        ("binary_vs_visual", "Compare Binary Code to Visual Output Side-by-Side"),
        ("music_bytes", "What an MP3 or WAV File Looks Like in Hex"),
        ("video_stream", "How Video Streams Look at the Byte Level"),
        ("qr_code_data", "Decode a QR Code to Binary and Text"),
        ("wifi_packet", "Peek into a Raw Wi-Fi Packet's Hex Structure"),
        ("password_hashes", "What Do Hashed Passwords Look Like in Hex?"),
        ("compression_formats", "ZIP and GZIP: How Compression Affects Bytes"),
        ("utf8_file_mess", "Broken UTF-8 in Editors: Encoding Failures Explained"),
        ("keyboard_input", "What Happens Digitally When You Type a Key"),
        ("url_encoding", "See How URLs are Encoded for the Web (Percent-Encoding)"),
        ("websocket_bytes", "Explore WebSocket Frames in Raw Hex/Binary"),
        ("pdf_file_bytes", "Inspect a PDF's Structure and Encoding"),
        ("dns_query", "View a DNS Request in Raw Hex"),
        ("tcp_three_way", "Visualize a TCP Handshake in Binary"),
        ("tcp_flags_bits", "See Binary Flags Set in TCP Packets"),
        ("jpeg_headers", "Explore JPEG Structure via Magic Bytes"),
        ("csv_vs_json", "Compare CSV and JSON at the Byte Level"),
        ("cli_utf8_output", "Analyze UTF-8 Output from a Terminal Program"),
        ("ip_packet_bytes", "Dissect an IPv4 Packet's Header in Hex"),
        ("docker_image_fs", "What a Docker Layer Looks Like in Hex"),
        ("env_variables", "Explore Environment Variables in Raw Memory"),
        ("malware_signature", "How Malware is Identified by Hex Signatures"),
        ("font_file_hex", "Peek Inside a TTF or OTF Font File"),
        ("bash_script_ascii", "Inspect a Bash Script's Text and Encoding"),
        ("log_file_encoding", "Understand Encoding Differences in Log Files"),
        ("web_request_headers", "Analyze HTTP Headers in ASCII and Hex"),
        ("tls_handshake", "TLS Handshake Messages in Binary Form")        
    ]
}

CATEGORY_TITLES = {
    "intro": "🧑‍💻 Introduction",
    "intermediate": "⚙️ Intermediate",
    "advanced": "🚀 Advanced",
    "practice": "🚀 Practice Time",
    "number_system": "🧮 See the Matrix: Digital World in Numbers",
    "digital_world": "🔍 See how binary, hex, ASCII, and UTF-8 shape our everyday digital experience"
}

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def choose(prompt, options, include_back=False):
    while True:
        print(f"\n{C.BOLD}{prompt}{C.RESET}")
        for i, option in enumerate(options, 1):
            print(f"  {C.CYAN}{i}.{C.RESET} {option}")
        if include_back:
            print(f"  {C.CYAN}0.{C.RESET} Back")
        else:
            print(f"  {C.CYAN}0.{C.RESET} Exit")
        choice = input(f"{C.YELLOW}> {C.RESET}")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return None
            elif 1 <= choice <= len(options):
                return options[choice - 1]
        print(f"{C.RED}❌ Invalid selection. Try again.{C.RESET}")

def main():
    print(f"{C.HEADER}{C.BOLD}👋 Welcome to x86-64 Assembly Tutor!{C.RESET}\n")
    time.sleep(0.5)

    try:
        while True:  # Category menu
            try:
                categories = list(LESSON_STRUCTURE.keys())
                display_titles = [CATEGORY_TITLES.get(c, c.title()) for c in categories]
                category_choice = choose("📁 Choose a category:", display_titles)
                if not category_choice:
                    break

                category_key = next(key for key in categories if CATEGORY_TITLES.get(key, key.title()) == category_choice)
                category_data = LESSON_STRUCTURE[category_key]

                if isinstance(category_data, dict):  # Has subcategories
                    while True:  # Subcategory menu
                        try:
                            subcategories = list(category_data.keys())
                            sub_display = [sub.title() for sub in subcategories]
                            sub_choice = choose(f"📂 Choose a subcategory in '{CATEGORY_TITLES.get(category_key, category_key)}':", sub_display, include_back=True)
                            if not sub_choice:
                                break

                            sub_key = subcategories[sub_display.index(sub_choice)]
                            lessons = category_data[sub_key]

                            while True:  # Lesson menu
                                try:
                                    lesson_titles = [title for _, title in lessons]
                                    lesson_choice = choose("📚 Choose a lesson:", lesson_titles, include_back=True)
                                    if not lesson_choice:
                                        break

                                    lesson_internal = next(internal for internal, title in lessons if title == lesson_choice)

                                    try:
                                        # saide
                                        module = importlib.import_module(f"lessons.{category_key}.{lesson_internal}")
                                        if hasattr(module, "run"):
                                            print(f"\n{C.GREEN}▶️ Running lesson: {C.BOLD}{lesson_choice}{C.RESET}\n")
                                            time.sleep(0.5)
                                            try:
                                                module.run()
                                            except KeyboardInterrupt:
                                                print(f"\n{C.YELLOW}⏪ Interrupted. Returning to lesson list...{C.RESET}")
                                                continue
                                        else:
                                            print(f"{C.RED}⚠️ Lesson has no 'run()' function.{C.RESET}")
                                    except Exception as e:
                                        print(f"{C.RED}💥 Error loading lesson: {e}{C.RESET}")
                                except KeyboardInterrupt:
                                    print(f"\n{C.YELLOW}⏪ Interrupted. Returning to subcategory menu...{C.RESET}")
                                    break
                        except KeyboardInterrupt:
                            print(f"\n{C.YELLOW}⏪ Interrupted. Returning to category menu...{C.RESET}")
                            break
                else:  # Flat category
                    lessons = category_data

                    while True:
                        try:
                            lesson_titles = [title for _, title in lessons]
                            lesson_choice = choose("📚 Choose a lesson:", lesson_titles, include_back=True)
                            if not lesson_choice:
                                break

                            lesson_internal = next(internal for internal, title in lessons if title == lesson_choice)

                            try:
                                module = importlib.import_module(f"lessons.{category_key}.{lesson_internal}")
                                if hasattr(module, "run"):
                                    print(f"\n{C.GREEN}▶️ Running lesson: {C.BOLD}{lesson_choice}{C.RESET}\n")
                                    time.sleep(0.5)
                                    try:
                                        module.run()
                                    except KeyboardInterrupt:
                                        print(f"\n{C.YELLOW}⏪ Interrupted. Returning to lesson list...{C.RESET}")
                                        continue
                                else:
                                    print(f"{C.RED}⚠️ Lesson has no 'run()' function.{C.RESET}")
                            except Exception as e:
                                print(f"{C.RED}💥 Error loading lesson: {e}{C.RESET}")
                        except KeyboardInterrupt:
                            print(f"\n{C.YELLOW}⏪ Interrupted. Returning to category menu...{C.RESET}")
                            break
            except KeyboardInterrupt:
                print(f"\n{C.YELLOW}⏪ Interrupted. Staying in main menu...{C.RESET}")
                continue
    except KeyboardInterrupt:
        print(f"\n{C.YELLOW}🚪 Exiting gracefully. Press again to force quit.{C.RESET}")
        return

    print(f"\n{C.BLUE}{C.BOLD}👋 Goodbye! Keep hacking!{C.RESET}\n")

if __name__ == "__main__":
    main()
