# Installation Guide

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning repository)

## 🖥️ Linux Installation

### Method 1: Using pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/steganography-tool.git
cd steganography-tool

# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3-pil python3-cryptography -y

# Install using pip
pip install -r requirements.txt
