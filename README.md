
# Ransomeware

**Ransomeware** is a Python-based tool designed to simulate ransomware behavior by encrypting files within a target directory and displaying a humorous (yet alarming) message on the desktop. The tool uses `pyAesCrypt` for file encryption/decryption and the `Pillow` library to generate an image with a custom message. **Use responsibly and only for educational or authorized testing purposes.**

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Disclaimer & Legal Notice](#disclaimer--legal-notice)

---

## Features

- **File Encryption & Decryption:** Encrypts all files in the current working directory using a user-provided key, and decrypts them when given the correct key.
- **Humorous Warning Message:** Generates an image with a funny message and saves it to the desktop.
- **Command-Line Interface:** Simple input-driven process to control encryption and decryption.

---

## Requirements

- **Python 3.x**
- **Required Libraries:**
  - `pyAesCrypt`
  - `Pillow`
  - `os`, `sys`, `subprocess` (Standard Python libraries)

Make sure to install the necessary external libraries using `pip` if you haven't already.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ransomeware.git
   cd ransomeware
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install pyAesCrypt Pillow
   ```

---

## Usage

1. **Run the Script:**

   Execute the script using Python:

   ```bash
   python ransomeware.py
   ```

2. **Encryption:**
   - **Input the Key:** When prompted, enter an encryption key (a numeric value recommended by the script).
   - **Encrypt Files:** All files in the current working directory will be encrypted, and the original files will be removed.
   - **Desktop Message:** A humorous image with the ransom message will be saved to your desktop.

3. **Decryption:**
   - **Decryption Prompt:** Enter the decryption key when prompted.
   - **Decryption Process:** If the correct key is provided, the script will decrypt the previously encrypted files. If the key is incorrect, a message is displayed indicating that the files remain encrypted.

---

## How It Works

- **File Encryption:**  
  The script recursively walks through the current directory and encrypts every file using `pyAesCrypt.encryptFile()`. The encrypted files are given a `.encrypted` extension, and the original files are deleted.

- **Displaying the Message:**  
  A new image is generated using the `Pillow` library. This image contains a text message about the files being encrypted, serving as an alarming, humorous prompt. The image is saved directly to the desktop.

- **File Decryption:**  
  The decryption process reverses the encryption. The script searches for files with the `.encrypted` extension, decrypts them with the provided key using `pyAesCrypt.decryptFile()`, and removes the encrypted files.

---

## Disclaimer

> **Important:**  
> This project is intended strictly for educational purposes and authorized testing.  
> **Unauthorized use of ransomware or malware simulation tools is illegal and unethical.**  
> Use this tool only on systems where you have explicit permission, and understand the risks associated with data encryption.  
> **I am not liable for any misuse of this code.**



---

Enjoy experimenting with **Ransomeware** for educational purposes. Remember, with great power comes great responsibility—always use your tools ethically and lawfully!  

---
