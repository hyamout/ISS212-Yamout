'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use Command: python reg3.py SYSTEM
'''

import winreg  # Import Windows registry module for system registry access
import sys  # Import sys for command-line argument handling

def getCurrentControlSet():
    """
    Retrieves the current ControlSet from the Windows Registry.
    ControlSets store system configuration settings used by Windows during startup.
    """

    try:
        hkey_local_machine = winreg.HKEY_LOCAL_MACHINE  # Reference the main registry hive
        select_subkey = "SYSTEM\\Select"  # Define the registry path to 'SYSTEM\\Select'

        # Open the registry key to retrieve system configuration details
        with winreg.OpenKey(hkey_local_machine, select_subkey) as key:
            # Iterate over values in the registry key
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                value_name, value_data, _ = winreg.EnumValue(key, i)

                # Find the 'Current' value, which specifies the active ControlSet
                if value_name == "Current":
                    return value_data  # Return the active ControlSet number

    except FileNotFoundError as exception:
        print("Couldn't find SYSTEM\\Select key", exception)  # Handle missing registry key errors

def getServiceInfo(dictionary):
    """
    Retrieves detailed service information from the registry and prints it in a readable format.
    """

    # Dictionary mapping service type codes to human-readable descriptions
    serviceType = {
        1: "Kernel device driver", 2: "File system driver", 4: "Arguments for an adapter",
        8: "File system driver interpreter", 16: "Own process", 32: "Shared process",
        272: "Independent interactive program", 288: "Shared interactive program"
    }

    print(" Service name: %s" % dictionary["SERVICE_NAME"])  # Print the service name

    # Print additional service details if available
    if "DisplayName" in dictionary:
        print(" Display name: %s" % dictionary["DisplayName"])

    if "ImagePath" in dictionary:
        print(" ImagePath: %s" % dictionary["ImagePath"])

    if "Type" in dictionary:
        print(" Type: %s" % serviceType.get(dictionary["Type"], "Unknown"))  # Map service type to description

    if "Group" in dictionary:
        print(" Group: %s" % dictionary["Group"])

    print("--------------------------")  # Separate service entries for clarity

def serviceParams(subkey):
    """
    Extracts relevant service parameters from the registry subkey.
    """

    service = {}  # Create an empty dictionary to store service details
    service["SERVICE_NAME"] = subkey  # Store the service name
    service["ModifiedTime"] = winreg.QueryInfoKey(subkey)[2]  # Retrieve last modified time

    try:
        # Retrieve all stored values inside the subkey
        for i in range(0, winreg.QueryInfoKey(subkey)[1]):
            value_name, value_data, _ = winreg.EnumValue(subkey, i)
            service[value_name] = value_data  # Store key-value pairs in the dictionary

    except OSError as exception:
        print("Error accessing registry subkey", exception)  # Handle errors gracefully

    getServiceInfo(service)  # Print extracted service details

def servicesKey(controlset):
    """
    Retrieves all services from the specified ControlSet and extracts relevant information.
    """

    # Construct the full path to the 'Services' registry key
    serviceskey = "SYSTEM\\ControlSet00%d\\Services" % controlset

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, serviceskey) as key:
            # Iterate over available subkeys (individual services)
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)  # Retrieve subkey name (service name)
                subkey = winreg.OpenKey(key, subkey_name)  # Open the specific subkey
                serviceParams(subkey)  # Extract and display service parameters

    except FileNotFoundError as exception:
        print("Couldn't find Services key", exception)  # Handle missing registry key scenario

if __name__ == "__main__":
    """
    Main execution of the script:
    1. Retrieves the active ControlSet number.
    2. Searches for services in the specified ControlSet.
    3. Extracts and displays service details from the registry.
    """

    controlset = getCurrentControlSet()  # Get current ControlSet
    if controlset is not None:  # Proceed only if ControlSet exists
        servicesKey(controlset)  # Extract and display service details
