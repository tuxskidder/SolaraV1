import base64
import os
import sys

def print_rainbow_text(text):
    """Print text with ANSI color codes for rainbow effect"""
    # ANSI color codes
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    reset = '\033[0m'
    
    rainbow_text = ""
    color_index = 0
    for char in text:
        if char != ' ' and char != '\n':
            rainbow_text += colors[color_index % len(colors)] + char + reset
            color_index += 1
        else:
            rainbow_text += char
    print(rainbow_text)

def print_title():
    """Print the main title in rainbow colors"""
    title = """
    ███████╗    ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
    ██╔════╝    ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
    █████╗      ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ 
    ██╔══╝      ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  
    ██║         ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   
    ╚═╝         ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   
                                                                      
    ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██████╗ 
    ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
    █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   █████╗  ██████╔╝
    ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██╗
    ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ███████╗██║  ██║
    ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝
    
                                    by Tux
    """
    print_rainbow_text(title)

def caesar_cipher(text, shift=13):
    """Apply Caesar cipher encryption"""
    encrypted = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted += char
    return encrypted

def base64_encode(text):
    """Encode text using Base64"""
    try:
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')
    except:
        return "Error encoding"

def xor_encrypt(text, key="FSOCIETY"):
    """Apply XOR encryption with repeating key"""
    encrypted = ""
    key_len = len(key)
    for i, char in enumerate(text):
        encrypted += chr(ord(char) ^ ord(key[i % key_len]))
    return encrypted

def hex_encode(text):
    """Convert text to hexadecimal"""
    try:
        return text.encode('utf-8').hex()
    except:
        return "Error encoding"

def clear_screen():
    """Clear the screen"""
    try:
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/Mac
            os.system('clear')
    except:
        print('\n' * 50)  # Fallback - print many newlines

def main():
    clear_screen()
    
    print_title()
    print()
    print_rainbow_text("=" * 80)
    print()
    print_rainbow_text("Welcome to F Society Encrypter!")
    print_rainbow_text("Protect your messages with multiple encryption methods.")
    print()
    print_rainbow_text("=" * 80)
    print()
    
    while True:
        try:
            # Get text to encrypt
            print_rainbow_text("What text do you want to encrypt/protect?")
            print("\033[97mEnter your message: \033[0m", end="")
            user_text = input()
            
            if user_text.lower() in ['quit', 'exit', 'q']:
                print_rainbow_text("Goodbye, hacktivist!")
                break
            
            if not user_text.strip():
                print_rainbow_text("Please enter some text to encrypt.")
                continue
            
            print()
            print_rainbow_text("=" * 60)
            print_rainbow_text("ENCRYPTION RESULTS:")
            print_rainbow_text("=" * 60)
            print()
            
            # Apply different encryption methods
            # Method 1: Caesar Cipher (ROT13)
            caesar_result = caesar_cipher(user_text, 13)
            print_rainbow_text("🔐 Caesar Cipher (ROT13):")
            print("\033[96m" + caesar_result + "\033[0m")
            print()
            
            # Method 2: Base64 Encoding
            b64_result = base64_encode(user_text)
            print_rainbow_text("🔐 Base64 Encoding:")
            print("\033[93m" + b64_result + "\033[0m")
            print()
            
            # Method 3: XOR Encryption
            xor_result = xor_encrypt(user_text)
            xor_hex = hex_encode(xor_result)
            print_rainbow_text("🔐 XOR Encryption (Hex):")
            print("\033[92m" + xor_hex + "\033[0m")
            print()
            
            # Method 4: Hexadecimal
            hex_result = hex_encode(user_text)
            print_rainbow_text("🔐 Hexadecimal Encoding:")
            print("\033[95m" + hex_result + "\033[0m")
            print()
            
            # Method 5: Combined encryption
            combined = base64_encode(caesar_cipher(user_text, 7))
            print_rainbow_text("🔐 Combined (Caesar + Base64):")
            print("\033[91m" + combined + "\033[0m")
            
            print()
            print_rainbow_text("=" * 60)
            print()
            print_rainbow_text("Enter another message or type 'quit' to exit.")
            print()
            
        except KeyboardInterrupt:
            print()
            print_rainbow_text("Operation terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Press Enter to continue...")
            input()

if __name__ == "__main__":
    main()
