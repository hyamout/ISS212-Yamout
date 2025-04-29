'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - bowser.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

import os               # to check file existence
import sqlite3          # to open and query the Chrome history database
from datetime import datetime  # to convert timestamps into readable dates

def analyze_chrome_history(history_path, output_file):
    """
    Reads the Chrome history SQLite database and writes each URL
    and its last visit time to an output text file.
    """
    # Verify the provided path actually points to a file
    if not os.path.isfile(history_path):
        print("Invalid file path. Please make sure the file exists.")
        return

    try:
        # Connect to the SQLite database at the given path
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()

        # Fetch every record from the 'urls' table
        cursor.execute("SELECT * FROM urls")
        rows = cursor.fetchall()

        print("[--- Browser History Analysis ---]\n")

        # Open the output file for writing (UTF-8 encoding to handle all characters)
        with open(output_file, 'w', encoding='utf-8') as file:
            for row in rows:
                url = row[1]  # URL is in the second column
                # Chrome records visit times in microseconds since Jan 1, 1601
                last_visit_time_microseconds = row[5]

                # Check that the timestamp is valid before converting
                if last_visit_time_microseconds and last_visit_time_microseconds < 2**63:
                    try:
                        # Convert Chrome's timestamp to a UNIX timestamp, then format it
                        visit_time = datetime.fromtimestamp(
                            (last_visit_time_microseconds - 11644473600000000) / 1_000_000
                        ).strftime('%Y-%m-%d %H:%M:%S')
                    except (ValueError, TypeError) as e:
                        # Handle any errors during conversion
                        print(f"Error converting visit time: {e}")
                        visit_time = "N/A"
                else:
                    visit_time = "N/A"

                # Prepare the line of output with URL and visit time
                output_line = f"[+] URL: {url}\n   Last Visit Time: {visit_time}\n"
                print(output_line)         # Print to console
                file.write(output_line)    # Write to the output file

        print(f"\nBrowser history has been saved to {output_file}")

    except sqlite3.Error as e:
        # Catch any SQLite-related errors (e.g., malformed DB)
        print(f"SQLite error: {e}")

    finally:
        # Ensure the database connection is closed cleanly
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    # Prompt the user for the path to their Chrome history DB
    chrome_history_path = input("Enter the path to the Chrome history database: ")
    # Prompt the user for where to save the analysis output
    output_file_path = input("Enter the path to save the output file (e.g., output.txt): ")
    # Run the analysis with the provided paths
    analyze_chrome_history(chrome_history_path, output_file_path)
