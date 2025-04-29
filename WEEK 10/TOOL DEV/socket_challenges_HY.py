#ISS 212
#Week 10 Dev Tool - Socket Programming Scenarios

import socket  # Importing the socket module for network communication
import time  # Importing time module for delay simulation

# Defining server's IP and port
HOST = "127.0.0.1"  # Localhost IP (server will run on the same machine)
PORT = 9090  # Port number for communication (must match client configuration)

# Creating a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Using IPv4 and TCP stream socket
server.bind((HOST, PORT))  # Binding the socket to the specified IP and port
server.listen(1)  # Listening for incoming connections (1 client at a time)

print(f"Server is waiting for connections on {HOST}:{PORT}...")  # Informing the user that the server is ready

while True:  # Infinite loop to handle multiple incoming connections
    try:
        client_sock, addr = server.accept()  # Accepting a client connection
        print(f"Accepted connection from {addr}")  # Logging client details

        time.sleep(5)  # Simulating delay before sending a response to the client

        response_msg = f"Hello from server at {addr[0]}"  # Custom response message
        client_sock.sendall(response_msg.encode())  # Encoding and sending the response

        client_sock.close()  # Closing the client socket after interaction
    except KeyboardInterrupt:  # Handling server shutdown via Ctrl+C
        print("\nServer shutting down...")  # Graceful exit message
        server.close()  # Closing the server socket before termination
        break
    except Exception as e:  # Handling unexpected errors
        print(f"Error occurred: {e}")  # Logging the error message
