import sys  # Import system module to handle command-line arguments
import winreg  # Import Windows registry module for accessing registry keys

try:
    # Check if the user provided a registry key path as an argument
    if len(sys.argv) < 2:
        print("Usage: python reg1.py <Registry Key Path>")
        sys.exit(1)  # Exit the script if no argument is provided

    key_path = sys.argv[1]  # Store the registry key path provided by the user

    # Connect to the Windows registry under HKEY_LOCAL_MACHINE
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

    try:
        # Attempt to open the specified registry key
        key = winreg.OpenKey(reg, key_path)
    except FileNotFoundError:
        print(f"Registry key '{key_path}' not found.")  # Notify user if key does not exist
        sys.exit(1)  # Exit script if the registry key is not found

    print(f"Analyzing {key_path} in Windows registry...")  # Inform user that processing has started

    try:
        last_modified = winreg.QueryInfoKey(key)[2]  # Retrieve last modified timestamp
        print(f"Last modified: {last_modified} [UTC]")  # Display last modification time

        num_subkeys = winreg.QueryInfoKey(key)[0]  # Get the number of subkeys inside the registry key
        num_values = winreg.QueryInfoKey(key)[1]  # Get the number of stored values

        # Iterate over subkeys and display their names
        for i in range(num_subkeys):
            try:
                subkey_name = winreg.EnumKey(key, i)  # Retrieve the name of the subkey
                print("Subkey:", subkey_name)

                # Create full path of subkey for deeper inspection
                subkey_path = f"{key_path}\\{subkey_name}"
                subkey = winreg.OpenKey(reg, subkey_path)  # Open the subkey

                # Iterate over stored values inside the subkey
                for j in range(num_values):
                    try:
                        value_name, value_data, _ = winreg.EnumValue(subkey, j)  # Retrieve value name and data
                        print(f"  Name: {value_name}, Value: {value_data}")  # Display registry values
                    except OSError:
                        break  # Stop iteration if no more values exist
                winreg.CloseKey(subkey)  # Close the subkey after reading

            except OSError:
                pass  # Handle errors gracefully if a subkey cannot be accessed

        winreg.CloseKey(key)  # Close the main registry key after processing

    except OSError as e:
        print(f"Error processing registry key: {e}")  # Handle errors related to registry processing

except PermissionError:
    print("Permission error: Run as Administrator to access registry.")  # Warn user if they lack permissions
except Exception as e:
    print(f"An error occurred: {e}")  # Catch and display other unexpected errors
