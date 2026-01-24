"""
Encryption/Decryption Module
AES-256 encryption with password
"""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

class Cryptographer:
    def __init__(self, salt=None):
        """
        Initialize cryptographer
        
        Args:
            salt: Optional salt for key derivation (default: random)
        """
        self.salt = salt or os.urandom(16)
    
    def encrypt(self, text, password):
        """
        Encrypt text with password
        
        Args:
            text: Text to encrypt
            password: Encryption password
            
        Returns:
            Encrypted text (base64 encoded)
        """
        # Derive key from password
        key = self._derive_key(password)
        
        # Create Fernet cipher
        cipher = Fernet(key)
        
        # Encrypt text
        encrypted = cipher.encrypt(text.encode())
        
        # Return as base64 string
        return base64.urlsafe_b64encode(self.salt + encrypted).decode()
    
    def decrypt(self, encrypted_text, password):
        """
        Decrypt text with password
        
        Args:
            encrypted_text: Encrypted text (base64 encoded)
            password: Decryption password
            
        Returns:
            Decrypted text
            
        Raises:
            ValueError: If password is incorrect
        """
        # Decode base64
        data = base64.urlsafe_b64decode(encrypted_text.encode())
        
        # Extract salt and encrypted data
        salt = data[:16]
        encrypted = data[16:]
        
        # Derive key from password with same salt
        key = self._derive_key(password, salt)
        
        try:
            # Create Fernet cipher and decrypt
            cipher = Fernet(key)
            decrypted = cipher.decrypt(encrypted)
            return decrypted.decode()
        except:
            raise ValueError("Incorrect password or corrupted data!")
    
    def _derive_key(self, password, salt=None):
        """
        Derive encryption key from password
        
        Args:
            password: The password
            salt: Salt for key derivation
            
        Returns:
            Encryption key (base64 encoded)
        """
        salt = salt or self.salt
        
        # Use PBKDF2 for key derivation
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        
        # Derive key
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
