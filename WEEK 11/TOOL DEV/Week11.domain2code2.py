import requests                          # For making HTTP requests to web pages
from bs4 import BeautifulSoup           # For parsing HTML content
from urllib.parse import urlparse       # For extracting components from URLs

# 1) Define the list of pages to scan
targets = [
    'https://www.ietf.org/contact'  # Example contact page URL
]

# 2) Open the output file for writing external links
with open('external_links2.txt', 'w') as f:
    # Loop through each target URL
    for url in targets:
        print(f"Scanning {url}...")     # Inform the user which URL is being scanned

        try:
            # 3) Fetch the page with a 10-second timeout
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()      # Raise an exception for HTTP errors (4xx/5xx)
        except requests.exceptions.RequestException as e:
            # Print error and skip to the next URL if the request fails
            print(f"Error fetching {url}: {e}")
            continue

        # 4) Determine the base domain to compare against
        base_domain = urlparse(url).netloc

        # 5) Parse the HTML content of the page
        soup = BeautifulSoup(resp.text, 'html.parser')

        # 6) Find all <a> tags with an href attribute
        for tag in soup.find_all('a', href=True):
            href = tag['href']          # Extract the URL from the tag
            parsed = urlparse(href)     # Parse the link to inspect its domain
            # Check if it’s an external link (has a domain and it differs from the base)
            if parsed.netloc and parsed.netloc != base_domain:
                f.write(href + "\n")    # Save external link to the output file

        print("Done scanning.")        # Indicate completion for this URL

# 7) Final message once all URLs have been processed
print("External links saved to external_links2.txt")
