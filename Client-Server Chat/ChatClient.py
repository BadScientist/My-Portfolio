# Author: Joseph D Tong
# Date: 12/3/2020
# Description: A simple chat client that connects to the chat server.

import socket
import select
import struct

# Create a TCP socket.
socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up a connection chat server.
host = "localhost"
port = 2989
socket_1.connect((host, port))
print("Connected to", host, "on port:", str(port) + ".")
print("Enter a message to send or type /q to exit.")

# Create the message to send to the server
message = input("\n>")

while len(message) == 0:
    print("Messages must be at least 1 character.")
    message = input("\n>")

if message[0:2] != "/q":
    socket_1.sendall(struct.pack("!H", len(message)) + message.encode())  # Encode length of message in first 2 bytes.

    while True:
        wait = select.select([socket_1], [], [])  # Wait to receive from chat server
        first_two_bytes = socket_1.recv(2)  # Get the first two bytes containing the length of the received message.

        if first_two_bytes:  # Check whether server closed the connection.
            rcvd_len = struct.unpack("!H", first_two_bytes)[0]  # Get the length.
            rcvd_msg = socket_1.recv(rcvd_len)  # Get the message.
            print("\n" + rcvd_msg.decode())
            message = input("\n>")
            while len(message) == 0:
                print("Messages must be at least 1 character.")
                message = input("\n>")
            if message[0:2] != "/q":
                socket_1.sendall(struct.pack("!H", len(message)) + message.encode())
            else:
                socket_1.close()  # Client closed the connection.
                break
        else:
            socket_1.close()  # Server closed the connection.
            break

else:
    socket_1.close()  # Client closed the connection.
