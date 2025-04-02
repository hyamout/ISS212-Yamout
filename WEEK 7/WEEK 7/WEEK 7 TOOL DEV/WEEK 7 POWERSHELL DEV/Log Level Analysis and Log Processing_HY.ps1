#ISS 212
#Week 7 Dev Tool - Log Level Analysis and Log Processing
# Check if the log file exists; if not, use the sampleLogs array.
if (-Not (Test-Path -Path $logFilePath)) {
    Write-Output "`nLog file not found at '$logFilePath'. Using sample log entries from the array for processing."
    $logEntries = $sampleLogs
} else {
    try {
        $logEntries = Get-Content -Path $logFilePath
    } catch {
        Write-Output "`nError: Unable to read the log file at '$logFilePath'. Exiting."
        exit
    }
}

# Initialize a hash table to store log level counts.
$logSummary = @{}

# Optional: Array to store IP addresses for failed authentication attempts.
$failedAuthIPs = @()

# Optional: Array to store recent logs (for recent activity extraction, if desired).
$recentLogs = @()

$logPattern = '^(?<Timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+\[(?<LogLevel>[A-Z]+)\]\s+(?<IPAddress>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+(?<LogMessage>.+)$'

# Process each log entry.
foreach ($log in $logEntries) {
    if ($log -match $logPattern) {
        $timestampStr = $matches['Timestamp']
        $logLevel   = $matches['LogLevel']
        $ipAddress  = $matches['IPAddress']
        $logMessage = $matches['LogMessage']

        # Convert timestamp string to a DateTime object.
        [DateTime]$timestamp = [DateTime]::ParseExact($timestampStr, 'yyyy-MM-dd HH:mm:ss', $null)

        # Increment log level count.
        if ($logSummary.ContainsKey($logLevel)) {
            $logSummary[$logLevel]++
        } else {
            $logSummary[$logLevel] = 1
        }

        # Optional use case: Detect failed authentication attempts.
        if ($logMessage -match "(?i)failed authentication") {
            Write-Output "`nFailed authentication detected: IP $ipAddress at $timestampStr"
            $failedAuthIPs += $ipAddress
        }

        # Display the extracted log components.
        Write-Output "`nLog Entry Processed:"
        Write-Output "Timestamp: $timestampStr"
        Write-Output "Log Level: $logLevel"
        Write-Output "IP Address: $ipAddress"
        Write-Output "Message: $logMessage"
    } else {
        Write-Output "`nSkipped line (invalid format): $log"
    }
}

# Display the log level analysis summary.
Write-Output "`nLog Level Analysis Summary:"
if ($logSummary.Count -eq 0) {
    Write-Output "No valid log levels found in the processed entries."
} else {
    foreach ($key in $logSummary.Keys) {
        # Guard against a null value for the count.
        $count = $logSummary[$key]
        if ($null -eq $count) { $count = 0 }
        Write-Output "${key}: ${count}"
    }
}

# Optional: Display failed authentication IP addresses.
if ($failedAuthIPs.Count -gt 0) {
    Write-Output "`nFailed Authentication IPs:"
    foreach ($ip in $failedAuthIPs) {
        Write-Output $ip
    }
}
