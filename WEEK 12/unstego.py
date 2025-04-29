'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - stego.py
NOTE: USE STEGO IMAGE FILE: drdoes-steg.png
'''

from PIL import Image  # Import PIL for image processing

def extract_message():
    """
    Extracts a hidden message from an image that has been encoded using **Least Significant Bit (LSB) steganography**.
    The message is retrieved by checking the least significant bits of pixel color values.
    """

    print("Stego Image Extraction Script")  # Display script title

    # Prompt user to input the path of the stego image file
    stego_image_path = input("Enter the path of the stego image: ").strip()

    # Open the stego image file
    img = Image.open(stego_image_path)

    data = ''  # Initialize an empty string to store extracted binary data
    terminator = '11111111'  # This serves as a termination sequence for the hidden message

    # Loop through each pixel in the image
    for i in range(img.width):  # Iterate over the image's width (X-axis)
        for j in range(img.height):  # Iterate over the image's height (Y-axis)
            pixel = img.getpixel((i, j))  # Retrieve pixel color values (RGB tuple)

            # Extract the least significant bit (LSB) from each color channel
            for color_channel in range(3):  # Iterate through Red, Green, Blue (RGB)
                data += format(pixel[color_channel], '08b')[-1]  # Append LSB to data string

    # Find the termination index (where the hidden message ends)
    terminator_index = data.find(terminator)  # Locate the '11111111' terminator sequence

    # Convert the extracted binary data into readable text (characters)
    message = ''.join([chr(int(data[i:i+8], 2)) for i in range(0, terminator_index, 8)])

    # Print the hidden message to the user
    print(f"Extracted Message: {message}")

# Execute function when the script runs
if __name__ == "__main__":
    extract_message()
