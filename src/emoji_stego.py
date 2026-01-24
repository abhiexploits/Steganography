"""
Emoji Steganography Module
Convert text to emojis and back
"""

import binascii

class EmojiSteganography:
    def __init__(self):
        # Emoji mapping - 16 emojis for 4-bit combinations
        self.emoji_map = {
            '0000': '😀', '0001': '😂', '0010': '🥰', '0011': '😎',
            '0100': '🤖', '0101': '👻', '0110': '👽', '0111': '🤠',
            '1000': '🧐', '1001': '🤩', '1010': '🥳', '1011': '😏',
            '1100': '😴', '1101': '🤢', '1110': '🤯', '1111': '🥶'
        }
        
        # Reverse mapping for decoding
        self.reverse_map = {v: k for k, v in self.emoji_map.items()}
        
        # Delimiter emoji
        self.delimiter = '🔒'
    
    def encode(self, text):
        """
        Encode text to emojis
        
        Args:
            text: Text to encode
            
        Returns:
            Emoji string
        """
        # Convert text to binary
        binary = self._text_to_binary(text)
        
        # Pad binary to make length multiple of 4
        while len(binary) % 4 != 0:
            binary += '0'
        
        # Convert to emojis
        emojis = ''
        for i in range(0, len(binary), 4):
            nibble = binary[i:i+4]
            emojis += self.emoji_map.get(nibble, '❓')
        
        # Add delimiter
        emojis += self.delimiter
        
        return emojis
    
    def decode(self, emoji_text):
        """
        Decode emojis to text
        
        Args:
            emoji_text: Emoji string
            
        Returns:
            Decoded text
        """
        # Remove delimiter if present
        if self.delimiter in emoji_text:
            emoji_text = emoji_text.split(self.delimiter)[0]
        
        # Convert emojis to binary
        binary = ''
        for emoji in emoji_text:
            if emoji in self.reverse_map:
                binary += self.reverse_map[emoji]
            else:
                # Skip invalid emojis
                continue
        
        # Convert binary to text
        return self._binary_to_text(binary)
    
    def _text_to_binary(self, text):
        """Convert text to binary string"""
        # First convert to bytes
        byte_data = text.encode('utf-8')
        # Then to binary string
        binary = ''.join(format(byte, '08b') for byte in byte_data)
        return binary
    
    def _binary_to_text(self, binary):
        """Convert binary string to text"""
        # Make sure binary length is multiple of 8
        binary = binary[:len(binary) - (len(binary) % 8)]
        
        # Convert to bytes
        byte_array = bytearray()
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                byte_array.append(int(byte, 2))
        
        # Convert to text
        try:
            return byte_array.decode('utf-8')
        except:
            # Try with error handling
            return byte_array.decode('utf-8', errors='ignore')
