#ISS 212
#Week 10 Dev Tool - Socket Programming Scenarios

import socket  # Importing the socket module for network communication
import time  # Importing time module for timestamp tracking

# Defining the server's IP and port
SERVER_HOST = "127.0.0.1"  # Localhost IP (client connects to the same machine)
SERVER_PORT = 9090  # Port number for communication (must match server configuration)

# Creating a TCP socket using a 'with' statement for automatic cleanup
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    try:
        client_sock.connect((SERVER_HOST, SERVER_PORT))  # Connecting to the server at defined host and port

        start_time = time.strftime('%Y-%m-%d %H:%M:%S')  # Capturing timestamp before sending request
        print(f"Sending request at: {start_time}")  # Logging the request time

        server_response = client_sock.recv(1024)  # Receiving server response (buffer size: 1024 bytes)

        end_time = time.strftime('%Y-%m-%d %H:%M:%S')  # Capturing timestamp after receiving response
        print(f"Received response at: {end_time}")  # Logging the response time

        print(f"Server says: {server_response.decode()}")  # Decoding and displaying the server's message
    except ConnectionRefusedError:  # Handling case when the server isn't running or unavailable
        print("Server is not running or unavailable!")
    except Exception as e:  # Handling unexpected errors gracefully
        print(f"Error occurred: {e}")  # Printing the error message for debugging
