#ISS 212
#Week 8 Assignment 6 - Configuring PowerShell Event Logging

# This sets the path where the logs folder will be created on the desktop
$logFolderPath = "C:\Users\Hani Yamout\Desktop\week 8"

# This joins the folder path with the filename to create the full path for the log file
$logFilePath = Join-Path -Path $logFolderPath -ChildPath "PowerShellEvents.log"

# Output the paths in the terminal so the user knows where the logs will be saved
Write-Host "Log folder path: $logFolderPath"
Write-Host "Log file path: $logFilePath"

# Check if the log folder already exists; if not, create it
if (-not (Test-Path -Path $logFolderPath -PathType Container)) {
    Write-Host "Logs folder does not exist. Creating..."
    try {
        # Try to create the folder
        New-Item -Path $logFolderPath -ItemType Directory
        Write-Host "Logs folder created successfully."
    } catch {
        # If folder creation fails, show the error and stop the script
        Write-Host "Error creating Logs folder: $_"
        exit
    }
} else {
    # If the folder exists, just inform the user
    Write-Host "Logs folder already exists."
}

# This is the Windows registry path used to enable script block logging in PowerShell
$regPath = "HKLM:\SOFTWARE\Microsoft\PowerShell\ScriptBlockLogging"
Write-Host "Registry path: $regPath"

# Check if the registry key exists; if not, create it
if (-not (Test-Path -Path $regPath)) {
    Write-Host "Registry key does not exist. Creating..."
    try {
        # Try to create the registry key
        New-Item -Path $regPath -Force
        Write-Host "Registry key created successfully."
    } catch {
        # If registry creation fails, show error and stop script
        Write-Host "Error creating registry key: $_"
        exit
    }
} else {
    # Inform that registry key is already there
    Write-Host "Registry key already exists."
}

# Try to configure the registry values for logging
try {
    # Enable Script Block Logging by setting the registry value to 1
    Set-ItemProperty -Path $regPath -Name "EnableScriptBlockLogging" -Value 1 -ErrorAction Stop

    # Optionally add a custom log path (Note: not always used by PowerShell itself)
    Set-ItemProperty -Path $regPath -Name "LogPath" -Value $logFilePath -ErrorAction Stop

    # Confirm logging is now set up
    Write-Host "PowerShell event logging has been configured. Events will be logged to $logFilePath."
} catch {
    # If setting registry values fails, print the error
    Write-Host "Error setting registry values: $_"
}

# Define a custom function to log a message with a timestamp
function Log-Event {
    param (
        [Parameter(Mandatory = $true)]
        [string]$Message  # The message we want to log
    )

    # Get current date and time in a readable format
    $Timestamp = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

    # Combine the timestamp and the message
    $MessageWithTimestamp = "$Timestamp - $Message"

    # Append the final message to the log file
    $MessageWithTimestamp | Out-File -FilePath $logFilePath -Append
}

# Use the custom function to log that the script has started
Log-Event "Script started"

# Try to get system information like OS version and type
try {
    $systemInfo = Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture

    # Log the type of information we’re saving
    Log-Event "System information:"

    # Log the actual system information (converted to string)
    Log-Event $systemInfo | Out-String
} catch {
    # Log any error that occurs while collecting system info
    Log-Event "Error retrieving system information: $_"
}

# Notify the user that the script has finished running
Write-Host "Script execution complete. Please check the log file for details: $logFilePath"
