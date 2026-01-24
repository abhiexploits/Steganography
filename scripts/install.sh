#!/bin/bash
# Installation script for Steganography Tool

echo "🔧 Installing Steganography Tool..."

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install python3 python3-pip -y
    else
        echo "Please install Python3 manually"
        exit 1
    fi
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# Make scripts executable
chmod +x main.py

echo ""
echo "✅ Installation complete!"
echo ""
echo "To use the tool:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run: python main.py"
echo ""
echo "Or use directly: ./main.py"
