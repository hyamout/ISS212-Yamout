'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - de-txt.py
NOTE: USE AES KEY IN **TXT** FILE TO DECRYPT FILE: sup3rs3cr37.txt.enc
'''

from Crypto.Cipher import AES  # Import AES encryption module from PyCryptodome

def decrypt_file_aes(encrypted_file_path, key):
    """
    Decrypts a file using AES encryption in EAX mode.
    The encrypted file must contain the nonce, authentication tag, and ciphertext.
    """

    # Open the encrypted file in binary mode
    with open(encrypted_file_path, 'rb') as encrypted_file:
        nonce = encrypted_file.read(16)  # Read the nonce (random initialization value)
        tag = encrypted_file.read(16)  # Read the authentication tag for integrity check
        ciphertext = encrypted_file.read()  # Read the encrypted data

    # Initialize the AES cipher for decryption using the same nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Decrypt and verify integrity using the authentication tag
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # Save the decrypted data to a new file
    with open(encrypted_file_path[:-4] + '_decrypted.txt', 'wb') as decrypted_file:
        decrypted_file.write(plaintext)

if __name__ == "__main__":
    """
    Main script execution:
    1. User provides the AES key in **hexadecimal format**.
    2. User specifies the encrypted file to be decrypted.
    3. The script decrypts and outputs the original file content.
    """

    aes_key = bytes.fromhex(input("Enter the AES key (hexadecimal format): "))  # Convert input key from hex to bytes

    file_to_decrypt = input("Enter the name of the file to decrypt: ")  # Prompt user for file name
    decrypt_file_aes(file_to_decrypt, aes_key)  # Call decryption function

    print(f'File "{file_to_decrypt}" decrypted.')  # Notify user that decryption is complete
