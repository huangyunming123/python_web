import socket

# TCP协议 type = socket.SOCK_STREAM   UDP type=socket.SOCK_DGRAM

tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

