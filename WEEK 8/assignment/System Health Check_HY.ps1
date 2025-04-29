#ISS 212
#Week 8 Assignment 6 - System Health Checl

Write-Host "System Health Check:"
Write-Host "---------------------"

# --------------------- Disk Space Usage ---------------------
# Retrieves details about the C: drive (main system drive)
# Using Get-CimInstance instead of Get-WmiObject (PowerShell 7 compatibility)
$disk = Get-CimInstance Win32_LogicalDisk | Where-Object {$_.DeviceID -eq "C:"}

# Ensure disk properties are valid before performing division
if ($disk -and $disk.Size -gt 0) {
    Write-Host "Disk Space Usage: $($disk.FreeSpace / 1GB)GB free of $($disk.Size / 1GB)GB ($($disk.FreeSpace / $disk.Size * 100)% free)"
} else {
    Write-Host "Disk information not available or inaccessible."
}

Write-Host "---------------------"

# --------------------- CPU Usage ---------------------
# Displays the current CPU load percentage using Get-CimInstance (PowerShell 7 compatibility)
Write-Host "CPU Usage:"
Get-CimInstance Win32_Processor | Format-Table LoadPercentage

Write-Host "---------------------"

# --------------------- Memory Usage ---------------------
# Retrieves memory usage details including used and total available memory
Write-Host "Memory Usage:"
Get-CimInstance Win32_OperatingSystem | Select-Object @{Name="Used"; Expression={($_.TotalVisibleMemorySize - $_.FreePhysicalMemory) / 1MB}},
                                                       @{Name="Total"; Expression={$_.TotalVisibleMemorySize / 1MB}}

Write-Host "---------------------"

# --------------------- Running Services ---------------------
# Lists all actively running services
# Uses -ErrorAction SilentlyContinue to ignore permission errors
Write-Host "Running Services:"
Get-Service | Where-Object {$_.Status -eq "Running"} | Format-Table DisplayName -ErrorAction SilentlyContinue

Write-Host "---------------------"
