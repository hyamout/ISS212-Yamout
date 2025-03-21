#Prompt the user to enter an IP adderess and store it in the variable $ip
$ip = Read-Host "Enter IP Address"

#Define an array of common ports to check (22 for SSH, 80 for HTTP, 443 for HTTPS)
$ports = @(22, 80, 443)

#Loop through each port in the $ports array
foreach($port in $ports){
    #Test the connection to the specified IP address and port
    $result = Test-NetConnection -ComputerName $ip -Port $port -WarningAction SilentlyContinue

    #Check if the TCP connection test succeeded
    if($result.TcpTestSucceeded){
        #If the connection succeeded, print that the port is OPEN
        Write-Host "Port${port}: OPEN"
    } else{
        #If the connection failed, print that the port is CLOSED
        Write-Host "Port${port}: CLOSED"
    }
}