# Brute-Force Detection Script - WK3-susaccess.py

def scan_log(file_path):
    failed_logins = {}  # Dictionary to track failed login attempts
    suspicious_activity = []  # List to store flagged activity

    with open(file_path, "r") as file:  # Open the log file
        for line in file:  # Loop through each line in the file
            parts = line.split()  # Split the line into parts
            ip = parts[0]  # Get the IP address
            status_code = parts[8]  # Get the status code
            file_requested = parts[6]  # Get the requested file

            # Check for failed login attempts (401 response code)
            if status_code == "401":
                if ip not in failed_logins:
                    failed_logins[ip] = 0  # Initialize the count for the IP
                failed_logins[ip] += 1  # Increment the count

                # Flag IP if it has more than 5 failed logins
                if failed_logins[ip] > 5:
                    suspicious_activity.append(f"Suspicious activity detected from IP: {ip} - Failed logins: {failed_logins[ip]}")

            # Check for access to suspicious files
            if "suspicious.php" in file_requested:
                suspicious_activity.append(f"IP: {ip} - Accessed: {file_requested}")

        # Print flagged activity
        for activity in suspicious_activity:
            print(activity)
# Run the script
if __name__ == "__main__":
    log_file_path = r"E:\classes\ISS 212\week 3\Assignment\sim_access.log"  # Path to the log file
    scan_log(log_file_path)  # Scan the log file

