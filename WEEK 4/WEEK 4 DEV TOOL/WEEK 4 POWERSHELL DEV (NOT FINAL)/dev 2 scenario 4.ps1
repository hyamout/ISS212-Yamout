#Check if the current user has administrator privileges
if (([System.Security.Principal.WindowsIdentity]::GetCurrent()).Groups -contains "S-1-5-32-544"){
    #If the user belongs to the Administrators group (SID: S-1-5-32-544)
    Write-Host "Administrator Privileges: Yes"
} else{
    #If the user does not belong to the Administrators group
    Write-Host "Administrator Privileges: No"
}