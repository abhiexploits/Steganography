"""
Main Steganography Tool Class
AUTHOR :- ABHISHEK 
"""

from .image_stego import ImageSteganography
from .emoji_stego import EmojiSteganography
from .crypto import Cryptographer
from .utils import color_print, get_input_path, get_output_path
import os

class SteganographyTool:
    def __init__(self):
        self.image_stego = ImageSteganography()
        self.emoji_stego = EmojiSteganography()
        self.crypto = Cryptographer()
        
    def encode_image(self, input_path, output_path, text, password):
        """Encode text into image"""
        # Encrypt the text
        encrypted_text = self.crypto.encrypt(text, password)
        
        # Encode into image
        self.image_stego.encode(input_path, output_path, encrypted_text)
        
    def decode_image(self, image_path, password):
        """Decode text from image"""
        # Decode from image
        encrypted_text = self.image_stego.decode(image_path)
        
        # Decrypt the text
        return self.crypto.decrypt(encrypted_text, password)
    
    def encode_emoji(self, text, password):
        """Encode text to emojis"""
        # Encrypt the text
        encrypted_text = self.crypto.encrypt(text, password)
        
        # Convert to emojis
        return self.emoji_stego.encode(encrypted_text)
    
    def decode_emoji(self, emoji_text, password):
        """Decode emojis to text"""
        # Convert from emojis
        encrypted_text = self.emoji_stego.decode(emoji_text)
        
        # Decrypt the text
        return self.crypto.decrypt(encrypted_text, password)
    
    def interactive_mode(self):
        """Run in interactive menu mode"""
        color_print("=" * 50, "cyan")
        color_print("🔐 STEGANOGRAPHY TOOL", "yellow", "bold")
        color_print("=" * 50, "cyan")
        
        while True:
            print("\n📋 Main Menu:")
            print("1. 📸 Image Steganography")
            print("2. 😊 Emoji Steganography")
            print("3. ℹ️  Help / Instructions")
            print("4. 🚪 Exit")
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == '1':
                self._image_menu()
            elif choice == '2':
                self._emoji_menu()
            elif choice == '3':
                self._show_help()
            elif choice == '4':
                color_print("\n👋 Goodbye!", "green")
                break
            else:
                color_print("Invalid option! Try again.", "red")
    
    def _image_menu(self):
        """Image steganography submenu"""
        while True:
            print("\n📸 Image Steganography:")
            print("1. Encode text into image")
            print("2. Decode text from image")
            print("3. Back to main menu")
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == '1':
                self._encode_image_interactive()
            elif choice == '2':
                self._decode_image_interactive()
            elif choice == '3':
                break
            else:
                color_print("Invalid option!", "red")
    
    def _encode_image_interactive(self):
        """Interactive image encoding"""
        try:
            color_print("\n📥 Image Encoding", "blue")
            
            # Get input image path
            input_path = get_input_path("Enter input image path: ")
            if not os.path.exists(input_path):
                color_print("File not found!", "red")
                return
            
            # Get output path
            output_path = get_output_path("Enter output image path (default: encoded.png): ", 
                                         "encoded.png")
            
            # Get secret text
            text = input("Enter secret text to hide: ").strip()
            if not text:
                color_print("Text cannot be empty!", "red")
                return
            
            # Get password
            password = input("Enter encryption password: ").strip()
            if not password:
                color_print("Password cannot be empty!", "red")
                return
            
            # Confirm password
            confirm = input("Confirm password: ").strip()
            if password != confirm:
                color_print("Passwords don't match!", "red")
                return
            
            # Encode
            color_print("\n⏳ Encoding message into image...", "yellow")
            self.encode_image(input_path, output_path, text, password)
            color_print(f"✅ Success! Image saved as: {output_path}", "green")
            
        except Exception as e:
            color_print(f"Error: {str(e)}", "red")
    
    def _decode_image_interactive(self):
        """Interactive image decoding"""
        try:
            color_print("\n📤 Image Decoding", "blue")
            
            # Get image path
            image_path = get_input_path("Enter encoded image path: ")
            if not os.path.exists(image_path):
                color_print("File not found!", "red")
                return
            
            # Get password
            password = input("Enter decryption password: ").strip()
            if not password:
                color_print("Password cannot be empty!", "red")
                return
            
            # Decode
            color_print("\n⏳ Decoding message from image...", "yellow")
            text = self.decode_image(image_path, password)
            color_print(f"✅ Decoded message: {text}", "green")
            
        except Exception as e:
            color_print(f"Error: {str(e)}", "red")
    
    def _emoji_menu(self):
        """Emoji steganography submenu"""
        while True:
            print("\n😊 Emoji Steganography:")
            print("1. Encode text to emojis")
            print("2. Decode emojis to text")
            print("3. Back to main menu")
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == '1':
                self._encode_emoji_interactive()
            elif choice == '2':
                self._decode_emoji_interactive()
            elif choice == '3':
                break
            else:
                color_print("Invalid option!", "red")
    
    def _encode_emoji_interactive(self):
        """Interactive emoji encoding"""
        try:
            color_print("\n📥 Emoji Encoding", "blue")
            
            # Get text
            text = input("Enter text to encode: ").strip()
            if not text:
                color_print("Text cannot be empty!", "red")
                return
            
            # Get password
            password = input("Enter encryption password: ").strip()
            if not password:
                color_print("Password cannot be empty!", "red")
                return
            
            # Confirm password
            confirm = input("Confirm password: ").strip()
            if password != confirm:
                color_print("Passwords don't match!", "red")
                return
            
            # Encode
            color_print("\n⏳ Encoding text to emojis...", "yellow")
            emojis = self.encode_emoji(text, password)
            color_print(f"✅ Encoded emojis: {emojis}", "green")
            
        except Exception as e:
            color_print(f"Error: {str(e)}", "red")
    
    def _decode_emoji_interactive(self):
        """Interactive emoji decoding"""
        try:
            color_print("\n📤 Emoji Decoding", "blue")
            
            # Get emojis
            emojis = input("Enter emojis to decode: ").strip()
            if not emojis:
                color_print("Emojis cannot be empty!", "red")
                return
            
            # Get password
            password = input("Enter decryption password: ").strip()
            if not password:
                color_print("Password cannot be empty!", "red")
                return
            
            # Decode
            color_print("\n⏳ Decoding emojis to text...", "yellow")
            text = self.decode_emoji(emojis, password)
            color_print(f"✅ Decoded text: {text}", "green")
            
        except Exception as e:
            color_print(f"Error: {str(e)}", "red")
    
    def _show_help(self):
        """Display help information"""
        color_print("\n📖 Help & Instructions", "cyan")
        print("=" * 40)
        print("\nImage Steganography:")
        print("- Hides text in images using LSB (Least Significant Bit) method")
        print("- Supports PNG, JPG, BMP formats")
        print("- Output is always PNG for better quality")
        
        print("\nEmoji Steganography:")
        print("- Converts text to sequence of emojis")
        print("- Each 2 bits of data = 1 emoji")
        print("- Emojis can be shared anywhere")
        
        print("\nSecurity Features:")
        print("- AES-256 encryption with password")
        print("- Salted password hashing (PBKDF2)")
        print("- No plain text storage")
        
        print("\nExample Commands:")
        print("  python main.py -m image -a encode -i pic.jpg -o secret.png")
        print("  python main.py -m emoji -a encode -t 'hello' -p mypass")
        
        input("\nPress Enter to continue...")
