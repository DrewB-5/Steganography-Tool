# LSB Steganography Tool with Fernet Encryption

A Python-based steganography tool that hides encrypted messages inside images using the **Least Significant Bit (LSB)** method.  
Supports both encoding (hiding) and decoding (retrieving) messages from PNG images.  

---

## Features
- **Encryption**: Messages are encrypted using `cryptography.Fernet` before being hidden.
- **LSB Steganography**: Data is embedded into the least significant bits of pixel values.
- **Delimiter-Based Extraction**: Reliable message retrieval using a bit-sequence delimiter.
- **Lossless Image Format Support**: Works with PNG/BMP to preserve hidden data.
- **Modular Structure**: Separated into utility modules for easy maintenance.

---

## Tech Stack
- **Python** 3.x
- **Pillow** – Image manipulation
- **cryptography** – Encryption/Decryption
- **argparse** – Command-line interface (built-in)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DrewB-5/Steganography-Tool.git
   cd steganography-tool
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt

---

## Usage
- Work in progress

---

## Project Structure
   ```pgsql
   steganograpy_tool/
   │
   ├── encode.py               # CLI script for embedding messages
   ├── decode.py               # CLI script for extracting messages
   ├── utils/
   │   ├── bit_utils.py        # Text↔Bits conversion, delimiter handling
   │   ├── image_utils.py      # Pixel-level LSB encoding/decoding
   |
   ├── encoded_image.png       # Example encoded image
   ├── test_image.png          # Example test image
   |
   ├── fernet_keygen.py        # Encyption key generator
   ├── example_key.txt         # Example key
   |
   ├── requirements.txt        # Dependencies list
   └── README.md               # Project documentation

---

## Limitations
- Only works reliably with lossless formats (PNG, BMP).
- The image must have enough pixels to store the message.
