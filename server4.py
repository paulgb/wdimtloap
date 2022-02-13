import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.2', 8080))
sock.listen()
print(sock.accept())
