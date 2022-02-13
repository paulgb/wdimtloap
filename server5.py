import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('128.0.0.3', 8080))
sock.listen()
print(sock.accept())
