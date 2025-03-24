#ISS 212
#Week 4 Dev Tool - Environment Variable Inspector
#Retrieve environent variables
$username = $env:USERNAME
$userdomain = $env:USERDOMAIN
$computername = $env:COMPUTERNAME
$systempath = $env:Path

#Display the values with formatted output
Write-Host "Username:$username"
Write-Host "User Domain:$userdomain"
Write-Host "Computer Name: $computername"
Write-Host "System Path:$systempath"