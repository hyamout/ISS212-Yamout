#!/bin/bash
# Bash Port Scanner - WK3-portscanner.sh
# Purpose: Checks open ports on a target system using PowerShell inside Git Bash.

# Prompt the user for target IP and port range
read -p "Enter the target IP: " target_ip
# Prompts the user to enter the target IP and stores it in the variable 'target_ip'

read -p "Enter the starting port: " start_port
# Prompts the user to enter the starting port and stores it in the variable 'start_port'

read -p "Enter the ending port: " end_port
# Prompts the user to enter the ending port and stores it in the variable 'end_port'

# Loop through the specified port range
for (( port=$start_port; port<=$end_port; port++ )); do
  # Iterates through each port from 'start_port' to 'end_port'
  echo "Checking port $port on $target_ip..."
  # Print a message indicating the current port being checked

  # Use PowerShell to check if each port is open
  result=$(pwsh.exe -Command "Test-NetConnection -ComputerName $target_ip -Port $port -WarningAction SilentlyContinue | Select-Object -ExpandProperty TcpTestSucceeded")
  # Executes a PowerShell command to check if the port is open and stores the result in the variable 'result'

  echo "Result for port $port: $result"
  # Print the result for the current port

  # Print open ports
  if [[ "$result" == "True" ]]; then
    # Checks if the result indicates that the port is open
    echo "Port $port is open on $target_ip."
    # Prints a message indicating that the port is open
  fi
done
# Ends the for loop


