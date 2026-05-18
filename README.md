# PRODIGY Cyber Security Internship

# PRODIGY_CS_02
## Pixel Manipulation for Image Encryption

### Task 02 – Pixel-Based Image Encryption


## Description
This project is a basic image encryption and decryption tool developed using Python and the Pillow library. The program works by manipulating image pixel values to encrypt and decrypt images.

## Concept
Each pixel’s RGB (Red, Green, Blue) values are modified using mathematical operations.

Encryption:
(R + key, G + key, B + key)

Decryption:
(R - key, G - key, B - key)

The modulo operation ensures pixel values remain within the valid range of 0–255.

## Features
- Image encryption using pixel manipulation
- Image decryption support
- Command line interface
- Uses Python Pillow library

## Requirements
Install Pillow library before running the program:

```bash
pip install pillow
```


## How to Use
Add the image file inside the project folder
Run the program:
```Bash
python image_encryptor.py
```
Choose:
'e' for encryption
'd' for decryption
Enter:
image file name
encryption key
Output Files
Encrypted image: encrypted_image.png
Decrypted image: decrypted_image.png

## Technologies Used
Python
Pillow Library

## Author
Manpreet Kaur Cyber Security Intern @ Prodigy InfoTech
