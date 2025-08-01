# Import the socket library for network communication
import socket

# Import the datetime module to get the current date and time
from datetime import datetime


# Returns the hostname of your local machine as a string.
# Then takes that hostname and resolves it to an IP address.
HOST = socket.gethostbyname(socket.gethostname())

# Port to listen on (non-privileged ports are > 1023)
PORT = 65432

# Size of the buffer to hold incoming data
BUFFER_SIZE = 1024

# Create a TCP socket using the IPv4 address family (AF_INET) and TCP protocol (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    
    # Bind the socket to the specified host and port, Note: That binding input is a tuple (host, port)
    server_socket.bind((HOST, PORT))

    # Start listening for incoming connections on the socket
    server_socket.listen()

    # Print the server's address and port to the console
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [+] Server listening on {HOST}:{PORT}")

    """
        Accept a connection from a client, Note: That connection is a new socket object that is used to communicate with the client,
        and address is the address of the client containing the IP address and port number.
    """
    connection, address = server_socket.accept()

    # Use the accepted connection to receive and send data
    with connection:
        
        # Print the address of the connected client to the console which is a tuple containing the IP address and port number.
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [+] Connected by {address}")

        # Loop to continuously receive data from the client
        while True:

            # Receive data from the client, Note: That connection.recv() is a blocking call that waits for data to be received.
            Data = connection.recv(BUFFER_SIZE)

            # If no data is received, it means the client has closed the connection
            if not Data:

                # Print a message indicating that the connection has been closed by the client
                print(f"[{datetime.now().strftime('%H:%M:%S')}] [-] No data sent, may connection closed by client")
                
                # Break the loop to stop receiving data
                break

            # Decode the received data from byte object to a string
            Decoded_Data = Data.decode()
            
            # Check if the client is requesting to close the connection
            if Decoded_Data.lower() == "connection closed by client":
                
                # Print a message indicating that the client has requested to close the connection
                print(f"[{datetime.now().strftime('%H:%M:%S')}] [-] Client requested to close the connection.")
                
                # Print a message indicating that the server is closing the connection
                print(f"[{datetime.now().strftime('%H:%M:%S')}] [!] Closing server socket...")
                
                # Close the server socket to free up the port
                server_socket.close()
                
                # Exit the loop gracefully without echoing the message back
                break
            
            # Otherwise: Print the received data from the client to the console, if the data is available
            # This includes the decoded message, its hexadecimal representation, binary representation, and length in bytes
            print(f"[{datetime.now().strftime('%H:%M:%S')}] [Client]: {Decoded_Data}, [Hex]: {Data.hex()}\n\t   [Binary]: {' '.join(format(byte, '08b') for byte in Data)}, [Length]: {len(Data)} bytes")

            # Send the received data back to the client (echo)
            connection.sendall(Data)