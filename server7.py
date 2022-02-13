import socket

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.bind(('::', 8080))
sock.listen()
print(sock.accept())
