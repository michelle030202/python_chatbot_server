import socket

host = socket.gethostbyname(socket.gethostname())   # server hostname
port = 5050    # Port to listen on
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
FORMAT = 'utf-8'

inp = input("Your choice: ")
client.send(inp.encode(FORMAT))
print(client.recv(2048).decode(FORMAT))
