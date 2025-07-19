# Import the socket library for network communication
import socket

# Import the datetime module to get the current date and time
from datetime import datetime


# Returns the hostname of your local machine as a string
# Then takes that hostname and resolves it to an IP address
HOST = socket.gethostbyname(socket.gethostname())

# Port to listen on (non-privileged ports are > 1023)
PORT = 65432

# Size of the buffer to hold incoming data
BUFFER_SIZE = 1024

# Create a TCP socket using the IPv4 address family (AF_INET) and TCP protocol (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    
    # Connect the socket to the specified host and port, Note: That connect input is a tuple (host, port)
    client_socket.connect((HOST, PORT))
    
    # Print the Connected server's address and port to the console
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [+] Connected to server at {HOST}:{PORT}")
    
    # Loop to continuously send and receive data from the server
    while True:
        
        # Give the user the ability to close the connection by typing 'exit' word
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [*] Type 'exit' to close the connection.")
        
        # Prompt the user for input to send to the server
        message = input("You: ")
        
        # Check if the user wants to exit the chat
        if message.lower() == 'exit':
            
            # Send a message to the server indicating that the connection is being closed
            client_socket.sendall("Connection closed by client".encode())
            
            # Print a message indicating that the client is exiting
            print(f"[{datetime.now().strftime('%H:%M:%S')}] [!] Exiting...")
            
            # Close the client socket
            client_socket.close()
            
            # Break the loop to stop sending data
            break
        
        # Encode the user's message from a string to bytes using the default UTF-8 encoding
        # This is necessary because sockets send and receive data in bytes format
        Encoded_Message = message.encode()
        
        # Send the user's message to the server
        client_socket.sendall(Encoded_Message)
        
        # Receive data from the server while ensuring that the data is available using a non-blocking call
        # Where the Data type is a bytes object that contains the data received from the server
        # walrus operator ":=" #? is used to check and assign the received data in a single line 
        if Data := client_socket.recv(BUFFER_SIZE):
            
            # Decode the received data from bytes to a string
            Decoded_Data = Data.decode()

            # Print the received data from the server to the console, if the data is available
            print(f"[{datetime.now().strftime('%H:%M:%S')}] [Server]: {Decoded_Data}")

        # If no data is received
        else:
            
            # Print a message indicating that no data was received from the server
            print(f"[{datetime.now().strftime('%H:%M:%S')}] [-] No data received from server, connection may be closed.")
            
            # Then break the loop to stop receiving data
            break