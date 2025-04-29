import dns.resolver  # Import dnspython for performing DNS queries

# 1) Define the list of domains to look up A-records for
domains = [
    'ietf.org',  # University of Texas at Dallas
]

# 2) Configure the DNS resolver to use Cloudflare’s DNS (1.1.1.1)
resolver = dns.resolver.Resolver()
resolver.nameservers = ['1.1.1.1']  # List of DNS servers to query

# 3) Open the output file for writing DNS results
with open('dns_records2.txt', 'w') as f:
    # Loop through each domain in our list
    for domain in domains:
        # Write a header for the current domain’s A-records
        f.write(f"A Records for {domain}:\n")
        try:
            # Query the DNS server for A records of the domain
            answers = resolver.resolve(domain, 'A')
            # Loop through each returned record and write it to the file
            for record in answers:
                f.write(record.to_text() + "\n")
            # Print a message to the console confirming resolution
            print(f"Resolved {domain}")
        except dns.exception.DNSException as e:
            # If an error occurs (e.g., timeout or NXDOMAIN), log it in the file
            f.write(f"Error: {e}\n")
        # Add a blank line to separate entries for readability
        f.write("\n")

# 4) Notify the user that the DNS lookup results have been saved
print("DNS records saved to dns_records2.txt")
