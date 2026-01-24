"""
Image Steganography Module
Hide and extract text in images using LSB method
"""

from PIL import Image
import binascii

class ImageSteganography:
    def __init__(self):
        self.delimiter = "#####"  # Message delimiter
    
    def encode(self, image_path, output_path, text):
        """
        Encode text into image using LSB method
        
        Args:
            image_path: Path to input image
            output_path: Path to save encoded image
            text: Text to hide
        """
        # Add delimiter to mark end of message
        text += self.delimiter
        
        # Convert text to binary
        binary_text = self._text_to_binary(text)
        
        # Open image
        image = Image.open(image_path)
        pixels = image.load()
        
        width, height = image.size
        
        # Check if image can hold the message
        max_bits = width * height * 3
        if len(binary_text) > max_bits:
            raise ValueError(f"Image too small! Need {len(binary_text)} bits, has {max_bits} bits")
        
        # Encode message into pixels
        bit_index = 0
        for y in range(height):
            for x in range(width):
                if bit_index >= len(binary_text):
                    break
                    
                r, g, b = pixels[x, y][:3]
                
                # Encode in LSB of each color channel
                if bit_index < len(binary_text):
                    r = self._set_lsb(r, int(binary_text[bit_index]))
                    bit_index += 1
                
                if bit_index < len(binary_text):
                    g = self._set_lsb(g, int(binary_text[bit_index]))
                    bit_index += 1
                
                if bit_index < len(binary_text):
                    b = self._set_lsb(b, int(binary_text[bit_index]))
                    bit_index += 1
                
                # For PNG with alpha channel
                if len(pixels[x, y]) == 4:
                    pixels[x, y] = (r, g, b, pixels[x, y][3])
                else:
                    pixels[x, y] = (r, g, b)
        
        # Save as PNG (lossless)
        image.save(output_path, "PNG")
        image.close()
    
    def decode(self, image_path):
        """
        Decode text from image
        
        Args:
            image_path: Path to encoded image
            
        Returns:
            Decoded text
        """
        # Open image
        image = Image.open(image_path)
        pixels = image.load()
        
        width, height = image.size
        
        # Extract binary data
        binary_data = ""
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y][:3]
                
                # Extract LSB from each color channel
                binary_data += str(self._get_lsb(r))
                binary_data += str(self._get_lsb(g))
                binary_data += str(self._get_lsb(b))
        
        # Convert binary to text
        text = self._binary_to_text(binary_data)
        
        # Find delimiter
        if self.delimiter in text:
            text = text.split(self.delimiter)[0]
        
        image.close()
        return text
    
    def _text_to_binary(self, text):
        """Convert text to binary string"""
        binary = ''
        for char in text:
            # Convert character to 8-bit binary
            binary += format(ord(char), '08b')
        return binary
    
    def _binary_to_text(self, binary):
        """Convert binary string to text"""
        text = ''
        # Process 8 bits at a time
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                try:
                    text += chr(int(byte, 2))
                except:
                    break  # Stop at invalid byte
        return text
    
    def _set_lsb(self, value, bit):
        """Set LSB of a byte"""
        return (value & 0xFE) | bit
    
    def _get_lsb(self, value):
        """Get LSB of a byte"""
        return value & 1
