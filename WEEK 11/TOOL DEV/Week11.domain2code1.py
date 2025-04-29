import re         # Import regular expressions module for pattern matching
import requests   # Import requests module for making HTTP requests
import csv        # Import csv module for reading/writing CSV files

# 1) Define the target URLs to scan for email addresses
targets = [
    'https://www.ietf.org/contact'  # Example contact page URL
]

# 2) Compile a regex pattern to match basic email addresses (user@domain.tld)
email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')

# 3) Open the CSV file for writing results
#    'w' mode overwrites any existing file; newline='' prevents extra blank lines on Windows
with open('emails_found2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)         # Create a CSV writer object
    writer.writerow(['url', 'email'])    # Write the header row

    # 4) Loop through each URL in the targets list
    for url in targets:
        try:
            # 4a) Fetch the page content with a 10-second timeout
            resp = requests.get(url, timeout=10)
            # 4b) Extract all unique emails from the HTML text using the regex
            emails = set(email_pattern.findall(resp.text))

            # 5) Write each found email to the CSV file, paired with its source URL
            for email in emails:
                writer.writerow([url, email])

            # 6) If no emails were found, note that in the CSV
            if not emails:
                writer.writerow([url, "No emails found"])

            # 7) Print a summary to the console
            print(f"Checked {url}, found {len(emails)} emails.")
        except requests.exceptions.RequestException as e:
            # 8) Handle request errors (e.g., network issues, timeouts)
            print(f"Error fetching {url}: {e}")
            writer.writerow([url, "Error"])  # Log the error in the CSV
