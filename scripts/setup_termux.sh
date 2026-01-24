#!/data/data/com.termux/files/usr/bin/bash
# Termux setup script

echo "📱 Setting up Steganography Tool for Termux..."

# Update packages
pkg update -y && pkg upgrade -y

# Install Python and dependencies
pkg install python -y
pkg install git -y

# Install Python packages
pip install --upgrade pip
pip install pillow cryptography

echo ""
echo "✅ Termux setup complete!"
echo ""
echo "Usage:"
echo "1. Clone repository: git clone https://github.com/abhiexploits/Steganography"
echo "2. cd steganography-tool"
echo "3. python main.py"
