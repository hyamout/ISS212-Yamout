#Week 8 Dev Tool - Bash - Redacting IP Addresses in Web Server Logs

#!/bin/bash

# Define input and output log files
input_log="access.log"
output_log="access_redacted.log"

# Check if the input log file exists
if [[ ! -f "$input_log" ]]; then
    echo "Error: Log file '$input_log' not found!"
    exit 1
fi

# Redact IP addresses in the access log file using sed
sed -E 's/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[REDACTED]/g' "$input_log" > "$output_log"

# Confirm completion
echo "Redacted IP addresses in '$input_log' and saved as '$output_log'."
