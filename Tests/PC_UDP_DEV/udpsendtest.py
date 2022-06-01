# Just for local dev testing not used for evaluation ! 

import socket

UDP_IP = "10.10.10.20"
UDP_PORT = 6666
MESSAGE = b"Hi"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))