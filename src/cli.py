"""
Command Line Interface Parser
Handles command line arguments for the tool
"""

import argparse

def parse_arguments():
    """
    Parse command line arguments
    
    Returns:
        Parsed arguments object
    """
    parser = argparse.ArgumentParser(
        description='Steganography Tool - Hide secrets in images and emojis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Encode text in image:
    python main.py -m image -a encode -i input.jpg -o output.png -t "secret" -p password
  
  Decode text from image:
    python main.py -m image -a decode -i output.png -p password
  
  Encode text to emojis:
    python main.py -m emoji -a encode -t "hello" -p password
  
  Decode emojis to text:
    python main.py -m emoji -a decode -t "😀😂🥰" -p password
  
Interactive Mode:
  Run without arguments: python main.py
        """
    )
    
    # Main arguments
    parser.add_argument('-m', '--mode', 
                       choices=['image', 'emoji'],
                       help='Steganography mode: image or emoji')
    
    parser.add_argument('-a', '--action', 
                       choices=['encode', 'decode'],
                       help='Action: encode or decode')
    
    # Image mode arguments
    parser.add_argument('-i', '--input',
                       help='Input image path (for image mode)')
    
    parser.add_argument('-o', '--output',
                       help='Output image path (for image encode)')
    
    # Text arguments
    parser.add_argument('-t', '--text',
                       help='Text to encode or decode')
    
    # Security arguments
    parser.add_argument('-p', '--password',
                       help='Password for encryption/decryption')
    
    # Optional arguments
    parser.add_argument('-v', '--verbose', 
                       action='store_true',
                       help='Verbose output')
    
    parser.add_argument('--version', 
                       action='version',
                       version='Steganography Tool v1.0.0')
    
    return parser.parse_args()

def validate_arguments(args):
    """
    Validate command line arguments
    
    Args:
        args: Parsed arguments object
    
    Returns:
        bool: True if valid, False otherwise
    """
    if args.mode == 'image':
        if args.action == 'encode':
            required = [args.input, args.output, args.text, args.password]
            if not all(required):
                print("Error: For image encode, all of these are required:")
                print("  --input, --output, --text, --password")
                return False
        elif args.action == 'decode':
            if not all([args.input, args.password]):
                print("Error: For image decode, --input and --password are required")
                return False
    
    elif args.mode == 'emoji':
        if not all([args.text, args.password]):
            print("Error: For emoji mode, --text and --password are required")
            return False
    
    return True
