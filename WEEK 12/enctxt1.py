'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - enc-txt.py
NOTE: REMEMBER TO SAVE AES KEY IN **TXT** FILE TO USE FOR DECRYPTION!
'''

from Crypto.Cipher import AES  # Import AES encryption module from PyCryptodome
from Crypto.Random import get_random_bytes  # Import function for generating random bytes (AES key)

def generate_aes_key(key_size):
    """
    Generates a random AES key of the specified size.
    AES keys should be either 128, 192, or 256 bits in length.
    """
    return get_random_bytes(key_size // 8)  # Convert key size from bits to bytes

def encrypt_file_aes(file_path, key):
    """
    Encrypts a file using AES encryption in EAX mode.
    EAX mode ensures both confidentiality and integrity.
    """
    cipher = AES.new(key, AES.MODE_EAX)  # Create AES cipher object with EAX mode
    
    # Open the file to read its content
    with open(file_path, 'rb') as file:
        plaintext = file.read()  # Read file content as binary

        # Encrypt the file's content and generate authentication tag
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Save the encrypted file along with nonce and tag
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(cipher.nonce)  # Nonce ensures unique encryption per file
        encrypted_file.write(tag)  # Authentication tag ensures integrity
        encrypted_file.write(ciphertext)  # Encrypted content

# Example usage when script is executed
if __name__ == "__main__":
    # Generate a 256-bit AES encryption key
    aes_key = generate_aes_key(256)

    # Ask user for the file to encrypt
    file_to_encrypt = input("Enter the name of the file to encrypt: ")
    
    # Encrypt the file using AES encryption
    encrypt_file_aes(file_to_encrypt, aes_key)
    print(f'File "{file_to_encrypt}" encrypted.')  # Confirmation message

    # Print AES key in hexadecimal format (important for decryption)
    print(f'AES Key (Hex): {aes_key.hex()}')  # Always store this key securely!
