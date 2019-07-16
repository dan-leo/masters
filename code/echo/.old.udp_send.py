import socket

# UDP_IP = "127.0.0.1"
# UDP_PORT = 55056
# UDP_IP = "ec2-18-223-252-171.us-east-2.compute.amazonaws.com"
# UDP_IP = "34.74.25.60"
# UDP_IP = "104.196.163.132"
# UDP_PORT = 5555
# UDP_IP = "ping.online.net"
# UDP_PORT = 5200
IP = ('52.20.16.20', 40000)
# IP = ('195.34.89.241', 7) # this Ublox one works
# IP = ("127.0.0.1", 5555)
MESSAGE = "Hello, World!"

print("UDP target IP:", IP[0])
print("UDP target port:", IP[1])
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(5)
sock.sendto(MESSAGE.encode(), IP)
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print(addr, data)