import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 0.0.0.0 表示：绑定本机所有网卡上的所有 IP。
# 客户端不管是通过 127.0.0.1（本机访问），还是通过你的局域网 IP（比如 192.168.1.100），都能连上。

udp_socket.bind(('10.1.16.27', 8080))

while True:
    data, addr = udp_socket.recvfrom(1024)
    print(data.decode('utf-8'))
    udp_socket.sendto(b'hello', addr)
    if data.decode('utf-8') == 'bye bye':
        break
udp_socket.close()