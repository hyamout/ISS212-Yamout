#ISS 212
#Week 7 Dev Tool - Arrays & Hash Tables
Wa# Define an explicit array of sample log entries using your updated log format.
[string[]]$sampleLogs = @(
    "2024-01-01 00:00:00 [CRITICAL] 192.168.1.38 - Configuration file updated",
    "2024-01-01 00:07:09 [WARNING] 192.168.1.41 - Security alert: Suspicious activity detected",
    "2024-01-01 00:09:22 [WARNING] 192.168.1.40 - File system error",
    "2024-01-01 00:10:28 [ERROR] 192.168.1.24 - Configuration file updated",
    "2024-01-01 00:11:24 [CRITICAL] 192.168.1.24 - Database connection failed"
)
# Loop through the array and output each log entry.
Write-Output "`nSample Log Entries (from array):"
foreach ($log in $sampleLogs) {
    Write-Output $log
}

# Define a hash table with at least three key-value pairs for log filters.
$logFilters = @{
    "INFO"    = "Informational messages"
    "WARNING" = "Warnings that may require attention"
    "ERROR"   = "Errors that need fixing"
}
# Display available log filters.
Write-Output "`nAvailable Log Filters:"
foreach ($key in $logFilters.Keys) {
    Write-Output ($key + ": " + $logFilters[$key])
}
# Allow user to retrieve a value from the hash table.
$userKey = Read-Host "`nEnter a key to retrieve its value from logFilters (INFO, WARNING, or ERROR)"
if ($logFilters.ContainsKey($userKey)) {
    Write-Output "Retrieved value for '$userKey': $($logFilters[$userKey])"
} else {
    Write-Output "Key '$userKey' not found in logFilters."
}
