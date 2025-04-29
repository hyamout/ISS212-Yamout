'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use command: python reg2.py SOFTWARE
'''

import sys  # Import sys to handle command-line arguments
from regipy.registry import RegistryHive  # Import Regipy for working with Windows registry hives

try:
    # Ensure the user provides a registry hive file path as an argument
    hive_path = sys.argv[1]  # Extract the hive path from command-line arguments
    reg = RegistryHive(hive_path)  # Load the registry hive file

    print(f"Analyzing {hive_path}...")  # Inform user that analysis has started

    # Attempt to access the 'SOFTWARE\Microsoft\Windows NT\CurrentVersion' registry key
    software_key = reg.get_key(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    if software_key:
        # Extract and display important information from the registry key
        print("\tProduct name:", software_key.get_value("ProductName"))  # Display Windows product name
        print("\tCurrentVersion:", software_key.get_value("CurrentVersion"))  # Display version number
        print("\tServicePack:", software_key.get_value("CSDVersion"))  # Show service pack details
        print("\tProductID:", software_key.get_value("ProductId"))  # Display Windows product ID

    else:
        print("Subkey 'CurrentVersion' not found in the provided registry file.")  # Handle missing key scenario

except FileNotFoundError as exception:
    print(f"Registry hive file not found: {exception}")  # Handle cases where the hive file is missing
except Exception as exception:
    print(f"An error occurred: {exception}")  # Handle unexpected errors gracefully
