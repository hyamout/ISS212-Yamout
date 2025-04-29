#Week 8 Dev Tool - Python - Suspicious IP Address Extraction
# Python script to find IPs involved in FAILED SSH login attempts
# Scenario: As a SOC analyst, identify unique sources of brute-force login failures

import re  # import the regular‐expressions module

# 1) Read in the entire auth.log file
#    This file contains all authentication events, including failed logins.
with open('auth.log', 'r') as file:
    log_data = file.read()      # store the whole file contents as a single string

# 2) Define a regex to find the IP address in each 'Failed password ... from <IP>' line
#    (\d{1,3}\.){3}\d{1,3} matches any IPv4 address
pattern = r"Failed password .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# 3) Search the log data for all occurrences of the pattern
#    This returns a list of every IP address that matched
suspicious_ips = re.findall(pattern, log_data)

# 4) Remove duplicates by converting the list to a set
unique_ips = set(suspicious_ips)

# 5) Output the results so we can see which IPs to investigate further
print("Suspicious IP addresses:")
for ip in unique_ips:
    print(ip)
