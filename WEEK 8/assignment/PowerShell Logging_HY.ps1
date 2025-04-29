#ISS 212
#Week 8 Assignment 6 - Powershell Logging

# Function to ensure the registry path exists before modifying it
function Ensure-RegistryPath {
    param (
        [string]$Path  # Accepts the registry path as an argument
    )

    # Check if the registry path exists in Windows Registry
    if (-not (Test-Path $Path)) {
        # If it doesn't exist, create the registry key to store logging settings
        $null = New-Item -Path $Path -Force
        Write-Host "Created registry path: $Path"
    }
}

# Function to enable PowerShell Event Logging
function Enable-EventLogging {
    # Display information to the user about Event Logging
    Write-Host "Event Logging enables the recording of PowerShell engine events."

    # Ask the user whether they want to enable Event Logging
    $userChoice = Read-Host "Do you want to enable Event Logging? (Y/N)"

    # If the user selects 'Y', proceed with enabling Event Logging
    if ($userChoice -eq 'Y') {
        # Ensure the registry path for ScriptBlockLogging exists before modifying it
        Ensure-RegistryPath -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"

        # Modify the registry to enable Script Block Logging, which logs PowerShell commands
        Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Name "EnableScriptBlockLogging" -Value 1

        # Confirmation message for the user
        Write-Host "Event Logging has been enabled."
    } else {
        Write-Host "Skipping Event Logging."
    }
}

# Function to enable PowerShell Module Logging
function Enable-ModuleLogging {
    # Display information about Module Logging
    Write-Host "Module Logging records events from PowerShell modules."

    # Ask the user whether they want to enable Module Logging
    $userChoice = Read-Host "Do you want to enable Module Logging? (Y/N)"

    # If the user selects 'Y', proceed with enabling Module Logging
    if ($userChoice -eq 'Y') {
        # Ensure the registry path for ModuleLogging exists before modifying it
        Ensure-RegistryPath -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging"

        # Modify the registry to enable Module Logging, which tracks PowerShell module activity
        Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging" -Name "EnableModuleLogging" -Value 1

        # Set the logging to track **all** PowerShell modules (* wildcard)
        Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging" -Name "ModuleNames" -Value "*"

        # Confirmation message for the user
        Write-Host "Module Logging has been enabled for all modules."
    } else {
        Write-Host "Skipping Module Logging."
    }
}

# Function to enable PowerShell Script Block Logging
function Enable-ScriptBlockLogging {
    # Display information about Script Block Logging
    Write-Host "Script Block Logging records the content of all script blocks that are processed."

    # Ask the user whether they want to enable Script Block Logging
    $userChoice = Read-Host "Do you want to enable Script Block Logging? (Y/N)"

    # If the user selects 'Y', proceed with enabling Script Block Logging
    if ($userChoice -eq 'Y') {
        # Ensure the registry path for ScriptBlockLogging exists before modifying it
        Ensure-RegistryPath -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"

        # Modify the registry to enable Script Block Logging, which logs executed PowerShell scripts
        Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Name "EnableScriptBlockLogging" -Value 1

        # Confirmation message for the user
        Write-Host "Script Block Logging has been enabled."
    } else {
        Write-Host "Skipping Script Block Logging."
    }
}

# Display a welcome message to the user explaining the purpose of the script
Write-Host "Welcome to the PowerShell Logging Setup Script"
Write-Host "This script will guide you through enabling various PowerShell logging features."

# Execute each logging setup function based on user input
Enable-EventLogging
Enable-ModuleLogging
Enable-ScriptBlockLogging

# Final message indicating that the logging setup process is complete
Write-Host "PowerShell Logging setup is complete."
