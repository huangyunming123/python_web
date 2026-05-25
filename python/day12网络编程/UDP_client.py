import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    input_data = input("请输入数据：")
    client_sendto = udp_client.sendto(input_data.encode('utf-8'), ('10.1.16.27', 8080))
    print(client_sendto)#发送数据长度
    recvfrom, addr = udp_client.recvfrom(1024)
    decode = recvfrom.decode('utf-8')
    print(f'服务器返回{decode} 地址{addr}')