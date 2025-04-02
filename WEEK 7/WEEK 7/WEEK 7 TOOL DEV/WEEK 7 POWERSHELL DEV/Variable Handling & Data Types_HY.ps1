#ISS 212
#Week 7 Dev Tool - Variable Handling & Data Types
# Define the path to the log file on the Desktop with an explicit data type.
[string]$logFilePath = "$($env:USERPROFILE)\Desktop\WK7LOG.txt"
# Dynamically check and display the variable's data type.
Write-Output "The variable 'logFilePath' is of type: $($logFilePath.GetType().Name)"