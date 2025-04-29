'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - dca-hw.py
NOTE: Use files: dca-log.csv & dca-db.db.
'''

import csv  # Import CSV module to handle log file data
import sqlite3  # Import SQLite3 for database interactions

def retrieve_log_data(log_file):
    """
    Reads data from a CSV log file and returns it as a list of dictionaries.
    Each row in the CSV file represents a dictionary with key-value pairs.
    """

    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # Read the CSV file as a dictionary
        return list(reader)  # Convert the data into a list for easier processing

def retrieve_database_data(db_file):
    """
    Connects to an SQLite database, retrieves all records from the 'users' table,
    and formats the data into a list of dictionaries.
    """

    conn = sqlite3.connect(db_file)  # Establish connection to the SQLite database
    cursor = conn.cursor()  # Create a cursor to execute SQL queries

    cursor.execute("SELECT * FROM users")  # Fetch all rows from the 'users' table
    rows = cursor.fetchall()  # Retrieve query results as a list of tuples
    conn.close()  # Close the database connection

    # Convert the list of tuples into a list of dictionaries for better readability
    return [{'id': row[0], 'username': row[1], 'role': row[2], 'email': row[3], 'website': row[4]} for row in rows]

def prompt_for_username(log_data):
    """
    Displays a list of available usernames from the log file and allows the user to select one.
    Returns the selected username.
    """

    print("Available usernames:")
    for i, entry in enumerate(log_data):  # Loop through usernames from the log file
        print(f"{i + 1}. {entry.get('username')}")  # Display usernames with a numbered list

    # Get user selection and adjust for zero-based indexing
    selection = int(input("Select a username by entering its number: ")) - 1
    return log_data[selection].get('username').strip()  # Return selected username after stripping whitespace

def correlate_data_based_on_user_input(database, log_data, selected_username):
    """
    Finds and displays log file entries that match the selected username.
    """

    correlated_data = [entry for entry in log_data if entry.get('username').strip() == selected_username]

    if correlated_data:
        print(f"\nCorrelated data for '{selected_username}':")
        for entry in correlated_data:
            print(entry)  # Display matching entries
    else:
        print(f"No data found for the entered username '{selected_username}'.")  # Handle case where no matches are found

# Prompt user for log file and database file locations
log_file = input("Enter the log file name (e.g., logfile.csv): ")
db_file = input("Enter the database file name (e.g., local_db_file.db): ")

# Load log and database data
log_data = retrieve_log_data(log_file)
database = retrieve_database_data(db_file)

# Ask the user to select a username from the log file
selected_username = prompt_for_username(log_data)

# Find and display matching records based on the selected username
correlate_data_based_on_user_input(database, log_data, selected_username)
