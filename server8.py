import socket

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
sock.bind(('::', 8080))
sock.listen()
print(sock.accept())
