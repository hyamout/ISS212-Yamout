#ISS 212
#Week 4 Dev Tool - Execitoon Policy Check
$currentPolicy = Get-ExecutionPolicy

#Print the current execution policy
Write-Host "Current Execution Policy: $currentPolicy"

#Conditional logic to check the execution policy and print appropriate messages
if ($currentPolicy -in "Unrestricted", "Bypass"){
    #If the execution plocy is Unrestricted or Bypass, print a warning message
    Write-Host "WARNING: Your execution policy allows all scripts to run. Ensure you trust the source."
}elseif($currentPolicy -eq "Restricted"){
    #If the execution policy is Restricted, print a message explaining that scripts cannot be executed
    Write-Host "Scripts cannot be executed on this system."
} else{
    #If the execution policy is set to any other value, print the current execution policy
    Write-Host "Your execution policy is set to: $currentPolicy"

}