from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="steganography-tool",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for hiding text in images and emojis with encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/steganography-tool",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Pillow>=9.0.0",
        "cryptography>=38.0.0",
    ],
    entry_points={
        "console_scripts": [
            "stego-tool=main:main",
        ],
    },
)
