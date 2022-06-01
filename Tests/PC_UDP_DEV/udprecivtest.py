# Just for local dev testing not used for evaluation ! 

import socket
import threading
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 6666

def wait_for_udp(sock):
    while True:
        data, addr = sock.recvfrom(8) # buffer size is 1024 bytes
        print("received message: %s" % data)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

udpThread = threading.Thread(target=wait_for_udp, args=(sock,))
udpThread.start()

while True:
    time.sleep(1)