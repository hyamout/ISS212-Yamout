import argparse  # Import argparse for handling command-line arguments
from PIL import Image  # Import PIL to open and process images
from PIL.ExifTags import TAGS, GPSTAGS  # Import EXIF tags for metadata extraction
import sys  # Import sys to handle script exit

def get_geotagging(exif):
    """Extracts GPS metadata from EXIF data."""
    
    # Check if EXIF metadata exists
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}  # Dictionary to store extracted GPS metadata
    
    # Loop through available EXIF tags
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo' and idx in exif:  # Check if GPS metadata exists
            # Loop through GPS tags and store their values
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:  
                    geotagging[val] = exif[idx][key]

    return geotagging  # Return dictionary containing GPS metadata

def dms_to_dd(d, m, s, ref):
    """Converts DMS (Degrees, Minutes, Seconds) format to Decimal Degrees."""
    
    # Convert degrees, minutes, and seconds to decimal format
    decimal_degrees = d + float(m)/60 + float(s)/(60*60)
    
    # Adjust for Southern or Western hemisphere coordinates
    return -decimal_degrees if ref in ['S', 'W'] else decimal_degrees

def extract_gps_coords(exif_data):
    """Extracts latitude and longitude from EXIF metadata."""
    
    # Get GPS metadata from EXIF data
    geotags = get_geotagging(exif_data)
    
    # Return None if GPS metadata is unavailable
    if not geotags:
        return None, None

    # Convert latitude and longitude to decimal format
    latitude = dms_to_dd(*geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    longitude = dms_to_dd(*geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return latitude, longitude  # Return GPS coordinates

def main():
    """Main function to process an image file."""
    
    # Create argument parser to receive image path from command-line
    parser = argparse.ArgumentParser(description='Extract GPS metadata from images')
    parser.add_argument('image_path', help='Path to the image file')  # Define command-line argument

    args = parser.parse_args()  # Parse command-line arguments
    img_file = Image.open(args.image_path)  # Open image file using PIL
    exif_data = img_file._getexif()  # Extract EXIF metadata from the image

    # Handle case where no EXIF metadata is found
    if not exif_data:
        print("No EXIF metadata found in the image.")
        sys.exit()  # Exit script execution

    # Get GPS coordinates from EXIF metadata
    latitude, longitude = extract_gps_coords(exif_data)

    # Display GPS coordinates if available
    if latitude and longitude:
        print(f"GPS Coordinates: {latitude}, {longitude}")
        print(f"Google Maps URL: https://www.google.com/maps?q={latitude},{longitude}")
    else:
        print("No GPS data found in EXIF metadata.")  # Inform user if no GPS data is present

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
