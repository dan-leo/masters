import socket
from time import sleep

UDP_IP = "127.0.0.1"
UDP_PORT = 5555
# UDP_PORT = 7

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(addr, data)
    sleep(1)
    sock.sendto(data, addr)
