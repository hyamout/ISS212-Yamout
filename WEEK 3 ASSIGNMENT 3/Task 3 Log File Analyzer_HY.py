# Log File Analyzer for Suspicious Activity - WK3-logfileanalyzer.py
# Purpose: This script scans a log file for entries associated with suspicious IP addresses, highlighting potential indicators of compromise.

# Import necessary modules
import os

# Define the log file paths
auth_log_file_path = r'E:\classes\ISS 212\week 3\Assignment\sim_auth.log'
access_log_file_path = r'E:\classes\ISS 212\week 3\Assignment\sim_access.log'


# Function to extract IP addresses from a log file
def extract_ips(file_path):
    ips = set()  # Use a set to avoid duplicate IPs
    with open(file_path, 'r') as log_file:
        for line in log_file:  # Read each line in the log file
            parts = line.split(' ')  # Split the log line into components
            ip_address = parts[0]  # Extract the IP address from the log line
            ips.add(ip_address)  # Add the IP address to the set
    return ips

# Extract IPs from both log files
auth_ips = extract_ips(auth_log_file_path)  # Extract IPs from the auth log file
access_ips = extract_ips(access_log_file_path)  # Extract IPs from the access log file

# Combine IPs from both log files into a single set
flagged_ips = auth_ips.union(access_ips)  # Union of both sets to get unique IPs

# Function to process each line in the log file and check for flagged IPs
def process_log_file(file_path):
    with open(file_path, 'r') as log_file:
        for line in log_file:  # Read each line in the log file
            for ip in flagged_ips:  # Iterate through the list of flagged IPs
                if ip in line:  # Check if the IP appears in the log entry
                    print(f"Suspicious activity detected: {line.strip()}")  # Print the line if a flagged IP is found

# Process both log files
print("Analyzing auth log file...")  # Print a message indicating analysis of auth log file
process_log_file(auth_log_file_path)  # Analyze the auth log file

print("Analyzing access log file...")  # Print a message indicating analysis of access log file
process_log_file(access_log_file_path)  # Analyze the access log file

