'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use files: ioc-bfa.log, ioc-malexec.log, ioc-unauth.log
'''

import logging  # Import Python's logging module for capturing system logs
from logging.handlers import TimedRotatingFileHandler  # Import handler for log rotation

def basic_logging(output_file):
    """
    Configures basic logging functionality.
    Logs all messages at DEBUG level to the specified output file.
    """

    logging.basicConfig(filename=output_file, level=logging.DEBUG)  # Set up basic file logging

def file_rotation_logging(output_file):
    """
    Configures logging with automatic file rotation.
    Log files rotate at midnight, with up to 7 backups stored.
    """

    logger = logging.getLogger(__name__)  # Create a logger instance
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Format log messages

    file_handler = TimedRotatingFileHandler(output_file, when='midnight', backupCount=7)  # Rotate logs daily
    file_handler.setLevel(logging.DEBUG)  # Set log level to DEBUG
    file_handler.setFormatter(formatter)  # Apply formatting to log entries

    logger.addHandler(file_handler)  # Attach file handler to the logger

def log_error_with_traceback(output_file):
    """
    Logs errors with detailed traceback information.
    Demonstrates error handling by attempting to open a non-existent file.
    """

    logger = logging.getLogger(__name__)  # Create a logger instance
    logging.basicConfig(filename=output_file, level=logging.DEBUG)  # Set up logging

    try:
        open('non_existent_file.txt', 'rb')  # Attempt to open a non-existent file
    except Exception as exception:
        logger.error('Failed to open file', exc_info=True)  # Log error with traceback details
        logger.exception('Failed to open file')  # Exception logging with additional context

if __name__ == "__main__":
    """
    Main execution:
    1. Prompt user for log file names.
    2. Apply basic logging, rotating logging, and error logging.
    3. Combine logs from all methods into a single file.
    """

    # Prompt user for log file names
    output_file_basic = input("Enter log file name for basic logging: ")
    output_file_rotation = input("Enter log file name for file rotation logging: ")
    output_file_error = input("Enter log file name for logging errors with traceback: ")
    output_file_combined = input("Enter log file name to combine all logs: ")

    # Apply logging configurations
    basic_logging(output_file_basic)
    file_rotation_logging(output_file_rotation)
    log_error_with_traceback(output_file_error)

    # Combine logs into a single file for review
    with open(output_file_combined, 'w') as combined_file:
        for log_file in [output_file_basic, output_file_rotation, output_file_error]:
            with open(log_file, 'r') as log:
                combined_file.write(log.read())  # Append log contents to the combined log file
