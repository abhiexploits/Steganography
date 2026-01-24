"""
Utility Functions
"""

import os
import sys

def color_print(text, color="white", style="normal"):
    """
    Print colored text to terminal
    
    Args:
        text: Text to print
        color: Text color
        style: Text style
    """
    colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        'reset': '0'
    }
    
    styles = {
        'normal': '0',
        'bold': '1',
        'dim': '2',
        'italic': '3',
        'underline': '4'
    }
    
    color_code = colors.get(color.lower(), '37')
    style_code = styles.get(style.lower(), '0')
    
    print(f"\033[{style_code};{color_code}m{text}\033[0m")

def get_input_path(prompt):
    """
    Get input file path with auto-completion
    
    Args:
        prompt: Input prompt
        
    Returns:
        File path
    """
    path = input(prompt).strip()
    
    # Handle tilde expansion
    if path.startswith('~'):
        path = os.path.expanduser(path)
    
    # Handle relative paths
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    
    return path

def get_output_path(prompt, default):
    """
    Get output file path
    
    Args:
        prompt: Input prompt
        default: Default filename
        
    Returns:
        File path
    """
    path = input(prompt).strip()
    
    if not path:
        path = default
    
    # Handle tilde expansion
    if path.startswith('~'):
        path = os.path.expanduser(path)
    
    # Handle relative paths
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    
    # Create directory if it doesn't exist
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    return path

def check_requirements():
    """Check if all requirements are installed"""
    try:
        from PIL import Image
        from cryptography.fernet import Fernet
        return True
    except ImportError as e:
        return False

def get_terminal_size():
    """Get terminal width"""
    try:
        return os.get_terminal_size().columns
    except:
        return 80
