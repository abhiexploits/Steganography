##  Steganography Tool - Hide Secrets in Images & Emojis

A powerful Python tool to hide secret messages in images and convert text to emoji sequences with military-grade encryption. Perfect for privacy enthusiasts, cybersecurity students, and anyone who loves digital mysteries!

GitHub Repository: https://github.com/abhiexploits/Steganography

---

##  Features

### ·  Image Steganography - Hide text in PNG/JPG images using LSB method
### ·  Emoji Steganography - Convert text to emoji sequences and back
### ·  AES-256 Encryption - Password protect your secrets
### ·  Image Preservation - Maintain original image quality
### ·  Custom Paths - Full control over input/output files
### ·  Cross-Platform - Works on Termux & Linux
### ·  Interactive Menu - Easy-to-use interface
### ·  CLI Support - Command-line automation

---

# Quick Start

### Termux (Android) Installation

```bash
# Update packages
pkg update && pkg upgrade

# Install Python and Git
pkg install python git

# Clone the repository
git clone https://github.com/abhiexploits/Steganography.git

# Enter directory
cd Steganography

# Install dependencies
pip install pillow cryptography

# Run the tool
python main.py
```

### Linux Installation

```bash
# Clone repository
git clone https://github.com/abhiexploits/Steganography.git
cd Steganography

# Install dependencies
pip install pillow cryptography

# Or use system packages (Ubuntu/Debian)
sudo apt-get install python3-pil python3-cryptography

# Run the tool
python main.py
```

---

###  Usage Examples

 Interactive Mode (Easy)

```bash
python main.py
```

Then follow the on-screen menus to encode/decode messages!

###  Command Line Mode (Fast)

1. Hide Text in Image

```bash
python main.py -m image -a encode \
  -i input.jpg \
  -o secret.png \
  -t "This is my secret message" \
  -p mypassword123
```

2. Extract Text from Image

```bash
python main.py -m image -a decode \
  -i secret.png \
  -p mypassword123
```

3. Convert Text to Emojis

```bash
python main.py -m emoji -a encode \
  -t "Hello World!" \
  -p mypassword123
```

Output: 😀😂🥰😎🤖👻👽🤠🧐🤩🥳😏😴🤢🤯🥶

4. Convert Emojis to Text

```bash
python main.py -m emoji -a decode \
  -t "😀😂🥰😎🤖👻" \
  -p mypassword123
```

---

### 🎯 Advanced Usage

Batch Processing

Create a script for multiple files:

```bash
#!/bin/bash
# encode_secrets.sh
for file in images/*.jpg; do
    python main.py -m image -a encode \
        -i "$file" \
        -o "secrets/$(basename "$file" .jpg)_secret.png" \
        -t "Secret for $(basename "$file")" \
        -p mypassword
done
```

Use in Python Scripts

```python
from src.steganography import SteganographyTool

tool = SteganographyTool()

# Hide message in image
tool.encode_image("input.jpg", "output.png", "My secret", "password123")

# Extract message
message = tool.decode_image("output.png", "password123")
print(f"Secret: {message}")

# Convert to emojis
emojis = tool.encode_emoji("Hidden text", "password456")
print(f"Emojis: {emojis}")
```

---

## Project Structure

```
Steganography/
├── main.py              # Main entry point
├── src/                 # Source code
│   ├── steganography.py    # Main tool class
│   ├── image_stego.py      # Image hiding functions
│   ├── emoji_stego.py      # Emoji conversion functions
│   ├── crypto.py          # Encryption functions
│   ├── utils.py           # Utility functions
│   └── cli.py            # Command line interface
├── examples/            # Example files
├── docs/               # Documentation
├── scripts/            # Installation scripts
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

---

# 🔧 Technical Details

How It Works

1. Image Steganography: Uses LSB (Least Significant Bit) method to hide data in image pixels
2. Emoji Steganography: Maps binary data to 16 different emojis
3. Encryption: AES-256 with PBKDF2 key derivation
4. Security: Salted passwords prevent rainbow table attacks

Supported Formats

· Images: PNG, JPG, BMP (output always PNG)
· Text: Any UTF-8 text
· Passwords: Any length (recommended: 8+ characters)

---

##  Contributing

Love this tool? Want to make it better? Contributions are welcome!

1. Fork the repository
2. Create a feature branch (git checkout -b feature/AmazingFeature)
3. Commit changes (git commit -m 'Add AmazingFeature')
4. Push to branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

Development Setup

```bash
git clone https://github.com/abhiexploits/Steganography.git
cd Steganography
pip install -r requirements.txt
# Run tests
python -m pytest tests/
```

---

##  FAQ

#### Q: Is this tool safe to use?

#### A: Yes! All encryption happens locally on your device. No data is sent to any server.

#### Q: Can I use this on Windows?

#### A: Yes, but it's primarily tested on Termux and Linux. Windows may need additional setup.

#### Q: What's the maximum text size for images?

#### A: Depends on image resolution. Formula: (width × height × 3) / 8 characters

#### Q: Can the hidden data be detected?

#### A: LSB steganography is visually undetectable but can be found with statistical analysis.

#### Q: What if I forget the password?

#### A: The data is irrecoverable. Always remember your passwords!

---

#  Performance Tips

1. Use PNG for output - Better quality than JPG
2. Large images for long messages - More pixels = more space
3. Strong passwords - Use mix of letters, numbers, symbols
4. Backup originals - Always keep original images safe

---

##  Example Workflow

Scenario: Send a secret birthday message

1. Encode your message:
   ```bash
   python main.py -m image -a encode \
     -i birthday_photo.jpg \
     -o birthday_secret.png \
     -t "The party is at 8 PM, location: 123 Main St" \
     -p birthday2024
   ```
2. Send the image to your friend via WhatsApp/Telegram
3. Friend decodes it:
   ```bash
   python main.py -m image -a decode \
     -i birthday_secret.png \
     -p birthday2024
   ```
4. Success! Secret message received without anyone knowing!

---

##  Disclaimer

This tool is for educational and legitimate privacy purposes only. Do not use it for:

· Hiding illegal content
· Bypassing security systems
· Harassment or cyberbullying
· Any unlawful activities

The developer is not responsible for misuse of this tool.

---

##  Support

Found a bug? Need help? Here's what to do:

1. Check existing issues: GitHub Issues
2. Create new issue: Describe your problem with details
3. Email: NHI DALNE KA MAN HE😂
4. Telegram: https://t.me/abhiexploits

---

##  Show Some Love

If this tool helped you:

·  Star the repository on GitHub
·  Fork it for your own projects
·  Share with friends
·  Contribute code improvements


##  Links

· GitHub: https://github.com/abhiexploits/Steganography
· Report Bug: https://github.com/abhiexploits/Steganography/issues
· Request Feature: https://github.com/abhiexploits/Steganography/issues

---

Made with ❤️ by AbhiExploits | Stay curious, stay secure!

---

Last Updated: January 2026 | Version: 1.0.0

---

##  Quick Copy-Paste Commands

For Termux Users:

```bash
# One-line installer
pkg install python git -y && git clone https://github.com/abhiexploits/Steganography.git && cd Steganography && pip install pillow cryptography && python main.py
```

For Quick Testing:

```bash
# Encode test message
python main.py -m emoji -a encode -t "Test Message" -p test123

# Decode test message
python main.py -m emoji -a decode -t "😀😂🥰😎🤖👻" -p test123
```

---

Pro Tip: Bookmark this page and star the GitHub repo to stay updated!
