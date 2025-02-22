#!/bin/bash
# Log File Analyzer for Suspicious Activity - WK3-logfileanalyzer.sh
# Purpose: This script scans a log file for entries associated with suspicious IP addresses.

# Define the log file paths
auth_log_file="/e/classes/ISS 212/week 3/Assignment/sim_auth.log"
access_log_file="/e/classes/ISS 212/week 3/Assignment/sim_access.log" 

# List of flagged suspicious IP addresses
flagged_ips=("199.203.100.103" "10.0.0.35" "192.168.1.50")

# Function to process a log file
process_log_file() {
  local log_file="$1"
  # Check if the log file exists
  if [[ ! -f "$log_file" ]]; then
    echo "Error: Log file $log_file not found!"
    return
  fi
  # Read the log file line by line
  while IFS= read -r line; do
    # Iterate through the list of flagged IPs
    for ip in "${flagged_ips[@]}"; do
      # Check if the IP appears in the log entry
      if [[ "$line" == *"$ip"* ]]; then
        # Print the line if a flagged IP is found
        echo "Suspicious activity detected: $line"
      fi
    done
  done < "$log_file"
}

# Process the auth log file
echo "Analyzing auth log file..."
process_log_file "$auth_log_file"

# Process the access log file
echo "Analyzing access log file..."
process_log_file "$access_log_file"
