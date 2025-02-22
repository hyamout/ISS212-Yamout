#!/bin/bash
# File Permission Audit - WK3-fileperm.sh
# Purpose: Scans files in the current directory and flags those with world-writable permissions.

# List all files in the directory and check their permissions
echo "Starting file permission audit..."
for file in *; do
  echo "Checking $file..."
  # Check if the current item is a file
  if [[ -f "$file" ]]; then
    # Extract the file permissions using ls -l
    permissions=$(ls -l "$file" | awk '{print $1}')
    # Check if the file is world-writable (indicated by 'others' write permission 'w' in the last three characters)
    if [[ "${permissions:8:1}" == "w" ]]; then
      # Print a warning if the file is world-writable
      echo "Warning: $file is world-writable!"
    fi
  fi
done
echo "File permission audit completed."
