#Week 8 Dev Tool - Powershell - Event log Monitoring
# PowerShell script using Regex -- Extracting data using pattern matching

'''
.DESCRIPTION
Add {your name} and {date} to the first comment line.
ISS 212 - CS Scripting - PowerShell Script: ps-FailLog.ps1
Citations:

.PURPOSE
Week 8 PowerShell script using Regex to match IP data in security logs.

.USAGE
Run script from file with command or from terminal. | .\ps-FailLog.ps1
'''

# Week 8 PowerShell script using Regex -- extracting data using pattern matching

# Define the log file that contains authentication events
$logFile = "security.log"

# Use Select-String to search for "Login attempt failed" messages followed by an IP address
# The regular expression extracts IPv4 addresses formatted as x.x.x.x
$failedAttempts = Select-String -Path $logFile -Pattern "Login attempt failed from IP (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" -AllMatches

# Create an empty hash table to store the IP addresses and count occurrences
$ipCounts = @{}

# Loop through each matched instance of failed login attempts
foreach ($match in $failedAttempts) {
    # Extract the captured IP address from the regex match
    $ip = $match.Matches.Groups[1].Value
    
    # If the IP address already exists in the hash table, increment its count
    if ($ipCounts.ContainsKey($ip)) {
        $ipCounts[$ip] += 1
    } else {
        # Otherwise, add it to the hash table with an initial count of 1
        $ipCounts[$ip] = 1
    }
}

# Display a list of flagged IPs that have more than 3 failed login attempts
Write-Host "Potentially Malicious IPs:"
foreach ($ip in $ipCounts.Keys) {
    if ($ipCounts[$ip] -gt 3) {
        # Print IP addresses that have exceeded the threshold of failed attempts
        Write-Host "$ip has $($ipCounts[$ip]) failed login attempts"
    }
}
