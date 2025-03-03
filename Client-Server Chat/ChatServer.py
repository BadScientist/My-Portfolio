# Author: Joseph D Tong
# Date: 12/3/2020
# Description: Creates a simple chat server.

import socket
import select
import struct

# Create a server socket bound to port 2989 on the localhost.
host = "localhost"
port = 2989
socket_1 = socket.create_server((host, port))

# Start listening for connections
socket_1.listen()

print("Server listening on", host, "on port", str(port) + ".")

# Accept a connection to the server
connection, address = socket_1.accept()

print("Connected by", address)  # Address of the connected client
print("Waiting for a message...")
wait = select.select([connection], [], [])  # Wait to receive from chat client.

first_two_bytes = connection.recv(2)  # Get the first two bytes containing the length of the received message.

if first_two_bytes:  # Check whether client closed the connection.
    rcvd_len = struct.unpack("!H", first_two_bytes)[0]  # Get the length.
    rcvd_msg = connection.recv(rcvd_len)  # Get the message.
    print("\n" + rcvd_msg.decode())
    print("\nEnter a message to send or type /q to exit.")
    message = input("\n>")
    while len(message) == 0:
        print("Messages must be at least 1 character.")
        message = input("\n>")
    if message[0:2] != "/q":
        connection.sendall(struct.pack("!H", len(message)) + message.encode())  # Encode length of msg in first 2 bytes.

        while True:
            wait = select.select([connection], [], [])
            first_two_bytes = connection.recv(2)

            if first_two_bytes:
                rcvd_len = struct.unpack("!H", first_two_bytes)[0]
                rcvd_msg = connection.recv(rcvd_len)
                print("\n" + rcvd_msg.decode())
                message = input("\n>")
                while len(message) == 0:
                    print("Messages must be at least 1 character.")
                    message = input("\n>")
                if message[0:2] != "/q":
                    connection.sendall(struct.pack("!H", len(message)) + message.encode())
                else:
                    connection.close()  # Server closed the connection.
                    break
            else:
                connection.close()  # Client closed the connection.
                break
    else:
        connection.close()  # Server closed the connection.
else:
    connection.close()  # Client closed the connection.
