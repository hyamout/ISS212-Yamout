"""
whatthepdf1.py

This script extracts metadata from a PDF file using PyPDF2.
Usage:
    python whatthepdf1.py <PDF File Path>

Citation: Python for Networking & Security vol 3 - JOrtega
"""

import os  # Importing the os module for file path verification
from PyPDF2 import PdfReader  # Importing PyPDF2 for reading PDFs

def get_metadata():
    """
    Reads a PDF file and extracts metadata.
    """

    # Prompt user for the PDF file path
    pdf_path = input("Enter the path to the PDF file: ")

    # Verify if the file exists before proceeding
    if not os.path.isfile(pdf_path):
        print("Invalid file path. Please make sure the file exists.")
        return  # Exit function if the file does not exist

    print(f"[--- Metadata for: {pdf_path} ---]")  # Display the file path
    print("---------------------------------------------------------")

    try:
        # Open the PDF file in read-binary ('rb') mode
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)  # Initialize PdfReader object

            # Extract metadata (such as title, author, subject) from the PDF
            info = pdf_reader.metadata

            # Display metadata if available
            if info:
                for key, value in info.items():
                    print(f"[+] {key.strip('/')} : {value}")  # Format metadata keys and values

            # Display page layout information (e.g., Single Page, Continuous, etc.)
            print(f"[+] Layout: {pdf_reader.page_layout}")

            # Extract additional metadata using XMP metadata (if available)
            xmp_info = pdf_reader.xmp_metadata
            if xmp_info:
                print(f"[+] Contributor: {getattr(xmp_info, 'dc_contributor', 'N/A')}")
                print(f"[+] Identifier: {getattr(xmp_info, 'dc_identifier', 'N/A')}")
                print(f"[+] Date: {getattr(xmp_info, 'dc_date', 'N/A')}")
                print(f"[+] Source: {getattr(xmp_info, 'dc_source', 'N/A')}")
                print(f"[+] Subject: {getattr(xmp_info, 'dc_subject', 'N/A')}")
                print(f"[+] Modify Date: {getattr(xmp_info, 'xmp_modify_date', 'N/A')}")
                print(f"[+] Metadata Date: {getattr(xmp_info, 'xmp_metadata_date', 'N/A')}")
                print(f"[+] Document ID: {getattr(xmp_info, 'xmpmm_document_id', 'N/A')}")
                print(f"[+] Instance ID: {getattr(xmp_info, 'xmpmm_instance_id', 'N/A')}")
                print(f"[+] PDF Keywords: {getattr(xmp_info, 'pdf_keywords', 'N/A')}")
                print(f"[+] PDF Version: {getattr(xmp_info, 'pdf_pdfversion', 'N/A')}")

    except Exception as e:
        # Catch and display any errors encountered while processing the PDF
        print(f"Error processing PDF: {e}")

# Ensure the function runs only when the script is executed directly
if __name__ == "__main__":
    get_metadata()
