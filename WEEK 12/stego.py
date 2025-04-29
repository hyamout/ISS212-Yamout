'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - stego.py
NOTE: USE IMAGE FILE: drdoes.png
'''

from PIL import Image  # Importing PIL for image processing

def hide_message():
    """
    Embeds a secret message into an image using **Least Significant Bit (LSB) encoding**.
    The message is stored in the least significant bit of the pixel color values.
    """

    # Ask user for the path to the image file
    image_path = input("Enter the path of the original image: ").strip()
    
    # Ask user for the secret message to embed
    message = input("Enter the secret message to hide: ").strip()

    # Open the image file using PIL
    img = Image.open(image_path)
    img = img.convert('RGB')  # Convert image to RGB format (ensures compatibility)

    data = []  # List to store the binary representation of the message

    # Convert each character in the message to its binary form (8-bit)
    for char in message:
        data.extend(format(ord(char), '08b'))  # Convert ASCII character to binary

    pixel_index = 0  # Tracks the position in the binary data

    # Iterate through each pixel in the image
    for i in range(img.width):  # Loop through width (X-axis)
        for j in range(img.height):  # Loop through height (Y-axis)
            pixel = list(img.getpixel((i, j)))  # Convert pixel to list of RGB values

            # Modify pixel color channels to embed the binary data
            for color_channel in range(3):  # Iterate over Red, Green, Blue (RGB)
                if pixel_index < len(data):  # Check if there is still data to embed
                    # Modify the least significant bit of the color channel
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + data[pixel_index], 2)
                    pixel_index += 1  # Move to the next bit of the message

            # Update the pixel with modified values
            img.putpixel((i, j), tuple(pixel))

    # Ask user for output image file name
    stego_image_path = input("Enter the path to save the stego image (e.g., stego_image.png): ").strip()
    
    # Save the modified image as PNG format
    img.save(stego_image_path, format='PNG')

    print("Message hidden successfully!")  # Display success message

# Execute function to run the script
hide_message()
