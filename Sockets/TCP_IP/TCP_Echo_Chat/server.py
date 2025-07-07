# Import the socket library for network communication
import socket

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
    print(f"[+] Server listening on {HOST}:{PORT}")

    """
        Accept a connection from a client, Note: That conn is a new socket object that is used to communicate with the client,
        and addr is the address of the client containing the IP address and port number.
    """
    conn, addr = server_socket.accept()

    # Use the accepted connection to receive and send data
    with conn:
        
        # Print the address of the connected client to the console which is a tuple containing the IP address and port number.
        print(f"[+] Connected by {addr}")

        # Loop to continuously receive data from the client
        while True:

            # Receive data from the client, Note: That conn.recv() is a blocking call that waits for data to be received.
            Data = conn.recv(BUFFER_SIZE)

            # If no data is received, it means the client has closed the connection
            if not Data:

                # Print a message indicating that the connection has been closed by the client
                print("[-] Connection closed by client")
                
                # Break the loop to stop receiving data
                break

            # Decode the received data from bytes to a string
            Decoded_Data = Data.decode()
            
            # Print the received data from the client to the console, if the data is available.
            print(f"[Client]: {Decoded_Data}")

            # Send the received data back to the client (echo)
            conn.sendall(Data)